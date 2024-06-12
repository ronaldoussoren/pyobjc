"""
Wrappers for the "InputMethodKit" framework on macOS 10.5 or later. The
interfaces in this framework allow you to develop input methods.

These wrappers don't include documentation, please check Apple's documentation
for information on how to use this framework and PyObjC's documentation
for general tips and tricks regarding the translation between Python
and (Objective-)C frameworks
"""

import os
import sys

sys.path.insert(0, os.path.dirname(__file__))


from pyobjc_setup import Extension, setup  # noqa: E402

VERSION = "10.3.2"

setup(
    name="pyobjc-framework-InputMethodKit",
    description="Wrappers for the framework InputMethodKit on macOS",
    min_os_level="10.5",
    packages=["InputMethodKit"],
    ext_modules=[
        Extension(
            "InputMethodKit._InputMethodKit",
            ["Modules/_InputMethodKit.m"],
            extra_link_args=["-framework", "InputMethodKit"],
            py_limited_api=True,
            depends=[
                os.path.join("Modules", fn)
                for fn in os.listdir("Modules")
                if fn.startswith("_InputMethodKit")
            ],
        )
    ],
    version=VERSION,
    install_requires=["pyobjc-core>=" + VERSION, "pyobjc-framework-Cocoa>=" + VERSION],
    long_description=__doc__,
    options={"bdist_wheel": {"py_limited_api": "cp36"}},
)
