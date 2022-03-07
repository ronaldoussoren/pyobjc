"""
Deprecated wrappers for the "LaunchServices" framework on macOS.

Use the "CoreServices" bindings instead.
"""
from pyobjc_setup import setup

VERSION = "8.4"

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
