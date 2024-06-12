"""
Wrappers for the "SyncServices" framework on macOS.

Sync Services is a framework containing all the components you need
to sync your applications and devices. If your application uses
Sync Services, user data can be synced with other applications and
devices on the same computer, or other computers over the network via
MobileMe.

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
    name="pyobjc-framework-SyncServices",
    description="Wrappers for the framework SyncServices on macOS",
    packages=["SyncServices"],
    ext_modules=[
        Extension(
            "SyncServices._SyncServices",
            ["Modules/_SyncServices.m"],
            extra_link_args=["-framework", "SyncServices"],
            py_limited_api=True,
            depends=[
                os.path.join("Modules", fn)
                for fn in os.listdir("Modules")
                if fn.startswith("_SyncServices")
            ],
        )
    ],
    version=VERSION,
    install_requires=[
        "pyobjc-core>=" + VERSION,
        "pyobjc-framework-Cocoa>=" + VERSION,
        "pyobjc-framework-CoreData>=" + VERSION,
    ],
    long_description=__doc__,
    options={"bdist_wheel": {"py_limited_api": "cp36"}},
)
