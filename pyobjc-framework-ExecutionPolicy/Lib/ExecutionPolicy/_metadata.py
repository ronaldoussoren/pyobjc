# This file is generated by objective.metadata
#
# Last update: Tue Jun 11 10:10:39 2024
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
constants = """$EPErrorDomain$"""
enums = """$EPDeveloperToolStatusAuthorized@3$EPDeveloperToolStatusDenied@2$EPDeveloperToolStatusNotDetermined@0$EPDeveloperToolStatusRestricted@1$EPErrorGeneric@1$EPErrorNotADeveloperTool@2$"""
misc.update(
    {
        "EPError": NewType("EPError", int),
        "EPDeveloperToolStatus": NewType("EPDeveloperToolStatus", int),
    }
)
misc.update({})
misc.update({})
r = objc.registerMetaDataForSelector
objc._updatingMetadata(True)
try:
    r(
        b"EPDeveloperTool",
        b"requestDeveloperToolAccessWithCompletionHandler:",
        {
            "arguments": {
                2: {
                    "callable": {
                        "retval": {"type": b"v"},
                        "arguments": {0: {"type": b"^v"}, 1: {"type": b"Z"}},
                    }
                }
            }
        },
    )
    r(
        b"EPExecutionPolicy",
        b"addPolicyExceptionForURL:error:",
        {"retval": {"type": b"Z"}, "arguments": {3: {"type_modifier": b"o"}}},
    )
finally:
    objc._updatingMetadata(False)
expressions = {}

# END OF FILE
