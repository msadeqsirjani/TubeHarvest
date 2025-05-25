# 📦 Publishing TubeHarvest to PyPI

This guide covers the complete process for publishing TubeHarvest to PyPI so users can install it with `pip install tubeharvest`.

## 📋 Prerequisites

### 1. PyPI Accounts

Create accounts on both platforms:

- **Test PyPI**: https://test.pypi.org/account/register/
- **Production PyPI**: https://pypi.org/account/register/

### 2. API Tokens

Generate API tokens for secure uploads:

#### Test PyPI Token:
1. Go to https://test.pypi.org/manage/account/token/
2. Click "Add API token"
3. Name: `TubeHarvest-TestPyPI`
4. Scope: "Entire account" or "Project: tubeharvest"
5. Copy the token (starts with `pypi-`)

#### Production PyPI Token:
1. Go to https://pypi.org/manage/account/token/
2. Click "Add API token"
3. Name: `TubeHarvest-PyPI`
4. Scope: "Entire account" or "Project: tubeharvest"
5. Copy the token (starts with `pypi-`)

### 3. Required Tools

Install the publishing tools:

```bash
pip install build twine
```

## 🔧 Setup

### 1. Configure Git and GitHub

Ensure your repository is properly configured:

```bash
# Set GitHub repository secrets (for automated publishing)
# Go to: https://github.com/msadeqsirjani/TubeHarvest/settings/secrets/actions

# Add these secrets:
# - PYPI_API_TOKEN: Your production PyPI token
# - TEST_PYPI_API_TOKEN: Your test PyPI token
```

### 2. Local Configuration

Create `~/.pypirc` for local publishing:

```ini
[distutils]
index-servers = 
    pypi
    testpypi

[pypi]
repository = https://upload.pypi.org/legacy/
username = __token__
password = pypi-YOUR_PRODUCTION_TOKEN_HERE

[testpypi]
repository = https://test.pypi.org/legacy/
username = __token__
password = pypi-YOUR_TEST_TOKEN_HERE
```

## 🚀 Publishing Process

### Method 1: Automated Script (Recommended)

Use the provided automation script:

```bash
# Test publishing to Test PyPI
python scripts/publish.py --test

# Publish to production PyPI
python scripts/publish.py --prod

# Skip tests/checks (for development)
python scripts/publish.py --test --skip-tests --skip-checks
```

### Method 2: Manual Step-by-Step

#### Step 1: Pre-publishing Checks

```bash
# Run tests
python -m pytest tests/ -v

# Check code formatting
python -m black --check tubeharvest/

# Check linting
python -m flake8 tubeharvest/

# Check types (optional)
python -m mypy tubeharvest/
```

#### Step 2: Clean and Build

```bash
# Clean previous builds
rm -rf build/ dist/ *.egg-info/

# Build the package
python -m build

# Check the built package
python -m twine check dist/*
```

#### Step 3: Test Upload

```bash
# Upload to Test PyPI
python -m twine upload --repository testpypi dist/*

# Test installation
pip install --index-url https://test.pypi.org/simple/ tubeharvest

# Test the CLI
tubeharvest --help
```

#### Step 4: Production Upload

```bash
# Upload to production PyPI
python -m twine upload dist/*

# Verify on PyPI
# Visit: https://pypi.org/project/tubeharvest/

# Test installation
pip install tubeharvest
```

### Method 3: GitHub Actions (Automated)

The repository includes automated publishing via GitHub Actions:

#### For Releases:
1. Create a new release on GitHub
2. The workflow automatically publishes to PyPI
3. Package is available within minutes

#### Manual Trigger:
1. Go to Actions tab in GitHub
2. Select "Publish to PyPI" workflow
3. Click "Run workflow"
4. Choose environment (testpypi/pypi)

## 📋 Version Management

### Updating Version

Update version in `pyproject.toml`:

```toml
[project]
name = "tubeharvest"
version = "2.1.0"  # Update this
```

