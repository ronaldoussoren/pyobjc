"""
Wrappers for the "MediaToolbox" framework on macOS.

These wrappers don't include documentation, please check Apple's documention
for information on how to use this framework and PyObjC's documentation
for general tips and tricks regarding the translation between Python
and (Objective-)C frameworks
"""

from pyobjc_setup import Extension, setup

VERSION = '7.0'

setup(
    name="pyobjc-framework-MediaToolbox",
    description="Wrappers for the framework MediaToolbox on macOS",
    min_os_level="10.9",
    packages=["MediaToolbox"],
    ext_modules=[
        Extension(
            "MediaToolbox._MediaToolbox",
            ["Modules/_MediaToolbox.m"],
            extra_link_args=["-framework", "MediaToolbox"],
            py_limited_api=True,
        )
    ],
    version=VERSION,
    install_requires=["pyobjc-core>=" + VERSION, "pyobjc-framework-Cocoa>=" + VERSION],
    long_description=__doc__,
    options={"bdist_wheel": {"py_limited_api": "cp36"}},
)
