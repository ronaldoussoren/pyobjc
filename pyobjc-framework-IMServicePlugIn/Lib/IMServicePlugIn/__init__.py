"""
Python mapping for the IMServicePlugIn framework.

This module does not contain docstrings for the wrapped code, check Apple's
documentation for details on how to use these functions and classes.
"""


def _setup():
    import sys

    import AppKit
    import objc
    from . import _metadata, _IMServicePlugIn

    dir_func, getattr_func = objc.createFrameworkDirAndGetattr(
        name="IMServicePlugIn",
        frameworkIdentifier="com.apple.IMServicePlugIn",
        frameworkPath=objc.pathForFramework(
            "/System/Library/Frameworks/IMServicePlugIn.framework"
        ),
        globals_dict=globals(),
        inline_list=None,
        parents=(
            _IMServicePlugIn,
            AppKit,
        ),
        metadict=_metadata.__dict__,
    )

    globals()["__dir__"] = dir_func
    globals()["__getattr__"] = getattr_func

    del sys.modules["IMServicePlugIn._metadata"]


globals().pop("_setup")()
