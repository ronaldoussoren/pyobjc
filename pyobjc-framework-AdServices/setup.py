"""
Wrappers for the "AdServices" framework on macOS 11.1 or later.

These wrappers don't include documentation, please check Apple's documentation
for information on how to use this framework and PyObjC's documentation
for general tips and tricks regarding the translation between Python
and (Objective-)C frameworks
"""

from pyobjc_setup import setup

VERSION = "8.4"

setup(
    name="pyobjc-framework-AdServices",
    description="Wrappers for the framework AdServices on macOS",
    min_os_level="11.0",
    packages=["AdServices"],
    version=VERSION,
    install_requires=["pyobjc-core>=" + VERSION, "pyobjc-framework-Cocoa>=" + VERSION],
    long_description=__doc__,
)
