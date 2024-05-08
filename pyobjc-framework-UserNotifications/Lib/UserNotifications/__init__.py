"""
Python mapping for the UserNotifications framework.

This module does not contain docstrings for the wrapped code, check Apple's
documentation for details on how to use these functions and classes.
"""


def _setup():
    import sys

    import Foundation
    import objc
    from . import _metadata, _UserNotifications

    dir_func, getattr_func = objc.createFrameworkDirAndGetattr(
        name="UserNotifications",
        frameworkIdentifier="com.apple.UserNotifications",
        frameworkPath=objc.pathForFramework(
            "/System/Library/Frameworks/UserNotifications.framework"
        ),
        globals_dict=globals(),
        inline_list=None,
        parents=(
            _UserNotifications,
            Foundation,
        ),
        metadict=_metadata.__dict__,
    )

    globals()["__dir__"] = dir_func
    globals()["__getattr__"] = getattr_func

    for cls, sel in (
        ("UNNotificationActionIcon", b"init"),
        ("UNUserNotificationCenter", b"init"),
        ("UNNotificationCategory", b"init"),
        ("UNNotificationRequest", b"init"),
        ("UNNotificationTrigger", b"init"),
        ("UNNotificationAttachment", b"init"),
        ("UNNotificationAction", b"init"),
        ("UNNotificationSound", b"init"),
        ("UNNotificationResponse", b"init"),
        ("UNNotificationSettings", b"init"),
    ):
        objc.registerUnavailableMethod(cls, sel)

    del sys.modules["UserNotifications._metadata"]


globals().pop("_setup")()
