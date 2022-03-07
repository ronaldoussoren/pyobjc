"""
Wrappers for the "ContactsUI" framework on macOS 10.11.

These wrappers don't include documentation, please check Apple's documentation
for information on how to use this framework and PyObjC's documentation
for general tips and tricks regarding the translation between Python
and (Objective-)C frameworks
"""

import os

from pyobjc_setup import Extension, setup

VERSION = "8.4"

setup(
    name="pyobjc-framework-ContactsUI",
    description="Wrappers for the framework ContactsUI on macOS",
    min_os_level="10.11",
    packages=["ContactsUI"],
    ext_modules=[
        Extension(
            "ContactsUI._ContactsUI",
            ["Modules/_ContactsUI.m"],
            extra_link_args=["-framework", "ContactsUI"],
            py_limited_api=True,
            depends=[
                os.path.join("Modules", fn)
                for fn in os.listdir("Modules")
                if fn.startswith("_ContactsUI")
            ],
        )
    ],
    version=VERSION,
    install_requires=[
        "pyobjc-core>=" + VERSION,
        "pyobjc-framework-Cocoa>=" + VERSION,
        "pyobjc-framework-Contacts>=" + VERSION,
    ],
    long_description=__doc__,
    options={"bdist_wheel": {"py_limited_api": "cp36"}},
)
