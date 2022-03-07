"""
Wrappers for the "DiscRecording" framework on macOS.

These wrappers don't include documentation, please check Apple's documentation
for information on how to use this framework and PyObjC's documentation
for general tips and tricks regarding the translation between Python
and (Objective-)C frameworks
"""

#
# Distutils doesn't understand '.mm' as an extension
#
import distutils.unixccompiler
import os

from pyobjc_setup import Extension, setup

VERSION = "8.4"


distutils.unixccompiler.UnixCCompiler.src_extensions.append(".mm")

setup(
    name="pyobjc-framework-DiscRecording",
    description="Wrappers for the framework DiscRecording on macOS",
    packages=["DiscRecording"],
    ext_modules=[
        Extension(
            "DiscRecording._DiscRecording",
            ["Modules/_DiscRecording.m"],
            extra_link_args=["-framework", "DiscRecording"],
            py_limited_api=True,
            depends=[
                os.path.join("Modules", fn)
                for fn in os.listdir("Modules")
                if fn.startswith("_DiscRecording")
            ],
        )
    ],
    version=VERSION,
    install_requires=["pyobjc-core>=" + VERSION, "pyobjc-framework-Cocoa>=" + VERSION],
    long_description=__doc__,
    options={"bdist_wheel": {"py_limited_api": "cp36"}},
)
