"""
Helper script that will install pyobjc-core and the framework wrappers
in editable mode.

Usage:
    pythonX.Y develop.py
"""

import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "development-support"))
print(sys.path[0])

import _install_tool  # noqa: E402

_install_tool.main("-e")
