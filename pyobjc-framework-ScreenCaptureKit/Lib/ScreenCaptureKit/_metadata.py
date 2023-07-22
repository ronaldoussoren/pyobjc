# This file is generated by objective.metadata
#
# Last update: Fri Jul  7 17:02:21 2023
#
# flake8: noqa

import objc, sys
from typing import NewType

if sys.maxsize > 2**32:

    def sel32or64(a, b):
        return b

else:

    def sel32or64(a, b):
        return a


if objc.arch == "arm64":

    def selAorI(a, b):
        return a

else:

    def selAorI(a, b):
        return b


misc = {}
constants = """$SCStreamErrorDomain$SCStreamFrameInfoContentRect$SCStreamFrameInfoContentScale$SCStreamFrameInfoDirtyRects$SCStreamFrameInfoDisplayTime$SCStreamFrameInfoScaleFactor$SCStreamFrameInfoScreenRect$SCStreamFrameInfoStatus$"""
enums = """$RP_REPORTING_END_REASON_SUMMARY_EVENT@2$RP_REPORTING_SCREENSHOT_EVENT@3$RP_REPORTING_SUMMARY_EVENT@1$SCCaptureResolutionAutomatic@0$SCCaptureResolutionBest@1$SCCaptureResolutionNominal@2$SCContentSharingPickerModeMultipleApplications@8$SCContentSharingPickerModeMultipleWindows@2$SCContentSharingPickerModeSingleApplication@4$SCContentSharingPickerModeSingleDisplay@16$SCContentSharingPickerModeSingleWindow@1$SCFrameStatusBlank@2$SCFrameStatusComplete@0$SCFrameStatusIdle@1$SCFrameStatusStarted@4$SCFrameStatusStopped@5$SCFrameStatusSuspended@3$SCShareableContentStyleApplication@3$SCShareableContentStyleDisplay@2$SCShareableContentStyleNone@0$SCShareableContentStyleWindow@1$SCStreamErrorAttemptToConfigState@-3810$SCStreamErrorAttemptToStartStreamState@-3807$SCStreamErrorAttemptToStopStreamState@-3808$SCStreamErrorAttemptToUpdateFilterState@-3809$SCStreamErrorFailedApplicationConnectionInterrupted@-3805$SCStreamErrorFailedApplicationConnectionInvalid@-3804$SCStreamErrorFailedNoMatchingApplicationContext@-3806$SCStreamErrorFailedToStart@-3802$SCStreamErrorFailedToStartAudioCapture@-3818$SCStreamErrorFailedToStopAudioCapture@-3819$SCStreamErrorInternalError@-3811$SCStreamErrorInvalidParameter@-3812$SCStreamErrorMissingEntitlements@-3803$SCStreamErrorNoCaptureSource@-3815$SCStreamErrorNoDisplayList@-3814$SCStreamErrorNoWindowList@-3813$SCStreamErrorRemovingStream@-3816$SCStreamErrorUserDeclined@-3801$SCStreamErrorUserStopped@-3817$SCStreamOutputTypeAudio@1$SCStreamOutputTypeScreen@0$SCStreamTypeDisplay@1$SCStreamTypeWindow@0$"""
misc.update(
    {
        "SCCaptureResolutionType": NewType("SCCaptureResolutionType", int),
        "SCContentSharingPickerMode": NewType("SCContentSharingPickerMode", int),
        "SCStreamErrorCode": NewType("SCStreamErrorCode", int),
        "SCStreamType": NewType("SCStreamType", int),
        "SCStreamOutputType": NewType("SCStreamOutputType", int),
        "SCShareableContentStyle": NewType("SCShareableContentStyle", int),
        "SCFrameStatus": NewType("SCFrameStatus", int),
    }
)
misc.update({"SCStreamFrameInfo": NewType("SCStreamFrameInfo", str)})
misc.update({})
r = objc.registerMetaDataForSelector
objc._updatingMetadata(True)
try:
    r(
        b"NSObject",
        b"contentSharingPicker:didCancelForStream:",
        {
            "required": True,
            "retval": {"type": b"v"},
            "arguments": {2: {"type": b"@"}, 3: {"type": b"@"}},
        },
    )
    r(
        b"NSObject",
        b"contentSharingPicker:didUpdateWithFilter:forStream:",
        {
            "required": True,
            "retval": {"type": b"v"},
            "arguments": {2: {"type": b"@"}, 3: {"type": b"@"}, 4: {"type": b"@"}},
        },
    )
    r(
        b"NSObject",
        b"contentSharingPickerStartDidFailWithError:",
        {"required": True, "retval": {"type": b"v"}, "arguments": {2: {"type": b"@"}}},
    )
    r(
        b"NSObject",
        b"outputVideoEffectDidStartForStream:",
        {"required": False, "retval": {"type": b"v"}, "arguments": {2: {"type": b"@"}}},
    )
    r(
        b"NSObject",
        b"outputVideoEffectDidStopForStream:",
        {"required": False, "retval": {"type": b"v"}, "arguments": {2: {"type": b"@"}}},
    )
    r(
        b"NSObject",
        b"stream:didOutputSampleBuffer:ofType:",
        {
            "required": False,
            "retval": {"type": b"v"},
            "arguments": {
                2: {"type": b"@"},
                3: {"type": b"^{opaqueCMSampleBuffer=}"},
                4: {"type": b"q"},
            },
        },
    )
    r(
        b"NSObject",
        b"stream:didStopWithError:",
        {
            "required": False,
            "retval": {"type": b"v"},
            "arguments": {2: {"type": b"@"}, 3: {"type": b"@"}},
        },
    )
    r(b"SCContentSharingPicker", b"isActive", {"retval": {"type": b"Z"}})
    r(b"SCContentSharingPicker", b"setActive:", {"arguments": {2: {"type": b"Z"}}})
    r(
        b"SCContentSharingPickerConfiguration",
        b"allowsChangingSelectedContent",
        {"retval": {"type": b"Z"}},
    )
    r(
        b"SCContentSharingPickerConfiguration",
        b"setAllowsChangingSelectedContent:",
        {"arguments": {2: {"type": b"Z"}}},
    )
    r(
        b"SCScreenshotManager",
        b"captureImageWithFilter:configuration:completionHandler:",
        {
            "arguments": {
                4: {
                    "callable": {
                        "retval": {"type": b"v"},
                        "arguments": {
                            0: {"type": b"^v"},
                            1: {"type": b"^{CGImage=}"},
                            2: {"type": b"@"},
                        },
                    }
                }
            }
        },
    )
    r(
        b"SCScreenshotManager",
        b"captureSampleBufferWithFilter:configuration:completionHandler:",
        {
            "arguments": {
                4: {
                    "callable": {
                        "retval": {"type": b"v"},
                        "arguments": {
                            0: {"type": b"^v"},
                            1: {"type": b"^{opaqueCMSampleBuffer=}"},
                            2: {"type": b"@"},
                        },
                    }
                }
            }
        },
    )
    r(
        b"SCShareableContent",
        b"getShareableContentExcludingDesktopWindows:onScreenWindowsOnly:completionHandler:",
        {
            "arguments": {
                2: {"type": b"Z"},
                3: {"type": b"Z"},
                4: {
                    "callable": {
                        "retval": {"type": b"v"},
                        "arguments": {
                            0: {"type": b"^v"},
                            1: {"type": b"@"},
                            2: {"type": b"@"},
                        },
                    }
                },
            }
        },
    )
    r(
        b"SCShareableContent",
        b"getShareableContentExcludingDesktopWindows:onScreenWindowsOnlyAboveWindow:completionHandler:",
        {
            "arguments": {
                2: {"type": b"Z"},
                4: {
                    "callable": {
                        "retval": {"type": b"v"},
                        "arguments": {
                            0: {"type": b"^v"},
                            1: {"type": b"@"},
                            2: {"type": b"@"},
                        },
                    }
                },
            }
        },
    )
    r(
        b"SCShareableContent",
        b"getShareableContentExcludingDesktopWindows:onScreenWindowsOnlyBelowWindow:completionHandler:",
        {
            "arguments": {
                2: {"type": b"Z"},
                4: {
                    "callable": {
                        "retval": {"type": b"v"},
                        "arguments": {
                            0: {"type": b"^v"},
                            1: {"type": b"@"},
                            2: {"type": b"@"},
                        },
                    }
                },
            }
        },
    )
    r(
        b"SCShareableContent",
        b"getShareableContentWithCompletionHandler:",
        {
            "arguments": {
                2: {
                    "callable": {
                        "retval": {"type": b"v"},
                        "arguments": {
                            0: {"type": b"^v"},
                            1: {"type": b"@"},
                            2: {"type": b"@"},
                        },
                    }
                }
            }
        },
    )
    r(
        b"SCStream",
        b"addStreamOutput:type:sampleHandlerQueue:error:",
        {"retval": {"type": b"Z"}, "arguments": {5: {"type_modifier": b"o"}}},
    )
    r(
        b"SCStream",
        b"removeStreamOutput:type:error:",
        {"retval": {"type": b"Z"}, "arguments": {4: {"type_modifier": b"o"}}},
    )
    r(
        b"SCStream",
        b"startCaptureWithCompletionHandler:",
        {
            "arguments": {
                2: {
                    "callable": {
                        "retval": {"type": b"v"},
                        "arguments": {0: {"type": b"^v"}, 1: {"type": b"@"}},
                    }
                }
            }
        },
    )
    r(
        b"SCStream",
        b"stopCaptureWithCompletionHandler:",
        {
            "arguments": {
                2: {
                    "callable": {
                        "retval": {"type": b"v"},
                        "arguments": {0: {"type": b"^v"}, 1: {"type": b"@"}},
                    }
                }
            }
        },
    )
    r(
        b"SCStream",
        b"updateConfiguration:completionHandler:",
        {
            "arguments": {
                3: {
                    "callable": {
                        "retval": {"type": b"v"},
                        "arguments": {0: {"type": b"^v"}, 1: {"type": b"@"}},
                    }
                }
            }
        },
    )
    r(
        b"SCStream",
        b"updateContentFilter:completionHandler:",
        {
            "arguments": {
                3: {
                    "callable": {
                        "retval": {"type": b"v"},
                        "arguments": {0: {"type": b"^v"}, 1: {"type": b"@"}},
                    }
                }
            }
        },
    )
    r(b"SCStreamConfiguration", b"capturesAudio", {"retval": {"type": b"Z"}})
    r(b"SCStreamConfiguration", b"capturesShadowsOnly", {"retval": {"type": b"Z"}})
    r(
        b"SCStreamConfiguration",
        b"excludesCurrentProcessAudio",
        {"retval": {"type": b"Z"}},
    )
    r(b"SCStreamConfiguration", b"ignoreGlobalClipDisplay", {"retval": {"type": b"Z"}})
    r(
        b"SCStreamConfiguration",
        b"ignoreGlobalClipSingleWindow",
        {"retval": {"type": b"Z"}},
    )
    r(b"SCStreamConfiguration", b"ignoreShadowsDisplay", {"retval": {"type": b"Z"}})
    r(
        b"SCStreamConfiguration",
        b"ignoreShadowsSingleWindow",
        {"retval": {"type": b"Z"}},
    )
    r(
        b"SCStreamConfiguration",
        b"minimumFrameInterval",
        {"retval": {"type": b"{_CMTime=qiIq}"}},
    )
    r(b"SCStreamConfiguration", b"preservesAspectRatio", {"retval": {"type": b"Z"}})
    r(b"SCStreamConfiguration", b"scalesToFit", {"retval": {"type": b"Z"}})
    r(
        b"SCStreamConfiguration",
        b"setCapturesAudio:",
        {"arguments": {2: {"type": b"Z"}}},
    )
    r(
        b"SCStreamConfiguration",
        b"setCapturesShadowsOnly:",
        {"arguments": {2: {"type": b"Z"}}},
    )
    r(
        b"SCStreamConfiguration",
        b"setExcludesCurrentProcessAudio:",
        {"arguments": {2: {"type": b"Z"}}},
    )
    r(
        b"SCStreamConfiguration",
        b"setIgnoreGlobalClipDisplay:",
        {"arguments": {2: {"type": b"Z"}}},
    )
    r(
        b"SCStreamConfiguration",
        b"setIgnoreGlobalClipSingleWindow:",
        {"arguments": {2: {"type": b"Z"}}},
    )
    r(
        b"SCStreamConfiguration",
        b"setIgnoreShadowsDisplay:",
        {"arguments": {2: {"type": b"Z"}}},
    )
    r(
        b"SCStreamConfiguration",
        b"setIgnoreShadowsSingleWindow:",
        {"arguments": {2: {"type": b"Z"}}},
    )
    r(
        b"SCStreamConfiguration",
        b"setMinimumFrameInterval:",
        {"arguments": {2: {"type": b"{_CMTime=qiIq}"}}},
    )
    r(
        b"SCStreamConfiguration",
        b"setPreservesAspectRatio:",
        {"arguments": {2: {"type": b"Z"}}},
    )
    r(b"SCStreamConfiguration", b"setScalesToFit:", {"arguments": {2: {"type": b"Z"}}})
    r(
        b"SCStreamConfiguration",
        b"setShouldBeOpaque:",
        {"arguments": {2: {"type": b"Z"}}},
    )
    r(b"SCStreamConfiguration", b"setShowsCursor:", {"arguments": {2: {"type": b"Z"}}})
    r(b"SCStreamConfiguration", b"shouldBeOpaque", {"retval": {"type": b"Z"}})
    r(b"SCStreamConfiguration", b"showsCursor", {"retval": {"type": b"Z"}})
    r(b"SCWindow", b"isActive", {"retval": {"type": b"Z"}})
    r(b"SCWindow", b"isOnScreen", {"retval": {"type": b"Z"}})
finally:
    objc._updatingMetadata(False)
expressions = {}

# END OF FILE
