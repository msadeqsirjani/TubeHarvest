# TubeHarvest 🎬

A comprehensive YouTube downloader built with Python featuring a **beautiful interactive console interface**. TubeHarvest allows you to easily download videos, playlists, and audio from YouTube with extensive customization options and a modern user experience.

## ✨ Features

### 🎯 Core Functionality
- **Versatile Download Options**: Download video with audio, video only, or audio only
- **Quality Selection**: Choose video resolution (e.g., 1080p, 720p, 480p)
- **Playlist Support**: Download entire YouTube playlists with a single command
- **Subtitle & Metadata**: Download subtitles and video metadata
- **Multiple Formats**: Support for MP4, MP3, WebM, and more
- **Performance Optimization**: Multithreaded downloads for playlists
- **Resumable Downloads**: Continue interrupted downloads

### 🎨 Enhanced User Experience
- **🌟 Beautiful Interactive Console**: Rich, colorful interface with emoji icons
- **📋 Interactive Setup Wizard**: Step-by-step configuration with smart defaults
- **📊 Real-time Progress Tracking**: Beautiful progress bars with live statistics
- **🎬 Video Information Display**: Rich metadata presentation
- **⚡ Smart Input Validation**: Instant feedback on URLs and settings
- **🔄 Error Recovery**: Graceful error handling with retry options
- **📈 Download Statistics**: Detailed completion reports

## Installation

```bash
# Clone the repository
git clone https://github.com/msadeqsirjani/TubeHarvest.git
cd TubeHarvest

# Install requirements
pip install -r requirements.txt
```

## 🚀 Quick Start

### Interactive Mode (Recommended)
Launch the beautiful interactive interface:
```bash
# Quick launch with interactive UI
./scripts/tubeharvest-gui

# Or use the main module
python -m tubeharvest --interactive

# Or if installed via pip
tubeharvest-gui
```

### Command Line Mode
```bash
# Basic usage
python -m tubeharvest -u "https://www.youtube.com/watch?v=VIDEO_ID"

# Audio only download in MP3 format
python -m tubeharvest -u "https://www.youtube.com/watch?v=VIDEO_ID" --audio-only --format mp3

# Download playlist with specific quality
python -m tubeharvest -u "https://www.youtube.com/playlist?list=PLAYLIST_ID" --quality 720

# Download with subtitles and custom output directory
python -m tubeharvest -u "https://www.youtube.com/watch?v=VIDEO_ID" --subtitles --output-dir "~/Videos"

# If installed via pip
tubeharvest -u "https://www.youtube.com/watch?v=VIDEO_ID"
```

For a complete list of options, run:
```bash
python -m tubeharvest --help
# or
tubeharvest --help
```

### 🎭 UI Demo
Want to see the beautiful interface in action? Run the demo:
```bash
python examples/ui_demo.py
```

## 🎨 What's New in v2.0

- **🌈 Rich Console Interface**: Beautiful colors, panels, and progress bars using the Rich library
- **🤖 Interactive Setup Wizard**: Step-by-step configuration with smart prompts
- **📊 Real-time Progress**: Live progress tracking with multiple concurrent downloads
- **🎬 Enhanced Video Info**: Beautiful display of video metadata and statistics
- **⚡ Smart Validation**: Instant feedback on URLs and configuration
- **🔄 Error Recovery**: Graceful error handling with retry options
- **📈 Download Statistics**: Comprehensive completion reports with success rates

## 📋 Requirements

- Python 3.7+
- yt-dlp
- rich (for beautiful console interface)
- inquirer (for interactive prompts)
- prompt-toolkit (for enhanced input)
- tqdm (for progress bars)
- ffmpeg (for some format conversions)

## License

MIT 