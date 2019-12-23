"""
Wrappers for the "CoreMedia" framework on macOS.

These wrappers don't include documentation, please check Apple's documention
for information on how to use this framework and PyObjC's documentation
for general tips and tricks regarding the translation between Python
and (Objective-)C frameworks
"""

from pyobjc_setup import setup, Extension

VERSION = "6.2b1"

setup(
    name="pyobjc-framework-CoreMedia",
    description="Wrappers for the framework CoreMedia on macOS",
    min_os_level="10.7",
    packages=["CoreMedia"],
    ext_modules=[
        Extension(
            "CoreMedia._CoreMedia",
            ["Modules/_CoreMedia.m"],
            extra_link_args=["-framework", "CoreMedia"],
            py_limited_api=True,
        )
    ],
    version=VERSION,
    install_requires=["pyobjc-core>=" + VERSION, "pyobjc-framework-Cocoa>=" + VERSION],
    long_description=__doc__,
    options=dict(bdist_wheel=dict(py_limited_api="cp36")),
)
