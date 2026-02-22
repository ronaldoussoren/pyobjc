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
            "/System/Library/Frameworks/HomeKit.framework"
        ),
        globals_dict=globals(),
        inline_list=None,
        parents=(Foundation,),
        metadict=_metadata.__dict__,
    )

    globals()["__dir__"] = dir_func
    globals()["__getattr__"] = getattr_func

    for cls, sel in (
        ("HMAccessControl", "init"),
        ("HMAccessControl", "new"),
        ("HMAccessory", "init"),
        ("HMAccessory", "new"),
        ("HMAccessoryCategory", "init"),
        ("HMAccessoryCategory", "new"),
        ("HMAccessoryProfile", "init"),
        ("HMAccessoryProfile", "new"),
        ("HMAccessoryOwnershipToken", "init"),
        ("HMAccessoryOwnershipToken", "new"),
        ("HMAccessorySetupPayload", "init"),
        ("HMAccessorySetupPayload", "new"),
        ("HMAccessorySetupResult", "init"),
        ("HMAccessorySetupResult", "new"),
        ("HMAction", "init"),
        ("HMAction", "new"),
        ("HMActionSet", "init"),
        ("HMActionSet", "new"),
        ("HMAddAccessoryRequest", "init"),
        ("HMAddAccessoryRequest", "new"),
        ("HMCalendarEvent", "init"),
        ("HMCalendarEvent", "new"),
        ("HMMutableCalendarEvent", "init"),
        ("HMMutableCalendarEvent", "new"),
        ("HMCameraAudioControl", "init"),
        ("HMCameraAudioControl", "new"),
        ("HMCameraControl", "init"),
        ("HMCameraControl", "new"),
        ("HMCameraProfile", "init"),
        ("HMCameraProfile", "new"),
        ("HMCameraSettingsControl", "init"),
        ("HMCameraSettingsControl", "new"),
        ("HMCameraSnapshot", "init"),
        ("HMCameraSnapshot", "new"),
        ("HMCameraSnapshotControl", "init"),
        ("HMCameraSnapshotControl", "new"),
        ("HMCameraSource", "init"),
        ("HMCameraSource", "new"),
        ("HMCharacteristic", "init"),
        ("HMCharacteristic", "new"),
        ("HMCharacteristicEvent", "init"),
        ("HMCharacteristicEvent", "new"),
        ("HMMutableCharacteristicEvent", "init"),
        ("HMMutableCharacteristicEvent", "new"),
        ("HMCharacteristicThresholdRangeEvent", "init"),
        ("HMCharacteristicThresholdRangeEvent", "new"),
        ("HMMutableCharacteristicThresholdRangeEvent", "init"),
        ("HMMutableCharacteristicThresholdRangeEvent", "new"),
        ("HMCharacteristicWriteAction", "init"),
        ("HMCharacteristicWriteAction", "new"),
        ("HMDurationEvent", "init"),
        ("HMDurationEvent", "new"),
        ("HMMutableDurationEvent", "init"),
        ("HMMutableDurationEvent", "new"),
        ("HMEvent", "init"),
        ("HMEvent", "new"),
        ("HMEventTrigger", "init"),
        ("HMEventTrigger", "new"),
        ("HMHome", "init"),
        ("HMHome", "new"),
        ("HMHomeAccessControl", "init"),
        ("HMHomeAccessControl", "new"),
        ("HMLocationEvent", "init"),
        ("HMLocationEvent", "new"),
        ("HMMutableLocationEvent", "init"),
        ("HMMutableLocationEvent", "new"),
        ("HMNetworkConfigurationProfile", "init"),
        ("HMNetworkConfigurationProfile", "new"),
        ("HMNumberRange", "init"),
        ("HMNumberRange", "new"),
        ("HMPresenceEvent", "init"),
        ("HMPresenceEvent", "new"),
        ("HMMutablePresenceEven", "init"),
        ("HMMutablePresenceEven", "new"),
        ("HMRoom", "init"),
        ("HMRoom", "new"),
        ("HMService", "init"),
        ("HMService", "new"),
        ("HMServiceGroup", "init"),
        ("HMServiceGroup", "new"),
        ("HMSignificantTimeEvent", "init"),
        ("HMSignificantTimeEvent", "new"),
        ("HMMutableSignificantTimeEvent", "init"),
        ("HMMutableSignificantTimeEvent", "new"),
        ("HMTimerTrigger", "init"),
        ("HMTimerTrigger", "new"),
        ("HMTrigger", "init"),
        ("HMTrigger", "new"),
        ("HMUser", "init"),
        ("HMUser", "new"),
        ("HMZone", "init"),
        ("HMZone", "new"),
    ):
        objc.registerUnavailableMethod(cls, sel)

    del sys.modules["HomeKit._metadata"]


globals().pop("_setup")()
