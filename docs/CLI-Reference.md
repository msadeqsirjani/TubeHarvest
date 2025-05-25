# 🖥️ Command Line Reference

Complete reference for TubeHarvest command line interface. This guide covers all available options, arguments, and usage patterns.

## 📋 Quick Reference

```bash
tubeharvest [OPTIONS] [-u URL | -i]
```

## 🚀 Basic Usage

### Entry Points

TubeHarvest can be invoked in several ways:

```bash
# Installed package
tubeharvest [options]

# Python module
python -m tubeharvest [options]

# Interactive GUI (if installed from source)
tubeharvest-gui
./scripts/tubeharvest-gui
```

### Get Help

```bash
# Show help message
tubeharvest --help
tubeharvest -h

# Show version
tubeharvest --version
```

## 📖 Command Options

### Required Arguments

#### URL or Interactive Mode

You must specify either a URL or interactive mode:

```bash
# Download specific video/playlist
tubeharvest -u "https://www.youtube.com/watch?v=VIDEO_ID"

# Launch interactive mode  
tubeharvest -i
tubeharvest --interactive
```

### Output Options

#### Output Directory

```bash
# Specify output directory
tubeharvest -u "URL" -o ~/Downloads
tubeharvest -u "URL" --output-dir ~/Downloads

# Default: ./downloads/
```

#### Custom Filename

```bash
# Custom filename (without extension)
tubeharvest -u "URL" --filename "my_video"

# Default: Uses video title
```

### Format Options

#### Output Format

```bash
# Specify output format
tubeharvest -u "URL" -f mp4    # Video (default)
tubeharvest -u "URL" -f mp3    # Audio  
tubeharvest -u "URL" -f webm   # Web video
tubeharvest -u "URL" -f mkv    # High quality video
tubeharvest -u "URL" -f m4a    # Audio (Apple)

# Long form
tubeharvest -u "URL" --format mp4
```

**Available Formats:**
- `mp4` - Standard video format (default)
- `mp3` - Audio format  
- `webm` - Web-optimized video
- `mkv` - High-quality video container
- `m4a` - Audio format (better for Apple devices)

### Quality Options

#### Video Quality

```bash
# Specify quality
tubeharvest -u "URL" -q best   # Best available (default)
tubeharvest -u "URL" -q 1080   # 1080p
tubeharvest -u "URL" -q 720    # 720p
tubeharvest -u "URL" -q 480    # 480p
tubeharvest -u "URL" -q 360    # 360p
tubeharvest -u "URL" -q 240    # 240p
tubeharvest -u "URL" -q 144    # 144p

# Long form
tubeharvest -u "URL" --quality 1080
```

**Quality Options:**
- `best` - Highest available quality (default)
- `1080`, `720`, `480`, `360`, `240`, `144` - Specific resolutions
- `worst` - Lowest available quality

### Content Type Options

#### Audio/Video Selection

```bash
# Download audio only
tubeharvest -u "URL" --audio-only

# Download video only (no audio)
tubeharvest -u "URL" --video-only

# Default: Download video with audio
```

### Additional Content Options

#### Subtitles

```bash
# Download available subtitles
tubeharvest -u "URL" --subtitles

# Default: No subtitles
```

#### Metadata

```bash
# Save video metadata to JSON
tubeharvest -u "URL" --metadata

# Default: No metadata file
```

### Performance Options

#### Multi-threading

```bash
# Specify number of worker threads
tubeharvest -u "URL" --workers 4    # Default
tubeharvest -u "URL" --workers 1    # Single thread
tubeharvest -u "URL" --workers 8    # High performance

# Valid range: 1-8 workers
```

## 🎯 Common Command Patterns

### Single Video Downloads

```bash
# Basic download
tubeharvest -u "https://www.youtube.com/watch?v=VIDEO_ID"

# High quality MP4
tubeharvest -u "VIDEO_URL" -f mp4 -q 1080

# Audio extraction
tubeharvest -u "VIDEO_URL" -f mp3 --audio-only

# With subtitles and metadata
tubeharvest -u "VIDEO_URL" --subtitles --metadata

# Custom location and filename
tubeharvest -u "VIDEO_URL" -o ~/Videos --filename "tutorial_01"
```

### Playlist Downloads

```bash
# Download entire playlist
tubeharvest -u "https://www.youtube.com/playlist?list=PLAYLIST_ID"

# Playlist as audio files
tubeharvest -u "PLAYLIST_URL" -f mp3 --audio-only

# High quality playlist
tubeharvest -u "PLAYLIST_URL" -q 1080 --subtitles --metadata

# Playlist to specific directory
tubeharvest -u "PLAYLIST_URL" -o ~/Courses/Python_Tutorial
```

### Channel Downloads

```bash
# Download from channel
tubeharvest -u "https://www.youtube.com/c/CHANNEL_NAME"

# Recent videos only (latest uploads)
tubeharvest -u "CHANNEL_URL" --limit 10

# Channel audio collection
tubeharvest -u "CHANNEL_URL" -f mp3 --audio-only
```

### Quality and Size Management

```bash
# Bandwidth-conscious downloads
tubeharvest -u "URL" -q 480 -f webm

# Maximum quality
tubeharvest -u "URL" -q best -f mkv

# Mobile-friendly
tubeharvest -u "URL" -q 360 -f mp4

# Audio quality focus
tubeharvest -u "URL" -f m4a --audio-only -q best
```

