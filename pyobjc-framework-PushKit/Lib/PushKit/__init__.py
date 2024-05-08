"""
Python mapping for the PushKit framework.

This module does not contain docstrings for the wrapped code, check Apple's
documentation for details on how to use these functions and classes.
"""


def _setup():
    import sys

    import Foundation
    import objc
    from . import _metadata, _PushKit

    dir_func, getattr_func = objc.createFrameworkDirAndGetattr(
        name="PushKit",
        frameworkIdentifier="com.apple.PushKit",
        frameworkPath=objc.pathForFramework(
            "/System/Library/Frameworks/PushKit.framework"
        ),
        globals_dict=globals(),
        inline_list=None,
        parents=(
            _PushKit,
            Foundation,
        ),
        metadict=_metadata.__dict__,
    )

    globals()["__dir__"] = dir_func
    globals()["__getattr__"] = getattr_func

    for cls, sel in (("PKPushRegistry", b"init"),):
        objc.registerUnavailableMethod(cls, sel)

    del sys.modules["PushKit._metadata"]


globals().pop("_setup")()
