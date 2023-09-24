"""
Python mapping for the ContactsUI framework.

This module does not contain docstrings for the wrapped code, check Apple's
documentation for details on how to use these functions and classes.
"""


def _setup():
    import sys

    import AppKit
    import Contacts
    import objc
    from . import _metadata, _ContactsUI

    dir_func, getattr_func = objc.createFrameworkDirAndGetattr(
        name="ContactsUI",
        frameworkIdentifier="com.apple.ContactsUI",
        frameworkPath=objc.pathForFramework(
            "/System/Library/Frameworks/ContactsUI.framework"
        ),
        globals_dict=globals(),
        inline_list=None,
        parents=(_ContactsUI, Contacts, AppKit),
        metadict=_metadata.__dict__,
    )

    globals()["__dir__"] = dir_func
    globals()["__getattr__"] = getattr_func

    del sys.modules["ContactsUI._metadata"]


globals().pop("_setup")()
