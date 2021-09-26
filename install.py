"""
Helper script that will install pyobjc-core and the framework wrappers

Usage:
    pythonX.Y install.py ARGS...

This accepts the same commandline arguments as "python setup.py install"
in a setuptools using project.
"""
import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname("__file__"), "development-support"))

import _install_tool  # noqa: E402

_install_tool.main("install")
