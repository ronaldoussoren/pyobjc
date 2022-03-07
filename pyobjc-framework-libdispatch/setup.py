"""
Wrappers for the "AVFoundation" framework on macOS.

These wrappers don't include documentation, please check Apple's documentation
for information on how to use this framework and PyObjC's documentation
for general tips and tricks regarding the translation between Python
and (Objective-)C frameworks
"""

from pyobjc_setup import Extension, setup

VERSION = "8.4"

setup(
    name="pyobjc-framework-libdispatch",
    description="Wrappers for libdispatch on macOS",
    min_os_level="10.8",
    packages=["libdispatch"],
    ext_modules=[
        Extension(
            "libdispatch._inlines",
            ["Modules/_libdispatch_inlines.m"],
            py_limited_api=True,
        ),
        Extension(
            "libdispatch._libdispatch",
            ["Modules/_libdispatch.m"],
            # py_limited_api=True
        ),
    ],
    version=VERSION,
    install_requires=["pyobjc-core>=" + VERSION],
    long_description=__doc__,
)
