"""
Wrappers for the "IOBluetoothUI" framework on macOS.

These wrappers don't include documentation, please check Apple's documentation
for information on how to use this framework and PyObjC's documentation
for general tips and tricks regarding the translation between Python
and (Objective-)C frameworks
"""

from pyobjc_setup import setup

VERSION = "9.1"

setup(
    name="pyobjc-framework-IOBluetoothUI",
    description="Wrappers for the framework IOBluetoothUI on macOS",
    packages=["IOBluetoothUI"],
    version=VERSION,
    install_requires=[
        "pyobjc-core>=" + VERSION,
        "pyobjc-framework-IOBluetooth>=" + VERSION,
    ],
    long_description=__doc__,
    options={"bdist_wheel": {"py_limited_api": "cp36"}},
)
