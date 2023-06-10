"""
Python mapping for the AddressBook framework.

This module does not contain docstrings for the wrapped code, check Apple's
documentation for details on how to use these functions and classes.
"""


def _setup():
    import sys

    import AppKit
    import objc
    from . import _metadata

    dir_func, getattr_func = objc.createFrameworkDirAndGetattr(
        name="MediaAccessibility",
        frameworkIdentifier="com.apple.MediaAccessibility",
        frameworkPath=objc.pathForFramework(
            "/System/Library/Frameworks/MediaAccessibility.framework"
        ),
        globals_dict=globals(),
        inline_list=None,
        parents=(AppKit,),
        metadict=_metadata.__dict__,
    )

    globals()["__dir__"] = dir_func
    globals()["__getattr__"] = getattr_func

    del sys.modules["MediaAccessibility._metadata"]


globals().pop("_setup")()
