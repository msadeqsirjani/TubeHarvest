# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [2.0.0] - 2024-01-15

### Added
- 🎨 Beautiful interactive console interface using Rich library
- 📋 Interactive setup wizard with smart prompts and validation
- 📊 Real-time progress tracking with live statistics
- 🎬 Enhanced video information display with rich formatting
- ⚡ Smart input validation with instant feedback
- 🔄 Graceful error handling with retry options
- 📈 Comprehensive download statistics and completion reports
- 🌟 Professional project structure with proper packaging
- 🧪 Comprehensive test suite with fixtures and mocks
- 📚 Complete documentation and GitHub workflows
- 🔒 Security scanning with CodeQL and Bandit
- 📦 Modern Python packaging with pyproject.toml

### Enhanced
- 🚀 Improved CLI interface with better argument handling
- 🎯 Better quality selection options
- 💾 Enhanced resume functionality for interrupted downloads
- 🔧 Modular architecture with proper separation of concerns
- 📁 Professional directory structure following best practices

### Technical Improvements
- Migrated from basic colorama to Rich library for enhanced UI
- Implemented proper package structure with subpackages
- Added comprehensive type hints throughout codebase
- Integrated modern development tools (Black, MyPy, Pytest)
- Added GitHub Actions for CI/CD pipeline
- Implemented proper configuration management

### Breaking Changes
- Changed package structure from `src/` to `tubeharvest/`
- Updated import paths for all modules
- Renamed script files for better clarity

## [1.0.0] - 2023-12-01

### Added
- Initial release of TubeHarvest
- Basic YouTube video and playlist downloading
- Command-line interface
- Multiple format support (MP4, MP3, WebM, etc.)
- Quality selection options
- Subtitle and metadata downloading
- Basic progress tracking with tqdm
- Multithreaded playlist downloads 