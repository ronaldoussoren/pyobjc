"""
Python mapping for the MultipeerConnectivity framework.

This module does not contain docstrings for the wrapped code, check Apple's
documentation for details on how to use these functions and classes.
"""


def _setup():
    import sys

    import Foundation
    import objc
    from . import _metadata, _MultipeerConnectivity

    dir_func, getattr_func = objc.createFrameworkDirAndGetattr(
        name="MultipeerConnectivity",
        frameworkIdentifier="com.apple.MultipeerConnectivity",
        frameworkPath=objc.pathForFramework(
            "/System/Library/Frameworks/MultipeerConnectivity.framework"
        ),
        globals_dict=globals(),
        inline_list=None,
        parents=(
            _MultipeerConnectivity,
            Foundation,
        ),
        metadict=_metadata.__dict__,
    )

    globals()["__dir__"] = dir_func
    globals()["__getattr__"] = getattr_func

    del sys.modules["MultipeerConnectivity._metadata"]


globals().pop("_setup")()
