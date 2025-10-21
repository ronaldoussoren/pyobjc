"""
Wrappers for the "PassKit" framework on macOS.

These wrappers don't include documentation, please check Apple's documentation
for information on how to use this framework and PyObjC's documentation
for general tips and tricks regarding the translation between Python
and (Objective-)C frameworks
"""

import os
import sys

sys.path.insert(0, os.path.dirname(__file__))


from pyobjc_setup import setup, Extension  # noqa: E402

VERSION = "12.1"

setup(
    name="pyobjc-framework-PassKit",
    description="Wrappers for the framework PassKit on macOS",
    min_os_level="11.0",
    packages=["PassKit"],
    ext_modules=[
        Extension(
            "PassKit._PassKit",
            ["Modules/_PassKit.m"],
            extra_link_args=["-framework", "PassKit"],
            depends=[
                os.path.join("Modules", fn)
                for fn in os.listdir("Modules")
                if fn.startswith("_PassKit")
            ],
        )
    ],
    version=VERSION,
    install_requires=["pyobjc-core>=" + VERSION, "pyobjc-framework-Cocoa>=" + VERSION],
    long_description=__doc__,
)
