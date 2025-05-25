# 🔧 Troubleshooting Guide

This guide helps you solve common issues with TubeHarvest. Find solutions for installation problems, download failures, and performance issues.

## 🚨 Quick Diagnostics

### Check Your Setup

Before troubleshooting, verify your installation:

```bash
# Check TubeHarvest version
tubeharvest --version

# Check Python version
python --version

# Check dependencies
pip list | grep -E "(yt-dlp|rich|tqdm)"

# Test basic functionality
tubeharvest --help
```

### System Information

```bash
# Check system info
uname -a                    # Linux/macOS
systeminfo                 # Windows

# Check disk space
df -h                       # Linux/macOS
dir                         # Windows

# Check network connectivity
ping google.com
```

## 🐛 Common Issues

### Installation Problems

#### Problem: "Command not found: tubeharvest"

**Symptoms:**
```bash
$ tubeharvest --help
bash: tubeharvest: command not found
```

**Solutions:**

1. **Check if installed:**
   ```bash
   pip show tubeharvest
   ```

2. **Install TubeHarvest:**
   ```bash
   pip install tubeharvest
   ```

3. **Use Python module:**
   ```bash
   python -m tubeharvest --help
   ```

4. **Check PATH (if installed with --user):**
   ```bash
   # Add to ~/.bashrc or ~/.zshrc
   export PATH="$HOME/.local/bin:$PATH"
   ```

#### Problem: "Permission denied" during installation

**Symptoms:**
```bash
ERROR: Could not install packages due to an EnvironmentError: [Errno 13] Permission denied
```

**Solutions:**

1. **Use user installation:**
   ```bash
   pip install --user tubeharvest
   ```

2. **Use virtual environment:**
   ```bash
   python -m venv tubeharvest-env
   source tubeharvest-env/bin/activate  # Linux/macOS
   # tubeharvest-env\Scripts\activate    # Windows
   pip install tubeharvest
   ```

3. **Use sudo (Linux/macOS only):**
   ```bash
   sudo pip install tubeharvest
   ```

#### Problem: "No module named 'tubeharvest'"

**Symptoms:**
```bash
ModuleNotFoundError: No module named 'tubeharvest'
```

**Solutions:**

1. **Install in correct Python environment:**
   ```bash
   which python
   which pip
   pip install tubeharvest
   ```

2. **Check virtual environment:**
   ```bash
   # Activate the correct environment
   source venv/bin/activate
   pip install tubeharvest
   ```

### Download Issues

#### Problem: "Video unavailable" or "Private video"

**Symptoms:**
```
ERROR: Video unavailable
ERROR: This is a private video
```

**Solutions:**

1. **Check URL validity:**
   - Ensure the video is public
   - Verify the URL is correct
   - Try accessing the video in a browser

2. **Update yt-dlp:**
   ```bash
   pip install --upgrade yt-dlp
   ```

3. **Try different URL format:**
   ```bash
   # If using youtu.be link, try full YouTube URL
   https://www.youtube.com/watch?v=VIDEO_ID
   ```

#### Problem: Slow download speeds

**Symptoms:**
- Downloads taking very long
- Low MB/s transfer rates

**Solutions:**

1. **Reduce worker count:**
   ```bash
   tubeharvest -u "URL" --workers 1
   ```

2. **Lower quality:**
   ```bash
   tubeharvest -u "URL" -q 720
   ```

3. **Check network:**
   ```bash
   # Test internet speed
   speedtest-cli
   ```

4. **Use different format:**
   ```bash
   # WebM is often smaller/faster
   tubeharvest -u "URL" -f webm
   ```

#### Problem: "HTTP Error 429: Too Many Requests"

**Symptoms:**
```
ERROR: HTTP Error 429: Too Many Requests
```

**Solutions:**

1. **Wait and retry:**
   ```bash
   # Wait 15-30 minutes then try again
   tubeharvest -u "URL"
   ```

2. **Reduce concurrent downloads:**
   ```bash
   tubeharvest -u "URL" --workers 1
   ```

