"""
Wrappers for the "FSEvents" API in macOS. The functions in this framework
allow you to reliably observe changes to the filesystem, even when your
program is not running al the time.

These wrappers don't include documentation, please check Apple's documentation
for information on how to use this framework and PyObjC's documentation
for general tips and tricks regarding the translation between Python
and (Objective-)C frameworks
"""
from pyobjc_setup import Extension, setup

VERSION = "8.4"

setup(
    name="pyobjc-framework-FSEvents",
    description="Wrappers for the framework FSEvents on macOS",
    min_os_level="10.5",
    packages=["FSEvents"],
    ext_modules=[
        Extension("FSEvents._callbacks", ["Modules/_callbacks.m"], py_limited_api=True)
    ],
    version=VERSION,
    install_requires=["pyobjc-core>=" + VERSION, "pyobjc-framework-Cocoa>=" + VERSION],
    long_description=__doc__,
    options={"bdist_wheel": {"py_limited_api": "cp36"}},
)
