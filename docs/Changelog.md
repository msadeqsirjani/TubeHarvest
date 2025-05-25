# 📋 Changelog

All notable changes to TubeHarvest will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Added
- Advanced filtering options for playlist downloads
- Custom post-processing hooks
- Support for chapter extraction
- Enhanced proxy configuration

### Changed
- Improved error handling and user feedback
- Updated dependencies to latest versions
- Optimized memory usage for large downloads

### Fixed
- Minor UI glitches in interactive mode
- Configuration validation edge cases

## [2.0.0] - 2024-05-15

### 🎉 Major Release - Complete Rewrite

#### Added
- **🎨 Interactive Mode**: Beautiful console interface with Rich UI
- **⚙️ Configuration System**: Comprehensive YAML/JSON configuration
- **👤 Profile Management**: Multiple configuration profiles
- **🔌 Plugin System**: Extensible architecture with plugins
- **🎵 Enhanced Audio Extraction**: High-quality audio downloads
- **📝 Subtitle Support**: Download subtitles in multiple languages
- **📊 Progress Tracking**: Real-time progress with ETA and speed
- **🎯 Batch Processing**: Queue multiple downloads
- **📱 Format Selection**: Smart format selection with preferences
- **🌐 Metadata Extraction**: Rich video information and thumbnails
- **🛠️ Developer API**: Complete Python API for integration
- **📚 Comprehensive Documentation**: Detailed guides and examples

#### Changed
- **Complete rewrite** in modern Python with Rich library
- **New CLI interface** with improved argument structure
- **Enhanced architecture** with modular design
- **Better error handling** with user-friendly messages
- **Improved performance** with optimized download engine

#### Breaking Changes
- New CLI argument structure (see migration guide)
- Configuration file format changed to YAML
- Python API completely redesigned

### Migration from 1.x

```bash
# Old command structure
tubeharvest-old "VIDEO_URL" --quality 1080

# New command structure
tubeharvest -u "VIDEO_URL" -q 1080

# Or use interactive mode
tubeharvest -i
```

## [1.5.2] - 2024-03-20

### Fixed
- YouTube URL parsing for new URL formats
- FFmpeg compatibility with latest versions
- Windows path handling issues

### Security
- Updated dependencies to fix security vulnerabilities

## [1.5.1] - 2024-02-15

### Added
- Support for YouTube Shorts
- Basic playlist download functionality

### Fixed
- Quality selection for age-restricted videos
- Download resume functionality

## [1.5.0] - 2024-01-10

### Added
- Multi-threaded downloads for playlists
- Custom output filename templates
- Basic configuration file support

### Changed
- Improved download speed estimation
- Better error messages

### Fixed
- Memory leaks during large downloads
- Unicode filename handling

## [1.4.3] - 2023-12-05

### Fixed
- Critical bug in format selection
- YouTube API changes compatibility
- Progress bar display issues

## [1.4.2] - 2023-11-20

### Added
- Support for private videos with cookies
- Basic subtitle download

### Fixed
- Network timeout handling
- File permission issues on Linux

## [1.4.1] - 2023-10-15

### Fixed
- YouTube throttling bypass
- Audio extraction quality issues

### Security
- Updated yt-dlp to latest version

## [1.4.0] - 2023-09-30

### Added
- Audio-only download mode
- Multiple video quality options
- Basic progress tracking

### Changed
- Switched to yt-dlp as backend
- Improved CLI interface

### Removed
- Support for Python 3.6 and earlier

## [1.3.2] - 2023-08-15

### Fixed
- Format availability checking
- Download interruption handling

## [1.3.1] - 2023-07-20

### Added
- Support for YouTube playlists (basic)
- Custom output directory option

### Fixed
- File naming conflicts
- Large file download stability

## [1.3.0] - 2023-06-10

### Added
- Multiple format support (MP4, WebM, MKV)
- Quality selection (1080p, 720p, 480p, 360p)
- Resume interrupted downloads

### Changed
- Improved command-line interface
- Better error reporting

## [1.2.1] - 2023-05-05

### Fixed
- YouTube URL validation
- Download path creation

