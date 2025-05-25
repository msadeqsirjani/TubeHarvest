#!/bin/bash
# Development installation script for TubeHarvest

set -e

echo "🚀 Setting up TubeHarvest development environment..."

# Create virtual environment if it doesn't exist
if [ ! -d ".venv" ]; then
    echo "📦 Creating virtual environment..."
    python -m venv .venv
fi

# Activate virtual environment
echo "⚡ Activating virtual environment..."
source .venv/bin/activate

# Upgrade pip
echo "📈 Upgrading pip..."
pip install --upgrade pip

# Install development dependencies
echo "📚 Installing development dependencies..."
pip install -r requirements/dev.txt

# Install package in editable mode
echo "🔧 Installing TubeHarvest in editable mode..."
pip install -e .

# Install pre-commit hooks
echo "🎣 Installing pre-commit hooks..."
pre-commit install

echo "✅ Development environment setup complete!"
echo ""
echo "🎯 Quick commands:"
echo "  • Run tests: pytest"
echo "  • Run linting: black src/ && flake8 src/"
echo "  • Run type check: mypy src/"
echo "  • Run TubeHarvest: python -m tubeharvest"
echo "  • Run GUI: ./scripts/tubeharvest-gui" 