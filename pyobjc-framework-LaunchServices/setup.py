"""
Deprecated wrappers for the "LaunchServices" framework on macOS.

Use the "CoreServices" bindings instead.
"""

import os
import sys

sys.path.insert(0, os.path.dirname(__file__))


from pyobjc_setup import setup  # noqa: E402

VERSION = "10.3.2"

setup(
    name="pyobjc-framework-LaunchServices",
    description="Wrappers for the framework LaunchServices on macOS",
    packages=["LaunchServices"],
    version=VERSION,
    install_requires=[
        "pyobjc-core>=" + VERSION,
        "pyobjc-framework-CoreServices>=" + VERSION,
    ],
    long_description=__doc__,
)
