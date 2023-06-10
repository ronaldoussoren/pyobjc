"""
Python mapping for the DiskArbitration framework.

This module does not contain docstrings for the wrapped code, check Apple's
documentation for details on how to use these functions and classes.
"""


def _setup():
    import sys

    import CoreFoundation
    import objc
    from . import _metadata

    dir_func, getattr_func = objc.createFrameworkDirAndGetattr(
        name="DiskArbitration",
        frameworkIdentifier="com.apple.DiskArbitration",
        frameworkPath=objc.pathForFramework(
            "/System/Library/Frameworks/DiskArbitration.framework"
        ),
        globals_dict=globals(),
        inline_list=None,
        parents=(CoreFoundation,),
        metadict=_metadata.__dict__,
    )

    globals()["__dir__"] = dir_func
    globals()["__getattr__"] = getattr_func

    del sys.modules["DiskArbitration._metadata"]


globals().pop("_setup")()
