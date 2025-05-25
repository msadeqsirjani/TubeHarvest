#!/usr/bin/env python3
"""
Automated script for publishing TubeHarvest to PyPI.

Usage:
    python scripts/publish.py --help
    python scripts/publish.py --test      # Publish to test PyPI
    python scripts/publish.py --prod      # Publish to production PyPI
"""

import argparse
import subprocess
import sys
from pathlib import Path
from typing import List


def run_command(cmd: List[str], check: bool = True) -> subprocess.CompletedProcess:
    """Run a shell command."""
    print(f"Running: {' '.join(cmd)}")
    result = subprocess.run(cmd, check=check, capture_output=True, text=True)
    if result.stdout:
        print(result.stdout)
    if result.stderr:
        print(result.stderr, file=sys.stderr)
    return result


def clean_build():
    """Clean build artifacts."""
    print("🧹 Cleaning build artifacts...")
    
    # Remove build directories
    build_dirs = ["build", "dist", "*.egg-info"]
    for pattern in build_dirs:
        run_command(["rm", "-rf"] + list(Path(".").glob(pattern)), check=False)
    
    print("✅ Build artifacts cleaned")


def run_tests():
    """Run tests before publishing."""
    print("🧪 Running tests...")
    
    try:
        run_command(["python", "-m", "pytest", "tests/", "-v"])
        print("✅ All tests passed")
    except subprocess.CalledProcessError:
        print("❌ Tests failed! Please fix issues before publishing.")
        sys.exit(1)


def check_code_quality():
    """Run code quality checks."""
    print("🔍 Running code quality checks...")
    
    # Run black
    try:
        run_command(["python", "-m", "black", "--check", "tubeharvest/"])
        print("✅ Black formatting check passed")
    except subprocess.CalledProcessError:
        print("❌ Code formatting issues found. Run: black tubeharvest/")
        sys.exit(1)
    
    # Run flake8
    try:
        run_command(["python", "-m", "flake8", "tubeharvest/"])
        print("✅ Flake8 check passed")
    except subprocess.CalledProcessError:
        print("❌ Linting issues found. Please fix them.")
        sys.exit(1)


def build_package():
    """Build the package."""
    print("📦 Building package...")
    
    run_command(["python", "-m", "build"])
    
    # Verify build artifacts
    dist_dir = Path("dist")
    if not dist_dir.exists():
        print("❌ Build failed - no dist directory created")
        sys.exit(1)
    
    wheel_files = list(dist_dir.glob("*.whl"))
    tar_files = list(dist_dir.glob("*.tar.gz"))
    
    if not wheel_files or not tar_files:
        print("❌ Build failed - missing wheel or source distribution")
        sys.exit(1)
    
    print(f"✅ Package built successfully:")
    for file in wheel_files + tar_files:
        print(f"  - {file}")


def check_package():
    """Check package with twine."""
    print("🔍 Checking package...")
    
    run_command(["python", "-m", "twine", "check", "dist/*"])
    print("✅ Package check passed")


def upload_to_test_pypi():
    """Upload to Test PyPI."""
    print("🚀 Uploading to Test PyPI...")
    
    run_command([
        "python", "-m", "twine", "upload",
        "--repository", "testpypi",
        "dist/*"
    ])
    
    print("✅ Uploaded to Test PyPI successfully!")
    print("🔗 Check your package at: https://test.pypi.org/project/tubeharvest/")
    print("📦 Test installation with:")
    print("   pip install --index-url https://test.pypi.org/simple/ tubeharvest")


def upload_to_pypi():
    """Upload to production PyPI."""
    print("🚀 Uploading to PyPI...")
    
    # Final confirmation
    response = input("Are you sure you want to publish to production PyPI? (yes/no): ")
    if response.lower() != "yes":
        print("❌ Upload cancelled")
        sys.exit(1)
    
    run_command(["python", "-m", "twine", "upload", "dist/*"])
    
    print("🎉 Successfully uploaded to PyPI!")
    print("🔗 Check your package at: https://pypi.org/project/tubeharvest/")
    print("📦 Install with: pip install tubeharvest")


def verify_installation(test_pypi: bool = False):
    """Verify the package can be installed."""
    print("🔍 Verifying installation...")
    
    # Create a temporary virtual environment
    run_command(["python", "-m", "venv", "/tmp/tubeharvest_test_env"])
    
    # Install the package
    if test_pypi:
        install_cmd = [
            "/tmp/tubeharvest_test_env/bin/pip", "install",
            "--index-url", "https://test.pypi.org/simple/",
            "--extra-index-url", "https://pypi.org/simple/",
            "tubeharvest"
        ]
    else:
        install_cmd = ["/tmp/tubeharvest_test_env/bin/pip", "install", "tubeharvest"]
    
    try:
        run_command(install_cmd)
        
        # Test basic import
        test_cmd = [
            "/tmp/tubeharvest_test_env/bin/python", "-c",
            "import tubeharvest; print('✅ Import successful')"
        ]
        run_command(test_cmd)
        
        # Test CLI command
        help_cmd = ["/tmp/tubeharvest_test_env/bin/tubeharvest", "--help"]
        run_command(help_cmd)
        
        print("✅ Installation verification successful!")
        
    except subprocess.CalledProcessError:
        print("❌ Installation verification failed!")
        sys.exit(1)
    finally:
        # Clean up
        run_command(["rm", "-rf", "/tmp/tubeharvest_test_env"], check=False)


def main():
    """Main function."""
    parser = argparse.ArgumentParser(description="Publish TubeHarvest to PyPI")
    parser.add_argument(
        "--test", action="store_true",
        help="Publish to Test PyPI"
    )
    parser.add_argument(
        "--prod", action="store_true",
        help="Publish to production PyPI"
    )
    parser.add_argument(
        "--skip-tests", action="store_true",
        help="Skip running tests"
    )
    parser.add_argument(
        "--skip-checks", action="store_true",
        help="Skip code quality checks"
    )
    parser.add_argument(
        "--verify-only", action="store_true",
        help="Only verify installation from PyPI"
    )
    
    args = parser.parse_args()
    
    if not (args.test or args.prod or args.verify_only):
        parser.print_help()
        sys.exit(1)
    
    # Change to project root
    project_root = Path(__file__).parent.parent
    sys.path.insert(0, str(project_root))
    
    print("🎯 TubeHarvest PyPI Publishing Script")
    print("=" * 40)
    
    if args.verify_only:
        verify_installation(test_pypi=args.test)
        return
    
    # Pre-publishing checks
    if not args.skip_tests:
        run_tests()
    
    if not args.skip_checks:
        check_code_quality()
    
    # Build and upload
    clean_build()
    build_package()
    check_package()
    
    if args.test:
        upload_to_test_pypi()
        verify_installation(test_pypi=True)
    elif args.prod:
        upload_to_pypi()
        verify_installation(test_pypi=False)
    
    print("\n🎉 Publishing completed successfully!")


if __name__ == "__main__":
    main() 