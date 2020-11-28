"""
Wrappers for the "Virtualization" framework on macOS.

These wrappers don't include documentation, please check Apple's documention
for information on how to use this framework and PyObjC's documentation
for general tips and tricks regarding the translation between Python
and (Objective-)C frameworks
"""
import os

from pyobjc_setup import setup, Extension

VERSION = '7.0'

setup(
    name="pyobjc-framework-Virtualization",
    description="Wrappers for the framework Virtualization on macOS",
    min_os_level="10.16",
    packages=["Virtualization"],
    ext_modules=[
        Extension(
            "Virtualization._Virtualization",
            ["Modules/_Virtualization.m"],
            extra_link_args=["-framework", "Virtualization"],
            py_limited_api=True,
            depends=[
                os.path.join("Modules", fn)
                for fn in os.listdir("Modules")
                if fn.startswith("_Virtualization")
            ],
        )
    ],
    version=VERSION,
    install_requires=["pyobjc-core>=" + VERSION, "pyobjc-framework-Cocoa>=" + VERSION],
    long_description=__doc__,
    options={"bdist_wheel": {"py_limited_api": "cp36"}},
)
