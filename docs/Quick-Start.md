# 🚀 Quick Start Guide

Get up and running with TubeHarvest in minutes! This guide covers the essential commands to start downloading YouTube content.

## ⚡ First Download

### Single Video Download

```bash
# Basic video download
tubeharvest -u "https://www.youtube.com/watch?v=VIDEO_ID"

# Or using Python module
python -m tubeharvest -u "https://www.youtube.com/watch?v=VIDEO_ID"
```

### Launch Interactive Mode

For the best experience, use the beautiful interactive interface:

```bash
# Launch interactive mode
tubeharvest -i

# Or
python -m tubeharvest -i
```

## 🎯 Common Use Cases

### 1. Download Video in Specific Quality

```bash
# Download in 1080p
tubeharvest -u "VIDEO_URL" -q 1080

# Download best available quality
tubeharvest -u "VIDEO_URL" -q best
```

### 2. Download Audio Only (MP3)

```bash
# Extract audio as MP3
tubeharvest -u "VIDEO_URL" -f mp3 --audio-only

# Custom audio quality
tubeharvest -u "VIDEO_URL" -f mp3 --audio-only -q best
```

### 3. Download Entire Playlist

```bash
# Download all videos in playlist
tubeharvest -u "https://www.youtube.com/playlist?list=PLAYLIST_ID"

# Playlist as audio files
tubeharvest -u "PLAYLIST_URL" -f mp3 --audio-only
```

### 4. Custom Output Directory

```bash
# Save to specific folder
tubeharvest -u "VIDEO_URL" -o "~/Downloads/YouTube"

# With custom filename
tubeharvest -u "VIDEO_URL" --filename "my_video" -o "~/Downloads"
```

### 5. Download with Subtitles

```bash
# Include subtitles
tubeharvest -u "VIDEO_URL" --subtitles

# With metadata
tubeharvest -u "VIDEO_URL" --subtitles --metadata
```

## 🎨 Interactive Mode Features

The interactive mode provides a beautiful console interface:

```bash
tubeharvest -i
```

**Features:**
- 🎯 **Setup Wizard**: Guided configuration
- 📊 **Real-time Progress**: Beautiful progress bars
- 📋 **Batch Downloads**: Queue multiple videos
- 🎨 **Rich UI**: Colorful and intuitive interface
- ⚙️ **Smart Defaults**: Intelligent suggestions

## 📁 Output Structure

By default, TubeHarvest saves files to:

```
downloads/
├── videos/
│   ├── Amazing_Video_Title.mp4
│   └── Another_Video.mp4
├── audio/
│   ├── Music_Track.mp3
│   └── Podcast_Episode.mp3
└── metadata/
    ├── Amazing_Video_Title.json
    └── Another_Video.json
```

## 🔧 Essential Options

| Option | Description | Example |
|--------|-------------|---------|
| `-u, --url` | YouTube URL (video/playlist) | `-u "VIDEO_URL"` |
| `-i, --interactive` | Launch interactive mode | `-i` |
| `-o, --output-dir` | Output directory | `-o "~/Downloads"` |
| `-f, --format` | Output format | `-f mp3` |
| `-q, --quality` | Video quality | `-q 1080` |
| `--audio-only` | Download audio only | `--audio-only` |
| `--subtitles` | Download subtitles | `--subtitles` |
| `--filename` | Custom filename | `--filename "my_video"` |

## 🎵 Format Options

| Format | Use Case | Quality |
|--------|----------|---------|
| `mp4` | Standard video (default) | Best compatibility |
| `mp3` | Audio extraction | Good quality |
| `webm` | Web-optimized video | Smaller file size |
| `mkv` | High-quality video | Best quality |
| `m4a` | Audio (Apple devices) | Best audio quality |

## 🎯 Quality Options

| Quality | Description | Recommended For |
|---------|-------------|-----------------|
| `best` | Highest available (default) | Best quality |
| `1080` | Full HD (1920x1080) | Standard viewing |
| `720` | HD (1280x720) | Good quality, smaller size |
| `480` | Standard definition | Older devices |
| `360` | Low quality | Slow connections |

## 📱 Example Workflows

### Workflow 1: Music Collection
```bash
# Download music playlist as MP3
tubeharvest -u "MUSIC_PLAYLIST_URL" \
  -f mp3 \
  --audio-only \
  -o "~/Music/YouTube" \
  --metadata
```

### Workflow 2: Educational Content
```bash
# Download course videos with subtitles
tubeharvest -u "COURSE_PLAYLIST_URL" \
  -q 720 \
  --subtitles \
  --metadata \
  -o "~/Education/Course_Name"
```

### Workflow 3: Podcast Collection
```bash
# Download podcast episodes
tubeharvest -u "PODCAST_URL" \
  -f m4a \
  --audio-only \
  --filename "Podcast_Episode_01" \
  -o "~/Podcasts"
```

### Workflow 4: Video Archive
```bash
# Archive channel videos
tubeharvest -u "CHANNEL_URL" \
  -q best \
  --metadata \
  --subtitles \
  -o "~/Archive/Channel_Name"
```

## 🚨 Important Notes

### ⚖️ Legal Considerations
- Only download content you have permission to download
- Respect YouTube's Terms of Service
- Consider copyright and fair use laws
- Use for personal/educational purposes

### 🔒 Privacy & Security
- TubeHarvest doesn't store your data
- No tracking or analytics
- Downloads are stored locally
- Your privacy is protected

### 🌐 Network Considerations
- Large downloads require stable internet
- Consider data usage on mobile connections
- Use quality settings appropriate for your bandwidth

## 🆘 Need Help?

### Quick Troubleshooting
```bash
# Check TubeHarvest version
tubeharvest --version

# Get help for specific command
tubeharvest --help

# Test with verbose output
tubeharvest -u "VIDEO_URL" --verbose
```

### Support Resources
- 📖 [User Guide](User-Guide) - Detailed documentation
- 🔧 [Troubleshooting](Troubleshooting) - Common issues
- 💬 [FAQ](FAQ) - Frequently asked questions
- 🐛 [Report Issues](https://github.com/msadeqsirjani/TubeHarvest/issues)

## ✅ Next Steps

Now that you're started:

1. 🎨 Try the [Interactive Mode](Interactive-Mode)
2. 📖 Read the complete [User Guide](User-Guide)
3. ⚙️ Learn about [Configuration](Configuration-Guide)
4. 🔧 Explore [Advanced Features](CLI-Reference)

---

*Happy downloading! 🎉* 