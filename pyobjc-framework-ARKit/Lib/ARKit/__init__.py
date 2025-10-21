"""
Python mapping for the ARKit framework.

This module does not contain docstrings for the wrapped code, check Apple's
documentation for details on how to use these functions and classes.
"""


def _setup():
    import sys

    import objc
    import Foundation
    from . import _metadata

    dir_func, getattr_func = objc.createFrameworkDirAndGetattr(
        name="ARKit",
        frameworkIdentifier="com.apple.ARKit",
        frameworkPath=objc.pathForFramework(
            "/System/Library/Frameworks/ARKit.framework"
        ),
        globals_dict=globals(),
        inline_list=None,
        parents=(Foundation,),
        metadict=_metadata.__dict__,
    )

    globals()["__dir__"] = dir_func
    globals()["__getattr__"] = getattr_func

    del sys.modules["ARKit._metadata"]


globals().pop("_setup")()
