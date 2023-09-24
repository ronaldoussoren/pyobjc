"""
Python mapping for the SyncServices framework.

This module does not contain docstrings for the wrapped code, check Apple's
documentation for details on how to use these functions and classes.
"""


def _setup():
    import sys

    import CoreData
    import objc
    from . import _metadata, _SyncServices

    dir_func, getattr_func = objc.createFrameworkDirAndGetattr(
        name="SyncServices",
        frameworkIdentifier="com.apple.syncservices",
        frameworkPath=objc.pathForFramework(
            "/System/Library/Frameworks/SyncServices.framework"
        ),
        globals_dict=globals(),
        inline_list=None,
        parents=(
            _SyncServices,
            CoreData,
        ),
        metadict=_metadata.__dict__,
    )

    globals()["__dir__"] = dir_func
    globals()["__getattr__"] = getattr_func

    del sys.modules["SyncServices._metadata"]


globals().pop("_setup")()
