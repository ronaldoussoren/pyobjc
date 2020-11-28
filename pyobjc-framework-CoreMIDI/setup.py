"""
Wrappers for the "CoreMIDI" framework on macOS.

These wrappers don't include documentation, please check Apple's documention
for information on how to use this framework and PyObjC's documentation
for general tips and tricks regarding the translation between Python
and (Objective-)C frameworks
"""

import os

from pyobjc_setup import setup, Extension

VERSION = '7.0'

setup(
    name="pyobjc-framework-CoreMIDI",
    description="Wrappers for the framework CoreMIDI on macOS",
    packages=["CoreMIDI"],
    ext_modules=[
        Extension(
            "CoreMIDI._CoreMIDI",
            ["Modules/_CoreMIDI.m"],
            extra_link_args=["-framework", "CoreMIDI"],
            py_limited_api=True,
            depends=[
                os.path.join("Modules", fn)
                for fn in os.listdir("Modules")
                if fn.startswith("_CoreMIDI")
            ],
        )
    ],
    version=VERSION,
    install_requires=["pyobjc-core>=" + VERSION, "pyobjc-framework-Cocoa>=" + VERSION],
    long_description=__doc__,
    options={"bdist_wheel": {"py_limited_api": "cp36"}},
)
