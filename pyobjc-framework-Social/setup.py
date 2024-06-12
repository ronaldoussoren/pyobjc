"""
Wrappers for the "Social" framework on macOS 10.8 or later.

Note that this framework is only available for 64-bit code.
"""

import os
import sys

sys.path.insert(0, os.path.dirname(__file__))


from pyobjc_setup import setup  # noqa: E402

VERSION = "10.3.2"

setup(
    name="pyobjc-framework-Social",
    description="Wrappers for the framework Social on macOS",
    min_os_level="10.8",
    packages=["Social"],
    version=VERSION,
    install_requires=["pyobjc-core>=" + VERSION, "pyobjc-framework-Cocoa>=" + VERSION],
    long_description=__doc__,
)
