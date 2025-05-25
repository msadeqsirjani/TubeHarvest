#!/usr/bin/env python3
"""
TubeHarvest - A comprehensive YouTube downloader.
Command-line interface for YouTube content downloading.
"""

import os
import sys
import argparse
import signal
from typing import List, Dict, Any, Optional

from ..core.utils import print_banner, print_error, print_info, validate_url
from ..core.downloader import TubeHarvestDownloader
from .interactive import interactive_main


def parse_arguments() -> argparse.Namespace:
    """
    Parse command line arguments.

    Returns:
        argparse.Namespace: Parsed command line arguments
    """
    parser = argparse.ArgumentParser(
        description="TubeHarvest - A comprehensive YouTube downloader",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )

    parser.add_argument(
        "-u",
        "--url",
        type=str,
        required=False,
        help="YouTube URL to download (video or playlist)",
    )

    parser.add_argument(
        "-i",
        "--interactive",
        action="store_true",
        help="Launch interactive mode with beautiful UI",
    )

    parser.add_argument(
        "-o",
        "--output-dir",
        type=str,
        default="downloads",
        help="Directory to save downloaded files",
    )

    parser.add_argument(
        "-f",
        "--format",
        type=str,
        default="mp4",
        choices=["mp4", "mp3", "webm", "mkv", "m4a"],
        help="Output format for the downloaded file",
    )

    parser.add_argument(
        "-q",
        "--quality",
        type=str,
        default="best",
        help="Video quality (best, 1080, 720, 480, 360, 240, 144)",
    )

    parser.add_argument("--audio-only", action="store_true", help="Download audio only")

    parser.add_argument(
        "--video-only", action="store_true", help="Download video only (no audio)"
    )

    parser.add_argument(
        "--subtitles", action="store_true", help="Download available subtitles"
    )

    parser.add_argument(
        "--metadata", action="store_true", help="Save video metadata to a JSON file"
    )

    parser.add_argument(
        "--filename",
        type=str,
        help="Custom filename for the downloaded file (without extension)",
    )

    parser.add_argument(
        "--workers",
        type=int,
        default=4,
        help="Maximum number of workers for multithreaded downloads",
    )

    return parser.parse_args()


def setup_signal_handlers() -> None:
    """Setup signal handlers for graceful termination."""

    def signal_handler(sig, frame):
        print_info("\nReceived termination signal. Exiting gracefully...")
        sys.exit(0)

    signal.signal(signal.SIGINT, signal_handler)
    signal.signal(signal.SIGTERM, signal_handler)


def validate_arguments(args: argparse.Namespace) -> bool:
    """
    Validate command line arguments.

    Args:
        args: Parsed command line arguments

    Returns:
        bool: True if arguments are valid, False otherwise
    """
    # Validate URL
    if not validate_url(args.url):
        print_error(f"Invalid YouTube URL: {args.url}")
        return False

    # Check for conflicting arguments
    if args.audio_only and args.video_only:
        print_error(
            "Cannot use both --audio-only and --video-only options simultaneously"
        )
        return False

    # Validate quality argument
    if args.quality != "best" and not args.quality.isdigit():
        print_error("Quality must be 'best' or a number (e.g., 1080, 720)")
        return False

    # Check if output directory is writable
    try:
        os.makedirs(args.output_dir, exist_ok=True)
        test_file = os.path.join(args.output_dir, ".test_write_permission")
        with open(test_file, "w") as f:
            f.write("test")
        os.remove(test_file)
    except (IOError, PermissionError) as e:
        print_error(f"Cannot write to output directory {args.output_dir}: {str(e)}")
        return False

    return True


def main() -> int:
    """
    Main entry point of the program.

    Returns:
        int: Exit code (0 for success, non-zero for failure)
    """
    # Parse arguments
    args = parse_arguments()

    # Check if interactive mode is requested or no URL provided
    if args.interactive or not args.url:
        return interactive_main()

    # Traditional CLI mode
    # Print banner
    print_banner()

    # Setup signal handlers for graceful termination
    setup_signal_handlers()

    # Validate arguments
    if not validate_arguments(args):
        return 1

    # Create and configure the downloader
    downloader = TubeHarvestDownloader(
        url=args.url,
        output_dir=args.output_dir,
        format_type=args.format,
        quality=args.quality,
        audio_only=args.audio_only,
        video_only=args.video_only,
        download_subtitles=args.subtitles,
        save_metadata_info=args.metadata,
        max_workers=args.workers,
        custom_filename=args.filename,
    )

    # Start the download process
    success = downloader.download()

    return 0 if success else 1


if __name__ == "__main__":
    sys.exit(main())
