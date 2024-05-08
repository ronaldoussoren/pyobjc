"""
Python mapping for the ScreenTime framework.

This module does not contain docstrings for the wrapped code, check Apple's
documentation for details on how to use these functions and classes.
"""


def _setup():
    import sys

    import Foundation
    import objc
    from . import _metadata

    dir_func, getattr_func = objc.createFrameworkDirAndGetattr(
        name="ScreenTime",
        frameworkIdentifier="com.apple.ScreenTime",
        frameworkPath=objc.pathForFramework(
            "/System/Library/Frameworks/ScreenTime.framework"
        ),
        globals_dict=globals(),
        inline_list=None,
        parents=(Foundation,),
        metadict=_metadata.__dict__,
    )

    globals()["__dir__"] = dir_func
    globals()["__getattr__"] = getattr_func

    for cls, sel in (
        ("STWebpageController", b"initWithNibName:bundle:"),
        ("STWebpageController", b"initWithCoder:"),
        ("STScreenTimeConfiguration", b"init"),
        ("STScreenTimeConfiguration", b"new"),
        ("STScreenTimeConfigurationObserver", b"init"),
        ("STScreenTimeConfigurationObserver", b"new"),
    ):
        objc.registerUnavailableMethod(cls, sel)

    del sys.modules["ScreenTime._metadata"]


globals().pop("_setup")()
