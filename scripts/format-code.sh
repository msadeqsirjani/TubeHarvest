#!/bin/bash
# Code formatting script for TubeHarvest

set -e

echo "🎨 Formatting TubeHarvest code..."

# Activate virtual environment if it exists
if [ -d ".venv" ]; then
    source .venv/bin/activate
fi

# Format code with black
echo "⚫ Running black formatter..."
black tubeharvest/ tests/ examples/

# Sort imports with isort
echo "📚 Sorting imports with isort..."
isort tubeharvest/ tests/ examples/

# Remove unused imports (if autopep8 is available)
if command -v autopep8 &> /dev/null; then
    echo "🧹 Cleaning up with autopep8..."
    autopep8 --in-place --recursive tubeharvest/ tests/ examples/
fi

echo "✅ Code formatting complete!" 