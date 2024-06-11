# This file is generated by objective.metadata
#
# Last update: Tue Jun 11 10:11:13 2024
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
constants = """$FPUIErrorDomain$"""
enums = """$FPUIExtensionErrorCodeFailed@1$FPUIExtensionErrorCodeUserCancelled@0$"""
misc.update({"FPUIExtensionErrorCode": NewType("FPUIExtensionErrorCode", int)})
misc.update({})
misc.update({})
r = objc.registerMetaDataForSelector
objc._updatingMetadata(True)
try:
    r(
        b"FPUIActionExtensionContext",
        b"completeRequestReturningItems:completionHandler:",
        {
            "arguments": {
                3: {
                    "callable": {
                        "retval": {"type": b"v"},
                        "arguments": {0: {"type": b"^v"}, 1: {"type": b"Z"}},
                    }
                }
            }
        },
    )
finally:
    objc._updatingMetadata(False)
expressions = {}

# END OF FILE
