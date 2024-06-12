"""
Wrappers for the "CoreAudio" framework on macOS.

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
import sys

sys.path.insert(0, os.path.dirname(__file__))


from pyobjc_setup import Extension, setup  # noqa: E402

VERSION = "10.3.2"


distutils.unixccompiler.UnixCCompiler.src_extensions.append(".mm")

setup(
    name="pyobjc-framework-CoreAudio",
    description="Wrappers for the framework CoreAudio on macOS",
    packages=["CoreAudio"],
    ext_modules=[
        Extension(
            "CoreAudio._inlines",
            ["Modules/_CoreAudio_inlines.mm"],
            extra_link_args=["-framework", "CoreAudio"],
            py_limited_api=True,
        ),
        Extension(
            "CoreAudio._CoreAudio",
            ["Modules/_CoreAudio.m"],
            extra_link_args=["-framework", "CoreAudio"],
            # py_limited_api=True,
            depends=[
                os.path.join("Modules", fn)
                for fn in os.listdir("Modules")
                if fn.startswith("_CoreAudio")
            ],
        ),
    ],
    version=VERSION,
    install_requires=["pyobjc-core>=" + VERSION, "pyobjc-framework-Cocoa>=" + VERSION],
    long_description=__doc__,
    #    options={"bdist_wheel": {"py_limited_api": "cp36"}},
)
