# 🎬 TubeHarvest Wiki

Welcome to the **TubeHarvest** documentation! TubeHarvest is a comprehensive YouTube downloader with a beautiful interactive console interface.

![TubeHarvest Banner](https://img.shields.io/badge/TubeHarvest-YouTube%20Downloader-red?style=for-the-badge&logo=youtube)

## ✨ Features

- 🎥 **Download YouTube videos** in various formats (MP4, MP3, WebM, MKV, M4A)
- 📱 **Beautiful interactive console** with Rich UI components
- 🎯 **Multiple quality options** (4K, 1080p, 720p, 480p, etc.)
- 📋 **Playlist support** with batch downloading
- 🎵 **Audio-only downloads** for music extraction
- 📝 **Subtitle downloads** with automatic language detection
- 🏷️ **Metadata extraction** and custom filename support
- ⚡ **Multi-threaded downloads** for faster performance
- 🎨 **Progress tracking** with real-time statistics

## 📚 Documentation

### Getting Started
- [**Installation Guide**](Installation-Guide) - Complete installation instructions
- [**Quick Start**](Quick-Start) - Get up and running in minutes
- [**User Guide**](User-Guide) - Comprehensive usage instructions

### Advanced Usage
- [**Configuration Guide**](Configuration-Guide) - Customize TubeHarvest settings
- [**Command Line Reference**](CLI-Reference) - Complete CLI documentation
- [**Interactive Mode**](Interactive-Mode) - Beautiful GUI interface guide

### Development
- [**Developer Guide**](Developer-Guide) - Contributing and development setup
- [**API Reference**](API-Reference) - Python API documentation
- [**Project Structure**](Project-Structure) - Codebase organization

### Help & Support
- [**Troubleshooting**](Troubleshooting) - Common issues and solutions
- [**FAQ**](FAQ) - Frequently asked questions
- [**Changelog**](Changelog) - Version history and updates

## 🚀 Quick Examples

### Basic Download
```bash
# Download a single video
python -m tubeharvest -u "https://www.youtube.com/watch?v=VIDEO_ID"

# Launch interactive mode
python -m tubeharvest -i
```

### Advanced Usage
```bash
# Download playlist in MP3 format
python -m tubeharvest -u "PLAYLIST_URL" -f mp3 --audio-only

# Custom quality and filename
python -m tubeharvest -u "VIDEO_URL" -q 1080 --filename "my_video"
```

## 🤝 Community

- 🐛 [Report Issues](https://github.com/msadeqsirjani/TubeHarvest/issues)
- 💡 [Feature Requests](https://github.com/msadeqsirjani/TubeHarvest/issues/new?template=feature_request.md)
- 🤝 [Contributing Guidelines](https://github.com/msadeqsirjani/TubeHarvest/blob/main/CONTRIBUTING.md)

## 📄 License

TubeHarvest is released under the [MIT License](https://github.com/msadeqsirjani/TubeHarvest/blob/main/LICENSE).

---

*Last updated: May 2024 | Version 2.0.0* 