"""
Wrappers for the "Message" framework on macOS. This framework contains a
number of utilities for sending e-mail.

These wrappers don't include documentation, please check Apple's documention
for information on how to use this framework and PyObjC's documentation
for general tips and tricks regarding the translation between Python
and (Objective-)C frameworks
"""
from pyobjc_setup import setup

VERSION = '7.0'

setup(
    name="pyobjc-framework-Message",
    description="Wrappers for the framework Message on macOS",
    max_os_level="10.8",
    packages=["Message"],
    version=VERSION,
    install_requires=["pyobjc-core>=" + VERSION, "pyobjc-framework-Cocoa>=" + VERSION],
    long_description=__doc__,
)
