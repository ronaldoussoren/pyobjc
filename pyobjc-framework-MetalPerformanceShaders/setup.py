"""
Wrappers for the "MetalPerformanceShaders" framework on macOS.

These wrappers don't include documentation, please check Apple's documention
for information on how to use this framework and PyObjC's documentation
for general tips and tricks regarding the translation between Python
and (Objective-)C frameworks
"""

import os

from pyobjc_setup import Extension, setup

VERSION = '7.0'

setup(
    name="pyobjc-framework-MetalPerformanceShaders",
    description="Wrappers for the framework MetalPerformanceShaders on macOS",
    min_os_level="10.13",
    packages=["MetalPerformanceShaders"],
    ext_modules=[
        Extension(
            "MetalPerformanceShaders._inlines",
            ["Modules/_MetalPerformanceShaders_inlines.m"],
            extra_link_args=["-framework", "MetalPerformanceShaders"],
            py_limited_api=True,
        ),
        Extension(
            "MetalPerformanceShaders._MetalPerformanceShaders",
            ["Modules/_MetalPerformanceShaders.m"],
            extra_link_args=["-framework", "MetalPerformanceShaders"],
            py_limited_api=True,
            depends=[
                os.path.join("Modules", fn)
                for fn in os.listdir("Modules")
                if fn.startswith("_MetalPerformanceShaders")
            ],
        ),
    ],
    version=VERSION,
    install_requires=["pyobjc-core>=" + VERSION, "pyobjc-framework-Metal>=" + VERSION],
    long_description=__doc__,
    options={"bdist_wheel": {"py_limited_api": "cp36"}},
)
