"""
Basic tests for TubeHarvest package.
"""

import pytest
from tubeharvest import __version__


def test_version():
    """Test that version is defined."""
    assert __version__ is not None
    assert isinstance(__version__, str)
    assert len(__version__) > 0


def test_package_imports():
    """Test that main package components can be imported."""
    try:
        import tubeharvest
        import tubeharvest.core
        import tubeharvest.cli
        import tubeharvest.config
        import tubeharvest.ui
    except ImportError as e:
        pytest.fail(f"Failed to import package components: {e}")


def test_cli_entrypoints():
    """Test that CLI entry points are accessible."""
    try:
        from tubeharvest.cli.main import main
        from tubeharvest.cli.interactive import interactive_main
        
        assert callable(main)
        assert callable(interactive_main)
    except ImportError as e:
        pytest.fail(f"Failed to import CLI components: {e}")


def test_core_downloader():
    """Test that core downloader can be imported."""
    try:
        from tubeharvest.core.downloader import TubeHarvestDownloader
        
        # Test that the class can be instantiated with a valid URL
        test_url = "https://www.youtube.com/watch?v=dQw4w9WgXcQ"
        downloader = TubeHarvestDownloader(test_url)
        assert downloader is not None
        assert downloader.url == test_url
    except ImportError as e:
        pytest.fail(f"Failed to import TubeHarvestDownloader: {e}")


def test_config_settings():
    """Test that configuration can be imported."""
    try:
        from tubeharvest.config import settings
        assert settings is not None
    except ImportError as e:
        pytest.fail(f"Failed to import settings: {e}")


class TestTubeHarvestDownloader:
    """Test suite for TubeHarvestDownloader."""
    
    def test_initialization(self):
        """Test downloader initialization."""
        from tubeharvest.core.downloader import TubeHarvestDownloader
        
        test_url = "https://www.youtube.com/watch?v=dQw4w9WgXcQ"
        downloader = TubeHarvestDownloader(test_url)
        assert downloader is not None
        assert hasattr(downloader, 'download')
        assert downloader.url == test_url
        assert downloader.output_dir == "downloads"
        assert downloader.format_type == "mp4"
    
    def test_url_validation(self):
        """Test URL validation method."""
        from tubeharvest.core.utils import validate_url
        
        # Test valid YouTube URLs
        valid_urls = [
            "https://www.youtube.com/watch?v=dQw4w9WgXcQ",
            "https://youtu.be/dQw4w9WgXcQ",
            "https://www.youtube.com/playlist?list=PLrAXtmRdnEQy4Xyx7q0j"
        ]
        
        for url in valid_urls:
            assert validate_url(url) == True
            
        # Test invalid URLs
        invalid_urls = [
            "https://www.google.com",
            "not_a_url",
            ""
        ]
        
        for url in invalid_urls:
            assert validate_url(url) == False


class TestUtils:
    """Test suite for utility functions."""
    
    def test_format_size(self):
        """Test file size formatting utility."""
        try:
            from tubeharvest.core.utils import format_file_size
            
            assert format_file_size(1024) == "1.00 KB"
            assert format_file_size(1024 * 1024) == "1.00 MB"
            assert format_file_size(1024 * 1024 * 1024) == "1.00 GB"
            assert format_file_size(0) == "0B"
        except ImportError:
            # If the function doesn't exist, skip the test
            pytest.skip("format_file_size function not implemented yet")
    
    def test_sanitize_filename(self):
        """Test filename sanitization utility."""
        try:
            from tubeharvest.core.utils import sanitize_filename
            
            # Test basic sanitization
            assert sanitize_filename("test file") == "test file"  # spaces are allowed
            assert sanitize_filename("test/file") == "test_file"  # slashes become underscores
            assert sanitize_filename("test<>file") == "test__file"  # invalid chars become underscores
            assert sanitize_filename("test:file") == "test_file"
        except ImportError:
            # If the function doesn't exist, skip the test
            pytest.skip("sanitize_filename function not implemented yet") 