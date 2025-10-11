"""
Wrappers for the "MapKit" framework on macOS.

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
    name="pyobjc-framework-MapKit",
    description="Wrappers for the framework MapKit on macOS",
    min_os_level="10.9",
    packages=["MapKit"],
    ext_modules=[
        Extension(
            "MapKit._MapKit",
            ["Modules/_MapKit.m"],
            extra_link_args=["-framework", "MapKit"],
            depends=[
                os.path.join("Modules", fn)
                for fn in os.listdir("Modules")
                if fn.startswith("_MapKit")
            ],
        ),
        Extension("MapKit._inlines", ["Modules/_MapKit_inlines.m"]),
    ],
    version=VERSION,
    install_requires=[
        "pyobjc-core>=" + VERSION,
        "pyobjc-framework-Cocoa>=" + VERSION,
        "pyobjc-framework-CoreLocation>=" + VERSION,
        "pyobjc-framework-Quartz>=" + VERSION,
    ],
    long_description=__doc__,
)
