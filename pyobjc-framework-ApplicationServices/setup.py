"""
Wrappers for the "ApplicationServices" framework on macOS 10.5 or later. Core Text is an
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


from pyobjc_setup import setup, Extension  # noqa: E402

VERSION = "10.3.2"

setup(
    name="pyobjc-framework-ApplicationServices",
    description="Wrappers for the framework ApplicationServices on macOS",
    packages=["ApplicationServices", "HIServices", "PrintCore"],
    ext_modules=[
        Extension(
            "HIServices._HIServices",
            ["Modules/_HIServices.m"],
            extra_link_args=["-framework", "ApplicationServices"],
            py_limited_api=True,
            depends=[
                os.path.join("Modules", fn)
                for fn in os.listdir("Modules")
                if fn.startswith("_HIServices")
            ],
        ),
        Extension(
            "PrintCore._PrintCore",
            ["Modules/_PrintCore.m"],
            extra_link_args=["-framework", "ApplicationServices"],
            py_limited_api=True,
            depends=[
                os.path.join("Modules", fn)
                for fn in os.listdir("Modules")
                if fn.startswith("_PrintCore")
            ],
        ),
    ],
    version=VERSION,
    install_requires=[
        "pyobjc-core>=" + VERSION,
        "pyobjc-framework-Cocoa>=" + VERSION,
        "pyobjc-framework-Quartz>=" + VERSION,
        "pyobjc-framework-CoreText>=" + VERSION,
    ],
    long_description=__doc__,
)
