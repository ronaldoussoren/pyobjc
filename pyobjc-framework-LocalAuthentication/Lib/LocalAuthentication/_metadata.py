# This file is generated by objective.metadata
#
# Last update: Thu Jul  7 22:05:00 2022
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
constants = """$LAErrorDomain$LATouchIDAuthenticationMaximumAllowableReuseDuration@d$"""
enums = """$LAAccessControlOperationCreateItem@0$LAAccessControlOperationCreateKey@2$LAAccessControlOperationUseItem@1$LAAccessControlOperationUseKeyDecrypt@4$LAAccessControlOperationUseKeyKeyExchange@5$LAAccessControlOperationUseKeySign@3$LABiometryNone@0$LABiometryTypeFaceID@2$LABiometryTypeNone@0$LABiometryTypeTouchID@1$LACredentialTypeApplicationPassword@0$LACredentialTypeSmartCardPIN@-3$LAErrorAppCancel@-9$LAErrorAuthenticationFailed@-1$LAErrorBiometryDisconnected@-13$LAErrorBiometryLockout@-8$LAErrorBiometryNotAvailable@-6$LAErrorBiometryNotEnrolled@-7$LAErrorBiometryNotPaired@-12$LAErrorInvalidContext@-10$LAErrorInvalidDimensions@-14$LAErrorNotInteractive@-1004$LAErrorPasscodeNotSet@-5$LAErrorSystemCancel@-4$LAErrorTouchIDLockout@-8$LAErrorTouchIDNotAvailable@-6$LAErrorTouchIDNotEnrolled@-7$LAErrorUserCancel@-2$LAErrorUserFallback@-3$LAErrorWatchNotAvailable@-11$LAPolicyDeviceOwnerAuthentication@2$LAPolicyDeviceOwnerAuthenticationWithBiometrics@1$LAPolicyDeviceOwnerAuthenticationWithBiometricsOrWatch@4$LAPolicyDeviceOwnerAuthenticationWithWatch@3$LAPolicyDeviceOwnerAuthenticationWithWristDetection@5$LARightStateAuthorized@2$LARightStateAuthorizing@1$LARightStateNotAuthorized@3$LARightStateUnknown@0$kLACredentialCTKPIN@-3$kLACredentialSmartCardPIN@-3$kLACredentialTypeApplicationPassword@0$kLACredentialTypePasscode@-1$kLACredentialTypePassphrase@-2$kLAErrorAppCancel@-9$kLAErrorAuthenticationFailed@-1$kLAErrorBiometryDisconnected@-13$kLAErrorBiometryNotPaired@-12$kLAErrorInvalidContext@-10$kLAErrorInvalidDimensions@-14$kLAErrorNotInteractive@-1004$kLAErrorPasscodeNotSet@-5$kLAErrorSystemCancel@-4$kLAErrorTouchIDLockout@-8$kLAErrorTouchIDNotAvailable@-6$kLAErrorTouchIDNotEnrolled@-7$kLAErrorUserCancel@-2$kLAErrorUserFallback@-3$kLAErrorWatchNotAvailable@-11$kLAOptionAuthenticationReason@2$kLAOptionUserFallback@1$kLAPolicyDeviceOwnerAuthentication@2$kLAPolicyDeviceOwnerAuthenticationWithBiometrics@1$kLAPolicyDeviceOwnerAuthenticationWithBiometricsOrWatch@4$kLAPolicyDeviceOwnerAuthenticationWithWatch@3$kLAPolicyDeviceOwnerAuthenticationWithWristDetection@5$"""
misc.update(
    {
        "LABiometryType": NewType("LABiometryType", int),
        "LAError": NewType("LAError", int),
        "LAAccessControlOperation": NewType("LAAccessControlOperation", int),
        "LACredentialType": NewType("LACredentialType", int),
        "LAPolicy": NewType("LAPolicy", int),
        "LARightState": NewType("LARightState", int),
    }
)
misc.update({})
misc.update({"kLAErrorDomain": "com.apple.LocalAuthentication"})
aliases = {
    "LACredentialTypeSmartCardPIN": "kLACredentialSmartCardPIN",
    "LAErrorBiometryLockout": "kLAErrorBiometryLockout",
    "LAErrorBiometryNotEnrolled": "kLAErrorBiometryNotEnrolled",
    "LABiometryNone": "LABiometryTypeNone",
    "kLAErrorBiometryNotEnrolled": "kLAErrorTouchIDNotEnrolled",
    "kLAErrorBiometryNotAvailable": "kLAErrorTouchIDNotAvailable",
    "LAErrorBiometryNotAvailable": "kLAErrorBiometryNotAvailable",
    "kLAErrorBiometryLockout": "kLAErrorTouchIDLockout",
}
r = objc.registerMetaDataForSelector
objc._updatingMetadata(True)
try:
    r(
        b"LAContext",
        b"canEvaluatePolicy:error:",
        {"retval": {"type": b"Z"}, "arguments": {3: {"type_modifier": b"o"}}},
    )
    r(
        b"LAContext",
        b"evaluateAccessControl:operation:localizedReason:reply:",
        {
            "arguments": {
                5: {
                    "callable": {
                        "retval": {"type": b"v"},
                        "arguments": {
                            0: {"type": b"^v"},
                            1: {"type": b"Z"},
                            2: {"type": b"@"},
                        },
                    }
                }
            }
        },
    )
    r(
        b"LAContext",
        b"evaluatePolicy:localizedReason:reply:",
        {
            "arguments": {
                4: {
                    "callable": {
                        "retval": {"type": b"v"},
                        "arguments": {
                            0: {"type": b"^v"},
                            1: {"type": b"Z"},
                            2: {"type": b"@"},
                        },
                    }
                }
            }
        },
    )
    r(
        b"LAContext",
        b"evaluatePolicy:operation:localizedReason:reply:",
        {
            "arguments": {
                5: {
                    "callable": {
                        "retval": {"type": b"v"},
                        "arguments": {
                            0: {"type": b"^v"},
                            1: {"type": b"Z"},
                            2: {"type": b"@"},
                        },
                    }
                }
            }
        },
    )
    r(b"LAContext", b"interactionNotAllowed", {"retval": {"type": "Z"}})
    r(b"LAContext", b"isCancelButtonVisible", {"retval": {"type": "Z"}})
    r(b"LAContext", b"isCredentialSet:", {"retval": {"type": "Z"}})
    r(b"LAContext", b"isFallbackButtonVisible", {"retval": {"type": "Z"}})
    r(b"LAContext", b"setCancelButtonVisible:", {"arguments": {2: {"type": "Z"}}})
    r(b"LAContext", b"setCredential:type:", {"retval": {"type": "Z"}})
    r(b"LAContext", b"setFallbackButtonVisible:", {"arguments": {2: {"type": "Z"}}})
    r(b"LAContext", b"setInteractionNotAllowed:", {"arguments": {2: {"type": "Z"}}})
    r(b"LAPrivateKey", b"canDecryptUsingSecKeyAlgorithm:", {"retval": {"type": b"Z"}})
    r(
        b"LAPrivateKey",
        b"canExchangeKeysUsingSecKeyAlgorithm:",
        {"retval": {"type": b"Z"}},
    )
    r(b"LAPrivateKey", b"canSignUsingSecKeyAlgorithm:", {"retval": {"type": b"Z"}})
    r(
        b"LAPrivateKey",
        b"decryptData:secKeyAlgorithm:completion:",
        {
            "arguments": {
                4: {
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
        b"LAPrivateKey",
        b"exchangeKeysWithPublicKey:secKeyAlgorithm:secKeyParameters:completion:",
        {
            "arguments": {
                5: {
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
        b"LAPrivateKey",
        b"signData:secKeyAlgorithm:completion:",
        {
            "arguments": {
                4: {
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
    r(b"LAPublicKey", b"canEncryptUsingSecKeyAlgorithm:", {"retval": {"type": b"Z"}})
    r(b"LAPublicKey", b"canVerifyUsingSecKeyAlgorithm:", {"retval": {"type": b"Z"}})
    r(
        b"LAPublicKey",
        b"encryptData:secKeyAlgorithm:completion:",
        {
            "arguments": {
                4: {
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
        b"LAPublicKey",
        b"exportBytesWithCompletion:",
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
        b"LAPublicKey",
        b"verifyData:signature:secKeyAlgorithm:completion:",
        {
            "arguments": {
                5: {
                    "callable": {
                        "retval": {"type": b"v"},
                        "arguments": {0: {"type": b"^v"}, 1: {"type": b"@"}},
                    }
                }
            }
        },
    )
    r(
        b"LARight",
        b"authorizeWithLocalizedReason:completion:",
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
        b"LARight",
        b"checkCanAuthorizeWithCompletion:",
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
        b"LARight",
        b"deauthorizeWithCompletion:",
        {
            "arguments": {
                2: {
                    "callable": {
                        "retval": {"type": b"v"},
                        "arguments": {0: {"type": b"^v"}},
                    }
                }
            }
        },
    )
    r(
        b"LARightStore",
        b"removeAllRightsWithCompletion:",
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
        b"LARightStore",
        b"removeRight:completion:",
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
        b"LARightStore",
        b"removeRightForIdentifier:completion:",
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
        b"LARightStore",
        b"rightForIdentifier:completion:",
        {
            "arguments": {
                3: {
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
        b"LARightStore",
        b"saveRight:identifier:completion:",
        {
            "arguments": {
                4: {
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
        b"LARightStore",
        b"saveRight:identifier:secret:completion:",
        {
            "arguments": {
                5: {
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
        b"LASecret",
        b"loadDataWithCompletion:",
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
finally:
    objc._updatingMetadata(False)
expressions = {}

# END OF FILE
