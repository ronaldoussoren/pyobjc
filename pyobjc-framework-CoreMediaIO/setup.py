"""
Wrappers for the "CoreMediaIO" framework on macOS.

These wrappers don't include documentation, please check Apple's documentation
for information on how to use this framework and PyObjC's documentation
for general tips and tricks regarding the translation between Python
and (Objective-)C frameworks
"""

from pyobjc_setup import Extension, setup

VERSION = "8.4"

setup(
    name="pyobjc-framework-CoreMediaIO",
    description="Wrappers for the framework CoreMediaIO on macOS",
    min_os_level="10.7",
    packages=["CoreMediaIO"],
    ext_modules=[
        Extension(
            "CoreMediaIO._CoreMediaIO",
            ["Modules/_CoreMediaIO.m"],
            extra_link_args=["-framework", "CoreMediaIO"],
            py_limited_api=True,
        )
    ],
    version=VERSION,
    install_requires=["pyobjc-core>=" + VERSION, "pyobjc-framework-Cocoa>=" + VERSION],
    long_description=__doc__,
    options={"bdist_wheel": {"py_limited_api": "cp36"}},
)
