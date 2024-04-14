"""
Helper script that will install pyobjc-core and the framework wrappers

Usage:
    pythonX.Y install.py
"""

import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "development-support"))

import _install_tool  # noqa: E402

_install_tool.main()
