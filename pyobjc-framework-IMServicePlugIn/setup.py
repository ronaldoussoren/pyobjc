"""
Wrappers for the "IMServicePlugIn" framework on macOS.

These wrappers don't include documentation, please check Apple's documention
for information on how to use this framework and PyObjC's documentation
for general tips and tricks regarding the translation between Python
and (Objective-)C frameworks
"""

import os

from pyobjc_setup import Extension, setup

VERSION = '7.0'

setup(
    name="pyobjc-framework-IMServicePlugIn",
    description="Wrappers for the framework IMServicePlugIn on macOS",
    min_os_level="10.7",
    packages=["IMServicePlugIn"],
    ext_modules=[
        Extension(
            "IMServicePlugIn._IMServicePlugIn",
            ["Modules/_IMServicePlugIn.m"],
            extra_link_args=["-framework", "GameKit"],
            py_limited_api=True,
            depends=[
                os.path.join("Modules", fn)
                for fn in os.listdir("Modules")
                if fn.startswith("_IMServicePlugIn")
            ],
        )
    ],
    version=VERSION,
    install_requires=["pyobjc-core>=" + VERSION, "pyobjc-framework-Cocoa>=" + VERSION],
    long_description=__doc__,
    options={"bdist_wheel": {"py_limited_api": "cp36"}},
)
