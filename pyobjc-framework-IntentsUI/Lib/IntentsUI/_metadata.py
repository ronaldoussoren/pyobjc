# This file is generated by objective.metadata
#
# Last update: Tue Jun 11 10:13:15 2024
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
constants = """$IntentsUIVersionNumber@d$"""
enums = """$INUIAddVoiceShortcutButtonStyleAutomatic@4$INUIAddVoiceShortcutButtonStyleAutomaticOutline@5$INUIAddVoiceShortcutButtonStyleBlack@2$INUIAddVoiceShortcutButtonStyleBlackOutline@3$INUIAddVoiceShortcutButtonStyleWhite@0$INUIAddVoiceShortcutButtonStyleWhiteOutline@1$"""
misc.update(
    {"INUIAddVoiceShortcutButtonStyle": NewType("INUIAddVoiceShortcutButtonStyle", int)}
)
misc.update({})
misc.update({})
r = objc.registerMetaDataForSelector
objc._updatingMetadata(True)
try:
    r(
        b"NSObject",
        b"addVoiceShortcutViewController:didFinishWithVoiceShortcut:error:",
        {
            "required": True,
            "retval": {"type": b"v"},
            "arguments": {2: {"type": b"@"}, 3: {"type": b"@"}, 4: {"type": b"@"}},
        },
    )
    r(
        b"NSObject",
        b"addVoiceShortcutViewControllerDidCancel:",
        {"required": True, "retval": {"type": b"v"}, "arguments": {2: {"type": b"@"}}},
    )
    r(
        b"NSObject",
        b"editVoiceShortcutViewController:didDeleteVoiceShortcutWithIdentifier:",
        {
            "required": True,
            "retval": {"type": b"v"},
            "arguments": {2: {"type": b"@"}, 3: {"type": b"@"}},
        },
    )
    r(
        b"NSObject",
        b"editVoiceShortcutViewController:didUpdateVoiceShortcut:error:",
        {
            "required": True,
            "retval": {"type": b"v"},
            "arguments": {2: {"type": b"@"}, 3: {"type": b"@"}, 4: {"type": b"@"}},
        },
    )
    r(
        b"NSObject",
        b"editVoiceShortcutViewControllerDidCancel:",
        {"required": True, "retval": {"type": b"v"}, "arguments": {2: {"type": b"@"}}},
    )
    r(
        b"NSObject",
        b"presentAddVoiceShortcutViewController:forAddVoiceShortcutButton:",
        {
            "required": True,
            "retval": {"type": b"v"},
            "arguments": {2: {"type": b"@"}, 3: {"type": b"@"}},
        },
    )
    r(
        b"NSObject",
        b"presentEditVoiceShortcutViewController:forAddVoiceShortcutButton:",
        {
            "required": True,
            "retval": {"type": b"v"},
            "arguments": {2: {"type": b"@"}, 3: {"type": b"@"}},
        },
    )
finally:
    objc._updatingMetadata(False)

objc.registerNewKeywordsFromSelector("INUIAddVoiceShortcutButton", b"initWithFrame:")
objc.registerNewKeywordsFromSelector("INUIAddVoiceShortcutButton", b"initWithStyle:")
objc.registerNewKeywordsFromSelector(
    "INUIAddVoiceShortcutViewController", b"initWithNibName:bundle:"
)
objc.registerNewKeywordsFromSelector(
    "INUIAddVoiceShortcutViewController", b"initWithShortcut:"
)
objc.registerNewKeywordsFromSelector(
    "INUIEditVoiceShortcutViewController", b"initWithNibName:bundle:"
)
objc.registerNewKeywordsFromSelector(
    "INUIEditVoiceShortcutViewController", b"initWithVoiceShortcut:"
)
expressions = {}

# END OF FILE
