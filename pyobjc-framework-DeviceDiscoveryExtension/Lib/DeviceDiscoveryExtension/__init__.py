"""
Python mapping for the DeviceDiscoveryExtension framework.

This module does not contain docstrings for the wrapped code, check Apple's
documentation for details on how to use these functions and classes.
"""


def _setup():
    import sys

    import objc
    import Foundation
    from . import _metadata

    dir_func, getattr_func = objc.createFrameworkDirAndGetattr(
        name="DeviceDiscoveryExtension",
        frameworkIdentifier="com.apple.DeviceDiscoveryExtension",
        frameworkPath=objc.pathForFramework(
            "/System/Library/Frameworks/DeviceDiscoveryExtension.framework"
        ),
        globals_dict=globals(),
        inline_list=None,
        parents=(Foundation,),
        metadict=_metadata.__dict__,
    )

    globals()["__dir__"] = dir_func
    globals()["__getattr__"] = getattr_func

    del sys.modules["DeviceDiscoveryExtension._metadata"]


globals().pop("_setup")()
