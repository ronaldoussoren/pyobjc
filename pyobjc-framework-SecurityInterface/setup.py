"""
Wrappers for the "SecurityInterface" framework on macOS.

These wrappers don't include documentation, please check Apple's documentation
for information on how to use this framework and PyObjC's documentation
for general tips and tricks regarding the translation between Python
and (Objective-)C frameworks
"""

from pyobjc_setup import Extension, setup

VERSION = "8.4"

setup(
    name="pyobjc-framework-SecurityInterface",
    description="Wrappers for the framework SecurityInterface on macOS",
    packages=["SecurityInterface"],
    ext_modules=[
        Extension(
            "SecurityInterface._SecurityInterface",
            ["Modules/_SecurityInterface.m"],
            extra_link_args=["-framework", "SecurityInterface"],
            py_limited_api=True,
        )
    ],
    version=VERSION,
    install_requires=[
        "pyobjc-core>=" + VERSION,
        "pyobjc-framework-Cocoa>=" + VERSION,
        "pyobjc-framework-Security>=" + VERSION,
    ],
    long_description=__doc__,
    options={"bdist_wheel": {"py_limited_api": "cp36"}},
)
