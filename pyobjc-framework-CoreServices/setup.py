"""
Wrappers for the "CoreServices" framework on macOS.

These wrappers don't include documentation, please check Apple's documentation
for information on how to use this framework and PyObjC's documentation
for general tips and tricks regarding the translation between Python
and (Objective-)C frameworks
"""

import os
import sys

sys.path.insert(0, os.path.dirname(__file__))


from pyobjc_setup import Extension, setup  # noqa: E402

VERSION = '12.0a0'

setup(
    name="pyobjc-framework-CoreServices",
    description="Wrappers for the framework CoreServices on macOS",
    packages=[
        "CoreServices",
        "CoreServices.CarbonCore",
        "CoreServices.LaunchServices",
        "CoreServices.SearchKit",
        "CoreServices.DictionaryServices",
        "CoreServices.Metadata",
    ],
    ext_modules=[
        Extension(
            "CoreServices._inlines",
            ["Modules/_CoreServices_inlines.m"],
            extra_link_args=["-framework", "CoreServices"],
        )
    ],
    version=VERSION,
    install_requires=[
        "pyobjc-core>=" + VERSION,
        "pyobjc-framework-FSEvents>=" + VERSION,
        "pyobjc-framework-Cocoa>=" + VERSION,
    ],
    long_description=__doc__,
)
