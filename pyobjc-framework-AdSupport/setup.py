"""
Wrappers for the "AdSupport" framework on macOS 10.14 or later.

These wrappers don't include documentation, please check Apple's documention
for information on how to use this framework and PyObjC's documentation
for general tips and tricks regarding the translation between Python
and (Objective-)C frameworks
"""

from pyobjc_setup import setup

VERSION = '7.0'

setup(
    name="pyobjc-framework-AdSupport",
    description="Wrappers for the framework AdSupport on macOS",
    min_os_level="10.14",
    packages=["AdSupport"],
    version=VERSION,
    install_requires=["pyobjc-core>=" + VERSION, "pyobjc-framework-Cocoa>=" + VERSION],
    long_description=__doc__,
)
