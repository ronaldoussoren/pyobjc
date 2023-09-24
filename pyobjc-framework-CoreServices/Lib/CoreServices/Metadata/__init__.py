"""
Python mapping for the CoreServices/Metadata framework.

This module does not contain docstrings for the wrapped code, check Apple's
documentation for details on how to use these functions and classes.

Note that PyObjC only wrappers the non-deprecated parts of the CoreServices
framework.
"""


def _setup():
    import sys

    import Foundation
    import objc
    from . import _metadata

    dir_func, getattr_func = objc.createFrameworkDirAndGetattr(
        name="CoreServices.Metadata",
        frameworkIdentifier="com.apple.CoreServices",
        frameworkPath=objc.pathForFramework(
            "/System/Library/Frameworks/CoreServices.framework"
        ),
        globals_dict=globals(),
        inline_list=None,
        parents=(Foundation,),
        metadict=_metadata.__dict__,
    )

    globals()["__dir__"] = dir_func
    globals()["__getattr__"] = getattr_func

    del sys.modules["CoreServices.Metadata._metadata"]


globals().pop("_setup")()
