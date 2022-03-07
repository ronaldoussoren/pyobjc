"""
Wrappers for the "IntentsUI" framework on macOS.

These wrappers don't include documentation, please check Apple's documentation
for information on how to use this framework and PyObjC's documentation
for general tips and tricks regarding the translation between Python
and (Objective-)C frameworks
"""
import os
from pyobjc_setup import setup, Extension

VERSION = "8.4"

setup(
    name="pyobjc-framework-IntentsUI",
    description="Wrappers for the framework Intents on macOS",
    min_os_level="12.0",
    packages=["IntentsUI"],
    ext_modules=[
        Extension(
            "IntentsUI._IntentsUI",
            ["Modules/_IntentsUI.m"],
            extra_link_args=["-framework", "IntentsUI"],
            py_limited_api=True,
            depends=[
                os.path.join("Modules", fn)
                for fn in os.listdir("Modules")
                if fn.startswith("_IntentsUI")
            ],
        )
    ],
    version=VERSION,
    install_requires=[
        "pyobjc-core>=" + VERSION,
        "pyobjc-framework-Intents>=" + VERSION,
    ],
    long_description=__doc__,
)
