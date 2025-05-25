# ❓ Frequently Asked Questions (FAQ)

Common questions and answers about TubeHarvest. If you can't find what you're looking for, check the [Troubleshooting Guide](Troubleshooting) or visit our [GitHub Discussions](https://github.com/msadeqsirjani/TubeHarvest/discussions).

## 📖 Table of Contents

1. [General Questions](#general-questions)
2. [Installation & Setup](#installation--setup)
3. [Download Features](#download-features)
4. [Quality & Formats](#quality--formats)
5. [Interactive Mode](#interactive-mode)
6. [Configuration](#configuration)
7. [Performance](#performance)
8. [Errors & Troubleshooting](#errors--troubleshooting)
9. [Legal & Ethics](#legal--ethics)

## 🎯 General Questions

### What is TubeHarvest?

TubeHarvest is a comprehensive YouTube downloader with a beautiful interactive console interface. It supports downloading videos, playlists, and audio extraction with multiple format options and quality settings.

### How is TubeHarvest different from other YouTube downloaders?

- **Interactive Mode**: Beautiful console interface with real-time progress
- **Rich Features**: Subtitles, metadata, thumbnails, and batch processing
- **Flexible Configuration**: Extensive customization options
- **Developer-Friendly**: Python API for integration
- **Modern Architecture**: Built with best practices and extensibility

### Is TubeHarvest free?

Yes, TubeHarvest is completely free and open-source under the MIT License.

### What platforms does TubeHarvest support?

TubeHarvest works on:
- **Windows** (10, 11)
- **macOS** (10.14+)
- **Linux** (Most distributions)
- **Python 3.8+** required

## 📦 Installation & Setup

### How do I install TubeHarvest?

```bash
# Using pip (recommended)
pip install tubeharvest

# Using pipx (isolated environment)
pipx install tubeharvest

# From source
git clone https://github.com/msadeqsirjani/TubeHarvest.git
cd TubeHarvest
pip install -e .
```

### Do I need additional software?

For basic video downloads, no additional software is required. For advanced features:
- **FFmpeg**: Required for format conversion and audio extraction
- **Python 3.8+**: Required runtime

### How do I update TubeHarvest?

```bash
# Update via pip
pip install --upgrade tubeharvest

# Update from source
git pull origin main
pip install -e .
```

### Why can't I run `tubeharvest` command?

This usually means the installation directory isn't in your PATH:

```bash
# Try these alternatives
python -m tubeharvest
python3 -m tubeharvest

# Or find installation path
pip show tubeharvest
```

## 📥 Download Features

### Can I download entire playlists?

Yes! TubeHarvest supports playlist downloads:

```bash
# Download entire playlist
tubeharvest -u "https://www.youtube.com/playlist?list=PLAYLIST_ID"

# Limit number of videos
tubeharvest -u "PLAYLIST_URL" --max-videos 10
```

### How do I download only audio?

```bash
# Extract as MP3
tubeharvest -u "VIDEO_URL" -f mp3 --audio-only

# Extract as high-quality M4A
tubeharvest -u "VIDEO_URL" -f m4a --audio-only -q best
```

### Can I download multiple videos at once?

Yes, several ways:

```bash
# Multiple URLs
tubeharvest -u "URL1" "URL2" "URL3"

# From file
tubeharvest --batch-file urls.txt

# Interactive mode queue
tubeharvest -i  # Add multiple URLs to queue
```

### Does TubeHarvest support subtitles?

Yes, comprehensive subtitle support:

```bash
# Download with automatic subtitles
tubeharvest -u "VIDEO_URL" --subtitles

# Specific language
tubeharvest -u "VIDEO_URL" --subtitles --subtitle-lang en

# All available subtitles
tubeharvest -u "VIDEO_URL" --all-subs
```

### Can I download private or unlisted videos?

TubeHarvest can download unlisted videos if you have the URL. For private videos, you may need to provide authentication cookies.

## 🎬 Quality & Formats

### What video qualities are available?

Available qualities depend on the video, but typically:
- **4K** (2160p)
- **1080p** (Full HD)
- **720p** (HD)
- **480p** (SD)
- **360p** (Mobile)

```bash
# Specific quality
tubeharvest -u "VIDEO_URL" -q 1080

# Best available
tubeharvest -u "VIDEO_URL" -q best
```

### What formats does TubeHarvest support?

**Video Formats:**
- MP4 (recommended for compatibility)
- WebM (smaller file sizes)
- MKV (highest quality)

**Audio Formats:**
- MP3 (universal compatibility)
- M4A (high quality)
- AAC (streaming optimized)

### Why isn't 4K available for some videos?

4K availability depends on:
- Original upload quality
- YouTube's processing
- Copyright restrictions
- Channel settings

### How do I get the smallest file size?

```bash
# Lower quality with efficient format
tubeharvest -u "VIDEO_URL" -q 480 -f webm

# Audio only
tubeharvest -u "VIDEO_URL" --audio-only -f mp3
```

## 🎨 Interactive Mode

### How do I launch interactive mode?

```bash
tubeharvest -i
# or
tubeharvest --interactive
```

### Can I use interactive mode for batch downloads?

Yes! Interactive mode has a download queue feature:
1. Launch interactive mode
2. Add multiple URLs to queue
3. Configure batch settings
4. Start batch download

### How do I change themes in interactive mode?

Themes can be configured in the settings:
1. Launch interactive mode
2. Navigate to Settings
3. Select Theme option
4. Choose from available themes

### Why is interactive mode slow on my terminal?

Performance can be affected by:
- Terminal application (try modern terminals)
- System resources
- Network speed
- Large playlists

## ⚙️ Configuration

### Where are configuration files stored?

Default locations:
- **Linux/macOS**: `~/.config/tubeharvest/config.yaml`
- **Windows**: `%APPDATA%\TubeHarvest\config.yaml`

### How do I reset configuration to defaults?

```bash
# Reset all settings
tubeharvest --reset-config

# Generate new default config
tubeharvest --generate-config
```

### Can I have different settings for different use cases?

Yes! Use profiles:

```bash
# Create music profile
tubeharvest --create-profile music

# Use specific profile
tubeharvest --profile music -u "MUSIC_URL"
```

### How do I set a default download directory?

Edit configuration file or use command:

```bash
# Set default directory
tubeharvest --set-output-dir "~/Downloads/YouTube"
```

## ⚡ Performance

### How can I speed up downloads?

```bash
# Increase concurrent downloads
tubeharvest -u "PLAYLIST_URL" --concurrent-downloads 3

# Use lower quality for faster downloads
tubeharvest -u "VIDEO_URL" -q 720

# Skip existing files
tubeharvest --skip-existing
```

### Why are downloads slow?

Common causes:
- Network speed limitations
- YouTube's rate limiting
- High quality/large files
- Server load

### Can I limit bandwidth usage?

```bash
# Limit download speed
tubeharvest -u "VIDEO_URL" --rate-limit 1M

# 1M = 1 MB/s, 500K = 500 KB/s
```

### How much disk space do I need?

Approximate sizes:
- **1080p video (10 min)**: 100-300 MB
- **720p video (10 min)**: 50-150 MB
- **Audio MP3 (10 min)**: 7-15 MB

## 🚨 Errors & Troubleshooting

### "Video unavailable" error

Common solutions:
1. Check if video exists and is public
2. Update TubeHarvest to latest version
3. Try different quality setting
4. Check network connection

### "Format not available" error

```bash
# Try different format
tubeharvest -u "VIDEO_URL" -f mp4

# List available formats
tubeharvest -u "VIDEO_URL" --list-formats
```

### Permission denied errors

```bash
# Check directory permissions
ls -la ~/Downloads

# Use different output directory
tubeharvest -u "VIDEO_URL" -o ~/Desktop
```

### Python/pip not found

Ensure Python is installed and in PATH:
```bash
# Check Python installation
python --version
python3 --version

# Install Python (Linux)
sudo apt install python3 python3-pip

# Install Python (macOS with Homebrew)
brew install python
```

### FFmpeg not found

```bash
# Install FFmpeg (Linux)
sudo apt install ffmpeg

# Install FFmpeg (macOS)
brew install ffmpeg

# Install FFmpeg (Windows)
# Download from https://ffmpeg.org/download.html
```

### Memory/disk space errors

1. Check available disk space
2. Use lower quality settings
3. Clear temporary files
4. Close other applications

## ⚖️ Legal & Ethics

### Is downloading YouTube videos legal?

Legal considerations:
- **Personal use**: Generally acceptable for offline viewing
- **Copyrighted content**: Respect copyright laws
- **Terms of Service**: YouTube's ToS prohibits downloading
- **Fair use**: Educational/research purposes may be permitted

**Always ensure you have permission to download content.**

### Can I redistribute downloaded content?

No, unless you have explicit permission from the copyright holder. Downloaded content is for personal use only.

### Does TubeHarvest respect age restrictions?

TubeHarvest follows YouTube's public API restrictions, but cannot bypass age verification that requires sign-in.

### What about monetized content?

Downloading monetized content for personal use is a legal gray area. Consider supporting creators through official channels.

### Can I download copyrighted music?

Downloading copyrighted music without permission may violate copyright laws. Consider using official music streaming services.

## 🔧 Advanced Usage

### How do I integrate TubeHarvest into my Python project?

```python
from tubeharvest import TubeHarvest

downloader = TubeHarvest(
    output_dir="./downloads",
    quality="1080"
)

result = downloader.download("https://www.youtube.com/watch?v=VIDEO_ID")
```

See [API Reference](API-Reference) for complete documentation.

### Can I create custom plugins?

Yes! TubeHarvest has a plugin system:

```python
from tubeharvest.plugins import BasePlugin

class MyPlugin(BasePlugin):
    def on_download_complete(self, result):
        # Custom post-processing
        pass
```

### How do I automate downloads?

```bash
# Using cron (Linux/macOS)
# Add to crontab: 0 2 * * * tubeharvest --batch-file ~/urls.txt

# Using Task Scheduler (Windows)
# Create scheduled task to run tubeharvest command
```

### Can I use TubeHarvest on a server?

Yes, TubeHarvest works on headless servers:

```bash
# Run without interactive mode
tubeharvest -u "VIDEO_URL" --no-interactive

# Batch processing
tubeharvest --batch-file urls.txt --quiet
```

## 🆘 Still Need Help?

### Getting Support

1. **Check Documentation**: [User Guide](User-Guide), [Troubleshooting](Troubleshooting)
2. **Search Issues**: [GitHub Issues](https://github.com/msadeqsirjani/TubeHarvest/issues)
3. **Ask Questions**: [GitHub Discussions](https://github.com/msadeqsirjani/TubeHarvest/discussions)
4. **Report Bugs**: [New Issue](https://github.com/msadeqsirjani/TubeHarvest/issues/new)

### Before Reporting Issues

Include:
- TubeHarvest version (`tubeharvest --version`)
- Operating system and version
- Python version
- Complete error message
- Commands that caused the issue

### Contributing

Want to improve TubeHarvest?
- Check [Developer Guide](Developer-Guide)
- See [Contributing Guidelines](https://github.com/msadeqsirjani/TubeHarvest/blob/main/CONTRIBUTING.md)
- Join our community discussions

---

*This FAQ is regularly updated. For the latest information, visit our [documentation](Home) or [GitHub repository](https://github.com/msadeqsirjani/TubeHarvest).* 