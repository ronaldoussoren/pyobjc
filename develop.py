"""
Helper script that will install pyobjc-core and the framework wrappers
in editable mode.

Usage:
    pythonX.Y develop.py ARGS...

This accepts the same commandline arguments as "python setup.py develop"
in a setuptools using project.
"""
import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname("__file__"), "development-support"))

import _install_tool  # noqa: E402

_install_tool.main("develop")
