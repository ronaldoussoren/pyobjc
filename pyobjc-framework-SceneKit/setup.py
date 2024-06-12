"""
Wrappers for the "SceneKit" framework on macOS introduced in macOS 10.8.

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
    name="pyobjc-framework-SceneKit",
    description="Wrappers for the framework SceneKit on macOS",
    min_os_level="10.7",
    packages=["SceneKit"],
    ext_modules=[
        Extension(
            "SceneKit._SceneKit",
            ["Modules/_SceneKit.m"],
            extra_link_args=["-framework", "SceneKit"],
            py_limited_api=True,
            depends=[
                os.path.join("Modules", fn)
                for fn in os.listdir("Modules")
                if fn.startswith("_SceneKit")
            ],
        ),
        Extension(
            "SceneKit._inlines",
            ["Modules/_SceneKit_inlines.m"],
            extra_link_args=["-framework", "SceneKit"],
            py_limited_api=True,
        ),
    ],
    version=VERSION,
    install_requires=[
        "pyobjc-core>=" + VERSION,
        "pyobjc-framework-Cocoa>=" + VERSION,
        "pyobjc-framework-Quartz>=" + VERSION,
    ],
    long_description=__doc__,
    options={"bdist_wheel": {"py_limited_api": "cp36"}},
)
