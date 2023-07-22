"""
Wrappers for the "MediaExtension" framework on macOS.

These wrappers don't include documentation, please check Apple's documentation
for information on how to use this framework and PyObjC's documentation
for general tips and tricks regarding the translation between Python
and (Objective-)C frameworks
"""
import os
import sys

sys.path.insert(0, os.path.dirname(__file__))


from pyobjc_setup import setup, Extension  # noqa: E402

VERSION = "10.0a0"

setup(
    name="pyobjc-framework-MediaExtension",
    description="Wrappers for the framework MediaExtension on macOS",
    min_os_level="14.0",
    packages=["MediaExtension"],
    ext_modules=[
        Extension(
            "MediaExtension._MediaExtension",
            ["Modules/_MediaExtension.m"],
            extra_link_args=["-framework", "MediaExtension"],
            py_limited_api=True,
            depends=[
                os.path.join("Modules", fn)
                for fn in os.listdir("Modules")
                if fn.startswith("_MediaExtension")
            ],
        ),
    ],
    version=VERSION,
    install_requires=[
        "pyobjc-core>=" + VERSION,
        "pyobjc-framework-Cocoa>=" + VERSION,
        "pyobjc-framework-CoreMedia>=" + VERSION,
        "pyobjc-framework-AVFoundation>=" + VERSION,
        "pyobjc-framework-VideoToolbox>=" + VERSION,
        "pyobjc-framework-Quartz>=" + VERSION,
    ],
    long_description=__doc__,
    options={"bdist_wheel": {"py_limited_api": "cp36"}},
)