## [1.2.0] - 2023-04-15

### Added
- Basic GUI interface (experimental)
- Configuration file support
- Logging functionality

### Changed
- Refactored download engine
- Improved stability

## [1.1.2] - 2023-03-20

### Fixed
- YouTube API changes compatibility
- Unicode handling in video titles

## [1.1.1] - 2023-02-28

### Fixed
- Installation issues on Windows
- Dependencies version conflicts

## [1.1.0] - 2023-02-10

### Added
- Batch download from file
- Custom filename format
- Download history tracking

### Changed
- Improved download speed
- Better progress indication

## [1.0.1] - 2023-01-25

### Fixed
- Installation script issues
- Documentation errors

## [1.0.0] - 2023-01-15

### 🎉 Initial Release

#### Added
- Basic YouTube video download functionality
- Command-line interface
- MP4 format support
- Quality selection (basic)
- Progress bar
- Cross-platform support (Windows, macOS, Linux)

#### Features
- Download individual YouTube videos
- Choose video quality
- Basic progress tracking
- Simple command-line interface

---

## Version Numbering

TubeHarvest follows [Semantic Versioning](https://semver.org/):

- **MAJOR** version for incompatible API changes
- **MINOR** version for backwards-compatible functionality additions
- **PATCH** version for backwards-compatible bug fixes

### Version Types

- **🎉 Major Release**: Significant new features, breaking changes
- **✨ Minor Release**: New features, backwards compatible
- **🔧 Patch Release**: Bug fixes, security updates

## Release Process

1. **Development**: Features developed in feature branches
2. **Testing**: Comprehensive testing on multiple platforms
3. **Documentation**: Update documentation and changelog
4. **Release**: Tagged release with distribution packages
5. **Announcement**: Community notification and migration guides

## Breaking Changes Policy

Breaking changes are introduced only in major versions and are:
- Clearly documented in the changelog
- Accompanied by migration guides
- Communicated well in advance when possible

## Support Policy

- **Current Major Version**: Full support with features and bug fixes
- **Previous Major Version**: Bug fixes and security updates for 6 months
- **Older Versions**: Security updates only, community support

## Deprecation Notice

### Upcoming Changes in v3.0 (Planned)

- Enhanced plugin system with breaking API changes
- New configuration format with advanced features
- Improved interactive mode with additional screens
- Performance optimizations requiring Python 3.9+

### Migration Support

Migration guides are provided for:
- [v1.x to v2.0 Migration Guide](https://github.com/msadeqsirjani/TubeHarvest/wiki/Migration-v1-to-v2)
- Configuration file format changes
- CLI argument updates
- API changes for developers

## Contributing to Releases

### Reporting Issues

Found a bug? Please report it:
1. Check [existing issues](https://github.com/msadeqsirjani/TubeHarvest/issues)
2. Create [new issue](https://github.com/msadeqsirjani/TubeHarvest/issues/new) with details
3. Include version, platform, and reproduction steps

### Feature Requests

Have an idea? We'd love to hear it:
1. Check [discussions](https://github.com/msadeqsirjani/TubeHarvest/discussions)
2. Create feature request with use case
3. Join community discussions

### Development

Want to contribute? See:
- [Developer Guide](Developer-Guide)
- [Contributing Guidelines](https://github.com/msadeqsirjani/TubeHarvest/blob/main/CONTRIBUTING.md)
- [Code of Conduct](https://github.com/msadeqsirjani/TubeHarvest/blob/main/CODE_OF_CONDUCT.md)

## Security Updates

Security vulnerabilities are handled with priority:
- **High/Critical**: Emergency patch within 48 hours
- **Medium**: Patch in next scheduled release
- **Low**: Included in regular release cycle

Report security issues privately to: security@tubeharvest.dev

## Acknowledgments

Special thanks to:
- **yt-dlp team** for the excellent backend library
- **Rich library** for beautiful console interfaces
- **Community contributors** for bug reports and features
- **Beta testers** for early feedback and testing

---

*For the latest updates and detailed release notes, visit our [GitHub Releases](https://github.com/msadeqsirjani/TubeHarvest/releases) page.* 