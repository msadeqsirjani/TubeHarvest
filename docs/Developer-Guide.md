# 👨‍💻 Developer Guide

Welcome to TubeHarvest development! This guide covers everything you need to contribute to TubeHarvest, from setup to deployment.

## 🚀 Quick Start for Developers

### Prerequisites

- **Python 3.8+** (3.9+ recommended)
- **Git** for version control
- **FFmpeg** for video processing
- **Node.js** (optional, for additional tools)

### Development Setup

```bash
# Clone the repository
git clone https://github.com/msadeqsirjani/TubeHarvest.git
cd TubeHarvest

# Run automated development setup
make install-dev

# Or manual setup
chmod +x scripts/install-dev.sh
./scripts/install-dev.sh
```

This will:
- Create virtual environment
- Install all dependencies
- Install pre-commit hooks
- Install TubeHarvest in editable mode

## 📁 Project Structure

```
TubeHarvest/
├── tubeharvest/                 # Main package
│   ├── __init__.py             # Package initialization
│   ├── __main__.py             # Entry point for python -m tubeharvest
│   ├── cli/                    # Command line interface
│   │   ├── __init__.py
│   │   ├── main.py             # CLI main entry point
│   │   └── interactive.py      # Interactive mode
│   ├── core/                   # Core business logic
│   │   ├── __init__.py
│   │   ├── downloader.py       # Download engine
│   │   └── utils.py            # Utility functions
│   ├── ui/                     # User interface components
│   │   ├── __init__.py
│   │   └── console.py          # Rich console interface
│   └── config/                 # Configuration management
│       ├── __init__.py
│       └── settings.py         # App settings
├── tests/                      # Test suite
│   ├── conftest.py            # Test configuration
│   ├── test_downloader.py     # Downloader tests
│   ├── test_cli.py            # CLI tests
│   └── fixtures/              # Test fixtures
├── docs/                       # Documentation
├── examples/                   # Example scripts
├── scripts/                    # Development scripts
│   ├── install-dev.sh         # Development setup
│   ├── run-tests.sh           # Test runner
│   ├── format-code.sh         # Code formatter
│   └── tubeharvest-gui        # GUI launcher
├── requirements/               # Organized requirements
│   ├── base.txt               # Core dependencies
│   ├── dev.txt                # Development dependencies
│   ├── test.txt               # Testing dependencies
│   └── docs.txt               # Documentation dependencies
├── .github/                    # GitHub workflows
│   ├── workflows/             # CI/CD pipelines
│   └── ISSUE_TEMPLATE/        # Issue templates
├── pyproject.toml             # Modern Python packaging
├── Makefile                   # Development commands
└── README.md                  # Project overview
```

## 🛠️ Development Workflow

### Setting Up Your Environment

1. **Fork the repository** on GitHub
2. **Clone your fork:**
   ```bash
   git clone https://github.com/YOUR_USERNAME/TubeHarvest.git
   cd TubeHarvest
   ```

3. **Add upstream remote:**
   ```bash
   git remote add upstream https://github.com/msadeqsirjani/TubeHarvest.git
   ```

4. **Install development dependencies:**
   ```bash
   make install-dev
   ```

### Making Changes

1. **Create a feature branch:**
   ```bash
   git checkout -b feature/your-feature-name
   ```

2. **Make your changes** following our coding standards

3. **Run tests:**
   ```bash
   make test
   # or
   ./scripts/run-tests.sh
   ```

4. **Format code:**
   ```bash
   make format
   # or  
   ./scripts/format-code.sh
   ```

5. **Commit changes:**
   ```bash
   git add .
   git commit -m "feat: add your feature description"
   ```

### Testing Your Changes

```bash
# Run all tests
make test

# Run specific test file
pytest tests/test_downloader.py -v

# Run with coverage
make test-cov

# Run linting
make lint

# Run type checking
make type-check
```

## 🏗️ Architecture Overview

### Core Components

#### 1. Downloader Engine (`tubeharvest/core/downloader.py`)

The main download engine built on yt-dlp:

```python
class TubeHarvestDownloader:
    """Main downloader class."""
    
    def __init__(self, config: dict):
        self.config = config
        self.ydl_opts = self._build_ydl_opts()
    
    def download_video(self, url: str) -> dict:
        """Download a single video."""
        # Implementation
    
    def download_playlist(self, url: str) -> list:
        """Download entire playlist."""
        # Implementation
```

#### 2. CLI Interface (`tubeharvest/cli/`)

Command line interface using argparse:

```python
def main():
    """Main CLI entry point."""
    parser = create_parser()
    args = parser.parse_args()
    
    if args.interactive:
        return interactive_main()
    else:
        return run_download(args)
```

#### 3. UI Components (`tubeharvest/ui/`)

Rich console interface for beautiful output:

```python
class TubeHarvestUI:
    """Rich console interface."""
    
    def __init__(self):
        self.console = Console()
        self.progress = None
    
    def display_banner(self):
        """Show application banner."""
        # Implementation
```

