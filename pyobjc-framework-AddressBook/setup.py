"""
Wrappers for the "AddressBook" framework on macOS. The Address Book is
a centralized database for contact and other information for people. Applications
that make use of the AddressBook framework all use the same database.

These wrappers don't include documentation, please check Apple's documentation
for information on how to use this framework and PyObjC's documentation
for general tips and tricks regarding the translation between Python
and (Objective-)C frameworks
"""

import os
import sys

sys.path.insert(0, os.path.dirname(__file__))


from pyobjc_setup import Extension, setup  # noqa: E402

VERSION = "12.0a0"

setup(
    name="pyobjc-framework-AddressBook",
    description="Wrappers for the framework AddressBook on macOS",
    packages=["AddressBook"],
    ext_modules=[
        Extension(
            "AddressBook._AddressBook",
            ["Modules/_AddressBook.m"],
            extra_link_args=["-framework", "AddressBook"],
            depends=[
                os.path.join("Modules", fn)
                for fn in os.listdir("Modules")
                if fn.startswith("_AddressBook")
            ],
        )
    ],
    version=VERSION,
    install_requires=["pyobjc-core>=" + VERSION, "pyobjc-framework-Cocoa>=" + VERSION],
    long_description=__doc__,
)
