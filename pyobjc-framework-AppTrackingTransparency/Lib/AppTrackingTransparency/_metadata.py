# This file is generated by objective.metadata
#
# Last update: Tue Jun 11 10:05:03 2024
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
constants = """$AppTrackingTransparencyVersionNumber@d$AppTrackingTransparencyVersionString@*$"""
enums = """$ATTrackingManagerAuthorizationStatusAuthorized@3$ATTrackingManagerAuthorizationStatusDenied@2$ATTrackingManagerAuthorizationStatusNotDetermined@0$ATTrackingManagerAuthorizationStatusRestricted@1$"""
misc.update(
    {
        "ATTrackingManagerAuthorizationStatus": NewType(
            "ATTrackingManagerAuthorizationStatus", int
        )
    }
)
misc.update({})
misc.update({})
r = objc.registerMetaDataForSelector
objc._updatingMetadata(True)
try:
    r(
        b"ATTrackingManager",
        b"requestTrackingAuthorizationWithCompletionHandler:",
        {
            "arguments": {
                2: {
                    "callable": {
                        "retval": {"type": b"v"},
                        "arguments": {0: {"type": b"^v"}, 1: {"type": b"Q"}},
                    }
                }
            }
        },
    )
finally:
    objc._updatingMetadata(False)
expressions = {}

# END OF FILE
