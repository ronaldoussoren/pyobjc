"""
Wrappers for the "MetalPerformanceShadersGraph" framework on macOS.

These wrappers don't include documentation, please check Apple's documentation
for information on how to use this framework and PyObjC's documentation
for general tips and tricks regarding the translation between Python
and (Objective-)C frameworks
"""
# import os
#
# from pyobjc_setup import setup, Extension
from pyobjc_setup import setup

VERSION = "8.4"

setup(
    name="pyobjc-framework-MetalPerformanceShadersGraph",
    description="Wrappers for the framework MetalPerformanceShadersGraph on macOS",
    min_os_level="10.16",
    packages=["MetalPerformanceShadersGraph"],
    # ext_modules=[
    #    Extension(
    #        "MetalPerformanceShadersGraph._MetalPerformanceShadersGraph",
    #        ["Modules/_MetalPerformanceShadersGraph.m"],
    #        extra_link_args=["-framework", "MetalPerformanceShadersGraph"],
    #        py_limited_api=True,
    #        depends=[
    #            os.path.join("Modules", fn)
    #            for fn in os.listdir("Modules")
    #            if fn.startswith("_MetalPerformanceShadersGraph")
    #        ],
    #    )
    # ],
    version=VERSION,
    install_requires=[
        "pyobjc-core>=" + VERSION,
        "pyobjc-framework-MetalPerformanceShaders>=" + VERSION,
    ],
    long_description=__doc__,
    # options={"bdist_wheel": {"py_limited_api": "cp36"}},
)
