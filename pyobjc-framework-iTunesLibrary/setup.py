"""
Wrappers for the "iTunesLibrary" framework on macOS.

These wrappers don't include documentation, please check Apple's documention
for information on how to use this framework and PyObjC's documentation
for general tips and tricks regarding the translation between Python
and (Objective-)C frameworks

Note that using the library requires a signed application bundle.
"""

from pyobjc_setup import setup

VERSION = '7.0'

setup(
    name="pyobjc-framework-iTunesLibrary",
    description="Wrappers for the framework iTunesLibrary on macOS",
    min_os_level="10.6",
    packages=["iTunesLibrary"],
    version=VERSION,
    install_requires=["pyobjc-core>=" + VERSION, "pyobjc-framework-Cocoa>=" + VERSION],
    long_description=__doc__,
)
