"""
Wrappers for the "ThreadNetwork" framework on macOS.

These wrappers don't include documentation, please check Apple's documentation
for information on how to use this framework and PyObjC's documentation
for general tips and tricks regarding the translation between Python
and (Objective-)C frameworks
"""

from pyobjc_setup import setup

VERSION = "9.0"

setup(
    name="pyobjc-framework-ThreadNetwork",
    description="Wrappers for the framework ThreadNetwork on macOS",
    min_os_level="13.0",
    packages=["ThreadNetwork"],
    version=VERSION,
    install_requires=[
        "pyobjc-core>=" + VERSION,
        "pyobjc-framework-Cocoa>=" + VERSION,
    ],
    long_description=__doc__,
)
