"""
Wrappers for the "AuthenticationServices" framework on macOS.

These wrappers don't include documentation, please check Apple's documention
for information on how to use this framework and PyObjC's documentation
for general tips and tricks regarding the translation between Python
and (Objective-)C frameworks
"""

from pyobjc_setup import setup, Extension
import os

VERSION = "6.2b1"

setup(
    name="pyobjc-framework-AuthenticationServices",
    description="Wrappers for the framework AuthenticationServices on macOS",
    min_os_level="10.15",
    packages=["AuthenticationServices"],
    ext_modules=[
        Extension(
            "AuthenticationServices._AuthenticationServices",
            ["Modules/_AuthenticationServices.m"],
            extra_link_args=["-framework", "AuthenticationServices"],
            py_limited_api=True,
            depends=[
                os.path.join("Modules", fn)
                for fn in os.listdir("Modules")
                if fn.startswith("_AuthenticationServices")
            ],
        )
    ],
    version=VERSION,
    install_requires=["pyobjc-core>=" + VERSION, "pyobjc-framework-Cocoa>=" + VERSION],
    long_description=__doc__,
    options=dict(bdist_wheel=dict(py_limited_api="cp36")),
)
