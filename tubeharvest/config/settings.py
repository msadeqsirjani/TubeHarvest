"""
Configuration settings for TubeHarvest.

This module contains default settings and configuration management.
"""

import os
from pathlib import Path
from typing import Dict, Any

# Application information
APP_NAME = "TubeHarvest"
APP_VERSION = "2.0.0"
APP_DESCRIPTION = (
    "A comprehensive YouTube downloader with beautiful interactive console interface"
)

# Default download settings
DEFAULT_OUTPUT_DIR = "downloads"
DEFAULT_FORMAT = "mp4"
DEFAULT_QUALITY = "best"
DEFAULT_MAX_WORKERS = 4

# Supported formats
SUPPORTED_VIDEO_FORMATS = ["mp4", "webm", "mkv"]
SUPPORTED_AUDIO_FORMATS = ["mp3", "m4a", "wav", "aac"]
SUPPORTED_FORMATS = SUPPORTED_VIDEO_FORMATS + SUPPORTED_AUDIO_FORMATS

# Supported qualities
SUPPORTED_QUALITIES = ["best", "1080", "720", "480", "360", "240", "144"]

# Default configuration
DEFAULT_CONFIG: Dict[str, Any] = {
    "output_dir": DEFAULT_OUTPUT_DIR,
    "format": DEFAULT_FORMAT,
    "quality": DEFAULT_QUALITY,
    "audio_only": False,
    "video_only": False,
    "subtitles": False,
    "metadata": False,
    "max_workers": DEFAULT_MAX_WORKERS,
    "retry_attempts": 3,
    "timeout": 30,
}

# File paths
HOME_DIR = Path.home()
CONFIG_DIR = HOME_DIR / ".tubeharvest"
CONFIG_FILE = CONFIG_DIR / "config.json"
LOG_DIR = CONFIG_DIR / "logs"

# User agent for requests
USER_AGENT = f"{APP_NAME}/{APP_VERSION}"


def get_config_dir() -> Path:
    """Get the configuration directory path."""
    return CONFIG_DIR


def ensure_config_dir() -> None:
    """Ensure the configuration directory exists."""
    CONFIG_DIR.mkdir(exist_ok=True)
    LOG_DIR.mkdir(exist_ok=True)


def get_default_output_dir() -> str:
    """Get the default output directory."""
    return os.path.join(os.getcwd(), DEFAULT_OUTPUT_DIR)
