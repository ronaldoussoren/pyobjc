"""
Wrappers for the "CoreText" framework on macOS 10.5 or later. Core Text is an
advanced, low-level technology for laying out text and handling fonts. It is
designed for high performance and ease of use.

These wrappers don't include documentation, please check Apple's documentation
for information on how to use this framework and PyObjC's documentation
for general tips and tricks regarding the translation between Python
and (Objective-)C frameworks
"""

import os
import sys

sys.path.insert(0, os.path.dirname(__file__))


from pyobjc_setup import Extension, setup  # noqa: E402

VERSION = "12.0a0"

setup(
    name="pyobjc-framework-CoreText",
    description="Wrappers for the framework CoreText on macOS",
    min_os_level="10.5",
    packages=["CoreText"],
    ext_modules=[
        Extension(
            "CoreText._manual",
            ["Modules/_manual.m"],
            extra_link_args=["-framework", "CoreServices"],
        )
    ],
    version=VERSION,
    install_requires=[
        "pyobjc-core>=" + VERSION,
        "pyobjc-framework-Cocoa>=" + VERSION,
        "pyobjc-framework-Quartz>=" + VERSION,
    ],
    long_description=__doc__,
)
