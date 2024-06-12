"""
Wrappers for the "dispatch" library on macOS.

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
    name="pyobjc-framework-libdispatch",
    description="Wrappers for libdispatch on macOS",
    min_os_level="10.8",
    packages=["dispatch", "libdispatch"],
    ext_modules=[
        Extension(
            "dispatch._inlines",
            ["Modules/_libdispatch_inlines.m"],
            py_limited_api=True,
        ),
        Extension(
            "dispatch._dispatch",
            ["Modules/_libdispatch.m"],
            # py_limited_api=True
        ),
    ],
    version=VERSION,
    install_requires=[
        "pyobjc-core>=" + VERSION,
        "pyobjc-framework-Cocoa>=" + VERSION,
    ],
    long_description=__doc__,
)
