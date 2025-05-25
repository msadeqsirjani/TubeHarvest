"""
Utility functions for TubeHarvest YouTube downloader.
"""

import os
import re
import sys
import json
from typing import Dict, Any, Optional, List
from colorama import Fore, Style, init

# Initialize colorama for cross-platform colored terminal output
init()


def validate_url(url: str) -> bool:
    """
    Validate if the provided URL is a valid YouTube URL.

    Args:
        url: The YouTube URL to validate

    Returns:
        bool: True if valid, False otherwise
    """
    youtube_regex = (
        r"(https?://)?(www\.)?"
        r"(youtube|youtu|youtube-nocookie)\.(com|be)/"
        r"(watch\?v=|embed/|v/|.+\?v=)?([^&=%\?]{11})"
    )

    youtube_playlist_regex = (
        r"(https?://)?(www\.)?"
        r"(youtube|youtu|youtube-nocookie)\.(com|be)/"
        r"(playlist\?list=)([^&=%\?]+)"
    )

    match = re.match(youtube_regex, url)
    playlist_match = re.match(youtube_playlist_regex, url)

    return bool(match or playlist_match)


def is_playlist_url(url: str) -> bool:
    """
    Check if the URL is a YouTube playlist.

    Args:
        url: The URL to check

    Returns:
        bool: True if it's a playlist URL, False otherwise
    """
    return "playlist?list=" in url


def create_output_directory(directory: str) -> None:
    """
    Create the output directory if it doesn't exist.

    Args:
        directory: Path to the directory
    """
    if not os.path.exists(directory):
        try:
            os.makedirs(directory)
            print(f"{Fore.GREEN}Created output directory: {directory}{Style.RESET_ALL}")
        except OSError as e:
            print(
                f"{Fore.RED}Error creating directory {directory}: {e}{Style.RESET_ALL}"
            )
            sys.exit(1)


def format_file_size(size_bytes: int) -> str:
    """
    Format file size from bytes to human-readable format.

    Args:
        size_bytes: Size in bytes

    Returns:
        str: Human-readable file size (e.g., "15.2 MB")
    """
    if size_bytes == 0:
        return "0B"

    size_name = ("B", "KB", "MB", "GB", "TB")
    i = 0
    while size_bytes >= 1024 and i < len(size_name) - 1:
        size_bytes /= 1024.0
        i += 1

    return f"{size_bytes:.2f} {size_name[i]}"


def save_metadata(metadata: Dict[str, Any], output_dir: str, filename: str) -> None:
    """
    Save video metadata to a JSON file.

    Args:
        metadata: Dictionary containing video metadata
        output_dir: Directory to save the file
        filename: Base filename (without extension)
    """
    metadata_file = os.path.join(output_dir, f"{filename}.info.json")
    try:
        with open(metadata_file, "w", encoding="utf-8") as f:
            json.dump(metadata, f, indent=4, ensure_ascii=False)
        print(f"{Fore.GREEN}Metadata saved to: {metadata_file}{Style.RESET_ALL}")
    except Exception as e:
        print(f"{Fore.YELLOW}Warning: Could not save metadata: {e}{Style.RESET_ALL}")


def sanitize_filename(filename: str) -> str:
    """
    Sanitize filename by removing invalid characters.

    Args:
        filename: Original filename

    Returns:
        str: Sanitized filename
    """
    # Define characters not allowed in filenames
    invalid_chars = r'[<>:"/\\|?*]'
    # Replace invalid characters with underscore
    return re.sub(invalid_chars, "_", filename)


def print_banner() -> None:
    """
    Display the TubeHarvest banner.
    """
    banner = f"""
{Fore.CYAN}╔════════════════════════════════════════════╗
║  {Fore.YELLOW}████████╗██╗   ██╗██████╗ ███████╗{Fore.CYAN}         ║
║  {Fore.YELLOW}╚══██╔══╝██║   ██║██╔══██╗██╔════╝{Fore.CYAN}         ║
║  {Fore.YELLOW}   ██║   ██║   ██║██████╔╝█████╗  {Fore.CYAN}         ║
║  {Fore.YELLOW}   ██║   ██║   ██║██╔══██╗██╔══╝  {Fore.CYAN}         ║
║  {Fore.YELLOW}   ██║   ╚██████╔╝██████╔╝███████╗{Fore.CYAN}         ║
║  {Fore.YELLOW}   ╚═╝    ╚═════╝ ╚═════╝ ╚══════╝{Fore.CYAN}         ║
║                                            ║
║  {Fore.GREEN}██╗  ██╗ █████╗ ██████╗ ██╗   ██╗███████╗███████╗{Fore.CYAN}║
║  {Fore.GREEN}██║  ██║██╔══██╗██╔══██╗██║   ██║██╔════╝██╔════╝{Fore.CYAN}║
║  {Fore.GREEN}███████║███████║██████╔╝██║   ██║█████╗  ███████╗{Fore.CYAN}║
║  {Fore.GREEN}██╔══██║██╔══██║██╔══██╗╚██╗ ██╔╝██╔══╝  ╚════██║{Fore.CYAN}║
║  {Fore.GREEN}██║  ██║██║  ██║██║  ██║ ╚████╔╝ ███████╗███████║{Fore.CYAN}║
║  {Fore.GREEN}╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝  ╚═══╝  ╚══════╝╚══════╝{Fore.CYAN}║
╚════════════════════════════════════════════╝{Style.RESET_ALL}
     🎬 YouTube Downloader with Superpowers 🎬
"""
    print(banner)


def print_success(message: str) -> None:
    """Print a success message with green color."""
    print(f"{Fore.GREEN}✅ {message}{Style.RESET_ALL}")


def print_error(message: str) -> None:
    """Print an error message with red color."""
    print(f"{Fore.RED}❌ {message}{Style.RESET_ALL}")


def print_warning(message: str) -> None:
    """Print a warning message with yellow color."""
    print(f"{Fore.YELLOW}⚠️  {message}{Style.RESET_ALL}")


def print_info(message: str) -> None:
    """Print an info message with cyan color."""
    print(f"{Fore.CYAN}ℹ️  {message}{Style.RESET_ALL}")
