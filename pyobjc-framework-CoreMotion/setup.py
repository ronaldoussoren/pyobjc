"""
Wrappers for the "CoreMotion" framework on macOS.

These wrappers don't include documentation, please check Apple's documentation
for information on how to use this framework and PyObjC's documentation
for general tips and tricks regarding the translation between Python
and (Objective-)C frameworks
"""

import os
import sys

sys.path.insert(0, os.path.dirname(__file__))


from pyobjc_setup import setup, Extension  # noqa: E402

VERSION = "10.3.2"

setup(
    name="pyobjc-framework-CoreMotion",
    description="Wrappers for the framework CoreMotion on macOS",
    min_os_level="10.15",
    packages=["CoreMotion"],
    ext_modules=[
        Extension(
            "CoreMotion._CoreMotion",
            ["Modules/_CoreMotion.m"],
            extra_link_args=["-framework", "CoreMotion"],
            py_limited_api=True,
            depends=[
                os.path.join("Modules", fn)
                for fn in os.listdir("Modules")
                if fn.startswith("_CoreMotion")
            ],
        )
    ],
    version=VERSION,
    install_requires=["pyobjc-core>=" + VERSION, "pyobjc-framework-Cocoa>=" + VERSION],
    long_description=__doc__,
)
