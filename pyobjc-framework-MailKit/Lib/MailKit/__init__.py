"""
Python mapping for the MailKit framework.

This module does not contain docstrings for the wrapped code, check Apple's
documentation for details on how to use these functions and classes.
"""


def _setup():
    import sys

    import AppKit
    import objc
    from . import _metadata

    dir_func, getattr_func = objc.createFrameworkDirAndGetattr(
        name="MailKit",
        frameworkIdentifier="com.apple.MailKit",
        frameworkPath=objc.pathForFramework(
            "/System/Library/Frameworks/MailKit.framework"
        ),
        globals_dict=globals(),
        inline_list=None,
        parents=(AppKit,),
        metadict=_metadata.__dict__,
    )

    globals()["__dir__"] = dir_func
    globals()["__getattr__"] = getattr_func

    del sys.modules["MailKit._metadata"]


globals().pop("_setup")()
