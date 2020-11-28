"""
Wrappers for the "CoreAudioKit" framework on macOS.

These wrappers don't include documentation, please check Apple's documention
for information on how to use this framework and PyObjC's documentation
for general tips and tricks regarding the translation between Python
and (Objective-)C frameworks
"""

#
# Distutils doesn't undestand '.mm' as an extension
#
import distutils.unixccompiler
import os

from pyobjc_setup import Extension, setup

VERSION = '7.0'


distutils.unixccompiler.UnixCCompiler.src_extensions.append(".mm")

setup(
    name="pyobjc-framework-CoreAudioKit",
    description="Wrappers for the framework CoreAudioKit on macOS",
    packages=["CoreAudioKit"],
    ext_modules=[
        Extension(
            "CoreAudioKit._CoreAudioKit",
            ["Modules/_CoreAudioKit.m"],
            extra_link_args=["-framework", "CoreAudioKit"],
            py_limited_api=True,
            depends=[
                os.path.join("Modules", fn)
                for fn in os.listdir("Modules")
                if fn.startswith("_CoreAudioKit")
            ],
        )
    ],
    version=VERSION,
    install_requires=[
        "pyobjc-core>=" + VERSION,
        "pyobjc-framework-Cocoa>=" + VERSION,
        "pyobjc-framework-CoreAudio>=" + VERSION,
    ],
    long_description=__doc__,
    options={"bdist_wheel": {"py_limited_api": "cp36"}},
)
