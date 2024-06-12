"""
Wrappers for the "CoreMedia" framework on macOS.

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
    name="pyobjc-framework-CoreMedia",
    description="Wrappers for the framework CoreMedia on macOS",
    min_os_level="10.7",
    packages=["CoreMedia"],
    ext_modules=[
        Extension(
            "CoreMedia._inlines",
            ["Modules/_CoreMedia_inlines.m"],
            extra_link_args=["-framework", "CoreMedia"],
            py_limited_api=True,
        ),
        Extension(
            "CoreMedia._CoreMedia",
            ["Modules/_CoreMedia.m"],
            extra_link_args=["-framework", "CoreMedia"],
        ),
    ],
    version=VERSION,
    install_requires=["pyobjc-core>=" + VERSION, "pyobjc-framework-Cocoa>=" + VERSION],
    long_description=__doc__,
)
