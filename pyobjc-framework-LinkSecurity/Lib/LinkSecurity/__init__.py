"""
Python mapping for the LinkSecurity framework.

This module does not contain docstrings for the wrapped code, check Apple's
documentation for details on how to use these functions and classes.
"""


def _setup():
    import sys

    import objc
    import Foundation
    from . import _metadata

    dir_func, getattr_func = objc.createFrameworkDirAndGetattr(
        name="LinkSecurity",
        frameworkIdentifier="com.apple.LinkSecurity",
        frameworkPath=objc.pathForFramework(
            "/System/Library/Frameworks/LinkSecurity.framework"
        ),
        globals_dict=globals(),
        inline_list=None,
        parents=(Foundation,),
        metadict=_metadata.__dict__,
    )

    globals()["__dir__"] = dir_func
    globals()["__getattr__"] = getattr_func

    for cls, sel in (
        ("IMLinkSecurityManager", b"init"),
        ("IMLinkSecurityManager", b"new"),
    ):
        objc.registerUnavailableMethod(cls, sel)

    del sys.modules["LinkSecurity._metadata"]


globals().pop("_setup")()
