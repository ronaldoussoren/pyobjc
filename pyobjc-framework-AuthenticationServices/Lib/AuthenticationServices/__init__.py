"""
Python mapping for the AuthenticationServices framework.

This module does not contain docstrings for the wrapped code, check Apple's
documentation for details on how to use these functions and classes.
"""


def _setup():
    import sys

    import Foundation
    import objc
    from . import _metadata, _AuthenticationServices

    dir_func, getattr_func = objc.createFrameworkDirAndGetattr(
        name="AuthenticationServices",
        frameworkIdentifier="com.apple.AuthenticationServices",
        frameworkPath=objc.pathForFramework(
            "/System/Library/Frameworks/AuthenticationServices.framework"
        ),
        globals_dict=globals(),
        inline_list=None,
        parents=(_AuthenticationServices, Foundation),
        metadict=_metadata.__dict__,
    )

    globals()["__dir__"] = dir_func
    globals()["__getattr__"] = getattr_func

    del sys.modules["AuthenticationServices._metadata"]


globals().pop("_setup")()