### Version Strategy

Follow [Semantic Versioning](https://semver.org/):

- **MAJOR** (3.0.0): Breaking changes
- **MINOR** (2.1.0): New features, backward compatible
- **PATCH** (2.0.1): Bug fixes, backward compatible

### Release Process

1. **Update Version**: Modify `pyproject.toml`
2. **Update Changelog**: Add new version to `CHANGELOG.md`
3. **Create Git Tag**: `git tag v2.1.0`
4. **Push Tag**: `git push origin v2.1.0`
5. **Create GitHub Release**: Use the web interface
6. **Automated Publishing**: GitHub Actions handles the rest

## 🔍 Verification

### Test Installation

```bash
# Create test environment
python -m venv test_env
source test_env/bin/activate  # On Windows: test_env\Scripts\activate

# Install from PyPI
pip install tubeharvest

# Test basic functionality
tubeharvest --version
tubeharvest --help

# Test interactive mode
tubeharvest -i

# Clean up
deactivate
rm -rf test_env
```

### Package Health

Check package status:

- **PyPI Page**: https://pypi.org/project/tubeharvest/
- **Download Stats**: https://pypistats.org/packages/tubeharvest
- **Package Info**: `pip show tubeharvest`

## 🛠️ Troubleshooting

### Common Issues

#### 1. Package Name Already Exists
```
ERROR: The user 'username' isn't allowed to upload to project 'tubeharvest'
```

**Solution**: The package name is already taken. You need to:
- Choose a different name in `pyproject.toml`
- Or contact PyPI support if you own the name

#### 2. Authentication Failed
```
ERROR: Invalid or non-existent authentication information
```

**Solution**: 
- Check your API token
- Verify `~/.pypirc` configuration
- Regenerate token if needed

#### 3. Package Validation Errors
```
ERROR: File already exists
```

**Solution**:
- You can't upload the same version twice
- Increment version number
- Or use `--skip-existing` flag

#### 4. Build Failures
```
ERROR: Failed building wheel
```

**Solution**:
- Check `pyproject.toml` syntax
- Ensure all dependencies are available
- Verify Python version compatibility

### Getting Help

- **PyPI Support**: https://pypi.org/help/
- **Packaging Guide**: https://packaging.python.org/
- **Twine Documentation**: https://twine.readthedocs.io/
- **GitHub Issues**: https://github.com/msadeqsirjani/TubeHarvest/issues

## 📊 Monitoring

### Track Usage

Monitor package adoption:

1. **PyPI Stats**: https://pypistats.org/packages/tubeharvest
2. **GitHub Stars**: Repository star count
3. **Issues/PRs**: Community engagement
4. **Download Trends**: Monthly/weekly downloads

### Update Strategy

Keep package healthy:

1. **Regular Updates**: Monthly maintenance releases
2. **Security Patches**: Immediate for critical vulnerabilities
3. **Feature Releases**: Quarterly major features
4. **Documentation**: Keep docs updated with code

## 🎯 Best Practices

### Before Publishing

- [ ] All tests pass
- [ ] Code is properly formatted
- [ ] Documentation is updated
- [ ] Version is incremented
- [ ] Changelog is updated
- [ ] No security vulnerabilities

### Package Quality

- [ ] Clear description and keywords
- [ ] Proper license specification
- [ ] Complete dependency list
- [ ] Good README with examples
- [ ] Responsive to user issues

### Security

- [ ] Use API tokens, not passwords
- [ ] Keep tokens secure
- [ ] Enable 2FA on PyPI accounts
- [ ] Regular security audits

---

## 🎉 Success!

Once published, users can install TubeHarvest with:

```bash
pip install tubeharvest
```

Your package will be available at:
- **PyPI**: https://pypi.org/project/tubeharvest/
- **Documentation**: https://github.com/msadeqsirjani/TubeHarvest/wiki

Congratulations on publishing your package! 🚀 