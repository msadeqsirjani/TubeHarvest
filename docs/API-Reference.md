# 🏗️ API Reference

Complete Python API documentation for TubeHarvest. This reference covers all classes, methods, and integration examples for developers.

## 📖 Table of Contents

1. [Overview](#overview)
2. [Installation for Development](#installation-for-development)
3. [Core Classes](#core-classes)
4. [Download API](#download-api)
5. [Configuration API](#configuration-api)
6. [Progress Tracking](#progress-tracking)
7. [Error Handling](#error-handling)
8. [Integration Examples](#integration-examples)
9. [Advanced Usage](#advanced-usage)

## 🎯 Overview

TubeHarvest provides a comprehensive Python API for programmatic YouTube downloading. The API is designed to be:
- **Simple**: Easy to use for basic operations
- **Flexible**: Extensive customization options
- **Robust**: Comprehensive error handling
- **Async-Ready**: Support for asynchronous operations

### Key Components

- `TubeHarvest`: Main downloader class
- `DownloadOptions`: Configuration container
- `ProgressTracker`: Progress monitoring
- `MetadataExtractor`: Video information retrieval
- `FormatSelector`: Quality and format selection

## 📦 Installation for Development

```bash
# Install with development dependencies
pip install tubeharvest[dev]

# Or from source
git clone https://github.com/msadeqsirjani/TubeHarvest.git
cd TubeHarvest
pip install -e ".[dev]"
```

## 🎯 Core Classes

### TubeHarvest

The main downloader class providing the primary interface.

```python
from tubeharvest import TubeHarvest

class TubeHarvest:
    def __init__(
        self,
        output_dir: str = None,
        quality: str = "best",
        format: str = "mp4",
        **kwargs
    ):
        """
        Initialize TubeHarvest downloader.
        
        Args:
            output_dir (str): Output directory path
            quality (str): Video quality preference
            format (str): Output format
            **kwargs: Additional configuration options
        """
```

**Basic Usage:**
```python
from tubeharvest import TubeHarvest

# Create downloader instance
downloader = TubeHarvest(
    output_dir="./downloads",
    quality="1080",
    format="mp4"
)

# Download a video
result = downloader.download("https://www.youtube.com/watch?v=VIDEO_ID")
```

### DownloadOptions

Configuration container for download settings.

```python
from tubeharvest import DownloadOptions

class DownloadOptions:
    def __init__(
        self,
        quality: str = "best",
        format: str = "mp4",
        audio_only: bool = False,
        subtitles: bool = False,
        metadata: bool = False,
        thumbnail: bool = False,
        output_template: str = None,
        **kwargs
    ):
        """
        Download configuration options.
        
        Args:
            quality (str): Video quality (best, 1080, 720, etc.)
            format (str): Output format (mp4, mp3, webm, etc.)
            audio_only (bool): Extract audio only
            subtitles (bool): Download subtitles
            metadata (bool): Save metadata
            thumbnail (bool): Download thumbnail
            output_template (str): Filename template
        """
```

**Usage:**
```python
from tubeharvest import DownloadOptions

# Create options
options = DownloadOptions(
    quality="1080",
    format="mp4",
    subtitles=True,
    metadata=True,
    output_template="%(title)s.%(ext)s"
)

# Use with downloader
downloader = TubeHarvest(options=options)
```

## 📥 Download API

### Single Video Download

```python
def download(
    self,
    url: str,
    options: DownloadOptions = None,
    progress_callback: Callable = None
) -> DownloadResult:
    """
    Download a single video.
    
    Args:
        url (str): YouTube video URL
        options (DownloadOptions): Download configuration
        progress_callback (Callable): Progress callback function
        
    Returns:
        DownloadResult: Download result information
    """
```

**Example:**
```python
from tubeharvest import TubeHarvest, DownloadOptions

def progress_callback(progress_info):
    print(f"Progress: {progress_info.percentage:.1f}%")

downloader = TubeHarvest()
result = downloader.download(
    url="https://www.youtube.com/watch?v=VIDEO_ID",
    progress_callback=progress_callback
)

print(f"Downloaded: {result.filename}")
print(f"File size: {result.file_size}")
```

### Playlist Download

```python
def download_playlist(
    self,
    url: str,
    options: DownloadOptions = None,
    progress_callback: Callable = None,
    max_videos: int = None
) -> List[DownloadResult]:
    """
    Download playlist videos.
    
    Args:
        url (str): YouTube playlist URL
        options (DownloadOptions): Download configuration
        progress_callback (Callable): Progress callback function
        max_videos (int): Maximum videos to download
        
    Returns:
        List[DownloadResult]: List of download results
    """
```

**Example:**
```python
results = downloader.download_playlist(
    url="https://www.youtube.com/playlist?list=PLAYLIST_ID",
    max_videos=10
)

for result in results:
    if result.success:
        print(f"Downloaded: {result.title}")
    else:
        print(f"Failed: {result.error}")
```

### Batch Download

```python
def download_batch(
    self,
    urls: List[str],
    options: DownloadOptions = None,
    progress_callback: Callable = None,
    concurrent: int = 2
) -> List[DownloadResult]:
    """
    Download multiple URLs concurrently.
    
    Args:
        urls (List[str]): List of YouTube URLs
        options (DownloadOptions): Download configuration
        progress_callback (Callable): Progress callback function
        concurrent (int): Number of concurrent downloads
        
    Returns:
        List[DownloadResult]: List of download results
    """
```

**Example:**
```python
urls = [
    "https://www.youtube.com/watch?v=VIDEO_ID_1",
    "https://www.youtube.com/watch?v=VIDEO_ID_2",
    "https://www.youtube.com/watch?v=VIDEO_ID_3"
]

results = downloader.download_batch(urls, concurrent=3)
```

### Audio Extraction

```python
def extract_audio(
    self,
    url: str,
    audio_format: str = "mp3",
    audio_quality: str = "192",
    options: DownloadOptions = None
) -> DownloadResult:
    """
    Extract audio from video.
    
    Args:
        url (str): YouTube video URL
        audio_format (str): Audio format (mp3, m4a, ogg)
        audio_quality (str): Audio quality (320, 256, 192, 128)
        options (DownloadOptions): Additional options
        
    Returns:
        DownloadResult: Download result
    """
```

**Example:**
```python
# Extract high-quality MP3
result = downloader.extract_audio(
    url="https://www.youtube.com/watch?v=VIDEO_ID",
    audio_format="mp3",
    audio_quality="320"
)
```

## ⚙️ Configuration API

### Global Configuration

```python
from tubeharvest import Config

class Config:
    @staticmethod
    def load(config_path: str = None) -> dict:
        """Load configuration from file."""
    
    @staticmethod
    def save(config: dict, config_path: str = None) -> None:
        """Save configuration to file."""
    
    @staticmethod
    def get_default() -> dict:
        """Get default configuration."""
    
    @staticmethod
    def validate(config: dict) -> bool:
        """Validate configuration."""
```

**Example:**
```python
from tubeharvest import Config, TubeHarvest

# Load configuration
config = Config.load("~/.config/tubeharvest/config.yaml")

# Create downloader with configuration
downloader = TubeHarvest(config=config)

# Modify and save configuration
config["general"]["quality"] = "720"
Config.save(config, "~/.config/tubeharvest/config.yaml")
```

### Runtime Configuration

```python
# Update downloader configuration
downloader.update_config({
    "quality": "1080",
    "format": "mp4",
    "subtitles": True
})

# Get current configuration
current_config = downloader.get_config()
```

## 📊 Progress Tracking

### ProgressInfo Class

```python
from tubeharvest import ProgressInfo

class ProgressInfo:
    def __init__(self):
        self.url: str = None
        self.title: str = None
        self.status: str = None  # downloading, processing, completed, error
        self.percentage: float = 0.0
        self.downloaded_bytes: int = 0
        self.total_bytes: int = 0
        self.speed: float = 0.0  # bytes per second
        self.eta: float = 0.0    # seconds
        self.error: str = None
```

### Progress Callbacks

```python
def detailed_progress_callback(progress: ProgressInfo):
    """Detailed progress tracking example."""
    print(f"Title: {progress.title}")
    print(f"Status: {progress.status}")
    print(f"Progress: {progress.percentage:.1f}%")
    print(f"Speed: {progress.speed / 1024 / 1024:.1f} MB/s")
    print(f"ETA: {progress.eta:.0f} seconds")
    print("-" * 40)

# Use with downloader
downloader.download(url, progress_callback=detailed_progress_callback)
```

### Custom Progress Tracker

```python
from tubeharvest import ProgressTracker

class CustomProgressTracker(ProgressTracker):
    def __init__(self):
        self.downloads = {}
    
    def on_start(self, url: str, title: str):
        """Called when download starts."""
        self.downloads[url] = {
            "title": title,
            "start_time": time.time(),
            "status": "started"
        }
    
    def on_progress(self, url: str, progress: ProgressInfo):
        """Called during download progress."""
        self.downloads[url].update({
            "progress": progress.percentage,
            "speed": progress.speed
        })
    
    def on_complete(self, url: str, result: DownloadResult):
        """Called when download completes."""
        self.downloads[url]["status"] = "completed"
        self.downloads[url]["filename"] = result.filename

# Use custom tracker
tracker = CustomProgressTracker()
downloader = TubeHarvest(progress_tracker=tracker)
```

## ❌ Error Handling

### Exception Classes

```python
from tubeharvest.exceptions import (
    TubeHarvestError,
    DownloadError,
    NetworkError,
    FormatError,
    AuthenticationError
)

class TubeHarvestError(Exception):
    """Base exception for TubeHarvest."""
    pass

class DownloadError(TubeHarvestError):
    """Download-related errors."""
    pass

class NetworkError(TubeHarvestError):
    """Network-related errors."""
    pass

class FormatError(TubeHarvestError):
    """Format-related errors."""
    pass

class AuthenticationError(TubeHarvestError):
    """Authentication-related errors."""
    pass
```

### Error Handling Example

```python
from tubeharvest import TubeHarvest
from tubeharvest.exceptions import DownloadError, NetworkError

downloader = TubeHarvest()

try:
    result = downloader.download("https://www.youtube.com/watch?v=VIDEO_ID")
except NetworkError as e:
    print(f"Network error: {e}")
except DownloadError as e:
    print(f"Download error: {e}")
except Exception as e:
    print(f"Unexpected error: {e}")
```

### Retry Logic

```python
import time
from tubeharvest.exceptions import NetworkError

def download_with_retry(downloader, url, max_retries=3):
    """Download with retry logic."""
    for attempt in range(max_retries):
        try:
            return downloader.download(url)
        except NetworkError as e:
            if attempt < max_retries - 1:
                wait_time = 2 ** attempt  # Exponential backoff
                print(f"Retry {attempt + 1} in {wait_time} seconds...")
                time.sleep(wait_time)
            else:
                raise e
```

## 🔧 Integration Examples

### Flask Web Application

```python
from flask import Flask, request, jsonify
from tubeharvest import TubeHarvest

app = Flask(__name__)
downloader = TubeHarvest(output_dir="./downloads")

@app.route('/api/download', methods=['POST'])
def download_video():
    data = request.json
    url = data.get('url')
    quality = data.get('quality', 'best')
    
    try:
        result = downloader.download(url, quality=quality)
        return jsonify({
            'success': True,
            'filename': result.filename,
            'file_size': result.file_size
        })
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 400

if __name__ == '__main__':
    app.run(debug=True)
```

### Async Download Service

```python
import asyncio
from tubeharvest import TubeHarvest

class AsyncDownloadService:
    def __init__(self):
        self.downloader = TubeHarvest()
        self.download_queue = asyncio.Queue()
        self.active_downloads = {}
    
    async def add_download(self, url: str, options: dict = None):
        """Add download to queue."""
        download_id = self.generate_id()
        await self.download_queue.put({
            'id': download_id,
            'url': url,
            'options': options or {}
        })
        return download_id
    
    async def process_downloads(self):
        """Process download queue."""
        while True:
            download = await self.download_queue.get()
            asyncio.create_task(self._download(download))
    
    async def _download(self, download):
        """Execute download."""
        try:
            result = await asyncio.to_thread(
                self.downloader.download,
                download['url']
            )
            self.active_downloads[download['id']] = {
                'status': 'completed',
                'result': result
            }
        except Exception as e:
            self.active_downloads[download['id']] = {
                'status': 'error',
                'error': str(e)
            }

# Usage
service = AsyncDownloadService()
asyncio.run(service.process_downloads())
```

### GUI Application (Tkinter)

```python
import tkinter as tk
from tkinter import ttk, filedialog, messagebox
from tubeharvest import TubeHarvest
import threading

class TubeHarvestGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("TubeHarvest GUI")
        self.downloader = TubeHarvest()
        self.setup_ui()
    
    def setup_ui(self):
        # URL input
        tk.Label(self.root, text="YouTube URL:").pack(pady=5)
        self.url_entry = tk.Entry(self.root, width=60)
        self.url_entry.pack(pady=5)
        
        # Quality selection
        tk.Label(self.root, text="Quality:").pack(pady=5)
        self.quality_var = tk.StringVar(value="best")
        quality_combo = ttk.Combobox(
            self.root,
            textvariable=self.quality_var,
            values=["best", "1080", "720", "480", "360"]
        )
        quality_combo.pack(pady=5)
        
        # Download button
        self.download_btn = tk.Button(
            self.root,
            text="Download",
            command=self.start_download
        )
        self.download_btn.pack(pady=10)
        
        # Progress bar
        self.progress = ttk.Progressbar(
            self.root,
            length=400,
            mode='determinate'
        )
        self.progress.pack(pady=5)
        
        # Status label
        self.status_label = tk.Label(self.root, text="Ready")
        self.status_label.pack(pady=5)
    
    def start_download(self):
        url = self.url_entry.get()
        if not url:
            messagebox.showerror("Error", "Please enter a URL")
            return
        
        self.download_btn.config(state='disabled')
        self.progress['value'] = 0
        self.status_label.config(text="Starting download...")
        
        # Run download in separate thread
        thread = threading.Thread(target=self.download_video, args=(url,))
        thread.daemon = True
        thread.start()
    
    def download_video(self, url):
        def progress_callback(progress):
            self.root.after(0, self.update_progress, progress)
        
        try:
            result = self.downloader.download(
                url,
                quality=self.quality_var.get(),
                progress_callback=progress_callback
            )
            self.root.after(0, self.download_complete, result)
        except Exception as e:
            self.root.after(0, self.download_error, str(e))
    
    def update_progress(self, progress):
        self.progress['value'] = progress.percentage
        self.status_label.config(
            text=f"Downloading... {progress.percentage:.1f}%"
        )
    
    def download_complete(self, result):
        self.progress['value'] = 100
        self.status_label.config(text=f"Download complete: {result.filename}")
        self.download_btn.config(state='normal')
        messagebox.showinfo("Success", "Download completed!")
    
    def download_error(self, error):
        self.status_label.config(text=f"Error: {error}")
        self.download_btn.config(state='normal')
        messagebox.showerror("Error", f"Download failed: {error}")

if __name__ == "__main__":
    root = tk.Tk()
    app = TubeHarvestGUI(root)
    root.mainloop()
```

## 🚀 Advanced Usage

### Custom Format Selector

```python
from tubeharvest import FormatSelector

class CustomFormatSelector(FormatSelector):
    def select_format(self, formats, quality_preference):
        """Custom format selection logic."""
        # Prefer VP9 codec for web content
        vp9_formats = [f for f in formats if f.vcodec == 'vp9']
        if vp9_formats:
            return self.select_best_quality(vp9_formats, quality_preference)
        
        # Fallback to default selection
        return super().select_format(formats, quality_preference)

# Use custom selector
downloader = TubeHarvest(format_selector=CustomFormatSelector())
```

### Metadata Extraction

```python
from tubeharvest import MetadataExtractor

extractor = MetadataExtractor()

# Extract video information
info = extractor.extract_info("https://www.youtube.com/watch?v=VIDEO_ID")

print(f"Title: {info.title}")
print(f"Uploader: {info.uploader}")
print(f"Duration: {info.duration}")
print(f"View count: {info.view_count}")
print(f"Upload date: {info.upload_date}")

# Get available formats
formats = extractor.get_formats("https://www.youtube.com/watch?v=VIDEO_ID")
for fmt in formats:
    print(f"Format: {fmt.format_id}, Quality: {fmt.quality}, Extension: {fmt.ext}")
```

### Plugin System

```python
from tubeharvest.plugins import BasePlugin

class ThumbnailPlugin(BasePlugin):
    """Plugin to download video thumbnails."""
    
    def on_download_start(self, url, options):
        """Called before download starts."""
        if options.thumbnail:
            self.download_thumbnail(url, options)
    
    def download_thumbnail(self, url, options):
        """Download video thumbnail."""
        # Implementation here
        pass

# Register plugin
downloader = TubeHarvest()
downloader.register_plugin(ThumbnailPlugin())
```

### Custom Output Processor

```python
from tubeharvest import OutputProcessor

class CloudUploadProcessor(OutputProcessor):
    """Upload downloaded files to cloud storage."""
    
    def process_output(self, result):
        """Process downloaded file."""
        if result.success:
            self.upload_to_cloud(result.filepath)
            # Optionally remove local file
            os.remove(result.filepath)
    
    def upload_to_cloud(self, filepath):
        """Upload file to cloud storage."""
        # Implementation here
        pass

# Use custom processor
downloader = TubeHarvest(output_processor=CloudUploadProcessor())
```

## 📝 API Reference Summary

### Main Classes

| Class | Description |
|-------|-------------|
| `TubeHarvest` | Main downloader class |
| `DownloadOptions` | Configuration container |
| `ProgressInfo` | Progress information |
| `DownloadResult` | Download result data |
| `MetadataExtractor` | Video information extraction |
| `FormatSelector` | Format/quality selection |

### Key Methods

| Method | Description |
|--------|-------------|
| `download()` | Download single video |
| `download_playlist()` | Download playlist |
| `download_batch()` | Download multiple URLs |
| `extract_audio()` | Extract audio only |
| `get_info()` | Extract video metadata |

### Configuration Options

| Option | Type | Description |
|--------|------|-------------|
| `quality` | str | Video quality preference |
| `format` | str | Output format |
| `audio_only` | bool | Extract audio only |
| `subtitles` | bool | Download subtitles |
| `metadata` | bool | Save metadata |
| `output_dir` | str | Output directory |

---

*For usage examples and integration guides, see the [User Guide](User-Guide) and [Developer Guide](Developer-Guide).* 