"""
Python mapping for the CoreLocation framework.

This module does not contain docstrings for the wrapped code, check Apple's
documentation for details on how to use these functions and classes.
"""


def _setup():
    import sys

    import Foundation
    import objc
    from . import _metadata, _CoreLocation

    dir_func, getattr_func = objc.createFrameworkDirAndGetattr(
        name="CoreLocation",
        frameworkIdentifier="com.apple.corelocation",
        frameworkPath=objc.pathForFramework(
            "/System/Library/Frameworks/CoreLocation.framework"
        ),
        globals_dict=globals(),
        inline_list=None,
        parents=(
            _CoreLocation,
            Foundation,
        ),
        metadict=_metadata.__dict__,
    )

    globals()["__dir__"] = dir_func
    globals()["__getattr__"] = getattr_func

    for cls, sel in (
        ("CLMonitor", b"init"),
        ("CLMonitor", b"new"),
        ("CLMonitoringRecord", b"init"),
        ("CLMonitoringRecord", b"new"),
        ("CLMonitoringEvent", b"init"),
        ("CLMonitoringEvent", b"new"),
        ("CLBackgroundActivitySession", b"init"),
        ("CLBackgroundActivitySession", b"new"),
        ("CLCondition", b"init"),
        ("CLCondition", b"new"),
        ("CLLocationUpdater", b"init"),
        ("CLLocationUpdater", b"new"),
    ):
        objc.registerUnavailableMethod(cls, sel)

    del sys.modules["CoreLocation._metadata"]


globals().pop("_setup")()