3. **Use different IP/VPN:**
   - Connect to VPN
   - Restart router for new IP

#### Problem: "FFmpeg not found"

**Symptoms:**
```
ERROR: ffmpeg not found. Please install ffmpeg
```

**Solutions:**

1. **Install FFmpeg:**

   **Windows:**
   ```bash
   # Using Chocolatey
   choco install ffmpeg
   
   # Or download from https://ffmpeg.org
   ```

   **macOS:**
   ```bash
   brew install ffmpeg
   ```

   **Linux (Ubuntu/Debian):**
   ```bash
   sudo apt update
   sudo apt install ffmpeg
   ```

2. **Verify installation:**
   ```bash
   ffmpeg -version
   ```

3. **Add to PATH (Windows):**
   - Add FFmpeg bin directory to system PATH
   - Restart command prompt

### Network Issues

#### Problem: SSL Certificate errors

**Symptoms:**
```
ERROR: certificate verify failed
SSL: CERTIFICATE_VERIFY_FAILED
```

**Solutions:**

1. **Update certificates:**
   ```bash
   pip install --upgrade certifi
   ```

2. **Update Python:**
   ```bash
   # On macOS, run:
   /Applications/Python\ 3.x/Install\ Certificates.command
   ```

3. **Bypass SSL (temporary):**
   ```bash
   # NOT RECOMMENDED for permanent use
   pip install --trusted-host pypi.org --trusted-host pypi.python.org tubeharvest
   ```

#### Problem: Proxy/Firewall blocking downloads

**Symptoms:**
- Connection timeouts
- "Connection refused" errors

**Solutions:**

1. **Configure proxy:**
   ```bash
   export HTTP_PROXY=http://proxy.example.com:8080
   export HTTPS_PROXY=http://proxy.example.com:8080
   ```

2. **Use different DNS:**
   ```bash
   # Try using Google DNS: 8.8.8.8, 8.8.4.4
   # Or Cloudflare DNS: 1.1.1.1, 1.0.0.1
   ```

### Performance Issues

#### Problem: High memory usage

**Symptoms:**
- System becomes slow during downloads
- Out of memory errors

**Solutions:**

1. **Reduce workers:**
   ```bash
   tubeharvest -u "URL" --workers 1
   ```

2. **Download smaller files:**
   ```bash
   tubeharvest -u "URL" -q 480
   ```

3. **Clear temporary files:**
   ```bash
   # Linux/macOS
   rm -rf /tmp/tubeharvest*
   
   # Windows
   del /s /q %TEMP%\tubeharvest*
   ```

#### Problem: Disk space errors

**Symptoms:**
```
ERROR: No space left on device
OSError: [Errno 28] No space left on device
```

**Solutions:**

1. **Check available space:**
   ```bash
   df -h /path/to/downloads  # Linux/macOS
   dir "C:\Downloads"        # Windows
   ```

2. **Change output directory:**
   ```bash
   tubeharvest -u "URL" -o "/path/with/more/space"
   ```

3. **Use lower quality:**
   ```bash
   tubeharvest -u "URL" -q 360 -f webm
   ```

### Format and Quality Issues

#### Problem: "Requested format not available"

**Symptoms:**
```
ERROR: Requested format is not available
```

**Solutions:**

1. **Check available formats:**
   ```bash
   # Use yt-dlp directly to see formats
   yt-dlp -F "VIDEO_URL"
   ```

2. **Use automatic format selection:**
   ```bash
   tubeharvest -u "URL" -f mp4
   ```

3. **Try different quality:**
   ```bash
   tubeharvest -u "URL" -q best
   ```

#### Problem: Audio/video sync issues

**Symptoms:**
- Audio and video out of sync
- Missing audio in video files

**Solutions:**

1. **Use different format:**
   ```bash
   tubeharvest -u "URL" -f mkv
   ```

2. **Download video and audio separately:**
   ```bash
   # Video only
   tubeharvest -u "URL" --video-only
   
   # Audio only
   tubeharvest -u "URL" --audio-only
   ```

