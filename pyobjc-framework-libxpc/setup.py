"""
Wrappers for the "xpc" library on macOS.

These wrappers don't include documentation, please check Apple's documentation
for information on how to use this framework and PyObjC's documentation
for general tips and tricks regarding the translation between Python
and (Objective-)C frameworks
"""

from pyobjc_setup import Extension, setup

VERSION = "9.1"

setup(
    name="pyobjc-framework-libxpc",
    description="Wrappers for xpc on macOS",
    min_os_level="10.8",
    packages=["xpc"],
    ext_modules=[
        #        Extension(
        #            "xpc._inlines",
        #            ["Modules/_libxpc_inlines.m"],
        #            py_limited_api=True,
        #        ),
        Extension(
            "xpc._xpc",
            ["Modules/_xpc.m"],
            # py_limited_api=True
        ),
    ],
    version=VERSION,
    install_requires=["pyobjc-core>=" + VERSION],
    long_description=__doc__,
)
