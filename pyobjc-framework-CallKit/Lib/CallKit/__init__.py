"""
Python mapping for the CallKit framework.

This module does not contain docstrings for the wrapped code, check Apple's
documentation for details on how to use these functions and classes.
"""


def _setup():
    import sys

    import Foundation
    import objc
    from . import _metadata, _CallKit

    dir_func, getattr_func = objc.createFrameworkDirAndGetattr(
        name="CallKit",
        frameworkIdentifier="com.apple.CallKit",
        frameworkPath=objc.pathForFramework(
            "/System/Library/Frameworks/CallKit.framework"
        ),
        globals_dict=globals(),
        inline_list=None,
        parents=(Foundation, _CallKit),
        metadict=_metadata.__dict__,
    )

    globals()["__dir__"] = dir_func
    globals()["__getattr__"] = getattr_func

    for cls, sel in (
        ("CXProvider", b"init"),
        ("CXProvider", b"new"),
        ("CXCall", b"init"),
        (
            "CXCallDirectoryExtensionContext",
            b"completeRequestReturningItems:completionHandler:",
        ),
        ("CXSetMutedCallAction", b"initWithCallUUID:"),
        ("CXPlayDTMFCallAction", b"initWithCallUUID:"),
        ("CXSetHeldCallAction", b"initWithCallUUID:"),
        ("CXSetGroupCallAction", b"initWithCallUUID:"),
        ("CXStartCallAction", b"initWithCallUUID:"),
        ("CXCallAction", b"init"),
        ("CXHandle", b"init"),
    ):
        objc.registerUnavailableMethod(cls, sel)

    del sys.modules["CallKit._metadata"]


globals().pop("_setup")()
