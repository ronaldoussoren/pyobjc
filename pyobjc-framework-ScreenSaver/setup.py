"""
Wrappers for the "ScreenSaver" framework on macOS. This frameworks allows
you to write custom screensaver modules.

These wrappers don't include documentation, please check Apple's documentation
for information on how to use this framework and PyObjC's documentation
for general tips and tricks regarding the translation between Python
and (Objective-)C frameworks
"""

import os
import sys

sys.path.insert(0, os.path.dirname(__file__))


from pyobjc_setup import Extension, setup  # noqa: E402

VERSION = "10.3.2"

setup(
    name="pyobjc-framework-ScreenSaver",
    description="Wrappers for the framework ScreenSaver on macOS",
    packages=["ScreenSaver"],
    ext_modules=[
        Extension(
            "ScreenSaver._inlines",
            ["Modules/_ScreenSaver_inlines.m"],
            extra_link_args=["-framework", "ScreenSaver"],
            py_limited_api=True,
        )
    ],
    version=VERSION,
    install_requires=["pyobjc-core>=" + VERSION, "pyobjc-framework-Cocoa>=" + VERSION],
    long_description=__doc__,
    options={"bdist_wheel": {"py_limited_api": "cp36"}},
)
