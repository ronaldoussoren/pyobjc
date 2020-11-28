"""
Wrappers for framework 'SystemConfiguration'.

These wrappers don't include documentation, please check Apple's documention
for information on how to use this framework and PyObjC's documentation
for general tips and tricks regarding the translation between Python
and (Objective-)C frameworks
"""
from pyobjc_setup import Extension, setup

VERSION = '7.0'

setup(
    name="pyobjc-framework-SystemConfiguration",
    description="Wrappers for the framework SystemConfiguration on macOS",
    packages=["SystemConfiguration"],
    ext_modules=[
        Extension(
            "SystemConfiguration._manual", ["Modules/_manual.m"], py_limited_api=True
        )
    ],
    version=VERSION,
    install_requires=["pyobjc-core>=" + VERSION, "pyobjc-framework-Cocoa>=" + VERSION],
    long_description=__doc__,
    options={"bdist_wheel": {"py_limited_api": "cp36"}},
)
