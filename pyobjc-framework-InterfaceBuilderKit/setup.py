"""
Wrappers for the framework "InterfaceBuilderKit" on macOS. This framework
is only available when you've installed Xcode 3.x, but not with earlier or
later releases of Xcode.

The Interface Builder Kit is a framework containing the classes you use to
implement custom plug-ins for Interface Builder. A plug-in injects one or
more custom objects into Interface Builder's library window. From the library
window, users can access your custom objects and drag them into their nib
files just as they would the standard system controls. You can also use this
framework to implement inspectors for manipulating your objects at runtime.

These wrappers don't include documentation, please check Apple's documention
for information on how to use this framework and PyObjC's documentation
for general tips and tricks regarding the translation between Python
and (Objective-)C frameworks

NOTE: To run the unittests for this framework use::

    $ env DYLD_FRAMEWORK_PATH="$(xcode-select -print-path)/Library/PrivateFrameworks/" python setup.py test  # noqa: B950

This is needed because the InterfaceBuilderKit framework won't load otherwise.
"""
from pyobjc_setup import setup

VERSION = '7.0'

setup(
    name="pyobjc-framework-InterfaceBuilderKit",
    description="Wrappers for the framework InterfaceBuilderKit on macOS",
    min_os_level="10.5",
    max_os_level="10.6",
    packages=["InterfaceBuilderKit"],
    version=VERSION,
    install_requires=["pyobjc-core>=" + VERSION, "pyobjc-framework-Cocoa>=" + VERSION],
    long_description=__doc__,
)
