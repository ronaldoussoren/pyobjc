"""
Wrappers for framework 'SystemConfiguration'.

These wrappers don't include documentation, please check Apple's documentation
for information on how to use this framework and PyObjC's documentation
for general tips and tricks regarding the translation between Python
and (Objective-)C frameworks
"""

import os
import sys

sys.path.insert(0, os.path.dirname(__file__))


from pyobjc_setup import Extension, setup  # noqa: E402

VERSION = '12.0a0'

setup(
    name="pyobjc-framework-SystemConfiguration",
    description="Wrappers for the framework SystemConfiguration on macOS",
    packages=["SystemConfiguration"],
    ext_modules=[
        Extension(
            "SystemConfiguration._manual",
            ["Modules/_manual.m"],
        )
    ],
    version=VERSION,
    install_requires=["pyobjc-core>=" + VERSION, "pyobjc-framework-Cocoa>=" + VERSION],
    long_description=__doc__,
)
