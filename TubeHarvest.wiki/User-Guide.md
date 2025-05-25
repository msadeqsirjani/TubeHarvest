# 📘 User Guide

Welcome to the comprehensive TubeHarvest User Guide! This guide covers everything you need to know to master YouTube downloading with TubeHarvest.

## 📖 Table of Contents

1. [Overview](#overview)
2. [Basic Usage](#basic-usage)
3. [Download Modes](#download-modes)
4. [Format Selection](#format-selection)
5. [Quality Settings](#quality-settings)
6. [Advanced Features](#advanced-features)
7. [Batch Operations](#batch-operations)
8. [File Management](#file-management)
9. [Best Practices](#best-practices)

## 🎯 Overview

TubeHarvest is a powerful YouTube downloader that supports:
- Single video and playlist downloads
- Multiple output formats (MP4, MP3, WebM, MKV, M4A)
- Quality selection from 360p to 4K
- Interactive console interface
- Batch processing capabilities
- Subtitle and metadata extraction

## 🚀 Basic Usage

### Command Line Interface

```bash
# Download a single video
tubeharvest -u "https://www.youtube.com/watch?v=VIDEO_ID"

# Launch interactive mode
tubeharvest -i

# Download with specific options
tubeharvest -u "VIDEO_URL" -q 1080 -f mp4 -o "~/Downloads"
```

### Interactive Mode

The interactive mode provides a user-friendly interface:

```bash
tubeharvest -i
```

**Interactive Features:**
- 🎨 Beautiful console interface
- 📊 Real-time progress tracking
- 🎯 Smart quality suggestions
- 📋 Download queue management
- ⚙️ Configuration wizard

## 📥 Download Modes

### Single Video Download

Download individual YouTube videos:

```bash
# Basic download
tubeharvest -u "https://www.youtube.com/watch?v=VIDEO_ID"

# With custom settings
tubeharvest -u "VIDEO_URL" -q 720 -f mp4 --subtitles
```

### Playlist Download

Download entire playlists:

```bash
# Download all videos in playlist
tubeharvest -u "https://www.youtube.com/playlist?list=PLAYLIST_ID"

# Limit number of videos
tubeharvest -u "PLAYLIST_URL" --max-videos 10
```

### Channel Download

Download videos from a channel:

```bash
# Download all channel videos
tubeharvest -u "https://www.youtube.com/@CHANNEL_NAME"

# Download recent uploads only
tubeharvest -u "CHANNEL_URL" --max-videos 5
```

### Audio-Only Download

Extract audio from videos:

```bash
# Download as MP3
tubeharvest -u "VIDEO_URL" -f mp3 --audio-only

# High-quality audio
tubeharvest -u "VIDEO_URL" -f m4a --audio-only -q best
```

## 🎬 Format Selection

### Video Formats

| Format | Extension | Best For | File Size |
|--------|-----------|----------|-----------|
| MP4 | `.mp4` | General use, compatibility | Medium |
| WebM | `.webm` | Web streaming, smaller files | Small |
| MKV | `.mkv` | High quality, multiple streams | Large |

```bash
# Download as MP4 (default)
tubeharvest -u "VIDEO_URL" -f mp4

# Download as WebM
tubeharvest -u "VIDEO_URL" -f webm

# Download as MKV
tubeharvest -u "VIDEO_URL" -f mkv
```

### Audio Formats

| Format | Extension | Best For | Quality |
|--------|-----------|----------|---------|
| MP3 | `.mp3` | Universal compatibility | Good |
| M4A | `.m4a` | Apple devices, high quality | Excellent |
| AAC | `.aac` | Streaming, small files | Good |

```bash
# Extract as MP3
tubeharvest -u "VIDEO_URL" -f mp3 --audio-only

# Extract as M4A
tubeharvest -u "VIDEO_URL" -f m4a --audio-only

# Extract as AAC
tubeharvest -u "VIDEO_URL" -f aac --audio-only
```

## 🎯 Quality Settings

### Video Quality Options

| Quality | Resolution | Typical Use Case |
|---------|------------|------------------|
| `best` | Highest available | Best quality |
| `1080` | 1920x1080 (Full HD) | Standard viewing |
| `720` | 1280x720 (HD) | Good quality, manageable size |
| `480` | 854x480 (SD) | Older devices, slow internet |
| `360` | 640x360 | Low bandwidth, mobile |

```bash
# Download best available quality
tubeharvest -u "VIDEO_URL" -q best

# Download specific quality
tubeharvest -u "VIDEO_URL" -q 1080

# Download with fallback
tubeharvest -u "VIDEO_URL" -q "1080/720/best"
```

### Audio Quality

```bash
# Best audio quality
tubeharvest -u "VIDEO_URL" --audio-only -q best

# Specific audio bitrate
tubeharvest -u "VIDEO_URL" --audio-only --audio-quality 320
```

## 🔧 Advanced Features

### Subtitle Download

```bash
# Download with automatic subtitles
tubeharvest -u "VIDEO_URL" --subtitles

# Download specific language
tubeharvest -u "VIDEO_URL" --subtitles --subtitle-lang en

# Download all available subtitles
tubeharvest -u "VIDEO_URL" --subtitles --all-subs
```

### Metadata Extraction

```bash
# Save metadata with video
tubeharvest -u "VIDEO_URL" --metadata

# Extract thumbnail
tubeharvest -u "VIDEO_URL" --thumbnail

# Full metadata package
tubeharvest -u "VIDEO_URL" --metadata --thumbnail --subtitles
```

### Custom Naming

```bash
# Custom filename
tubeharvest -u "VIDEO_URL" --filename "My Custom Name"

# Template-based naming
tubeharvest -u "VIDEO_URL" --filename-template "%(title)s_%(uploader)s"

# Include upload date
tubeharvest -u "VIDEO_URL" --filename-template "%(upload_date)s_%(title)s"
```

### Download Filtering

```bash
# Download videos newer than date
tubeharvest -u "PLAYLIST_URL" --date-after 20240101

# Download videos older than date
tubeharvest -u "PLAYLIST_URL" --date-before 20241231

# Filter by duration
tubeharvest -u "PLAYLIST_URL" --min-duration 300 --max-duration 3600
```

## 📦 Batch Operations

### Multiple URLs

```bash
# Download multiple videos
tubeharvest -u "VIDEO_URL_1" "VIDEO_URL_2" "VIDEO_URL_3"

# From file
tubeharvest --batch-file urls.txt
```

### Download Queue

In interactive mode:
1. Add multiple URLs to queue
2. Configure settings for batch
3. Start batch download
4. Monitor progress

### Parallel Downloads

```bash
# Download with multiple threads
tubeharvest -u "PLAYLIST_URL" --concurrent-downloads 3

# Limit bandwidth per download
tubeharvest -u "PLAYLIST_URL" --rate-limit 1M
```

## 📁 File Management

### Output Organization

```bash
# Custom output directory
tubeharvest -u "VIDEO_URL" -o "~/Downloads/YouTube"

# Organize by uploader
tubeharvest -u "VIDEO_URL" -o "~/Downloads/%(uploader)s"

# Organize by date
tubeharvest -u "VIDEO_URL" -o "~/Downloads/%(upload_date)s"
```

### Archive Management

```bash
# Keep download history
tubeharvest -u "PLAYLIST_URL" --download-archive history.txt

# Skip already downloaded
tubeharvest -u "PLAYLIST_URL" --download-archive history.txt --continue
```

### Storage Options

```bash
# Check available space before download
tubeharvest -u "VIDEO_URL" --check-space

# Set maximum file size
tubeharvest -u "VIDEO_URL" --max-filesize 1G

# Minimum file size
tubeharvest -u "VIDEO_URL" --min-filesize 10M
```

## 🎨 User Interface

### Console Interface

TubeHarvest provides a rich console experience:
- 🎯 Colorized output
- 📊 Progress bars with ETA
- 📈 Download statistics
- 🎨 Interactive prompts

### Configuration Management

```bash
# Save current settings as default
tubeharvest --save-config

# Load configuration file
tubeharvest --config config.yaml

# Reset to defaults
tubeharvest --reset-config
```

## 🎯 Best Practices

### Performance Optimization

1. **Use appropriate quality**: Don't download 4K if you don't need it
2. **Batch downloads**: More efficient than individual downloads
3. **Parallel downloads**: Use `--concurrent-downloads` for playlists
4. **Storage management**: Regularly clean up downloads

### Quality Considerations

1. **Video Quality**: 1080p is sufficient for most use cases
2. **Audio Quality**: 320kbps MP3 or M4A for music
3. **Format Selection**: MP4 for videos, MP3 for audio
4. **Subtitle Inclusion**: Always download when available

### Organization Tips

1. **Folder Structure**: Organize by content type or creator
2. **Naming Convention**: Use consistent filename templates
3. **Archive Tracking**: Keep download history for large collections
4. **Metadata Preservation**: Save video information for reference

### Legal & Ethical Usage

1. **Respect Copyright**: Only download content you have permission to use
2. **Personal Use**: Keep downloads for personal/educational purposes
3. **Creator Support**: Consider supporting creators through official channels
4. **Terms of Service**: Respect YouTube's ToS and community guidelines

## 🔍 Common Workflows

### Music Collection
```bash
# Download music playlist
tubeharvest -u "MUSIC_PLAYLIST_URL" \
  -f mp3 \
  --audio-only \
  --audio-quality 320 \
  --metadata \
  --thumbnail \
  -o "~/Music/YouTube/%(uploader)s"
```

### Educational Content
```bash
# Download educational videos
tubeharvest -u "COURSE_PLAYLIST_URL" \
  -q 720 \
  --subtitles \
  --metadata \
  --filename-template "%(playlist_index)02d_%(title)s" \
  -o "~/Education/%(playlist_title)s"
```

### Podcast Archive
```bash
# Archive podcast episodes
tubeharvest -u "PODCAST_CHANNEL_URL" \
  -f m4a \
  --audio-only \
  --metadata \
  --download-archive podcast_archive.txt \
  -o "~/Podcasts/%(uploader)s"
```

### Video Backup
```bash
# Backup channel content
tubeharvest -u "CHANNEL_URL" \
  -q best \
  --metadata \
  --thumbnail \
  --subtitles \
  --download-archive channel_backup.txt \
  -o "~/Backup/%(uploader)s/%(upload_date)s"
```

## 📞 Getting Help

- **Interactive Help**: Use `tubeharvest --help` for quick reference
- **Documentation**: Check the [CLI Reference](CLI-Reference) for detailed options
- **Troubleshooting**: See [Troubleshooting Guide](Troubleshooting) for common issues
- **Community**: Visit our [GitHub Discussions](https://github.com/msadeqsirjani/TubeHarvest/discussions)

---

*For technical details and advanced configuration, see the [Developer Guide](Developer-Guide) and [Configuration Guide](Configuration-Guide).* 