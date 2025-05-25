# ⚙️ Configuration Guide

Master TubeHarvest configuration to customize your download experience. This guide covers all configuration options, settings management, and advanced customization.

## 📖 Table of Contents

1. [Configuration Overview](#configuration-overview)
2. [Configuration File](#configuration-file)
3. [Global Settings](#global-settings)
4. [Download Settings](#download-settings)
5. [Output Settings](#output-settings)
6. [Advanced Options](#advanced-options)
7. [Environment Variables](#environment-variables)
8. [Profile Management](#profile-management)
9. [Presets and Templates](#presets-and-templates)

## 🎯 Configuration Overview

TubeHarvest supports multiple configuration methods:
- **Command-line arguments**: Override any setting
- **Configuration files**: Persistent settings (YAML/JSON)
- **Environment variables**: System-level configuration
- **Interactive setup**: Guided configuration wizard
- **Profiles**: Multiple configuration sets

### Configuration Priority

Settings are applied in this order (highest to lowest priority):
1. Command-line arguments
2. Environment variables
3. User configuration file
4. Profile configuration
5. Default settings

## 📄 Configuration File

### Location

TubeHarvest looks for configuration files in:

```bash
# Primary locations (in order)
~/.config/tubeharvest/config.yaml
~/.config/tubeharvest/config.json
~/.tubeharvest.yaml
~/.tubeharvest.json

# Windows
%APPDATA%\TubeHarvest\config.yaml
%USERPROFILE%\.tubeharvest.yaml
```

### Creating Configuration

```bash
# Generate default configuration
tubeharvest --generate-config

# Interactive configuration wizard
tubeharvest --setup

# Save current settings
tubeharvest --save-config
```

### Configuration Format

**YAML Format (Recommended):**
```yaml
# ~/.config/tubeharvest/config.yaml
general:
  output_dir: "~/Downloads/TubeHarvest"
  quality: "1080"
  format: "mp4"
  interactive_mode: false

download:
  max_retries: 3
  retry_delay: 5
  concurrent_downloads: 2
  rate_limit: null

output:
  filename_template: "%(title)s.%(ext)s"
  organize_by: "none"  # none, uploader, date, playlist
  create_subdirs: true

features:
  subtitles: false
  metadata: false
  thumbnail: false
  audio_only: false

network:
  proxy: null
  user_agent: "TubeHarvest/2.0"
  cookies_file: null
  timeout: 30
```

**JSON Format:**
```json
{
  "general": {
    "output_dir": "~/Downloads/TubeHarvest",
    "quality": "1080",
    "format": "mp4",
    "interactive_mode": false
  },
  "download": {
    "max_retries": 3,
    "retry_delay": 5,
    "concurrent_downloads": 2,
    "rate_limit": null
  }
}
```

## 🎛️ Global Settings

### General Configuration

```yaml
general:
  # Default output directory
  output_dir: "~/Downloads/TubeHarvest"
  
  # Default video quality
  quality: "best"  # best, 1080, 720, 480, 360
  
  # Default output format
  format: "mp4"  # mp4, mp3, webm, mkv, m4a
  
  # Start in interactive mode
  interactive_mode: false
  
  # Verbose output
  verbose: false
  
  # Quiet mode (minimal output)
  quiet: false
  
  # Color output
  color: true
  
  # Progress bar style
  progress_style: "bar"  # bar, dots, spinner
```

### User Interface Settings

```yaml
ui:
  # Console theme
  theme: "default"  # default, dark, light, colorful
  
  # Progress bar width
  progress_width: 40
  
  # Show download speed
  show_speed: true
  
  # Show ETA
  show_eta: true
  
  # Show file size
  show_size: true
  
  # Confirm before download
  confirm_download: false
  
  # Auto-clear completed downloads
  auto_clear_completed: true
```

## 📥 Download Settings

### Basic Download Options

```yaml
download:
  # Maximum download retries
  max_retries: 3
  
  # Delay between retries (seconds)
  retry_delay: 5
  
  # Concurrent downloads for playlists
  concurrent_downloads: 2
  
  # Rate limit (e.g., "1M", "500K")
  rate_limit: null
  
  # Continue incomplete downloads
  continue_downloads: true
  
  # Skip downloaded files
  skip_existing: true
  
  # Maximum file size
  max_filesize: null  # e.g., "1G", "500M"
  
  # Minimum file size
  min_filesize: null  # e.g., "10M", "1M"
```

### Quality Preferences

```yaml
quality:
  # Video quality preferences (in order)
  video_quality: ["1080", "720", "best"]
  
  # Audio quality for audio-only downloads
  audio_quality: "best"  # best, 320, 256, 192, 128
  
  # Prefer certain formats
  preferred_formats: ["mp4", "webm"]
  
  # Video codec preference
  video_codec: "h264"  # h264, vp9, av01
  
  # Audio codec preference
  audio_codec: "aac"  # aac, mp3, opus
```

### Download Filtering

```yaml
filters:
  # Date range
  date_after: null  # YYYYMMDD
  date_before: null  # YYYYMMDD
  
  # Duration limits (seconds)
  min_duration: null
  max_duration: null
  
  # View count limits
  min_views: null
  max_views: null
  
  # Like ratio limits
  min_like_ratio: null
  max_like_ratio: null
```

## 📁 Output Settings

### File Organization

```yaml
output:
  # Output directory structure
  organize_by: "none"  # none, uploader, date, playlist, format
  
  # Create subdirectories
  create_subdirs: true
  
  # Filename template
  filename_template: "%(title)s.%(ext)s"
  
  # Available template variables:
  # %(title)s - Video title
  # %(uploader)s - Channel name
  # %(upload_date)s - Upload date (YYYYMMDD)
  # %(id)s - Video ID
  # %(playlist)s - Playlist name
  # %(playlist_index)s - Position in playlist
  # %(duration)s - Video duration
  # %(view_count)s - View count
  
  # Restrict filenames (remove special characters)
  restrict_filenames: true
  
  # Maximum filename length
  max_filename_length: 255
```

### File Handling

```yaml
files:
  # Overwrite existing files
  overwrite: false
  
  # Archive file for tracking downloads
  archive_file: null  # e.g., "~/.tubeharvest_archive.txt"
  
  # Write metadata files
  write_info_json: false
  
  # Write description files
  write_description: false
  
  # Write thumbnail files
  write_thumbnail: false
  
  # Embed metadata in files
  embed_metadata: true
```

## 🔧 Advanced Options

### Network Configuration

```yaml
network:
  # Proxy settings
  proxy: null  # e.g., "http://proxy.example.com:8080"
  
  # Custom User-Agent
  user_agent: "TubeHarvest/2.0"
  
  # Cookie file for authentication
  cookies_file: null
  
  # Network timeout (seconds)
  timeout: 30
  
  # Socket timeout (seconds)
  socket_timeout: 10
  
  # Source address to bind to
  source_address: null
  
  # Sleep interval between downloads (seconds)
  sleep_interval: 0
```

### Post-Processing

```yaml
postprocessing:
  # Extract audio from video
  extract_audio: false
  
  # Audio format for extraction
  audio_format: "mp3"  # mp3, m4a, ogg, wav
  
  # Audio quality for extraction
  audio_quality: "192"
  
  # Embed subtitles in video
  embed_subs: false
  
  # Embed thumbnail in audio files
  embed_thumbnail: false
  
  # Convert video format
  convert_format: null  # mp4, webm, mkv
  
  # Custom FFmpeg arguments
  ffmpeg_args: []
```

### Subtitle Configuration

```yaml
subtitles:
  # Download subtitles
  download_subtitles: false
  
  # Subtitle languages (in preference order)
  subtitle_langs: ["en", "auto"]
  
  # Download all available subtitles
  all_subtitles: false
  
  # Subtitle formats
  subtitle_format: "srt"  # srt, vtt, ass
  
  # Embed subtitles in video
  embed_subtitles: false
  
  # Convert subtitles to SRT
  convert_subs: true
```

## 🌍 Environment Variables

Override configuration using environment variables:

```bash
# General settings
export TUBEHARVEST_OUTPUT_DIR="~/Downloads/YouTube"
export TUBEHARVEST_QUALITY="1080"
export TUBEHARVEST_FORMAT="mp4"

# Download settings
export TUBEHARVEST_MAX_RETRIES="5"
export TUBEHARVEST_CONCURRENT_DOWNLOADS="3"
export TUBEHARVEST_RATE_LIMIT="2M"

# Network settings
export TUBEHARVEST_PROXY="http://proxy.example.com:8080"
export TUBEHARVEST_USER_AGENT="MyCustomBot/1.0"

# Feature toggles
export TUBEHARVEST_SUBTITLES="true"
export TUBEHARVEST_METADATA="true"
export TUBEHARVEST_INTERACTIVE="false"
```

### Environment Variable Naming

Convert configuration keys to environment variables:
- Prefix with `TUBEHARVEST_`
- Replace dots with underscores
- Convert to uppercase

Examples:
- `general.output_dir` → `TUBEHARVEST_OUTPUT_DIR`
- `download.max_retries` → `TUBEHARVEST_MAX_RETRIES`
- `network.proxy` → `TUBEHARVEST_PROXY`

## 👤 Profile Management

### Creating Profiles

```bash
# Create a new profile
tubeharvest --create-profile music

# Configure profile interactively
tubeharvest --profile music --setup
```

### Profile Configuration

```yaml
# ~/.config/tubeharvest/profiles/music.yaml
general:
  format: "mp3"
  quality: "best"

download:
  audio_only: true
  concurrent_downloads: 3

output:
  organize_by: "uploader"
  filename_template: "%(artist)s - %(title)s.%(ext)s"

features:
  metadata: true
  thumbnail: true
```

### Using Profiles

```bash
# Use specific profile
tubeharvest --profile music -u "MUSIC_URL"

# List available profiles
tubeharvest --list-profiles

# Set default profile
tubeharvest --set-default-profile music
```

### Built-in Profiles

TubeHarvest includes several built-in profiles:

**Music Profile:**
```yaml
format: "mp3"
audio_only: true
quality: "best"
metadata: true
organize_by: "uploader"
```

**Video Profile:**
```yaml
format: "mp4"
quality: "1080"
subtitles: true
metadata: true
organize_by: "date"
```

**Archive Profile:**
```yaml
quality: "best"
subtitles: true
metadata: true
thumbnail: true
organize_by: "uploader"
archive_file: "archive.txt"
```

## 📋 Presets and Templates

### Download Presets

```yaml
presets:
  high_quality:
    quality: "best"
    format: "mkv"
    subtitles: true
    metadata: true
  
  mobile_friendly:
    quality: "720"
    format: "mp4"
    max_filesize: "100M"
  
  audio_only:
    format: "mp3"
    audio_only: true
    audio_quality: "320"
    metadata: true
  
  quick_download:
    quality: "480"
    format: "mp4"
    concurrent_downloads: 5
```

### Filename Templates

```yaml
templates:
  simple: "%(title)s.%(ext)s"
  detailed: "%(uploader)s - %(title)s [%(id)s].%(ext)s"
  dated: "%(upload_date)s - %(title)s.%(ext)s"
  playlist: "%(playlist_index)02d - %(title)s.%(ext)s"
  music: "%(artist)s - %(track)s.%(ext)s"
```

### Using Presets

```bash
# Use preset
tubeharvest --preset high_quality -u "VIDEO_URL"

# Combine with custom options
tubeharvest --preset audio_only --audio-quality 192 -u "MUSIC_URL"
```

## 🔧 Configuration Examples

### Complete Configuration File

```yaml
# ~/.config/tubeharvest/config.yaml

general:
  output_dir: "~/Downloads/TubeHarvest"
  quality: "1080"
  format: "mp4"
  interactive_mode: false
  verbose: false

ui:
  theme: "default"
  progress_width: 50
  show_speed: true
  show_eta: true
  confirm_download: false

download:
  max_retries: 3
  retry_delay: 5
  concurrent_downloads: 2
  rate_limit: null
  continue_downloads: true
  skip_existing: true

quality:
  video_quality: ["1080", "720", "best"]
  audio_quality: "best"
  preferred_formats: ["mp4", "webm"]

output:
  organize_by: "uploader"
  create_subdirs: true
  filename_template: "%(title)s.%(ext)s"
  restrict_filenames: true

files:
  overwrite: false
  archive_file: "~/.tubeharvest_archive.txt"
  write_info_json: false
  embed_metadata: true

network:
  timeout: 30
  socket_timeout: 10
  sleep_interval: 1

subtitles:
  download_subtitles: true
  subtitle_langs: ["en", "auto"]
  subtitle_format: "srt"
  embed_subtitles: false

postprocessing:
  extract_audio: false
  embed_thumbnail: true
```

### Specialized Configurations

**Music Downloader Configuration:**
```yaml
general:
  format: "mp3"
  quality: "best"

download:
  audio_only: true
  concurrent_downloads: 3

output:
  organize_by: "uploader"
  filename_template: "%(uploader)s/%(title)s.%(ext)s"

features:
  metadata: true
  thumbnail: true

postprocessing:
  audio_quality: "320"
  embed_thumbnail: true
```

**Archival Configuration:**
```yaml
general:
  quality: "best"
  format: "mkv"

features:
  subtitles: true
  metadata: true
  thumbnail: true

output:
  organize_by: "date"
  filename_template: "%(upload_date)s/%(uploader)s/%(title)s.%(ext)s"

files:
  archive_file: "~/archive.txt"
  write_info_json: true
  write_description: true
```

## 🔍 Configuration Validation

### Validate Configuration

```bash
# Check configuration syntax
tubeharvest --validate-config

# Test configuration with dry run
tubeharvest --dry-run -u "VIDEO_URL"

# Show effective configuration
tubeharvest --show-config
```

### Common Configuration Issues

1. **Invalid paths**: Use absolute paths or proper home directory expansion
2. **Missing directories**: Ensure output directories exist or are creatable
3. **Permission issues**: Check write permissions for output directories
4. **Format conflicts**: Ensure format and quality combinations are valid
5. **Network settings**: Verify proxy and network configurations

## 📞 Getting Help

- **Configuration Help**: `tubeharvest --help-config`
- **Interactive Setup**: `tubeharvest --setup`
- **Reset Configuration**: `tubeharvest --reset-config`
- **Export Configuration**: `tubeharvest --export-config config.yaml`

---

*For more advanced usage and development configurations, see the [Developer Guide](Developer-Guide) and [CLI Reference](CLI-Reference).* 