"""
Python mapping for the CoreData framework.

This module does not contain docstrings for the wrapped code, check Apple's
documentation for details on how to use these functions and classes.
"""


def _setup():
    import sys

    import Foundation
    import objc
    from . import _metadata, _CoreData

    dir_func, getattr_func = objc.createFrameworkDirAndGetattr(
        name="CoreData",
        frameworkIdentifier="com.apple.CoreData",
        frameworkPath=objc.pathForFramework(
            "/System/Library/Frameworks/CoreData.framework"
        ),
        globals_dict=globals(),
        inline_list=None,
        parents=(
            _CoreData,
            Foundation,
        ),
        metadict=_metadata.__dict__,
    )

    globals()["__dir__"] = dir_func
    globals()["__getattr__"] = getattr_func

    del sys.modules["CoreData._metadata"]


globals().pop("_setup")()
