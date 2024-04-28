"""
Python mapping for the PencilKit framework.

This module does not contain docstrings for the wrapped code, check Apple's
documentation for details on how to use these functions and classes.
"""


def _setup():
    import sys

    import Foundation
    import objc
    from . import _metadata

    dir_func, getattr_func = objc.createFrameworkDirAndGetattr(
        name="PencilKit",
        frameworkIdentifier="com.apple.PencilKit",
        frameworkPath=objc.pathForFramework(
            "/System/Library/Frameworks/PencilKit.framework"
        ),
        globals_dict=globals(),
        inline_list=None,
        parents=(Foundation,),
        metadict=_metadata.__dict__,
    )

    globals()["__dir__"] = dir_func
    globals()["__getattr__"] = getattr_func

    for cls, sel in (
        ("PKStrokePoint", b"init"),
        ("PKTool", b"init"),
        ("PKTool", b"new"),
    ):
        objc.registerUnavailableMethod(cls, sel)

    del sys.modules["PencilKit._metadata"]


globals().pop("_setup")()
