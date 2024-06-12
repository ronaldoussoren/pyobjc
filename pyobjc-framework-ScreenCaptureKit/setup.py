"""
Wrappers for the "ScreenCaptureKit" framework on macOS.

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
    name="pyobjc-framework-ScreenCaptureKit",
    description="Wrappers for the framework ScreenCaptureKit on macOS",
    min_os_level="12.3",
    packages=["ScreenCaptureKit"],
    ext_modules=[
        Extension(
            "ScreenCaptureKit._ScreenCaptureKit",
            ["Modules/_ScreenCaptureKit.m"],
            extra_link_args=["-framework", "ScreenCaptureKit"],
            py_limited_api=True,
            depends=[
                os.path.join("Modules", fn)
                for fn in os.listdir("Modules")
                if fn.startswith("_ScreenCaptureKit")
            ],
        ),
    ],
    version=VERSION,
    install_requires=[
        "pyobjc-core>=" + VERSION,
        "pyobjc-framework-CoreMedia>=" + VERSION,
        "pyobjc-framework-Cocoa>=" + VERSION,
    ],
    long_description=__doc__,
)
