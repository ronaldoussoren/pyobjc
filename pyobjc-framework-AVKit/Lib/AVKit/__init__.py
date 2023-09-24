"""
Python mapping for the AddressBook framework.

This module does not contain docstrings for the wrapped code, check Apple's
documentation for details on how to use these functions and classes.
"""


def _setup():
    import sys

    import Cocoa
    import Quartz
    import objc
    from . import _AVKit, _metadata

    dir_func, getattr_func = objc.createFrameworkDirAndGetattr(
        name="AVKit",
        frameworkIdentifier="com.apple.AVKit",
        frameworkPath=objc.pathForFramework(
            "/System/Library/Frameworks/AVKit.framework"
        ),
        globals_dict=globals(),
        inline_list=None,
        parents=(_AVKit, Cocoa, Quartz),
        metadict=_metadata.__dict__,
    )

    globals()["__dir__"] = dir_func
    globals()["__getattr__"] = getattr_func

    del sys.modules["AVKit._metadata"]


globals().pop("_setup")()
