"""
Python mapping for the QuickLookUI framework.

This module does not contain docstrings for the wrapped code, check Apple's
documentation for details on how to use these functions and classes.
"""


def _setup():
    import sys
    import os

    import AppKit
    import objc
    from . import _metadata, _QuickLookUI

    frameworkPath = "/System/Library/Frameworks/QuickLookUI.framework"
    frameworkIdentifier = "com.apple.QuickLookUIFramework"
    if not os.path.exists(frameworkPath):
        frameworkPath = "/System/Library/Frameworks/Quartz.framework"
        if objc.macos_available(13, 0):
            frameworkIdentifier = "com.apple.Quartz"
        else:
            frameworkIdentifier = "com.apple.quartzframework"

    dir_func, getattr_func = objc.createFrameworkDirAndGetattr(
        name="Quartz.QuickLookUI",
        frameworkIdentifier=frameworkIdentifier,
        frameworkPath=objc.pathForFramework(frameworkPath),
        globals_dict=globals(),
        inline_list=None,
        parents=(
            _QuickLookUI,
            AppKit,
        ),
        metadict=_metadata.__dict__,
    )

    globals()["__dir__"] = dir_func
    globals()["__getattr__"] = getattr_func

    # XXX:
    del sys.modules["Quartz.QuickLookUI._metadata"]


globals().pop("_setup")()
