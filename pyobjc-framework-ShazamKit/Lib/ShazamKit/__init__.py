"""
Python mapping for the ShazamKit framework.

This module does not contain docstrings for the wrapped code, check Apple's
documentation for details on how to use these functions and classes.
"""


def _setup():
    import sys

    import AppKit
    import objc
    from . import _metadata, _ShazamKit

    dir_func, getattr_func = objc.createFrameworkDirAndGetattr(
        name="ShazamKit",
        frameworkIdentifier="com.apple.ShazamKit",
        frameworkPath=objc.pathForFramework(
            "/System/Library/Frameworks/ShazamKit.framework"
        ),
        globals_dict=globals(),
        inline_list=None,
        parents=(
            _ShazamKit,
            AppKit,
        ),
        metadict=_metadata.__dict__,
    )

    globals()["__dir__"] = dir_func
    globals()["__getattr__"] = getattr_func

    del sys.modules["ShazamKit._metadata"]


globals().pop("_setup")()
