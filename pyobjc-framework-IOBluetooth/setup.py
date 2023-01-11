"""
Wrappers for the "IOBluetooth" framework on macOS.

These wrappers don't include documentation, please check Apple's documentation
for information on how to use this framework and PyObjC's documentation
for general tips and tricks regarding the translation between Python
and (Objective-)C frameworks
"""

from pyobjc_setup import setup

VERSION = "9.1"

setup(
    name="pyobjc-framework-IOBluetooth",
    description="Wrappers for the framework IOBluetooth on macOS",
    min_os_level="10.7",
    packages=["IOBluetooth"],
    version=VERSION,
    install_requires=[
        "pyobjc-core>=" + VERSION,
        "pyobjc-framework-Cocoa>=" + VERSION,
    ],
    long_description=__doc__,
    options={"bdist_wheel": {"py_limited_api": "cp36"}},
)
