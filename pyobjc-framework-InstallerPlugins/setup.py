"""
Wrappers for the "InstallerPlugins" framework on macOS. This framework
allows you to develop plugin's for the "Installer.app" application, and those
make it possible to add new functionality to ".pkg" and ".mpkg" installers
on macOS.

These wrappers don't include documentation, please check Apple's documentation
for information on how to use this framework and PyObjC's documentation
for general tips and tricks regarding the translation between Python
and (Objective-)C frameworks
"""

import os
import sys

sys.path.insert(0, os.path.dirname(__file__))


from pyobjc_setup import setup  # noqa: E402

VERSION = "10.3.2"

setup(
    name="pyobjc-framework-InstallerPlugins",
    description="Wrappers for the framework InstallerPlugins on macOS",
    packages=["InstallerPlugins"],
    version=VERSION,
    install_requires=["pyobjc-core>=" + VERSION, "pyobjc-framework-Cocoa>=" + VERSION],
    long_description=__doc__,
)
