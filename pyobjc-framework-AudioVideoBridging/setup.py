"""
Wrappers for the "AudioVideoBriding" framework on macOS.

These wrappers don't include documentation, please check Apple's documention
for information on how to use this framework and PyObjC's documentation
for general tips and tricks regarding the translation between Python
and (Objective-)C frameworks
"""
from pyobjc_setup import setup

VERSION = "8.0b1"

setup(
    name="pyobjc-framework-AudioVideoBriding",
    description="Wrappers for the framework AudioVideoBriding on macOS",
    min_os_level="10.8",
    packages=["AudioVideoBriding"],
    version=VERSION,
    install_requires=[
        "pyobjc-core>=" + VERSION,
        "pyobjc-framework-Cocoa>=" + VERSION,
    ],
    long_description=__doc__,
)
