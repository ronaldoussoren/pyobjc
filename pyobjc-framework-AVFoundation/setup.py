"""
Wrappers for the "AVFoundation" framework on macOS.

These wrappers don't include documentation, please check Apple's documentation
for information on how to use this framework and PyObjC's documentation
for general tips and tricks regarding the translation between Python
and (Objective-)C frameworks
"""

import os

import sys

sys.path.insert(0, os.path.dirname(__file__))


from pyobjc_setup import Extension, setup  # noqa: E402

VERSION = "12.0"

setup(
    name="pyobjc-framework-AVFoundation",
    description="Wrappers for the framework AVFoundation on macOS",
    min_os_level="10.7",
    packages=["AVFoundation", "AVFAudio"],
    ext_modules=[
        Extension(
            "AVFAudio._inlines",
            ["Modules/_AVFAudio_inlines.m"],
            extra_link_args=["-framework", "AVFAudio"],
        ),
        Extension(
            "AVFoundation._inlines",
            ["Modules/_AVFoundation_inlines.m"],
            extra_link_args=["-framework", "AVFoundation"],
        ),
        Extension(
            "AVFoundation._AVFoundation",
            ["Modules/_AVFoundation.m"],
            extra_link_args=["-framework", "AVFoundation"],
            depends=[
                os.path.join("Modules", fn)
                for fn in os.listdir("Modules")
                if fn.startswith("_AVFoundation")
            ],
        ),
    ],
    version=VERSION,
    install_requires=[
        "pyobjc-core>=" + VERSION,
        "pyobjc-framework-CoreMedia>=" + VERSION,
        "pyobjc-framework-CoreAudio>=" + VERSION,
        "pyobjc-framework-Cocoa>=" + VERSION,
        "pyobjc-framework-Quartz>=" + VERSION,
    ],
    long_description=__doc__,
)
