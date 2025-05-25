# 📁 Project Structure

Complete overview of TubeHarvest's codebase organization, architecture, and file structure. This guide helps developers understand the project layout and navigate the codebase effectively.

## 📖 Table of Contents

1. [Overview](#overview)
2. [Directory Structure](#directory-structure)
3. [Core Modules](#core-modules)
4. [Configuration Files](#configuration-files)
5. [Documentation](#documentation)
6. [Testing Structure](#testing-structure)
7. [Build and Distribution](#build-and-distribution)
8. [Development Files](#development-files)

## 🎯 Overview

TubeHarvest follows a modular architecture with clear separation of concerns:

- **Core Engine**: Download functionality and media processing
- **CLI Interface**: Command-line interface and argument parsing
- **Interactive Mode**: Rich console interface with TUI components
- **Configuration**: Settings management and user preferences
- **Utilities**: Helper functions and common utilities
- **Tests**: Comprehensive test suite with unit and integration tests

### Architecture Principles

- **Modularity**: Each component has a specific responsibility
- **Extensibility**: Plugin system for custom functionality
- **Testability**: Comprehensive test coverage with mocks
- **Configuration**: Flexible configuration system
- **Error Handling**: Robust error handling and logging

## 📂 Directory Structure

```
TubeHarvest/
├── .github/                    # GitHub workflows and templates
│   ├── workflows/
│   │   ├── ci.yml             # Continuous Integration
│   │   ├── release.yml        # Automated releases
│   │   └── tests.yml          # Test automation
│   ├── ISSUE_TEMPLATE/        # Issue templates
│   └── PULL_REQUEST_TEMPLATE.md
├── docs/                      # Documentation
│   ├── README.md              # Documentation index
│   ├── Installation-Guide.md  # Installation instructions
│   ├── Quick-Start.md         # Quick start guide
│   ├── User-Guide.md          # Comprehensive user guide
│   ├── CLI-Reference.md       # Command-line reference
│   ├── Interactive-Mode.md    # Interactive mode guide
│   ├── Configuration-Guide.md # Configuration documentation
│   ├── API-Reference.md       # Python API documentation
│   ├── Developer-Guide.md     # Development guide
│   ├── Project-Structure.md   # This file
│   ├── Troubleshooting.md     # Common issues and solutions
│   ├── FAQ.md                 # Frequently asked questions
│   ├── Changelog.md           # Version history
│   ├── Home.md               # Wiki home page
│   └── _Sidebar.md           # Navigation sidebar
├── src/                       # Source code
│   └── tubeharvest/
│       ├── __init__.py        # Package initialization
│       ├── __main__.py        # Entry point for python -m tubeharvest
│       ├── core/              # Core functionality
│       │   ├── __init__.py
│       │   ├── downloader.py  # Main download engine
│       │   ├── extractor.py   # Metadata extraction
│       │   ├── formats.py     # Format selection logic
│       │   ├── progress.py    # Progress tracking
│       │   └── processor.py   # Post-processing
│       ├── cli/               # Command-line interface
│       │   ├── __init__.py
│       │   ├── main.py        # Main CLI entry point
│       │   ├── args.py        # Argument parsing
│       │   ├── commands.py    # Command handlers
│       │   └── validators.py  # Input validation
│       ├── interactive/       # Interactive mode
│       │   ├── __init__.py
│       │   ├── app.py         # Main interactive application
│       │   ├── components/    # UI components
│       │   │   ├── __init__.py
│       │   │   ├── download.py    # Download components
│       │   │   ├── progress.py    # Progress components
│       │   │   ├── settings.py    # Settings components
│       │   │   └── widgets.py     # Common widgets
│       │   ├── layouts/       # UI layouts
│       │   │   ├── __init__.py
│       │   │   ├── main.py        # Main layout
│       │   │   └── setup.py       # Setup wizard layout
│       │   └── themes/        # Color themes
│       │       ├── __init__.py
│       │       ├── default.py
│       │       ├── dark.py
│       │       └── light.py
│       ├── config/            # Configuration management
│       │   ├── __init__.py
│       │   ├── manager.py     # Configuration manager
│       │   ├── schema.py      # Configuration schema
│       │   ├── profiles.py    # Profile management
│       │   └── defaults.py    # Default settings
│       ├── utils/             # Utility modules
│       │   ├── __init__.py
│       │   ├── filesystem.py  # File operations
│       │   ├── network.py     # Network utilities
│       │   ├── formatting.py  # String formatting
│       │   ├── logging.py     # Logging utilities
│       │   └── validators.py  # Validation helpers
│       ├── plugins/           # Plugin system
│       │   ├── __init__.py
│       │   ├── base.py        # Base plugin class
│       │   ├── manager.py     # Plugin manager
│       │   └── builtin/       # Built-in plugins
│       │       ├── __init__.py
│       │       ├── thumbnail.py
│       │       ├── subtitle.py
│       │       └── metadata.py
│       └── exceptions.py      # Custom exceptions
├── tests/                     # Test suite
│   ├── __init__.py
│   ├── conftest.py           # Pytest configuration
│   ├── unit/                 # Unit tests
│   │   ├── __init__.py
│   │   ├── test_core/
│   │   │   ├── test_downloader.py
│   │   │   ├── test_extractor.py
│   │   │   └── test_formats.py
│   │   ├── test_cli/
│   │   │   ├── test_main.py
│   │   │   ├── test_args.py
│   │   │   └── test_commands.py
│   │   ├── test_config/
│   │   │   ├── test_manager.py
│   │   │   └── test_profiles.py
│   │   └── test_utils/
│   │       ├── test_filesystem.py
│   │       └── test_network.py
│   ├── integration/          # Integration tests
│   │   ├── __init__.py
│   │   ├── test_download_flow.py
│   │   ├── test_interactive_mode.py
│   │   └── test_config_integration.py
│   ├── fixtures/             # Test fixtures
│   │   ├── config/
│   │   ├── videos/
│   │   └── responses/
│   └── mocks/                # Mock objects
│       ├── __init__.py
│       ├── youtube.py
│       └── network.py
├── scripts/                  # Development scripts
│   ├── build.py             # Build automation
│   ├── release.py           # Release management
│   ├── test_runner.py       # Test automation
│   └── docs_generator.py    # Documentation generation
├── examples/                 # Usage examples
│   ├── basic_usage.py       # Basic API usage
│   ├── advanced_usage.py    # Advanced features
│   ├── custom_plugin.py     # Plugin development
│   └── integration/         # Integration examples
│       ├── flask_app.py
│       ├── django_app.py
│       └── fastapi_app.py
├── .gitignore               # Git ignore patterns
├── .gitattributes          # Git attributes
├── .editorconfig           # Editor configuration
├── .pre-commit-config.yaml # Pre-commit hooks
├── pyproject.toml          # Project configuration
├── setup.py                # Legacy setup file
├── requirements.txt        # Core dependencies
├── requirements-dev.txt    # Development dependencies
├── README.md               # Project README
├── LICENSE                 # License file
├── CHANGELOG.md            # Version history
├── CONTRIBUTING.md         # Contribution guidelines
└── MANIFEST.in             # Package manifest
```

## 🎯 Core Modules

### tubeharvest/core/

Contains the core functionality of TubeHarvest.

#### `downloader.py`
```python
"""
Main download engine with support for:
- Single video downloads
- Playlist processing
- Batch operations
- Concurrent downloads
- Retry logic
"""

class TubeHarvest:
    """Main downloader class"""
    
class DownloadSession:
    """Individual download session"""
    
class BatchDownloader:
    """Batch download manager"""
```

#### `extractor.py`
```python
"""
Metadata extraction and video information retrieval:
- Video metadata (title, description, etc.)
- Available formats and qualities
- Thumbnail URLs
- Subtitle tracks
"""

class MetadataExtractor:
    """Extract video metadata"""
    
class FormatExtractor:
    """Extract available formats"""
```

#### `formats.py`
```python
"""
Format selection and quality management:
- Quality preference resolution
- Format compatibility checks
- Codec preferences
- File size estimation
"""

class FormatSelector:
    """Select optimal format"""
    
class QualityResolver:
    """Resolve quality preferences"""
```

#### `progress.py`
```python
"""
Progress tracking and reporting:
- Download progress calculation
- Speed measurement
- ETA estimation
- Progress callbacks
"""

class ProgressTracker:
    """Track download progress"""
    
class ProgressReporter:
    """Report progress to UI"""
```

#### `processor.py`
```python
"""
Post-processing operations:
- Audio extraction
- Format conversion
- Metadata embedding
- File organization
"""

class PostProcessor:
    """Handle post-processing"""
    
class AudioProcessor:
    """Audio-specific processing"""
```

### tubeharvest/cli/

Command-line interface implementation.

#### `main.py`
```python
"""
Main CLI entry point:
- Argument parsing
- Command routing
- Error handling
- Output formatting
"""

def main():
    """Main CLI entry point"""
    
def run_command(args):
    """Execute CLI command"""
```

#### `args.py`
```python
"""
Argument parsing and validation:
- Command-line argument definitions
- Input validation
- Help text generation
- Default values
"""

class ArgumentParser:
    """Enhanced argument parser"""
    
def create_parser():
    """Create argument parser"""
```

#### `commands.py`
```python
"""
Command implementations:
- Download commands
- Configuration commands
- Information commands
- Utility commands
"""

class DownloadCommand:
    """Handle download operations"""
    
class ConfigCommand:
    """Handle configuration operations"""
```

### tubeharvest/interactive/

Interactive mode with rich console interface.

#### `app.py`
```python
"""
Main interactive application:
- Application lifecycle
- Screen management
- Event handling
- State management
"""

class InteractiveApp:
    """Main interactive application"""
    
class ScreenManager:
    """Manage application screens"""
```

#### `components/`

UI components for the interactive mode:

- **`download.py`**: Download-related components
- **`progress.py`**: Progress display components
- **`settings.py`**: Settings configuration components
- **`widgets.py`**: Common UI widgets

#### `layouts/`

Screen layouts and organization:

- **`main.py`**: Main application layout
- **`setup.py`**: Setup wizard layout

#### `themes/`

Color themes and styling:

- **`default.py`**: Default theme
- **`dark.py`**: Dark theme
- **`light.py`**: Light theme

### tubeharvest/config/

Configuration management system.

#### `manager.py`
```python
"""
Configuration manager:
- Configuration loading/saving
- Profile management
- Environment variable handling
- Validation
"""

class ConfigManager:
    """Manage configuration"""
    
class ProfileManager:
    """Manage configuration profiles"""
```

#### `schema.py`
```python
"""
Configuration schema definition:
- Configuration structure
- Validation rules
- Default values
- Type definitions
"""

CONFIG_SCHEMA = {
    # Schema definition
}
```

### tubeharvest/utils/

Utility modules and helper functions.

#### `filesystem.py`
```python
"""
File system utilities:
- Path manipulation
- Directory creation
- File operations
- Permission handling
"""

def ensure_directory(path):
    """Ensure directory exists"""
    
def safe_filename(name):
    """Create safe filename"""
```

#### `network.py`
```python
"""
Network utilities:
- HTTP requests
- Proxy handling
- Timeout management
- Error handling
"""

class NetworkClient:
    """HTTP client with utilities"""
```

### tubeharvest/plugins/

Plugin system for extensibility.

#### `base.py`
```python
"""
Base plugin class and interfaces:
- Plugin lifecycle
- Hook definitions
- Event system
- Plugin API
"""

class BasePlugin:
    """Base plugin class"""
    
class PluginHook:
    """Plugin hook definition"""
```

#### `manager.py`
```python
"""
Plugin manager:
- Plugin discovery
- Plugin loading
- Hook execution
- Plugin dependencies
"""

class PluginManager:
    """Manage plugins"""
```

## ⚙️ Configuration Files

### `pyproject.toml`

Modern Python project configuration:

```toml
[build-system]
requires = ["setuptools>=61.0", "wheel"]
build-backend = "setuptools.build_meta"

[project]
name = "tubeharvest"
version = "2.0.0"
description = "Advanced YouTube downloader with interactive console interface"
authors = [{name = "MSadeq Sirjani", email = "msadeqsirjani@gmail.com"}]
license = {text = "MIT"}
readme = "README.md"
requires-python = ">=3.8"

dependencies = [
    "yt-dlp>=2023.7.6",
    "rich>=13.0.0",
    "click>=8.0.0",
    "pyyaml>=6.0",
    "requests>=2.28.0"
]

[project.optional-dependencies]
dev = [
    "pytest>=7.0.0",
    "pytest-cov>=4.0.0",
    "black>=23.0.0",
    "flake8>=6.0.0",
    "mypy>=1.0.0"
]

[project.scripts]
tubeharvest = "tubeharvest.cli.main:main"

[tool.setuptools.packages.find]
where = ["src"]

[tool.black]
line-length = 88
target-version = ['py38']

[tool.pytest.ini_options]
testpaths = ["tests"]
python_files = ["test_*.py"]
addopts = "-v --cov=tubeharvest --cov-report=html"
```

### `requirements.txt`

Core dependencies:

```txt
yt-dlp>=2023.7.6
rich>=13.0.0
click>=8.0.0
pyyaml>=6.0
requests>=2.28.0
pathlib>=1.0.1
```

### `requirements-dev.txt`

Development dependencies:

```txt
pytest>=7.0.0
pytest-cov>=4.0.0
pytest-mock>=3.10.0
black>=23.0.0
flake8>=6.0.0
mypy>=1.0.0
pre-commit>=3.0.0
sphinx>=6.0.0
```

## 📚 Documentation

### Structure

- **`docs/`**: Main documentation directory
- **Wiki format**: GitHub Wiki compatible
- **Cross-references**: Extensive linking between documents
- **Examples**: Code examples throughout
- **Screenshots**: Visual guides for interactive mode

### Documentation Files

| File | Purpose |
|------|---------|
| `README.md` | Documentation index |
| `Installation-Guide.md` | Installation instructions |
| `Quick-Start.md` | Getting started quickly |
| `User-Guide.md` | Comprehensive user documentation |
| `CLI-Reference.md` | Command-line reference |
| `Interactive-Mode.md` | Interactive mode guide |
| `Configuration-Guide.md` | Configuration documentation |
| `API-Reference.md` | Python API documentation |
| `Developer-Guide.md` | Development guide |
| `Project-Structure.md` | This document |
| `Troubleshooting.md` | Common issues and solutions |
| `FAQ.md` | Frequently asked questions |
| `Changelog.md` | Version history |

## 🧪 Testing Structure

### Test Organization

```
tests/
├── unit/                   # Unit tests
│   ├── test_core/         # Core module tests
│   ├── test_cli/          # CLI tests
│   ├── test_config/       # Configuration tests
│   └── test_utils/        # Utility tests
├── integration/           # Integration tests
├── fixtures/              # Test data
└── mocks/                 # Mock objects
```

### Test Categories

1. **Unit Tests**: Test individual functions and classes
2. **Integration Tests**: Test component interactions
3. **End-to-End Tests**: Test complete workflows
4. **Mock Tests**: Test with external service mocks

### Test Configuration

**`conftest.py`**:
```python
"""
Pytest configuration and fixtures:
- Common test fixtures
- Mock setup
- Test utilities
- Configuration overrides
"""

@pytest.fixture
def sample_config():
    """Provide sample configuration"""
    
@pytest.fixture
def mock_youtube_response():
    """Mock YouTube API response"""
```

## 🔧 Build and Distribution

### Build Scripts

**`scripts/build.py`**:
```python
"""
Build automation:
- Package building
- Dependency checking
- Version validation
- Distribution preparation
"""

def build_package():
    """Build distribution packages"""
    
def validate_build():
    """Validate built packages"""
```

### Distribution

- **PyPI**: Python Package Index distribution
- **GitHub Releases**: Tagged releases with assets
- **Docker**: Containerized distribution
- **Homebrew**: macOS package manager

### CI/CD Pipeline

**`.github/workflows/ci.yml`**:
```yaml
name: CI
on: [push, pull_request]
jobs:
  test:
    runs-on: ubuntu-latest
    strategy:
      matrix:
        python-version: [3.8, 3.9, '3.10', 3.11]
    steps:
      - uses: actions/checkout@v3
      - name: Set up Python
        uses: actions/setup-python@v4
        with:
          python-version: ${{ matrix.python-version }}
      - name: Install dependencies
        run: |
          pip install -e ".[dev]"
      - name: Run tests
        run: pytest
```

## 🛠️ Development Files

### Code Quality

- **`.pre-commit-config.yaml`**: Pre-commit hooks
- **`.editorconfig`**: Editor configuration
- **`pyproject.toml`**: Tool configuration

### Version Control

- **`.gitignore`**: Ignore patterns
- **`.gitattributes`**: Git attributes

### Contributing

- **`CONTRIBUTING.md`**: Contribution guidelines
- **`CODE_OF_CONDUCT.md`**: Code of conduct
- **Issue templates**: Bug reports and feature requests
- **Pull request template**: PR guidelines

## 📝 Development Workflow

### Adding New Features

1. **Create Feature Branch**: `git checkout -b feature/new-feature`
2. **Implement Feature**: Add code in appropriate modules
3. **Add Tests**: Create comprehensive tests
4. **Update Documentation**: Update relevant docs
5. **Run Tests**: `pytest` and code quality checks
6. **Create Pull Request**: Submit for review

### Module Dependencies

```
Core Dependencies:
├── tubeharvest.core → tubeharvest.utils
├── tubeharvest.cli → tubeharvest.core
├── tubeharvest.interactive → tubeharvest.core
├── tubeharvest.config → tubeharvest.utils
└── tubeharvest.plugins → tubeharvest.core
```

### Best Practices

1. **Separation of Concerns**: Each module has a clear purpose
2. **Dependency Injection**: Use dependency injection for testability
3. **Error Handling**: Comprehensive error handling and logging
4. **Documentation**: Maintain up-to-date documentation
5. **Testing**: High test coverage with meaningful tests

---

*For development setup and contribution guidelines, see the [Developer Guide](Developer-Guide) and [Contributing Guidelines](https://github.com/msadeqsirjani/TubeHarvest/blob/main/CONTRIBUTING.md).* 