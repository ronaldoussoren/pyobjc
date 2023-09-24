"""
Python mapping for the AddressBook framework.

This module does not contain docstrings for the wrapped code, check Apple's
documentation for details on how to use these functions and classes.
"""


def _setup():
    import sys

    import Foundation
    import objc
    from . import _metadata, _AddressBook

    dir_func, getattr_func = objc.createFrameworkDirAndGetattr(
        name="AddressBook",
        frameworkIdentifier="com.apple.AddressBook.framework",
        frameworkPath=objc.pathForFramework(
            "/System/Library/Frameworks/AddressBook.framework"
        ),
        globals_dict=globals(),
        inline_list=None,
        parents=(_AddressBook, Foundation),
        metadict=_metadata.__dict__,
    )

    globals()["__dir__"] = dir_func
    globals()["__getattr__"] = getattr_func

    del sys.modules["AddressBook._metadata"]


globals().pop("_setup")()
