"""
TubeHarvest - A comprehensive YouTube downloader with beautiful interactive console interface.

A modern Python application for downloading YouTube videos and playlists with
enhanced user experience through rich console interfaces.
"""

__version__ = "2.0.0"
__author__ = "TubeHarvest Team"
__email__ = "contact@tubeharvest.com"
__license__ = "MIT"

from .core.downloader import TubeHarvestDownloader
from .ui.console import TubeHarvestUI

__all__ = [
    "TubeHarvestDownloader",
    "TubeHarvestUI",
    "__version__",
]
