"""
Python mapping for the iTunesLibrary framework.

This module does not contain docstrings for the wrapped code, check Apple's
documentation for details on how to use these functions and classes.
"""


def _setup():
    import sys
    import os

    import Foundation
    import objc
    from . import _metadata

    frameworkPath = "/System/Library/Frameworks/iTunesLibrary.framework"
    if not os.path.exists(frameworkPath):
        # macOS 10.15 or earlier
        frameworkPath = "/Library/Frameworks/iTunesLibrary.framework"

    dir_func, getattr_func = objc.createFrameworkDirAndGetattr(
        name="iTunesLibrary",
        frameworkIdentifier="com.apple.iTunesLibrary",
        frameworkPath=objc.pathForFramework(frameworkPath),
        globals_dict=globals(),
        inline_list=None,
        parents=(Foundation,),
        metadict=_metadata.__dict__,
    )

    globals()["__dir__"] = dir_func
    globals()["__getattr__"] = getattr_func

    del sys.modules["iTunesLibrary._metadata"]


globals().pop("_setup")()