## 🔧 Advanced Usage

### Batch Operations

```bash
# Multiple URLs (interactive selection)
tubeharvest -i
# Then paste multiple URLs

# Process URL list from file
# (Feature for future versions)
```

### Error Handling

```bash
# Verbose output for debugging
tubeharvest -u "URL" --verbose

# Continue on errors (for playlists)
tubeharvest -u "PLAYLIST_URL" --ignore-errors

# Retry failed downloads
tubeharvest -u "URL" --retry 3
```

### Output Organization

```bash
# Organize by content type
tubeharvest -u "URL" --organize

# Results in:
# downloads/
# ├── videos/
# ├── audio/  
# └── metadata/

# Custom directory structure
tubeharvest -u "URL" -o "~/Media/%(title)s.%(ext)s"
```

## 📊 Exit Codes

TubeHarvest returns specific exit codes:

| Code | Meaning |
|------|---------|
| `0` | Success - All downloads completed |
| `1` | Error - General error occurred |
| `2` | Error - Invalid arguments |
| `3` | Error - Network/connection issues |
| `4` | Error - File system issues |
| `130` | Interrupted - User cancelled (Ctrl+C) |

## 🌐 Environment Variables

Configure TubeHarvest behavior with environment variables:

```bash
# Default output directory
export TUBEHARVEST_OUTPUT_DIR="~/Downloads/YouTube"

# Default quality
export TUBEHARVEST_QUALITY="720"

# Default format
export TUBEHARVEST_FORMAT="mp4"

# Default workers
export TUBEHARVEST_WORKERS="4"

# Configuration file location
export TUBEHARVEST_CONFIG="~/.config/tubeharvest/config.json"
```

## 📁 Configuration Files

### Config File Location

TubeHarvest looks for configuration files in:

```bash
# Linux/macOS
~/.config/tubeharvest/config.json

# Windows
%APPDATA%/tubeharvest/config.json

# Current directory
./tubeharvest.config.json
```

### Sample Configuration

```json
{
  "default_output_dir": "~/Downloads/TubeHarvest",
  "default_format": "mp4",
  "default_quality": "best",
  "default_workers": 4,
  "organize_files": true,
  "download_subtitles": false,
  "save_metadata": false,
  "retry_attempts": 3,
  "user_agent": "TubeHarvest/2.0.0"
}
```

## 🚨 Important Notes

### URL Formats

Supported YouTube URL formats:

```bash
# Video URLs
https://www.youtube.com/watch?v=VIDEO_ID
https://youtu.be/VIDEO_ID
https://m.youtube.com/watch?v=VIDEO_ID

# Playlist URLs  
https://www.youtube.com/playlist?list=PLAYLIST_ID
https://www.youtube.com/watch?v=VIDEO_ID&list=PLAYLIST_ID

# Channel URLs
https://www.youtube.com/c/CHANNEL_NAME
https://www.youtube.com/channel/CHANNEL_ID
https://www.youtube.com/@CHANNEL_HANDLE
```

### File Naming

Default filename patterns:

```bash
# Video files
%(title)s.%(ext)s

# With quality
%(title)s_%(height)sp.%(ext)s

# With uploader
%(uploader)s_%(title)s.%(ext)s

# Safe characters only (removes special chars)
```

### Limitations

- **Rate Limiting**: YouTube may limit download speed
- **Private Videos**: Cannot download private/restricted content
- **Live Streams**: Limited support for ongoing streams
- **Copyright**: Respect content creators' rights

## 🔍 Examples by Use Case

### Educational Content

```bash
# Course playlist with subtitles
tubeharvest -u "COURSE_PLAYLIST_URL" \
  -q 720 \
  --subtitles \
  --metadata \
  -o "~/Education/Course_Name"
```

### Music Collection

```bash
# Album/music playlist as MP3
tubeharvest -u "MUSIC_PLAYLIST_URL" \
  -f mp3 \
  --audio-only \
  --metadata \
  -o "~/Music/Artist_Name"
```

### Content Archive

```bash
# High-quality archive with metadata
tubeharvest -u "CHANNEL_URL" \
  -q best \
  -f mkv \
  --subtitles \
  --metadata \
  --workers 2 \
  -o "~/Archive/Channel_Name"
```

### Mobile/Tablet Content

```bash
# Mobile-optimized downloads
tubeharvest -u "PLAYLIST_URL" \
  -q 480 \
  -f mp4 \
  --workers 3 \
  -o "~/Mobile/Content"
```

## 🆘 Getting Help

### Command Line Help

```bash
# General help
tubeharvest --help

# Specific option help
tubeharvest --help | grep -A 5 "format"
```

### Verbose Output

```bash
# Debug information
tubeharvest -u "URL" --verbose --debug
```

### Support Resources

- 📖 [User Guide](User-Guide) - Comprehensive usage guide
- 🔧 [Troubleshooting](Troubleshooting) - Common issues
- 💬 [FAQ](FAQ) - Frequently asked questions
- 🐛 [Issues](https://github.com/msadeqsirjani/TubeHarvest/issues) - Report bugs

---

*Master the command line for powerful YouTube downloading! 💪* 