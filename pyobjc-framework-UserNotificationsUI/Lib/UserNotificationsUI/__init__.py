"""
Python mapping for the UserNotificationsUI framework.

This module does not contain docstrings for the wrapped code, check Apple's
documentation for details on how to use these functions and classes.
"""

import sys

import Cocoa
import UserNotifications
import objc
from UserNotificationsUI import _metadata

sys.modules["UserNotificationsUI"] = mod = objc.ObjCLazyModule(
    "UserNotificationsUI",
    "com.apple.UserNotificationsUI",
    objc.pathForFramework("/System/Library/Frameworks/UserNotificationsUI.framework"),
    _metadata.__dict__,
    None,
    {
        "__doc__": __doc__,
        "objc": objc,
        "__path__": __path__,
        "__loader__": globals().get("__loader__", None),
    },
    (UserNotifications, Cocoa),
)


del sys.modules["UserNotificationsUI._metadata"]
