#!/usr/bin/env python3
"""
TubeHarvest - Interactive Mode
Enhanced interactive interface for YouTube content downloading.
"""

import os
import sys
import signal
from typing import Dict, Any
from contextlib import contextmanager

from ..ui.console import ui
from ..core.utils import validate_url
from ..core.downloader import TubeHarvestDownloader


def setup_signal_handlers() -> None:
    """Setup signal handlers for graceful termination."""

    def signal_handler(sig, frame):
        ui.show_info("\nReceived termination signal. Exiting gracefully...")
        ui.goodbye_message()
        sys.exit(0)

    signal.signal(signal.SIGINT, signal_handler)
    signal.signal(signal.SIGTERM, signal_handler)


@contextmanager
def download_progress_context():
    """Context manager for download progress display."""
    progress = ui.create_download_progress()
    try:
        with progress:
            yield progress
    finally:
        pass


def validate_configuration(config: Dict[str, Any]) -> bool:
    """
    Validate the interactive configuration.

    Args:
        config: Configuration dictionary from interactive setup

    Returns:
        bool: True if configuration is valid, False otherwise
    """
    # Validate URL
    if not validate_url(config["url"]):
        ui.show_error(f"Invalid YouTube URL: {config['url']}")
        return False

    # Check for conflicting arguments
    if config["audio_only"] and config["video_only"]:
        ui.show_error(
            "Cannot use both audio-only and video-only options simultaneously"
        )
        return False

    # Check if output directory is writable
    try:
        os.makedirs(config["output_dir"], exist_ok=True)
        test_file = os.path.join(config["output_dir"], ".test_write_permission")
        with open(test_file, "w") as f:
            f.write("test")
        os.remove(test_file)
    except (IOError, PermissionError) as e:
        ui.show_error(
            f"Cannot write to output directory {config['output_dir']}: {str(e)}"
        )
        return False

    return True


def run_download_with_ui(config: Dict[str, Any]) -> bool:
    """
    Run the download process with enhanced UI feedback.

    Args:
        config: Download configuration

    Returns:
        bool: True if download was successful, False otherwise
    """
    try:
        # Create and configure the downloader
        downloader = TubeHarvestDownloader(
            url=config["url"],
            output_dir=config["output_dir"],
            format_type=config["format"],
            quality=config["quality"],
            audio_only=config["audio_only"],
            video_only=config["video_only"],
            download_subtitles=config["subtitles"],
            save_metadata_info=config["metadata"],
            max_workers=config["workers"],
            custom_filename=config["filename"],
        )

        # Start the download session
        ui.start_download_session()

        # Use the progress context manager
        with download_progress_context() as progress:
            # Attach UI to downloader for progress updates
            downloader.ui = ui
            downloader.progress = progress

            # Start the download process
            success = downloader.download()

            # Show final statistics
            total_size = "Unknown"  # Could be enhanced to track total size
            ui.show_download_stats(
                downloader.total_downloads, downloader.failed_downloads, total_size
            )

            return success

    except KeyboardInterrupt:
        ui.show_warning("Download interrupted by user")
        return False
    except Exception as e:
        ui.show_error(f"Unexpected error during download: {str(e)}")
        return False


def interactive_main() -> int:
    """
    Main entry point for interactive mode.

    Returns:
        int: Exit code (0 for success, non-zero for failure)
    """
    try:
        # Setup signal handlers for graceful termination
        setup_signal_handlers()

        # Display welcome interface
        ui.display_banner()
        ui.show_welcome_info()

        while True:
            try:
                # Interactive setup
                config = ui.interactive_setup()

                # Validate configuration
                if not validate_configuration(config):
                    if ui.ask_retry("Configuration validation failed"):
                        continue
                    else:
                        break

                # Show configuration summary
                ui.show_config_summary(config)

                # Confirm before starting download
                if not ui.confirm_download():
                    ui.show_info("Download cancelled by user")
                    break

                # Run the download
                success = run_download_with_ui(config)

                if success:
                    ui.show_success("All downloads completed successfully!")
                else:
                    ui.show_warning(
                        "Some downloads may have failed. Check the output above."
                    )

                # Ask if user wants to download something else
                if not ui.ask_retry(
                    "Would you like to download another video/playlist?"
                ):
                    break

            except KeyboardInterrupt:
                ui.show_info("\nOperation cancelled by user")
                break
            except Exception as e:
                ui.show_error(f"Unexpected error: {str(e)}")
                if not ui.ask_retry("An error occurred"):
                    break

        # Show goodbye message
        ui.goodbye_message()
        return 0

    except Exception as e:
        ui.show_error(f"Fatal error: {str(e)}")
        return 1


if __name__ == "__main__":
    sys.exit(interactive_main())
