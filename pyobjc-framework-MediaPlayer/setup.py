"""
Wrappers for the "MediaPlayer" framework on macOS.

These wrappers don't include documentation, please check Apple's documentation
for information on how to use this framework and PyObjC's documentation
for general tips and tricks regarding the translation between Python
and (Objective-)C frameworks
"""

from pyobjc_setup import setup

VERSION = "8.4"

setup(
    name="pyobjc-framework-MediaPlayer",
    description="Wrappers for the framework MediaPlayer on macOS",
    min_os_level="10.12",
    packages=["MediaPlayer"],
    version=VERSION,
    install_requires=[
        "pyobjc-core>=" + VERSION,
        "pyobjc-framework-AVFoundation>=" + VERSION,
    ],
    long_description=__doc__,
)
