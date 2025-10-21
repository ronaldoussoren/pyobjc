"""
PyObjC wrappers for the framework "CFNetwork", part of "CoreServices" on
macOS.

The CFNetwork framework provides a library of abstractions for networking
protocols. The most interesting bits for Python programmers are the
API's for working with proxy autoconfiguration and the API's for networking
diagnostics.

These wrappers don't include documentation, please check Apple's documentation
for information on how to use this framework and PyObjC's documentation
for general tips and tricks regarding the translation between Python
and (Objective-)C frameworks
"""

import os
import sys

sys.path.insert(0, os.path.dirname(__file__))


from pyobjc_setup import Extension, setup  # noqa: E402

VERSION = "12.0"

setup(
    name="pyobjc-framework-CFNetwork",
    description="Wrappers for the framework CFNetwork on macOS",
    packages=["CFNetwork"],
    ext_modules=[
        Extension(
            "CFNetwork._manual",
            ["Modules/_manual.m"],
            extra_link_args=["-framework", "CoreServices"],
        )
    ],
    version=VERSION,
    install_requires=["pyobjc-core>=" + VERSION, "pyobjc-framework-Cocoa>=" + VERSION],
    long_description=__doc__,
)
