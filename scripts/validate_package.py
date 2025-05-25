#!/usr/bin/env python3
"""
Package validation script for TubeHarvest.

This script validates that the package is properly configured for PyPI publishing.
"""

import ast
import configparser
import sys
import tomllib
from pathlib import Path
from typing import Dict, List


def validate_pyproject_toml() -> Dict[str, bool]:
    """Validate pyproject.toml configuration."""
    results = {}
    
    try:
        with open("pyproject.toml", "rb") as f:
            data = tomllib.load(f)
        
        # Check build system
        results["build_system"] = "build-system" in data
        
        # Check project metadata
        project = data.get("project", {})
        results["name"] = "name" in project
        results["version"] = "version" in project
        results["description"] = "description" in project
        results["authors"] = "authors" in project
        results["license"] = "license" in project
        results["readme"] = "readme" in project
        results["requires_python"] = "requires-python" in project
        results["dependencies"] = "dependencies" in project
        results["classifiers"] = "classifiers" in project
        results["keywords"] = "keywords" in project
        results["urls"] = "urls" in project
        results["scripts"] = "scripts" in project
        
        # Check optional dependencies
        results["optional_dependencies"] = "optional-dependencies" in project
        
        print("✅ pyproject.toml validation passed")
        
    except Exception as e:
        print(f"❌ pyproject.toml validation failed: {e}")
        results["valid"] = False
    
    return results


def validate_package_structure() -> Dict[str, bool]:
    """Validate package directory structure."""
    results = {}
    
    # Check main package directory
    results["package_dir"] = Path("tubeharvest").exists()
    results["package_init"] = Path("tubeharvest/__init__.py").exists()
    results["main_module"] = Path("tubeharvest/__main__.py").exists()
    
    # Check CLI entry point
    results["cli_module"] = Path("tubeharvest/cli").exists()
    
    # Check core modules
    results["core_module"] = Path("tubeharvest/core").exists()
    
    print("✅ Package structure validation passed")
    return results


def validate_required_files() -> Dict[str, bool]:
    """Validate required files for PyPI."""
    results = {}
    
    required_files = [
        "README.md",
        "LICENSE",
        "CHANGELOG.md",
        "pyproject.toml",
        "MANIFEST.in",
        "requirements.txt"
    ]
    
    for file in required_files:
        results[file] = Path(file).exists()
        if not results[file]:
            print(f"❌ Missing required file: {file}")
    
    print("✅ Required files validation completed")
    return results


def validate_version_consistency() -> bool:
    """Check version consistency across files."""
    try:
        # Get version from pyproject.toml
        with open("pyproject.toml", "rb") as f:
            pyproject_data = tomllib.load(f)
        
        pyproject_version = pyproject_data["project"]["version"]
        
        # Get version from __init__.py
        with open("tubeharvest/__init__.py", "r") as f:
            tree = ast.parse(f.read())
        
        init_version = None
        for node in ast.walk(tree):
            if isinstance(node, ast.Assign):
                for target in node.targets:
                    if isinstance(target, ast.Name) and target.id == "__version__":
                        init_version = ast.literal_eval(node.value)
        
        if pyproject_version == init_version:
            print(f"✅ Version consistency check passed: {pyproject_version}")
            return True
        else:
            print(f"❌ Version mismatch: pyproject.toml={pyproject_version}, __init__.py={init_version}")
            return False
            
    except Exception as e:
        print(f"❌ Version consistency check failed: {e}")
        return False


def validate_dependencies() -> bool:
    """Validate that dependencies are properly specified."""
    try:
        with open("pyproject.toml", "rb") as f:
            data = tomllib.load(f)
        
        dependencies = data["project"]["dependencies"]
        
        # Check for common required dependencies
        required_deps = ["yt-dlp", "rich", "click"]
        missing_deps = []
        
        for dep in required_deps:
            if not any(dep in d for d in dependencies):
                missing_deps.append(dep)
        
        if missing_deps:
            print(f"❌ Missing critical dependencies: {missing_deps}")
            return False
        
        print(f"✅ Dependencies validation passed ({len(dependencies)} dependencies)")
        return True
        
    except Exception as e:
        print(f"❌ Dependencies validation failed: {e}")
        return False


