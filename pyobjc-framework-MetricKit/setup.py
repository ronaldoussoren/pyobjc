"""
Wrappers for the "MetricKit" framework on macOS.

These wrappers don't include documentation, please check Apple's documentation
for information on how to use this framework and PyObjC's documentation
for general tips and tricks regarding the translation between Python
and (Objective-)C frameworks
"""
import os

from pyobjc_setup import Extension, setup

VERSION = "8.4"

setup(
    name="pyobjc-framework-MetricKit",
    description="Wrappers for the framework MetricKit on macOS",
    min_os_level="10.16",
    packages=["MetricKit"],
    ext_modules=[
        Extension(
            "MetricKit._MetricKit",
            ["Modules/_MetricKit.m"],
            extra_link_args=["-framework", "MetricKit"],
            py_limited_api=True,
            depends=[
                os.path.join("Modules", fn)
                for fn in os.listdir("Modules")
                if fn.startswith("_MetricKit")
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
