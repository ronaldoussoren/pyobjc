"""
Python mapping for the UserNotificationsUI framework.

This module does not contain docstrings for the wrapped code, check Apple's
documentation for details on how to use these functions and classes.
"""


def _setup():
    import sys

    import AppKit
    import UserNotifications
    import objc
    from . import _metadata

    dir_func, getattr_func = objc.createFrameworkDirAndGetattr(
        name="UserNotificationsUI",
        frameworkIdentifier="com.apple.UserNotificationsUI",
        frameworkPath=objc.pathForFramework(
            "/System/Library/Frameworks/UserNotificationsUI.framework"
        ),
        globals_dict=globals(),
        inline_list=None,
        parents=(
            UserNotifications,
            AppKit,
        ),
        metadict=_metadata.__dict__,
    )

    globals()["__dir__"] = dir_func
    globals()["__getattr__"] = getattr_func

    del sys.modules["UserNotificationsUI._metadata"]


globals().pop("_setup")()
