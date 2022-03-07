"""
Wrappers for the "Accessibility" framework on macOS.

These wrappers don't include documentation, please check Apple's documentation
for information on how to use this framework and PyObjC's documentation
for general tips and tricks regarding the translation between Python
and (Objective-)C frameworks
"""
import os
from pyobjc_setup import setup, Extension

VERSION = "8.4"

setup(
    name="pyobjc-framework-Accessibility",
    description="Wrappers for the framework Accessibility on macOS",
    min_os_level="10.16",
    packages=["Accessibility"],
    ext_modules=[
        Extension(
            "Accessibility._Accessibility",
            ["Modules/_Accessibility.m"],
            extra_link_args=["-framework", "Accessibility"],
            py_limited_api=True,
            depends=[
                os.path.join("Modules", fn)
                for fn in os.listdir("Modules")
                if fn.startswith("_Accessibility")
            ],
        )
    ],
    version=VERSION,
    install_requires=[
        "pyobjc-core>=" + VERSION,
        "pyobjc-framework-Cocoa>=" + VERSION,
        "pyobjc-framework-Quartz>=" + VERSION,
    ],
    long_description=__doc__,
    options={"bdist_wheel": {"py_limited_api": "cp36"}},
)
