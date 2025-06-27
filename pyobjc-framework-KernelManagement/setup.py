"""
Wrappers for the "KernelManagement" framework on macOS.

These wrappers don't include documentation, please check Apple's documentation
for information on how to use this framework and PyObjC's documentation
for general tips and tricks regarding the translation between Python
and (Objective-)C frameworks
"""

import os
import sys

sys.path.insert(0, os.path.dirname(__file__))


from pyobjc_setup import setup  # noqa: E402

VERSION = "11.1.1"

setup(
    name="pyobjc-framework-KernelManagement",
    description="Wrappers for the framework KernelManagement on macOS",
    min_os_level="11.0",
    packages=["KernelManagement"],
    version=VERSION,
    install_requires=["pyobjc-core>=" + VERSION, "pyobjc-framework-Cocoa>=" + VERSION],
    long_description=__doc__,
)
