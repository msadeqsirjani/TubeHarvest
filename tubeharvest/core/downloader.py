"""
Core module for YouTube download functionality using yt-dlp.
"""

import os
import sys
import time
import json
import threading
from typing import Dict, List, Any, Optional, Tuple, Union
from concurrent.futures import ThreadPoolExecutor, as_completed

import yt_dlp
from tqdm import tqdm

from .utils import (
    validate_url,
    is_playlist_url,
    create_output_directory,
    format_file_size,
    save_metadata,
    sanitize_filename,
    print_success,
    print_error,
    print_warning,
    print_info,
)


class TubeHarvestDownloader:
    """Main downloader class for TubeHarvest."""

    def __init__(
        self,
        url: str,
        output_dir: str = "downloads",
        format_type: str = "mp4",
        quality: str = "best",
        audio_only: bool = False,
        video_only: bool = False,
        download_subtitles: bool = False,
        save_metadata_info: bool = False,
        max_workers: int = 4,
        custom_filename: Optional[str] = None,
    ):
        """
        Initialize the YouTube downloader.

        Args:
            url: YouTube URL to download from
            output_dir: Directory to save downloads
            format_type: Format to save the video/audio (mp4, mp3, webm, etc.)
            quality: Video quality to download (best, 1080p, 720p, 480p, etc.)
            audio_only: Whether to download audio only
            video_only: Whether to download video only (no audio)
            download_subtitles: Whether to download available subtitles
            save_metadata_info: Whether to save video metadata
            max_workers: Maximum number of workers for multithreading
            custom_filename: Custom filename for the downloaded file
        """
        self.url = url
        self.output_dir = output_dir
        self.format_type = format_type
        self.quality = quality
        self.audio_only = audio_only
        self.video_only = video_only
        self.download_subtitles = download_subtitles
        self.save_metadata_info = save_metadata_info
        self.max_workers = max_workers
        self.custom_filename = custom_filename

        # Validate the URL before proceeding
        if not validate_url(url):
            print_error(f"Invalid YouTube URL: {url}")
            sys.exit(1)

        # Create output directory
        create_output_directory(output_dir)

        # Initialize counters for download statistics
        self.total_downloads = 0
        self.failed_downloads = 0

        # UI integration (set externally)
        self.ui = None
        self.progress = None

    def _get_format_options(self) -> Dict[str, Any]:
        """
        Get the format options based on user preferences.

        Returns:
            Dict containing format options for yt-dlp
        """
        format_options = {}

        # Handle audio-only downloads
        if self.audio_only:
            if self.format_type == "mp3":
                format_options["format"] = "bestaudio/best"
                format_options["postprocessors"] = [
                    {
                        "key": "FFmpegExtractAudio",
                        "preferredcodec": "mp3",
                        "preferredquality": "192",
                    }
                ]
            else:
                format_options["format"] = (
                    f"bestaudio[ext={self.format_type}]/bestaudio/best"
                )

        # Handle video-only downloads
        elif self.video_only:
            if self.quality == "best":
                format_options["format"] = (
                    f"bestvideo[ext={self.format_type}]/bestvideo/best"
                )
            else:
                format_options["format"] = (
                    f"bestvideo[height<={self.quality}][ext={self.format_type}]/"
                    f"bestvideo[height<={self.quality}]/best[height<={self.quality}]"
                )

        # Handle combined video+audio downloads
        else:
            if self.quality == "best":
                format_options["format"] = f"bestvideo+bestaudio/best"
                format_options["merge_output_format"] = self.format_type
            else:
                format_options["format"] = (
                    f"bestvideo[height<={self.quality}]+bestaudio/"
                    f"best[height<={self.quality}]"
                )
                format_options["merge_output_format"] = self.format_type

        return format_options

    def _get_ydl_opts(self) -> Dict[str, Any]:
        """
        Configure yt-dlp options based on user preferences.

        Returns:
            Dict of yt-dlp options
        """
        format_options = self._get_format_options()

        # Base options
        ydl_opts = {
            "outtmpl": os.path.join(self.output_dir, "%(title)s.%(ext)s"),
            "ignoreerrors": True,
            "nooverwrites": False,  # Allow overwrites for resume capability
            "continue": True,  # Resume downloads
            "retries": 10,  # Retry on network errors
            "retry_sleep": 5,  # Sleep between retries
            "quiet": True,  # Don't print debug output
            "no_warnings": True,
            "progress_hooks": [self._progress_hook],
        }

        # Add format options
        ydl_opts.update(format_options)

        # Add subtitle options if requested
        if self.download_subtitles:
            ydl_opts.update(
                {
                    "writesubtitles": True,
                    "writeautomaticsub": True,
                    "subtitleslangs": ["en"],  # English subtitles, can be expanded
                    "subtitlesformat": "srt",
                }
            )

        # Add metadata options if requested
        if self.save_metadata_info:
            ydl_opts.update(
                {
                    "writeinfojson": True,
                    "write_description": True,
                }
            )

        # Set custom filename if provided
        if self.custom_filename:
            safe_filename = sanitize_filename(self.custom_filename)
            ydl_opts["outtmpl"] = os.path.join(
                self.output_dir, f"{safe_filename}.%(ext)s"
            )

        return ydl_opts

    def _progress_hook(self, d: Dict[str, Any]) -> None:
        """
        Hook to track download progress.

        Args:
            d: Progress information dictionary from yt-dlp
        """
        if d["status"] == "downloading":
            if "_speed_str" in d and d["_speed_str"] and "_percent_str" in d:
                # Update progress using UI or tqdm
                if self.ui and hasattr(self, "current_task_id"):
                    # Extract percentage for Rich progress
                    percent_str = d.get("_percent_str", "0%")
                    try:
                        percentage = float(percent_str.replace("%", ""))
                        self.ui.update_download_task(
                            self.current_task_id,
                            completed=percentage,
                            description=f"🎬 {d.get('filename', 'unknown').split('/')[-1]}",
                        )
                    except:
                        pass
                elif hasattr(self, "progress_bar") and self.progress_bar is not None:
                    # Update tqdm progress bar
                    self.progress_bar.set_description(
                        f"Downloading: {d.get('filename', 'unknown').split('/')[-1]}"
                    )
                    self.progress_bar.set_postfix_str(
                        f"{d.get('_percent_str', '0%')} at {d.get('_speed_str', 'unknown speed')}"
                    )

        elif d["status"] == "finished":
            file_path = d.get("filename", "unknown")
            file_name = os.path.basename(file_path)
            file_size = format_file_size(os.path.getsize(file_path))

            # Use UI if available, otherwise fall back to print functions
            if self.ui:
                self.ui.show_success(f"Downloaded: {file_name} ({file_size})")
            else:
                print_success(f"Downloaded: {file_name} ({file_size})")
            self.total_downloads += 1

        elif d["status"] == "error":
            error_message = d.get("error", "Unknown error")
            if self.ui:
                self.ui.show_error(f"Download failed: {error_message}")
            else:
                print_error(f"Download failed: {error_message}")
            self.failed_downloads += 1

    def _download_single_video(self, video_url: str = None) -> bool:
        """
        Download a single video.

        Args:
            video_url: Optional specific URL to download, defaults to self.url

        Returns:
            bool: True if download was successful, False otherwise
        """
        url_to_download = video_url or self.url

        # Get ytdl options
        ydl_opts = self._get_ydl_opts()

        try:
            # Extract info first to get metadata and total filesize
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                info = ydl.extract_info(url_to_download, download=False)

                if not info:
                    print_error(
                        f"Could not retrieve video information for: {url_to_download}"
                    )
                    return False

                # Show video info using UI if available
                video_title = info.get("title", "Unknown Title")
                if self.ui:
                    self.ui.show_video_info(info)
                else:
                    print_info(f"Title: {video_title}")
                    print_info(f"Duration: {info.get('duration_string', 'Unknown')}")

                # Create progress tracking
                if self.ui and self.progress:
                    # Use Rich progress for beautiful UI
                    task_id = self.ui.add_download_task(f"🎬 {video_title}", total=100)
                    self.current_task_id = task_id
                else:
                    # Fallback to tqdm for CLI mode
                    self.progress_bar = tqdm(
                        total=100,
                        unit="%",
                        desc=f"Downloading: {video_title}",
                        bar_format="{l_bar}{bar}| {n_fmt}/{total_fmt} [{elapsed}<{remaining}, {rate_fmt}]",
                    )

                # Save metadata if requested
                if self.save_metadata_info:
                    save_metadata(
                        info,
                        self.output_dir,
                        self.custom_filename or sanitize_filename(video_title),
                    )

                # Perform the download
                ydl.download([url_to_download])

                # Complete progress tracking
                if self.ui and hasattr(self, "current_task_id"):
                    self.ui.complete_download_task(self.current_task_id)
                elif hasattr(self, "progress_bar") and self.progress_bar:
                    # Close progress bar
                    self.progress_bar.close()
                    self.progress_bar = None

                return True

        except yt_dlp.utils.DownloadError as e:
            print_error(f"Download error: {str(e)}")
            return False
        except Exception as e:
            print_error(f"Unexpected error: {str(e)}")
            return False
        finally:
            # Ensure progress bar is closed
            if hasattr(self, "progress_bar") and self.progress_bar is not None:
                self.progress_bar.close()
                self.progress_bar = None

    def _download_playlist(self) -> bool:
        """
        Download all videos in a playlist using multithreading.

        Returns:
            bool: True if all downloads were successful, False otherwise
        """
        try:
            # First, extract playlist information
            base_opts = {
                "extract_flat": True,
                "quiet": True,
                "no_warnings": True,
                "ignoreerrors": True,
            }

            if self.ui:
                self.ui.show_info("Extracting playlist information...")
            else:
                print_info(f"Extracting playlist information...")
            with yt_dlp.YoutubeDL(base_opts) as ydl:
                playlist_info = ydl.extract_info(self.url, download=False)

                if not playlist_info:
                    print_error("Could not retrieve playlist information")
                    return False

                playlist_title = playlist_info.get("title", "Unknown Playlist")
                videos = playlist_info.get("entries", [])
                video_count = len(videos)

                if video_count == 0:
                    print_error("No videos found in playlist")
                    return False

                print_info(f"Playlist: {playlist_title}")
                print_info(f"Videos found: {video_count}")

                # Create a subdirectory for the playlist
                if self.custom_filename:
                    playlist_dir = os.path.join(
                        self.output_dir, sanitize_filename(self.custom_filename)
                    )
                else:
                    playlist_dir = os.path.join(
                        self.output_dir, sanitize_filename(playlist_title)
                    )

                create_output_directory(playlist_dir)

                # Save original output directory and update for playlist
                original_output_dir = self.output_dir
                self.output_dir = playlist_dir

                # Download each video in the playlist with multithreading
                video_urls = [
                    entry.get("url") for entry in videos if entry and entry.get("url")
                ]

                print_info(
                    f"Starting download of {len(video_urls)} videos with {self.max_workers} workers..."
                )

                with ThreadPoolExecutor(max_workers=self.max_workers) as executor:
                    # Submit all download tasks
                    future_to_url = {
                        executor.submit(self._download_single_video, url): url
                        for url in video_urls
                    }

                    # Process completed downloads
                    for i, future in enumerate(as_completed(future_to_url)):
                        url = future_to_url[future]
                        try:
                            result = future.result()
                            progress = (i + 1) / len(video_urls) * 100
                            print_info(
                                f"Overall progress: {progress:.1f}% ({i+1}/{len(video_urls)})"
                            )
                        except Exception as e:
                            print_error(f"Error downloading {url}: {str(e)}")

                # Restore original output directory
                self.output_dir = original_output_dir

                # Final report
                print_success(
                    f"Playlist download complete. Successfully downloaded: {self.total_downloads}/{video_count} videos"
                )
                if self.failed_downloads > 0:
                    print_warning(f"Failed downloads: {self.failed_downloads}")

                return self.failed_downloads == 0

        except Exception as e:
            print_error(f"Error processing playlist: {str(e)}")
            return False

    def download(self) -> bool:
        """
        Start the download process.

        Returns:
            bool: True if download was successful, False otherwise
        """
        start_time = time.time()

        # Check if URL is a playlist
        if is_playlist_url(self.url):
            result = self._download_playlist()
        else:
            result = self._download_single_video()

        elapsed_time = time.time() - start_time
        print_info(f"Download process completed in {elapsed_time:.2f} seconds")

        return result
