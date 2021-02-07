# This file is generated by objective.metadata
#
# Last update: Sat Jun 27 18:35:27 2020
#
# flake8: noqa

import objc, sys

if sys.maxsize > 2 ** 32:

    def sel32or64(a, b):
        return b


else:

    def sel32or64(a, b):
        return a


misc = {}
constants = """$$"""
enums = """$AXCustomContentImportanceDefault@0$AXCustomContentImportanceHigh@1$"""
misc.update({})
functions = {"AXNameFromColor": (b"@^{CGColor=}",)}
r = objc.registerMetaDataForSelector
objc._updatingMetadata(True)
try:
    r(
        b"NSObject",
        b"accessibilityCustomContent",
        {"required": True, "retval": {"type": b"@"}},
    )
    r(
        b"NSObject",
        b"setAccessibilityCustomContent:",
        {"required": True, "retval": {"type": b"v"}, "arguments": {2: {"type": b"@"}}},
    )
finally:
    objc._updatingMetadata(False)
expressions = {}

# END OF FILE
