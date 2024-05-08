"""
Python mapping for the OSLog framework.

This module does not contain docstrings for the wrapped code, check Apple's
documentation for details on how to use these functions and classes.
"""


def _setup():
    import sys

    import Foundation
    import objc
    from . import _metadata, _OSLog

    dir_func, getattr_func = objc.createFrameworkDirAndGetattr(
        name="OSLog",
        frameworkIdentifier="com.apple.OSLog",
        frameworkPath=objc.pathForFramework(
            "/System/Library/Frameworks/OSLog.framework"
        ),
        globals_dict=globals(),
        inline_list=None,
        parents=(
            _OSLog,
            Foundation,
        ),
        metadict=_metadata.__dict__,
    )

    globals()["__dir__"] = dir_func
    globals()["__getattr__"] = getattr_func

    for cls, sel in (("OSLogPosition", b"init"),):
        objc.registerUnavailableMethod(cls, sel)

    del sys.modules["OSLog._metadata"]


globals().pop("_setup")()
