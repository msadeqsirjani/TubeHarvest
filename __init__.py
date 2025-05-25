"""
TubeHarvest - A comprehensive YouTube downloader with beautiful interactive console interface.

This is the root package that provides access to the main TubeHarvest functionality.
For the actual package, see tubeharvest/ directory.
"""

# Import version from the main package
try:
    from tubeharvest import __version__
except ImportError:
    __version__ = "2.0.0"

__all__ = ["__version__"] 