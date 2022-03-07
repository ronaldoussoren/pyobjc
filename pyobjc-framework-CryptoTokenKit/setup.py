"""
Wrappers for the "CryptoTokenKit" framework on macOS.

These wrappers don't include documentation, please check Apple's documentation
for information on how to use this framework and PyObjC's documentation
for general tips and tricks regarding the translation between Python
and (Objective-)C frameworks
"""

import os

from pyobjc_setup import Extension, setup

VERSION = "8.4"

setup(
    name="pyobjc-framework-CryptoTokenKit",
    description="Wrappers for the framework CryptoTokenKit on macOS",
    min_os_level="10.10",
    packages=["CryptoTokenKit"],
    ext_modules=[
        Extension(
            "CryptoTokenKit._CryptoTokenKit",
            ["Modules/_CryptoTokenKit.m"],
            extra_link_args=["-framework", "CryptoTokenKit"],
            py_limited_api=True,
            depends=[
                os.path.join("Modules", fn)
                for fn in os.listdir("Modules")
                if fn.startswith("_CryptoTokenKit")
            ],
        )
    ],
    version=VERSION,
    install_requires=["pyobjc-core>=" + VERSION, "pyobjc-framework-Cocoa>=" + VERSION],
    long_description=__doc__,
    options={"bdist_wheel": {"py_limited_api": "cp36"}},
)
