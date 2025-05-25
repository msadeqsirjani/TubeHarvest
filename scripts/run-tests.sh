#!/bin/bash
# Test runner script for TubeHarvest

set -e

echo "🧪 Running TubeHarvest test suite..."

# Activate virtual environment if it exists
if [ -d ".venv" ]; then
    source .venv/bin/activate
fi

# Run tests with coverage
echo "📊 Running tests with coverage..."
pytest tests/ \
    --cov=tubeharvest \
    --cov-report=html \
    --cov-report=term-missing \
    --cov-report=xml \
    -v

# Run type checking
echo "🔍 Running type checks..."
mypy tubeharvest/

# Run linting
echo "🎨 Running code formatting checks..."
black --check tubeharvest/
isort --check-only tubeharvest/

# Run flake8
echo "📝 Running linting..."
flake8 tubeharvest/

# Run security checks
echo "🔒 Running security checks..."
bandit -r tubeharvest/

echo "✅ All tests and checks passed!" 