"""
Python mapping for the BackgroundAssets framework.

This module does not contain docstrings for the wrapped code, check Apple's
documentation for details on how to use these functions and classes.
"""


def _setup():
    import sys

    import Foundation
    import objc
    from . import _metadata, _BackgroundAssets

    dir_func, getattr_func = objc.createFrameworkDirAndGetattr(
        name="BackgroundAssets",
        frameworkIdentifier="com.apple.mobileasset.BackgroundAssets",
        frameworkPath=objc.pathForFramework(
            "/System/Library/Frameworks/BackgroundAssets.framework"
        ),
        globals_dict=globals(),
        inline_list=None,
        parents=(_BackgroundAssets, Foundation),
        metadict=_metadata.__dict__,
    )

    globals()["__dir__"] = dir_func
    globals()["__getattr__"] = getattr_func

    del sys.modules["BackgroundAssets._metadata"]


globals().pop("_setup")()
