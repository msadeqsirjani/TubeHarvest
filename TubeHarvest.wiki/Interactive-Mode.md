# 🎨 Interactive Mode Guide

TubeHarvest's interactive mode provides a beautiful, user-friendly console interface that makes downloading YouTube content intuitive and enjoyable.

![Interactive Mode Demo](https://img.shields.io/badge/Interactive-Mode-brightgreen?style=for-the-badge)

## 🚀 Launching Interactive Mode

### Quick Launch

```bash
# Launch interactive mode
tubeharvest -i

# Alternative methods
python -m tubeharvest -i
./scripts/tubeharvest-gui  # If using source installation
```

### GUI Launcher Script

For convenience, use the dedicated GUI script:

```bash
# Make executable (first time only)
chmod +x scripts/tubeharvest-gui

# Launch GUI
./scripts/tubeharvest-gui
```

## 🎯 Interface Overview

### Welcome Screen

When you launch interactive mode, you'll see:

```
╔══════════════════════════════════════════════════════════════╗
║  ████████╗██╗   ██╗██████╗ ███████╗██╗  ██╗ █████╗ ██████╗   ║
║  ╚══██╔══╝██║   ██║██╔══██╗██╔════╝██║  ██║██╔══██╗██╔══██╗  ║
║     ██║   ██║   ██║██████╔╝█████╗  ███████║███████║██████╔╝  ║
║     ██║   ██║   ██║██╔══██╗██╔══╝  ██╔══██║██╔══██║██╔══██╗  ║
║     ██║   ╚██████╔╝██████╔╝███████╗██║  ██║██║  ██║██║  ██║  ║
║     ╚═╝    ╚═════╝ ╚═════╝ ╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝  ║
╚══════════════════════════════════════════════════════════════╝

           🎬 YouTube Downloader with Style 🎬
```

### Navigation

The interface is organized into clear sections:

1. **🏠 Main Menu** - Primary navigation
2. **⚙️ Configuration** - Setup your preferences  
3. **📥 Download** - Start downloading content
4. **📊 Progress** - Monitor download status
5. **📈 Statistics** - View download summary

## 🛠️ Setup Wizard

### Initial Configuration

The setup wizard guides you through essential settings:

#### 1. Output Directory Selection
```
📁 Choose Output Directory
├── 🏠 Default: ~/Downloads/TubeHarvest
├── 📂 Custom: Choose your folder
└── ✨ Create New: Make a new directory
```

#### 2. Format Preferences
```
🎵 Select Default Format
├── 🎥 MP4 (Video) - Best compatibility
├── 🎵 MP3 (Audio) - Music/podcasts  
├── 🌐 WebM (Video) - Smaller size
├── 📼 MKV (Video) - Highest quality
└── 🎧 M4A (Audio) - Apple devices
```

#### 3. Quality Settings
```
🎯 Default Quality
├── 🏆 Best - Highest available
├── 🎬 1080p - Full HD
├── 📺 720p - HD
├── 📱 480p - Standard
└── 💾 360p - Save bandwidth
```

#### 4. Advanced Options
```
⚙️ Advanced Settings
├── 📝 Download subtitles: Yes/No
├── 🏷️ Save metadata: Yes/No
├── 🔄 Multi-threading: 1-8 workers
└── 📂 Organize by type: Yes/No
```

## 📥 Download Process

### URL Input

The interface provides smart URL handling:

```
🔗 Enter YouTube URL:
┌─────────────────────────────────────────────────┐
│ https://www.youtube.com/watch?v=...             │
└─────────────────────────────────────────────────┘

✅ Supported URLs:
• Single videos
• Playlists  
• Channel pages
• Live streams
```

### Content Detection

TubeHarvest automatically detects and displays content information:

```
🎬 Video Information
┌─────────────────────────────────────────────────┐
│ Title: Amazing YouTube Tutorial                 │
│ Channel: TechChannel                           │
│ Duration: 15:30                                │
│ Views: 1,234,567                               │
│ Quality: Up to 1080p available                 │
└─────────────────────────────────────────────────┘
```

### Download Options

Configure download settings on the fly:

```
⚙️ Download Configuration
┌─────────────────────────────────────────────────┐
│ Format: [MP4] [MP3] [WebM] [MKV] [M4A]         │
│ Quality: [Best] [1080] [720] [480] [360]       │
│ Options: [✓] Subtitles [✓] Metadata            │
│ Filename: [Custom name] or [Auto]              │
└─────────────────────────────────────────────────┘
```

## 📊 Progress Tracking

### Real-Time Progress

Beautiful progress bars show download status:

```
📊 Download Progress

🎬 Video 1: Amazing Tutorial
████████████████████████████████ 100% | 156.7 MB

🎬 Video 2: Follow-up Guide  
████████████████░░░░░░░░░░░░░░░░  45% | 67.3 MB

🎬 Video 3: Advanced Tips
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░   0% | Queued

Overall Progress: 2/3 completed (66.7%)
Total Size: 224.0 MB | Speed: 2.3 MB/s
```

### Status Indicators

| Symbol | Status | Description |
|--------|--------|-------------|
| 🟢 | Completed | Download finished successfully |
| 🔵 | In Progress | Currently downloading |
| 🟡 | Queued | Waiting to start |
| 🔴 | Failed | Download error occurred |
| ⏸️ | Paused | Download temporarily stopped |

## 🎛️ Interactive Controls

### During Download

Control your downloads with keyboard shortcuts:

| Key | Action | Description |
|-----|--------|-------------|
| `Space` | Pause/Resume | Toggle download pause |
| `S` | Skip Current | Skip to next download |
| `C` | Cancel | Cancel current download |
| `Q` | Quit | Exit application |
| `H` | Help | Show help menu |

### Batch Operations

Manage multiple downloads:

```
📋 Batch Download Manager
┌─────────────────────────────────────────────────┐
│ [✓] Video 1 - Amazing Tutorial                  │
│ [✓] Video 2 - Follow-up Guide                   │
│ [✓] Video 3 - Advanced Tips                     │
│ [ ] Video 4 - Expert Level                      │
│                                                 │
│ Actions: [Select All] [Deselect] [Download]     │
└─────────────────────────────────────────────────┘
```

## 📈 Statistics & Summary

### Download Summary

View detailed statistics after completion:

```
📈 Download Statistics
┌─────────────────────────────────────────────────┐
│ Total Downloads: 5                              │
│ Successful: 4 (80%)                             │
│ Failed: 1 (20%)                                 │
│ Total Size: 742.3 MB                            │
│ Average Speed: 3.2 MB/s                         │
│ Time Taken: 3m 45s                              │
└─────────────────────────────────────────────────┘
```

### File Organization

View where your files were saved:

```
📁 Downloaded Files
┌─────────────────────────────────────────────────┐
│ 📂 ~/Downloads/TubeHarvest/                     │
│   ├── 🎥 videos/                                │
│   │   ├── Amazing_Tutorial.mp4                  │
│   │   └── Follow_up_Guide.mp4                   │
│   ├── 🎵 audio/                                 │
│   │   └── Podcast_Episode.mp3                   │
│   └── 📄 metadata/                              │
│       ├── Amazing_Tutorial.json                 │
│       └── Follow_up_Guide.json                  │
└─────────────────────────────────────────────────┘
```

## 🔧 Advanced Features

### Smart Playlist Handling

When downloading playlists, get intelligent options:

```
📋 Playlist Detected: "Complete Python Course"
┌─────────────────────────────────────────────────┐
│ Videos Found: 25                                │
│ Total Duration: 8h 32m                          │
│ Estimated Size: 2.1 GB                          │
│                                                 │
│ Options:                                        │
│ • Download all videos                           │
│ • Select specific videos                        │
│ • Download range (e.g., 1-10)                   │
│ • Skip already downloaded                       │
└─────────────────────────────────────────────────┘
```

### Error Handling

Graceful error handling with retry options:

```
❌ Download Failed: Network timeout
┌─────────────────────────────────────────────────┐
│ Video: Amazing Tutorial                         │
│ Error: Connection timed out                     │
│                                                 │
│ Options:                                        │
│ • [R] Retry download                            │
│ • [S] Skip this video                           │
│ • [L] Try lower quality                         │
│ • [C] Cancel all downloads                      │
└─────────────────────────────────────────────────┘
```

### Configuration Management

Save and load download configurations:

```
⚙️ Configuration Profiles
┌─────────────────────────────────────────────────┐
│ 📁 Saved Profiles:                              │
│   • 🎵 Music Downloads (MP3, Best Quality)      │
│   • 🎥 HD Videos (MP4, 1080p)                   │
│   • 📚 Tutorials (MP4, 720p, Subtitles)         │
│   • 📱 Mobile (MP4, 480p, Small Size)           │
│                                                 │
│ Actions: [Load] [Save Current] [Delete]         │
└─────────────────────────────────────────────────┘
```

## 🎨 Customization

### Theme Options

Customize the interface appearance:

```
🎨 Interface Themes
├── 🌙 Dark Mode (default)
├── ☀️ Light Mode  
├── 🌈 Colorful
├── 🎯 Minimal
└── 🎪 Retro
```

### Layout Preferences

Adjust interface layout:

```
🖥️ Layout Options
├── 📊 Progress Focus - Emphasize download progress
├── 📋 List View - Compact file listing
├── 🎛️ Control Panel - Prominent controls
└── 📈 Stats Dashboard - Detailed statistics
```

## 🔍 Search & Discovery

### URL History

Access previously downloaded content:

```
🕒 Recent Downloads
┌─────────────────────────────────────────────────┐
│ 1. Amazing Python Tutorial (2 hours ago)        │
│ 2. Music Playlist (Yesterday)                   │
│ 3. Documentary Series (3 days ago)              │
│                                                 │
│ [Re-download] [Open Folder] [Copy URL]          │
└─────────────────────────────────────────────────┘
```

## 🚨 Tips & Best Practices

### Performance Tips

1. **Optimal Workers**: Use 2-4 workers for best performance
2. **Network**: Stable internet improves success rate
3. **Storage**: Ensure sufficient disk space
4. **Quality**: Balance quality vs. file size needs

### Troubleshooting

Common issues and solutions:

| Issue | Solution |
|-------|----------|
| Slow downloads | Reduce worker count or quality |
| Failed downloads | Check internet connection |
| Audio sync issues | Try different format (MKV/MP4) |
| Large file sizes | Use lower quality or WebM format |

## 🎯 Keyboard Shortcuts

Global shortcuts available in interactive mode:

| Shortcut | Action |
|----------|--------|
| `Ctrl+C` | Exit application |
| `Ctrl+R` | Refresh/Restart |
| `Tab` | Navigate options |
| `Enter` | Confirm selection |
| `Esc` | Cancel/Go back |
| `F1` | Help screen |

## ✅ Next Steps

Master interactive mode:

1. 📖 Practice with the [Quick Start Guide](Quick-Start)
2. 🔧 Learn [Advanced Configuration](Configuration-Guide)
3. 🎯 Explore [CLI Commands](CLI-Reference)
4. 🛠️ Check [Troubleshooting](Troubleshooting) if needed

---

*Enjoy the beautiful interface! 🎨✨* 