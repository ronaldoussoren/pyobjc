"""
Python mapping for the Contacts framework.

This module does not contain docstrings for the wrapped code, check Apple's
documentation for details on how to use these functions and classes.
"""


def _setup():
    import sys

    import Foundation
    import objc
    from . import _metadata, _Contacts

    if objc.macos_available(10, 13):
        identifier = "com.apple.contacts"
    else:
        identifier = "com.apple.contacts.Contacts"

    dir_func, getattr_func = objc.createFrameworkDirAndGetattr(
        name="Contacts",
        frameworkIdentifier=identifier,
        frameworkPath=objc.pathForFramework(
            "/System/Library/Frameworks/Contacts.framework"
        ),
        globals_dict=globals(),
        inline_list=None,
        parents=(
            _Contacts,
            Foundation,
        ),
        metadict=_metadata.__dict__,
    )

    globals()["__dir__"] = dir_func
    globals()["__getattr__"] = getattr_func

    for cls, sel in (
        ("CNFetchResult", b"init"),
        ("CNFetchResult", b"new"),
        ("CNContactFetchRequest", b"init"),
        ("CNContactFetchRequest", b"new"),
    ):
        objc.registerUnavailableMethod(cls, sel)

    del sys.modules["Contacts._metadata"]


globals().pop("_setup")()
