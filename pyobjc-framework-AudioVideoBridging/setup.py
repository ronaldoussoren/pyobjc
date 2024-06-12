"""
Wrappers for the "AudioVideoBridging" framework on macOS.

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
    name="pyobjc-framework-AudioVideoBridging",
    description="Wrappers for the framework AudioVideoBridging on macOS",
    min_os_level="10.8",
    packages=["AudioVideoBridging"],
    ext_modules=[
        Extension(
            "AudioVideoBridging._AudioVideoBridging",
            ["Modules/_AudioVideoBridging.m"],
            extra_link_args=["-framework", "AudioVideoBridging"],
            py_limited_api=True,
            depends=[
                os.path.join("Modules", fn)
                for fn in os.listdir("Modules")
                if fn.startswith("_AudioVideoBridging")
            ],
        ),
    ],
    version=VERSION,
    install_requires=[
        "pyobjc-core>=" + VERSION,
        "pyobjc-framework-Cocoa>=" + VERSION,
    ],
    long_description=__doc__,
)
