"""
Pytest configuration and shared fixtures.
"""

import pytest
import tempfile
import shutil
from pathlib import Path
from unittest.mock import MagicMock

@pytest.fixture
def temp_dir():
    """Create a temporary directory for tests."""
    temp_dir = tempfile.mkdtemp()
    yield Path(temp_dir)
    shutil.rmtree(temp_dir)

@pytest.fixture
def mock_youtube_video():
    """Mock YouTube video information."""
    return {
        'title': 'Test Video Title',
        'uploader': 'Test Channel',
        'duration': 120,
        'view_count': 1000,
        'upload_date': '20231215',
        'id': 'test_video_id',
        'ext': 'mp4',
        'filesize': 1024000,
    }

@pytest.fixture
def mock_youtube_playlist():
    """Mock YouTube playlist information."""
    return {
        'title': 'Test Playlist',
        'entries': [
            {'url': 'https://www.youtube.com/watch?v=test1', 'title': 'Video 1'},
            {'url': 'https://www.youtube.com/watch?v=test2', 'title': 'Video 2'},
            {'url': 'https://www.youtube.com/watch?v=test3', 'title': 'Video 3'},
        ]
    }

@pytest.fixture
def mock_ydl():
    """Mock yt-dlp YoutubeDL instance."""
    mock = MagicMock()
    mock.extract_info.return_value = {
        'title': 'Test Video',
        'duration': 120,
        'uploader': 'Test Channel'
    }
    return mock 