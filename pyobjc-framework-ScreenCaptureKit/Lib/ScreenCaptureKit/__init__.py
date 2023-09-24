"""
Python mapping for the ScreenCaptureKit framework.

This module does not contain docstrings for the wrapped code, check Apple's
documentation for details on how to use these functions and classes.
"""


def _setup():
    import sys

    import Foundation
    import objc
    from . import _metadata, _ScreenCaptureKit

    dir_func, getattr_func = objc.createFrameworkDirAndGetattr(
        name="ScreenCaptureKit",
        frameworkIdentifier="com.apple.ScreenCaptureKit",
        frameworkPath=objc.pathForFramework(
            "/System/Library/Frameworks/ScreenCaptureKit.framework"
        ),
        globals_dict=globals(),
        inline_list=None,
        parents=(
            _ScreenCaptureKit,
            Foundation,
        ),
        metadict=_metadata.__dict__,
    )

    globals()["__dir__"] = dir_func
    globals()["__getattr__"] = getattr_func

    del sys.modules["ScreenCaptureKit._metadata"]


globals().pop("_setup")()

RP_REPORTING_CLIENT_NAME = "ReplayKit"
RP_REPORTING_SERVICE_NAME_SYSTEM_RECORDING = "SystemRecording"
RP_REPORTING_SERVICE_NAME_SYSTEM_BROADCAST = "SystemBroadcast"
RP_REPORTING_SERVICE_NAME_IN_APP_RECORDING = "InAppRecording"
RP_REPORTING_SERVICE_NAME_IN_APP_BROADCAST = "InAppBroadcast"
RP_REPORTING_SERVICE_NAME_IN_APP_CAPTURE = "InAppCapture"
RP_REPORTING_SERVICE_NAME_IN_APP_CLIP = "InAppClip"
RP_REPORTING_SERVICE_NAME_SCREEN_CAPTURE_KIT = "SCKCapture"
