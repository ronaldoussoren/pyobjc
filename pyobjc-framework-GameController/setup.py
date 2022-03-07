"""
Wrappers for the "GameController" framework on macOS introduced in macOS 10.9.

These wrappers don't include documentation, please check Apple's documentation
for information on how to use this framework and PyObjC's documentation
for general tips and tricks regarding the translation between Python
and (Objective-)C frameworks
"""
import os

from pyobjc_setup import setup, Extension

VERSION = "8.4"

setup(
    name="pyobjc-framework-GameController",
    description="Wrappers for the framework GameController on macOS",
    packages=["GameController"],
    ext_modules=[
        Extension(
            "GameController._GameController",
            ["Modules/_GameController.m"],
            extra_link_args=["-framework", "GameController"],
            py_limited_api=True,
            depends=[
                os.path.join("Modules", fn)
                for fn in os.listdir("Modules")
                if fn.startswith("_GameController")
            ],
        )
    ],
    version=VERSION,
    install_requires=["pyobjc-core>=" + VERSION, "pyobjc-framework-Cocoa>=" + VERSION],
    long_description=__doc__,
    options={"bdist_wheel": {"py_limited_api": "cp36"}},
)
