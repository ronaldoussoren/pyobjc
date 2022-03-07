"""
Wrappers for the "PreferencePanes" framework on macOS. This framework allows
you to write Preference Panes for the "System Preferences" application.

These wrappers don't include documentation, please check Apple's documentation
for information on how to use this framework and PyObjC's documentation
for general tips and tricks regarding the translation between Python
and (Objective-)C frameworks
"""
from pyobjc_setup import setup

VERSION = "8.4"

setup(
    name="pyobjc-framework-PreferencePanes",
    description="Wrappers for the framework PreferencePanes on macOS",
    packages=["PreferencePanes"],
    version=VERSION,
    install_requires=["pyobjc-core>=" + VERSION, "pyobjc-framework-Cocoa>=" + VERSION],
    long_description=__doc__,
)