def validate_entry_points() -> bool:
    """Validate CLI entry points."""
    try:
        with open("pyproject.toml", "rb") as f:
            data = tomllib.load(f)
        
        scripts = data["project"]["scripts"]
        
        # Check main entry point
        if "tubeharvest" not in scripts:
            print("❌ Missing main CLI entry point 'tubeharvest'")
            return False
        
        print(f"✅ Entry points validation passed: {list(scripts.keys())}")
        return True
        
    except Exception as e:
        print(f"❌ Entry points validation failed: {e}")
        return False


def validate_manifest() -> bool:
    """Validate MANIFEST.in file."""
    try:
        with open("MANIFEST.in", "r") as f:
            content = f.read()
        
        # Check for essential includes
        essential_includes = ["README.md", "LICENSE", "CHANGELOG.md"]
        
        for include in essential_includes:
            if include not in content:
                print(f"❌ MANIFEST.in missing: {include}")
                return False
        
        print("✅ MANIFEST.in validation passed")
        return True
        
    except Exception as e:
        print(f"❌ MANIFEST.in validation failed: {e}")
        return False


def generate_report(results: Dict[str, Dict[str, bool]]) -> None:
    """Generate validation report."""
    print("\n" + "="*50)
    print("📋 PACKAGE VALIDATION REPORT")
    print("="*50)
    
    total_checks = 0
    passed_checks = 0
    
    for category, checks in results.items():
        print(f"\n📂 {category.upper()}")
        print("-" * 30)
        
        for check, status in checks.items():
            total_checks += 1
            if status:
                passed_checks += 1
                print(f"✅ {check}")
            else:
                print(f"❌ {check}")
    
    print(f"\n📊 SUMMARY")
    print("-" * 30)
    print(f"Total checks: {total_checks}")
    print(f"Passed: {passed_checks}")
    print(f"Failed: {total_checks - passed_checks}")
    print(f"Success rate: {(passed_checks/total_checks)*100:.1f}%")
    
    if passed_checks == total_checks:
        print("\n🎉 All validations passed! Ready for PyPI publishing.")
        return True
    else:
        print(f"\n⚠️  {total_checks - passed_checks} issues found. Please fix before publishing.")
        return False


def main():
    """Main validation function."""
    print("🔍 TubeHarvest Package Validation")
    print("=" * 40)
    
    # Change to project root if running from scripts/
    if Path.cwd().name == "scripts":
        import os
        os.chdir("..")
    
    results = {}
    
    # Run all validations
    print("\n🔍 Validating pyproject.toml...")
    results["pyproject"] = validate_pyproject_toml()
    
    print("\n🔍 Validating package structure...")
    results["structure"] = validate_package_structure()
    
    print("\n🔍 Validating required files...")
    results["files"] = validate_required_files()
    
    print("\n🔍 Checking version consistency...")
    results["version"] = {"consistency": validate_version_consistency()}
    
    print("\n🔍 Validating dependencies...")
    results["dependencies"] = {"valid": validate_dependencies()}
    
    print("\n🔍 Validating entry points...")
    results["entry_points"] = {"valid": validate_entry_points()}
    
    print("\n🔍 Validating MANIFEST.in...")
    results["manifest"] = {"valid": validate_manifest()}
    
    # Generate report
    success = generate_report(results)
    
    if success:
        print("\n🚀 Next steps:")
        print("1. Run tests: python -m pytest")
        print("2. Test build: python -m build")
        print("3. Test upload: python scripts/publish.py --test")
        print("4. Production upload: python scripts/publish.py --prod")
    
    sys.exit(0 if success else 1)


if __name__ == "__main__":
    main() 