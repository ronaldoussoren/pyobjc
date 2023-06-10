"""
Python mapping for the MLCompute framework.

This module does not contain docstrings for the wrapped code, check Apple's
documentation for details on how to use these functions and classes.
"""


def _setup():
    import sys

    import Foundation
    import objc
    from . import _metadata

    dir_func, getattr_func = objc.createFrameworkDirAndGetattr(
        name="MLCompute",
        frameworkIdentifier="com.apple.MLCompute",
        frameworkPath=objc.pathForFramework(
            "/System/Library/Frameworks/MLCompute.framework"
        ),
        globals_dict=globals(),
        inline_list=None,
        parents=(Foundation,),
        metadict=_metadata.__dict__,
    )

    globals()["__dir__"] = dir_func
    globals()["__getattr__"] = getattr_func

    del sys.modules["MLCompute._metadata"]


globals().pop("_setup")()
