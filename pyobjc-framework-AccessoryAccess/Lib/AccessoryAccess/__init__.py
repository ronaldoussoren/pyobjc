"""
Python mapping for the AccessoryAccess framework.

This module does not contain docstrings for the wrapped code, check Apple's
documentation for details on how to use these functions and classes.
"""


def _setup():
    import sys

    import Foundation
    import objc
    from . import _metadata

    dir_func, getattr_func = objc.createFrameworkDirAndGetattr(
        name="AccessoryAccess",
        frameworkIdentifier="com.apple.AccessoryAccess",
        frameworkPath=objc.pathForFramework(
            "/System/Library/Frameworks/AccessoryAccess.framework"
        ),
        globals_dict=globals(),
        inline_list=None,
        parents=(Foundation,),
        metadict=_metadata.__dict__,
    )

    globals()["__dir__"] = dir_func
    globals()["__getattr__"] = getattr_func

    for cls, sel in (
        ("AAUSBAccessory", b"init"),
        ("AAUSBAccessory", b"new"),
        ("AAUSBAccessoryManager", b"init"),
        ("AAUSBAccessoryManager", b"new"),
        ("AAUSBAccessoryMatchingCriteria", b"init"),
        ("AAUSBAccessoryMatchingCriteria", b"new"),
    ):
        objc.registerUnavailableMethod(cls, sel)

    del sys.modules["AccessoryAccess._metadata"]


globals().pop("_setup")()
