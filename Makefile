.PHONY: help install install-dev test test-cov lint format type-check security-check clean build upload-test upload docs sync-wiki validate-docs

# Default target
help:
	@echo "TubeHarvest Development Commands"
	@echo "================================"
	@echo ""
	@echo "Setup:"
	@echo "  install      Install package and basic dependencies"
	@echo "  install-dev  Install package with development dependencies"
	@echo ""
	@echo "Testing:"
	@echo "  test         Run tests"
	@echo "  test-cov     Run tests with coverage report"
	@echo ""
	@echo "Code Quality:"
	@echo "  lint         Run linting checks"
	@echo "  format       Format code with black and isort"
	@echo "  type-check   Run type checking with mypy"
	@echo "  security-check Run security checks with bandit"
	@echo ""
	@echo "Build & Deploy:"
	@echo "  clean        Clean build artifacts"
	@echo "  build        Build package distribution"
	@echo "  upload-test  Upload to test PyPI"
	@echo "  upload       Upload to PyPI"
	@echo ""
	@echo "Documentation:"
	@echo "  docs         Check documentation status"
	@echo "  sync-wiki    Sync docs with GitHub Wiki"
	@echo "  validate-docs Validate documentation files"

# Installation
install:
	pip install -e .

install-dev:
	./scripts/install-dev.sh

# Testing
test:
	pytest tests/ -v

test-cov:
	pytest tests/ --cov=tubeharvest --cov-report=html --cov-report=term-missing -v

# Code quality
lint:
	flake8 tubeharvest/ tests/
	black --check tubeharvest/ tests/
	isort --check-only tubeharvest/ tests/

format:
	./scripts/format-code.sh

type-check:
	mypy tubeharvest/

security-check:
	bandit -r tubeharvest/
	safety check

# Build and deploy
clean:
	rm -rf build/
	rm -rf dist/
	rm -rf *.egg-info/
	find . -type d -name __pycache__ -exec rm -rf {} +
	find . -type f -name "*.pyc" -delete

build: clean
	python -m build

upload-test: build
	python -m twine upload --repository testpypi dist/*

upload: build
	python -m twine upload dist/*

# Documentation
docs:
	@echo "📚 Building documentation..."
	@echo "Documentation files are ready in docs/ directory"
	@echo "To sync with GitHub Wiki, run: make sync-wiki"

sync-wiki:
	@echo "🌐 Syncing documentation with GitHub Wiki..."
	./scripts/sync-wiki.sh

validate-docs:
	@echo "🔍 Validating documentation..."
	@echo "Checking markdown files..."
	@for file in docs/*.md; do \
		echo "Checking $$file..."; \
		if ! grep -q "^# " "$$file"; then \
			echo "⚠️  Warning: $$file missing main heading"; \
		fi; \
	done
	@echo "✅ Documentation validation complete" 