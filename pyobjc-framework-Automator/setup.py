"""
Wrappers for the "Automator" framework on macOS. The Automator framework
supports the development of actions for the Automator application, as well
as the ability to run a workflow in developer applications. An action is
a bundle that, when loaded and run, performs a specific task.

These wrappers don't include documentation, please check Apple's documentation
for information on how to use this framework and PyObjC's documentation
for general tips and tricks regarding the translation between Python
and (Objective-)C frameworks
"""
import os
import sys

sys.path.insert(0, os.path.dirname(__file__))


from pyobjc_setup import setup  # noqa: E402

VERSION = "9.1.1"

setup(
    name="pyobjc-framework-Automator",
    description="Wrappers for the framework Automator on macOS",
    packages=["Automator"],
    version=VERSION,
    install_requires=["pyobjc-core>=" + VERSION, "pyobjc-framework-Cocoa>=" + VERSION],
    long_description=__doc__,
)
