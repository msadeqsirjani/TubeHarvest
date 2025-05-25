#!/usr/bin/env python3
"""
TubeHarvest - Main entry point for the package.

This allows running TubeHarvest with: python -m tubeharvest
"""

import sys
from .cli.main import main

if __name__ == "__main__":
    sys.exit(main())
