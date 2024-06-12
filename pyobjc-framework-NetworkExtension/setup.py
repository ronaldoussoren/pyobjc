"""
Wrappers for the "NetworkExtension" framework on macOS.

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
    name="pyobjc-framework-NetworkExtension",
    description="Wrappers for the framework NetworkExtension on macOS",
    min_os_level="10.11",
    packages=["NetworkExtension"],
    ext_modules=[
        Extension(
            "NetworkExtension._NetworkExtension",
            ["Modules/_NetworkExtension.m"],
            extra_link_args=["-framework", "NetworkExtension"],
            py_limited_api=True,
            depends=[
                os.path.join("Modules", fn)
                for fn in os.listdir("Modules")
                if fn.startswith("_NetworkExtension")
            ],
        )
    ],
    version=VERSION,
    install_requires=["pyobjc-core>=" + VERSION, "pyobjc-framework-Cocoa>=" + VERSION],
    long_description=__doc__,
    options={"bdist_wheel": {"py_limited_api": "cp36"}},
)
