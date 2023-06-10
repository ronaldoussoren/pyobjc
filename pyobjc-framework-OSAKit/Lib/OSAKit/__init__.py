"""
Python mapping for the OSAKit framework.

This module does not contain docstrings for the wrapped code, check Apple's
documentation for details on how to use these functions and classes.
"""


def _setup():
    import sys

    import AppKit
    import objc
    from . import _metadata

    dir_func, getattr_func = objc.createFrameworkDirAndGetattr(
        name="OSAKit",
        frameworkIdentifier="com.apple.OSAKit",
        frameworkPath=objc.pathForFramework(
            "/System/Library/Frameworks/OSAKit.framework"
        ),
        globals_dict=globals(),
        inline_list=None,
        parents=(AppKit,),
        metadict=_metadata.__dict__,
    )

    globals()["__dir__"] = dir_func
    globals()["__getattr__"] = getattr_func

    del sys.modules["OSAKit._metadata"]


globals().pop("_setup")()
