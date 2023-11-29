"""
Python mapping for the EventKit framework.

This module does not contain docstrings for the wrapped code, check Apple's
documentation for details on how to use these functions and classes.
"""


def _setup():
    import sys

    import Foundation
    import objc
    from . import _metadata

    if objc.macos_available(13, 0):
        identifier = "com.apple.eventkit"
    else:
        identifier = "com.apple.ical.EventKit"

    dir_func, getattr_func = objc.createFrameworkDirAndGetattr(
        name="EventKit",
        frameworkIdentifier=identifier,
        frameworkPath=objc.pathForFramework(
            "/System/Library/Frameworks/EventKit.framework"
        ),
        globals_dict=globals(),
        inline_list=None,
        parents=(Foundation,),
        metadict=_metadata.__dict__,
    )

    globals()["__dir__"] = dir_func
    globals()["__getattr__"] = getattr_func

    del sys.modules["EventKit._metadata"]


globals().pop("_setup")()