#### 4. Configuration (`tubeharvest/config/`)

Application settings and configuration:

```python
class Settings:
    """Application settings."""
    
    DEFAULT_OUTPUT_DIR = "downloads"
    DEFAULT_FORMAT = "mp4"
    DEFAULT_QUALITY = "best"
    DEFAULT_WORKERS = 4
```

### Data Flow

```
User Input → CLI Parser → Configuration → Downloader → UI Feedback
     ↓
URL Validation → yt-dlp → Progress Tracking → File Output
```

## 🧪 Testing

### Test Structure

```
tests/
├── conftest.py                 # Pytest configuration and fixtures
├── test_downloader.py         # Core downloader tests
├── test_cli.py                # CLI interface tests  
├── test_ui.py                 # UI component tests
├── test_utils.py              # Utility function tests
├── integration/               # Integration tests
│   ├── test_download_flow.py  # End-to-end tests
│   └── test_interactive.py    # Interactive mode tests
└── fixtures/                  # Test data
    ├── mock_video_info.json   # Mock video metadata
    └── sample_urls.txt         # Test URLs
```

### Writing Tests

#### Unit Tests

```python
import pytest
from tubeharvest.core.downloader import TubeHarvestDownloader

class TestDownloader:
    """Test downloader functionality."""
    
    def test_video_download(self, mock_video_info):
        """Test single video download."""
        downloader = TubeHarvestDownloader({})
        result = downloader.download_video("mock://test")
        assert result["status"] == "success"
    
    @pytest.mark.parametrize("format,expected", [
        ("mp4", "video"),
        ("mp3", "audio"),
    ])
    def test_format_detection(self, format, expected):
        """Test format detection."""
        downloader = TubeHarvestDownloader({"format": format})
        assert downloader.get_media_type() == expected
```

#### Integration Tests

```python
@pytest.mark.integration
def test_full_download_workflow():
    """Test complete download process."""
    # Test with real (but fast) video
    pass
```

### Test Fixtures

Create reusable test data in `tests/conftest.py`:

```python
@pytest.fixture
def mock_video_info():
    """Mock video information."""
    return {
        "title": "Test Video",
        "uploader": "Test Channel",
        "duration": 120,
        "formats": [...]
    }

@pytest.fixture
def temp_download_dir(tmp_path):
    """Temporary download directory."""
    return tmp_path / "downloads"
```

### Running Tests

```bash
# All tests
pytest

# Specific test file
pytest tests/test_downloader.py

# With coverage
pytest --cov=tubeharvest

# Integration tests only
pytest -m integration

# Skip slow tests
pytest -m "not slow"

# Verbose output
pytest -v -s
```

## 🎨 Code Style and Standards

### Python Style Guide

We follow **PEP 8** with some modifications:

- **Line length**: 88 characters (Black default)
- **Quotes**: Double quotes preferred
- **Imports**: Sorted with isort
- **Type hints**: Required for public functions

### Code Formatting

Automated with pre-commit hooks:

```bash
# Format code
make format

# Check formatting
black --check tubeharvest/
isort --check-only tubeharvest/
flake8 tubeharvest/
```

### Type Annotations

Use type hints for better code clarity:

```python
from typing import Dict, List, Optional, Union

def download_video(
    self, 
    url: str, 
    output_dir: Optional[str] = None
) -> Dict[str, Union[str, bool]]:
    """Download video with type safety."""
    pass
```

### Documentation

Follow Google docstring style:

```python
def download_playlist(self, url: str, max_downloads: int = 50) -> List[Dict]:
    """Download entire playlist.
    
    Args:
        url: YouTube playlist URL
        max_downloads: Maximum number of videos to download
        
    Returns:
        List of download results with metadata
        
    Raises:
        ValueError: If URL is invalid
        DownloadError: If download fails
        
    Example:
        >>> downloader = TubeHarvestDownloader()
        >>> results = downloader.download_playlist("playlist_url")
        >>> len(results)
        10
    """
    pass
```

## 🔧 Development Tools

### Available Make Commands

```bash
# Development setup
make install-dev          # Install development environment
make install              # Install package only

# Testing
make test                 # Run all tests
make test-cov             # Run tests with coverage

# Code quality
make lint                 # Run linting checks
make format               # Format code
make type-check           # Run type checking
make security-check       # Security analysis

# Building
make clean                # Clean build artifacts
make build                # Build distribution packages
make upload-test          # Upload to test PyPI
make upload               # Upload to PyPI

# Documentation
make docs                 # Build documentation

# Help
make help                 # Show all commands
```

### Pre-commit Hooks

Automatically installed with development setup:

```yaml
# .pre-commit-config.yaml
repos:
  - repo: https://github.com/psf/black
    rev: '23.7.0'
    hooks:
      - id: black
        
  - repo: https://github.com/pycqa/isort
    rev: '5.12.0'
    hooks:
      - id: isort
        
  - repo: https://github.com/pycqa/flake8
    rev: '6.0.0'
    hooks:
      - id: flake8
```

### IDE Configuration

#### VS Code

Recommended `.vscode/settings.json`:

```json
{
    "python.defaultInterpreterPath": ".venv/bin/python",
    "python.linting.enabled": true,
    "python.linting.flake8Enabled": true,
    "python.formatting.provider": "black",
    "python.sortImports.provider": "isort",
    "editor.formatOnSave": true,
    "editor.codeActionsOnSave": {
        "source.organizeImports": true
    }
}
```

#### PyCharm

1. Set interpreter to `.venv/bin/python`
2. Configure Black as external tool
3. Enable flake8 inspection
4. Set line length to 88

## 📦 Building and Distribution

### Package Building

```bash
# Clean previous builds
make clean

# Build source and wheel distributions
make build

# Check distribution
twine check dist/*
```

### Version Management

Version is managed in `pyproject.toml`:

```toml
[project]
name = "tubeharvest"
version = "2.0.0"
```

### Release Process

1. **Update version** in `pyproject.toml`
2. **Update CHANGELOG.md**
3. **Create release branch:**
   ```bash
   git checkout -b release/v2.0.0
   ```
4. **Run full test suite:**
   ```bash
   make test
   make lint
   make security-check
   ```
5. **Create pull request**
6. **After merge, create GitHub release**
7. **Automated deployment** via GitHub Actions

## 🌐 CI/CD Pipeline

### GitHub Actions Workflows

#### CI Pipeline (`.github/workflows/ci.yml`)

```yaml
name: CI/CD Pipeline

on:
  push:
    branches: [ main, develop ]
  pull_request:
    branches: [ main, develop ]

jobs:
  test:
    runs-on: ${{ matrix.os }}
    strategy:
      matrix:
        os: [ubuntu-latest, windows-latest, macos-latest]
        python-version: ['3.8', '3.9', '3.10', '3.11', '3.12']
```

Features:
- **Multi-platform testing** (Ubuntu, Windows, macOS)
- **Multiple Python versions** (3.8-3.12)
- **Code quality checks** (linting, formatting, type checking)
- **Security scanning** (bandit, safety)
- **Coverage reporting** (codecov)
- **Automated PyPI publishing** on releases

### Local CI Simulation

Test locally before pushing:

```bash
# Run the same checks as CI
./scripts/run-tests.sh

# Or individual checks
make test
make lint
make type-check
make security-check
```

## 🤝 Contributing Guidelines

### Submitting Changes

1. **Fork** the repository
2. **Create feature branch** from `develop`
3. **Make changes** with tests
4. **Ensure all checks pass**
5. **Submit pull request** to `develop` branch

### Pull Request Process

1. **Clear description** of changes
2. **Link related issues**
3. **Add tests** for new features
4. **Update documentation** if needed
5. **Ensure CI passes**

### Code Review

All changes require review:
- **Code quality** and style
- **Test coverage** requirements
- **Performance** impact
- **Security** considerations
- **Documentation** completeness

## 🔍 Debugging and Profiling

### Debug Mode

Enable verbose logging:

```python
import logging
logging.basicConfig(level=logging.DEBUG)

# Or set environment variable
export TUBEHARVEST_DEBUG=1
```

### Performance Profiling

```python
import cProfile
import pstats

# Profile a function
cProfile.run('downloader.download_video(url)', 'profile_stats')
stats = pstats.Stats('profile_stats')
stats.sort_stats('cumulative').print_stats(10)
```

### Memory Profiling

```bash
# Install memory profiler
pip install memory-profiler

# Profile memory usage
python -m memory_profiler script.py
```

## 📚 Additional Resources

### Documentation

- **API Reference**: Auto-generated from docstrings
- **User Guide**: Comprehensive usage documentation
- **Contributing**: Detailed contribution guidelines

### External Dependencies

- **yt-dlp**: YouTube download engine
- **Rich**: Beautiful terminal output
- **Click**: Command line interface
- **Pytest**: Testing framework
- **Black**: Code formatting

### Learning Resources

- [Python Packaging Guide](https://packaging.python.org/)
- [pytest Documentation](https://docs.pytest.org/)
- [Rich Documentation](https://rich.readthedocs.io/)
- [yt-dlp Documentation](https://github.com/yt-dlp/yt-dlp)

## 🆘 Getting Help

### Development Support

- **GitHub Discussions**: For development questions
- **GitHub Issues**: For bug reports
- **Code Review**: Request feedback on PRs

### Community

- **Contributing Guidelines**: Detailed in CONTRIBUTING.md
- **Code of Conduct**: Community standards
- **Developer Chat**: Discord/Slack (if available)

---

*Happy coding! 🚀 Thank you for contributing to TubeHarvest!* 