3. **Update FFmpeg:**
   ```bash
   # Update to latest FFmpeg version
   ```

## 🔍 Advanced Debugging

### Enable Verbose Output

```bash
# Maximum verbosity
tubeharvest -u "URL" --verbose --debug

# Check yt-dlp directly
yt-dlp --verbose "URL"
```

### Log Files

Check log files for detailed error information:

```bash
# Linux/macOS
~/.config/tubeharvest/logs/

# Windows
%APPDATA%/tubeharvest/logs/
```

### Environment Debugging

```bash
# Check environment variables
env | grep -i tube
env | grep -i python

# Check Python path
python -c "import sys; print('\n'.join(sys.path))"

# Check installed packages
pip list --verbose
```

## 🐞 Reporting Bugs

### Before Reporting

1. **Update to latest version:**
   ```bash
   pip install --upgrade tubeharvest
   ```

2. **Try minimal reproduction:**
   ```bash
   tubeharvest -u "SIMPLE_VIDEO_URL" --verbose
   ```

3. **Check existing issues:**
   - [GitHub Issues](https://github.com/msadeqsirjani/TubeHarvest/issues)

### Bug Report Information

Include this information in bug reports:

```bash
# System information
uname -a                    # Linux/macOS
ver                         # Windows

# TubeHarvest version
tubeharvest --version

# Python version
python --version

# Dependencies
pip list | grep -E "(yt-dlp|rich|tqdm|ffmpeg)"

# Command that failed
tubeharvest -u "URL" --verbose

# Error message (full output)
```

### Create Issue

1. Go to [GitHub Issues](https://github.com/msadeqsirjani/TubeHarvest/issues)
2. Click "New Issue"
3. Choose "Bug Report" template
4. Fill in all sections
5. Include system information and error logs

## 📞 Getting Help

### Support Channels

1. **📖 Documentation:**
   - [Quick Start Guide](Quick-Start)
   - [User Guide](User-Guide)
   - [FAQ](FAQ)

2. **🐛 Bug Reports:**
   - [GitHub Issues](https://github.com/msadeqsirjani/TubeHarvest/issues)

3. **💬 Community:**
   - [Discussions](https://github.com/msadeqsirjani/TubeHarvest/discussions)

### Self-Help Resources

```bash
# Built-in help
tubeharvest --help

# Check configuration
tubeharvest --show-config

# Test installation
python -c "import tubeharvest; print('OK')"
```

## 🔧 Recovery Procedures

### Reset Configuration

```bash
# Remove config files
rm -rf ~/.config/tubeharvest/  # Linux/macOS
rmdir /s "%APPDATA%\tubeharvest"  # Windows

# Reinstall TubeHarvest
pip uninstall tubeharvest
pip install tubeharvest
```

### Clean Installation

```bash
# Complete clean install
pip uninstall tubeharvest yt-dlp
pip cache purge
pip install tubeharvest

# Or use virtual environment
python -m venv fresh-tubeharvest
source fresh-tubeharvest/bin/activate
pip install tubeharvest
```

### Backup and Restore

```bash
# Backup downloads and config
tar -czf tubeharvest-backup.tar.gz ~/Downloads/TubeHarvest ~/.config/tubeharvest/

# Restore
tar -xzf tubeharvest-backup.tar.gz -C ~/
```

## ✅ Prevention Tips

1. **Keep Updated:**
   ```bash
   pip install --upgrade tubeharvest
   ```

2. **Use Virtual Environments:**
   - Isolate TubeHarvest installation
   - Avoid dependency conflicts

3. **Monitor Disk Space:**
   - Regularly clean download directories
   - Use appropriate quality settings

4. **Backup Important Downloads:**
   - Copy important files to secure storage
   - Keep metadata files for re-downloading

5. **Test Before Batch Operations:**
   - Try single video before playlist
   - Verify settings with small downloads

---

*Need more help? Check our [FAQ](FAQ) or [create an issue](https://github.com/msadeqsirjani/TubeHarvest/issues)! 🆘* 