"""
Wrappers for the "ApplicationServices" framework on macOS 10.5 or later. Core Text is an
advanced, low-level technology for laying out text and handling fonts. It is
designed for high performance and ease of use.

These wrappers don't include documentation, please check Apple's documention
for information on how to use this framework and PyObjC's documentation
for general tips and tricks regarding the translation between Python
and (Objective-)C frameworks
"""
from pyobjc_setup import setup

VERSION = '7.0'

setup(
    name="pyobjc-framework-ApplicationServices",
    description="Wrappers for the framework ApplicationServices on macOS",
    packages=["ApplicationServices", "HIServices", "PrintCore"],
    version=VERSION,
    install_requires=[
        "pyobjc-core>=" + VERSION,
        "pyobjc-framework-Cocoa>=" + VERSION,
        "pyobjc-framework-Quartz>=" + VERSION,
    ],
    long_description=__doc__,
)
