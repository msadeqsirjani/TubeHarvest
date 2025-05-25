# 📦 Installation Guide

This guide will help you install TubeHarvest on your system.

## 🔧 Prerequisites

Before installing TubeHarvest, ensure you have:

- **Python 3.8+** (Python 3.9+ recommended)
- **pip** (Python package manager)
- **FFmpeg** (for video processing)

### Installing Python

#### Windows
1. Download Python from [python.org](https://www.python.org/downloads/)
2. Run the installer and check "Add Python to PATH"
3. Verify installation: `python --version`

#### macOS
```bash
# Using Homebrew (recommended)
brew install python

# Or download from python.org
```

#### Linux (Ubuntu/Debian)
```bash
sudo apt update
sudo apt install python3 python3-pip
```

### Installing FFmpeg

#### Windows
```bash
# Using Chocolatey
choco install ffmpeg

# Or download from https://ffmpeg.org/download.html
```

#### macOS
```bash
# Using Homebrew
brew install ffmpeg
```

#### Linux (Ubuntu/Debian)
```bash
sudo apt update
sudo apt install ffmpeg
```

## 📥 Installation Methods

### Method 1: From PyPI (Recommended)

```bash
# Install TubeHarvest
pip install tubeharvest

# Verify installation
tubeharvest --help
```

### Method 2: From Source (Development)

```bash
# Clone the repository
git clone https://github.com/msadeqsirjani/TubeHarvest.git
cd TubeHarvest

# Create virtual environment (recommended)
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Install in editable mode
pip install -e .

# Verify installation
python -m tubeharvest --help
```

### Method 3: Development Setup

For contributors and developers:

```bash
# Clone and enter directory
git clone https://github.com/msadeqsirjani/TubeHarvest.git
cd TubeHarvest

# Run development setup script
chmod +x scripts/install-dev.sh
./scripts/install-dev.sh

# Or use Makefile
make install-dev
```

## 🚀 Quick Verification

After installation, verify TubeHarvest works correctly:

```bash
# Test CLI version
tubeharvest --help

# Test module version
python -m tubeharvest --help

# Test interactive mode
tubeharvest -i
```

## 🐳 Docker Installation

TubeHarvest can also be run in Docker:

```bash
# Pull the image
docker pull tubeharvest/tubeharvest:latest

# Run TubeHarvest
docker run -it --rm -v $(pwd)/downloads:/downloads tubeharvest/tubeharvest

# With custom options
docker run -it --rm -v $(pwd)/downloads:/downloads \
  tubeharvest/tubeharvest -u "VIDEO_URL" -o /downloads
```

## 🔧 Virtual Environment (Recommended)

Using virtual environments isolates TubeHarvest from your system Python:

```bash
# Create virtual environment
python -m venv tubeharvest-env

# Activate (Linux/macOS)
source tubeharvest-env/bin/activate

# Activate (Windows)
tubeharvest-env\Scripts\activate

# Install TubeHarvest
pip install tubeharvest

# Deactivate when done
deactivate
```

## 🎯 Platform-Specific Notes

### Windows
- Use PowerShell or Command Prompt as Administrator for global installation
- Add Python Scripts directory to PATH if commands not found
- Some antivirus software may flag downloaded files

### macOS
- May need to allow TubeHarvest in System Preferences > Security & Privacy
- Use Homebrew for easier dependency management
- Consider using pyenv for Python version management

### Linux
- Install python3-dev for compilation if needed: `sudo apt install python3-dev`
- Use package manager for system-wide installation
- May need sudo for global pip installations

## 🛠️ Troubleshooting Installation

### Common Issues

**Python not found:**
```bash
# Check Python installation
python --version
python3 --version

# Add to PATH or use full path
/usr/bin/python3 -m pip install tubeharvest
```

**Permission denied:**
```bash
# Use user installation
pip install --user tubeharvest

# Or use virtual environment (recommended)
```

**FFmpeg not found:**
```bash
# Verify FFmpeg installation
ffmpeg -version

# Install FFmpeg (see prerequisites above)
```

**SSL Certificate errors:**
```bash
# Upgrade pip and certificates
pip install --upgrade pip
pip install --upgrade certifi
```

### Getting Help

If you encounter issues:

1. Check the [Troubleshooting Guide](Troubleshooting)
2. Search [existing issues](https://github.com/msadeqsirjani/TubeHarvest/issues)
3. Create a [new issue](https://github.com/msadeqsirjani/TubeHarvest/issues/new) with:
   - Your operating system
   - Python version (`python --version`)
   - TubeHarvest version (`tubeharvest --version`)
   - Complete error message

## ✅ Next Steps

After successful installation:

1. Read the [Quick Start Guide](Quick-Start)
2. Explore [Interactive Mode](Interactive-Mode)
3. Check out [Advanced Usage](User-Guide)

---

*Need help? Visit our [Support Page](Troubleshooting) or [open an issue](https://github.com/msadeqsirjani/TubeHarvest/issues).* 