"""
Python mapping for the HomeKit framework.

This module does not contain docstrings for the wrapped code, check Apple's
documentation for details on how to use these functions and classes.
"""


def _setup():
    import sys

    import objc
    import Foundation
    from . import _metadata

    dir_func, getattr_func = objc.createFrameworkDirAndGetattr(
        name="HomeKit",
        frameworkIdentifier="com.apple.HomeKit",
        frameworkPath=objc.pathForFramework(
            # "/System/Library/Frameworks/HomeKit.framework"
            "/System/Library/PrivateFrameworks/HomeKit.framework"
        ),
        globals_dict=globals(),
        inline_list=None,
        parents=(Foundation,),
        metadict=_metadata.__dict__,
    )

    globals()["__dir__"] = dir_func
    globals()["__getattr__"] = getattr_func

    for cls, sel in (
        ("HMAccessControl", b"init"),
        ("HMAccessControl", b"new"),
        ("HMAccessory", b"init"),
        ("HMAccessory", b"new"),
        ("HMAccessoryCategory", b"init"),
        ("HMAccessoryCategory", b"new"),
        ("HMAccessoryProfile", b"init"),
        ("HMAccessoryProfile", b"new"),
        ("HMAccessoryOwnershipToken", b"init"),
        ("HMAccessoryOwnershipToken", b"new"),
        ("HMAccessorySetupPayload", b"init"),
        ("HMAccessorySetupPayload", b"new"),
        ("HMAccessorySetupResult", b"init"),
        ("HMAccessorySetupResult", b"new"),
        ("HMAction", b"init"),
        ("HMAction", b"new"),
        ("HMActionSet", b"init"),
        ("HMActionSet", b"new"),
        ("HMAddAccessoryRequest", b"init"),
        ("HMAddAccessoryRequest", b"new"),
        ("HMCalendarEvent", b"init"),
        ("HMCalendarEvent", b"new"),
        ("HMMutableCalendarEvent", b"init"),
        ("HMMutableCalendarEvent", b"new"),
        ("HMCameraAudioControl", b"init"),
        ("HMCameraAudioControl", b"new"),
        ("HMCameraControl", b"init"),
        ("HMCameraControl", b"new"),
        ("HMCameraProfile", b"init"),
        ("HMCameraProfile", b"new"),
        ("HMCameraSettingsControl", b"init"),
        ("HMCameraSettingsControl", b"new"),
        ("HMCameraSnapshot", b"init"),
        ("HMCameraSnapshot", b"new"),
        ("HMCameraSnapshotControl", b"init"),
        ("HMCameraSnapshotControl", b"new"),
        ("HMCameraSource", b"init"),
        ("HMCameraSource", b"new"),
        ("HMCharacteristic", b"init"),
        ("HMCharacteristic", b"new"),
        ("HMCharacteristicEvent", b"init"),
        ("HMCharacteristicEvent", b"new"),
        ("HMMutableCharacteristicEvent", b"init"),
        ("HMMutableCharacteristicEvent", b"new"),
        ("HMCharacteristicThresholdRangeEvent", b"init"),
        ("HMCharacteristicThresholdRangeEvent", b"new"),
        ("HMMutableCharacteristicThresholdRangeEvent", b"init"),
        ("HMMutableCharacteristicThresholdRangeEvent", b"new"),
        ("HMCharacteristicWriteAction", b"init"),
        ("HMCharacteristicWriteAction", b"new"),
        ("HMDurationEvent", b"init"),
        ("HMDurationEvent", b"new"),
        ("HMMutableDurationEvent", b"init"),
        ("HMMutableDurationEvent", b"new"),
        ("HMEvent", b"init"),
        ("HMEvent", b"new"),
        ("HMEventTrigger", b"init"),
        ("HMEventTrigger", b"new"),
        ("HMHome", b"init"),
        ("HMHome", b"new"),
        ("HMHomeAccessControl", b"init"),
        ("HMHomeAccessControl", b"new"),
        ("HMLocationEvent", b"init"),
        ("HMLocationEvent", b"new"),
        ("HMMutableLocationEvent", b"init"),
        ("HMMutableLocationEvent", b"new"),
        ("HMNetworkConfigurationProfile", b"init"),
        ("HMNetworkConfigurationProfile", b"new"),
        ("HMNumberRange", b"init"),
        ("HMNumberRange", b"new"),
        ("HMPresenceEvent", b"init"),
        ("HMPresenceEvent", b"new"),
        ("HMMutablePresenceEven", b"init"),
        ("HMMutablePresenceEven", b"new"),
        ("HMRoom", b"init"),
        ("HMRoom", b"new"),
        ("HMService", b"init"),
        ("HMService", b"new"),
        ("HMServiceGroup", b"init"),
        ("HMServiceGroup", b"new"),
        ("HMSignificantTimeEvent", b"init"),
        ("HMSignificantTimeEvent", b"new"),
        ("HMMutableSignificantTimeEvent", b"init"),
        ("HMMutableSignificantTimeEvent", b"new"),
        ("HMTimerTrigger", b"init"),
        ("HMTimerTrigger", b"new"),
        ("HMTrigger", b"init"),
        ("HMTrigger", b"new"),
        ("HMUser", b"init"),
        ("HMUser", b"new"),
        ("HMZone", b"init"),
        ("HMZone", b"new"),
    ):
        objc.registerUnavailableMethod(cls, sel)

    del sys.modules["HomeKit._metadata"]


globals().pop("_setup")()
