# Contributing to TubeHarvest

Thank you for your interest in contributing to TubeHarvest! This document provides guidelines and information for contributors.

## 🚀 Quick Start

1. **Fork the repository** on GitHub
2. **Clone your fork** locally:
   ```bash
   git clone https://github.com/msadeqsirjani/TubeHarvest.git
   cd TubeHarvest
   ```
3. **Create a virtual environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```
4. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   pip install -r requirements-dev.txt  # If available
   ```

## 🛠️ Development Setup

### Prerequisites
- Python 3.8 or higher
- FFmpeg (for video/audio processing)
- Git

### Local Development
1. Create a new branch for your feature/bugfix:
   ```bash
   git checkout -b feature/your-feature-name
   ```
2. Make your changes
3. Run tests to ensure everything works:
   ```bash
   python -m pytest tests/
   ```
4. Run linting and formatting:
   ```bash
   black src/
   flake8 src/
   mypy src/
   ```

## 📋 Code Standards

### Python Style Guide
- Follow [PEP 8](https://pep8.org/) style guidelines
- Use [Black](https://black.readthedocs.io/) for code formatting
- Maximum line length: 88 characters (Black default)
- Use type hints for function parameters and return values

### Code Quality
- Write clear, self-documenting code
- Add docstrings to all public functions and classes
- Follow the existing code structure and patterns
- Ensure your code is compatible with Python 3.8+

### Git Commit Guidelines
Use clear, descriptive commit messages following the conventional commit format:
```
type(scope): description

[optional body]

[optional footer]
```

Types:
- `feat`: New feature
- `fix`: Bug fix
- `docs`: Documentation changes
- `style`: Code style changes (formatting, etc.)
- `refactor`: Code refactoring
- `test`: Adding or updating tests
- `chore`: Maintenance tasks

Examples:
```
feat(downloader): add support for 4K video downloads
fix(ui): resolve progress bar display issue on Windows
docs(readme): update installation instructions
```

## 🧪 Testing

### Running Tests
```bash
# Run all tests
python -m pytest

# Run tests with coverage
python -m pytest --cov=src

# Run specific test file
python -m pytest tests/test_downloader.py

# Run tests in verbose mode
python -m pytest -v
```

### Writing Tests
- Write unit tests for all new functionality
- Use meaningful test names that describe what is being tested
- Follow the AAA pattern: Arrange, Act, Assert
- Mock external dependencies (YouTube API calls, file system operations)
- Test both success and failure scenarios

### Test Structure
```
tests/
├── __init__.py
├── conftest.py              # Pytest configuration and fixtures
├── test_downloader.py       # Tests for downloader module
├── test_ui.py              # Tests for UI module
├── test_utils.py           # Tests for utility functions
└── integration/            # Integration tests
    └── test_full_download.py
```

## 📝 Documentation

### Code Documentation
- Add docstrings to all public functions, classes, and modules
- Use Google-style docstrings:
```python
def download_video(url: str, output_path: str) -> bool:
    """Download a video from YouTube.
    
    Args:
        url: The YouTube video URL to download.
        output_path: The path where the video should be saved.
        
    Returns:
        True if download was successful, False otherwise.
        
    Raises:
        ValueError: If the URL is invalid.
        IOError: If the output path is not writable.
    """
    pass
```

### User Documentation
- Update README.md for user-facing changes
- Add examples for new features
- Update command-line help text
- Create or update wiki pages for complex features

## 🔍 Pull Request Process

### Before Submitting
1. **Test your changes** thoroughly
2. **Run the full test suite** and ensure all tests pass
3. **Check code style** with Black and Flake8
4. **Update documentation** if needed
5. **Add tests** for new functionality

### Submitting Your PR
1. **Push your branch** to your fork:
   ```bash
   git push origin feature/your-feature-name
   ```
2. **Create a pull request** on GitHub
3. **Fill out the PR template** completely
4. **Link any related issues** using "Fixes #issue-number"
5. **Request review** from maintainers

### PR Review Process
- All PRs require at least one review from a maintainer
- CI/CD checks must pass before merging
- Address any feedback promptly
- Keep PRs focused on a single feature/fix when possible

## 🐛 Reporting Issues

### Bug Reports
Use the bug report template and include:
- TubeHarvest version
- Python version
- Operating system
- Steps to reproduce
- Expected vs actual behavior
- Error logs (if applicable)

### Feature Requests
Use the feature request template and include:
- Clear description of the problem you're solving
- Proposed solution
- Use cases and examples
- Priority level

## 💡 Feature Development Guidelines

### Before Starting
1. **Check existing issues** to avoid duplicate work
2. **Discuss major features** in an issue first
3. **Consider backward compatibility**
4. **Think about performance implications**

### Implementation Guidelines
- Keep changes focused and atomic
- Follow existing architectural patterns
- Add comprehensive error handling
- Consider cross-platform compatibility
- Add appropriate logging

### UI/UX Considerations
- Maintain consistency with existing interface
- Test on different terminal sizes
- Ensure accessibility (color blind friendly)
- Provide clear feedback to users

## 🤝 Community Guidelines

### Code of Conduct
- Be respectful and inclusive
- Help others learn and grow
- Focus on constructive feedback
- Respect different viewpoints and experiences

### Getting Help
- Check existing documentation first
- Search issues for similar problems
- Ask questions in GitHub Discussions
- Join community channels (if available)

## 📞 Contact

- **GitHub Issues**: For bugs and feature requests
- **GitHub Discussions**: For questions and community discussion
- **Email**: [Maintainer email if available]

## 🎉 Recognition

Contributors will be recognized in:
- CONTRIBUTORS.md file
- Release notes for significant contributions
- GitHub repository insights

Thank you for contributing to TubeHarvest! 🚀 