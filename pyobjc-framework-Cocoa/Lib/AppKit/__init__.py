"""
Python mapping for the AppKit framework.

This module does not contain docstrings for the wrapped code, check Apple's
documentation for details on how to use these functions and classes.
"""
import sys

# Manually written wrappers:
import Foundation
import objc
from AppKit import _metadata
from AppKit._inlines import _inline_list_


def _setup_conveniences():
    def fontdescriptor_get(self, key, default=None):
        value = self.objectForKey_(key)
        if value is None:
            return default
        return value

    def fontdescriptor_getitem(self, key, default=None):
        value = self.objectForKey_(key)
        if value is None:
            raise KeyError(key)
        return value

    objc.addConvenienceForClass(
        "NSFontDescriptor",
        (("__getitem__", fontdescriptor_getitem), ("get", fontdescriptor_get)),
    )


_setup_conveniences()


def NSDictionaryOfVariableBindings(*names):
    """
    Return a dictionary with the given names and there values.
    """
    import sys

    variables = sys._getframe(1).f_locals

    return {nm: variables[nm] for nm in names}


sys.modules["AppKit"] = mod = objc.ObjCLazyModule(
    "AppKit",
    "com.apple.AppKit",
    objc.pathForFramework("/System/Library/Frameworks/AppKit.framework"),
    _metadata.__dict__,
    _inline_list_,
    {
        "__doc__": __doc__,
        "objc": objc,
        "NSDictionaryOfVariableBindings": NSDictionaryOfVariableBindings,
        "__path__": __path__,
        "__loader__": globals().get("__loader__", None),
        "__file__": globals().get("__file__", None),
        "__spec__": globals().get("__spec__", None),
    },
    (Foundation,),
)

# NSApp is a global variable that can be changed in ObjC,
# somewhat emulate that (it is *not* possible to assign to
# NSApp in Python)
from AppKit._nsapp import NSApp  # isort:skip  # noqa: E402

mod.NSApp = NSApp

import AppKit._AppKit  # isort:skip  # noqa: E402

for nm in dir(AppKit._AppKit):
    setattr(mod, nm, getattr(AppKit._AppKit, nm))

# Fix types for a number of character constants
mod.NSEnterCharacter = chr(mod.NSEnterCharacter)
mod.NSBackspaceCharacter = chr(mod.NSBackspaceCharacter)
mod.NSTabCharacter = chr(mod.NSTabCharacter)
mod.NSNewlineCharacter = chr(mod.NSNewlineCharacter)
mod.NSFormFeedCharacter = chr(mod.NSFormFeedCharacter)
mod.NSCarriageReturnCharacter = chr(mod.NSCarriageReturnCharacter)
mod.NSBackTabCharacter = chr(mod.NSBackTabCharacter)
mod.NSDeleteCharacter = chr(mod.NSDeleteCharacter)
mod.NSLineSeparatorCharacter = chr(mod.NSLineSeparatorCharacter)
mod.NSParagraphSeparatorCharacter = chr(mod.NSParagraphSeparatorCharacter)


for nm in [
    "NSUpArrowFunctionKey",
    "NSDownArrowFunctionKey",
    "NSLeftArrowFunctionKey",
    "NSRightArrowFunctionKey",
    "NSF1FunctionKey",
    "NSF2FunctionKey",
    "NSF3FunctionKey",
    "NSF4FunctionKey",
    "NSF5FunctionKey",
    "NSF6FunctionKey",
    "NSF7FunctionKey",
    "NSF8FunctionKey",
    "NSF9FunctionKey",
    "NSF10FunctionKey",
    "NSF11FunctionKey",
    "NSF12FunctionKey",
    "NSF13FunctionKey",
    "NSF14FunctionKey",
    "NSF15FunctionKey",
    "NSF16FunctionKey",
    "NSF17FunctionKey",
    "NSF18FunctionKey",
    "NSF19FunctionKey",
    "NSF20FunctionKey",
    "NSF21FunctionKey",
    "NSF22FunctionKey",
    "NSF23FunctionKey",
    "NSF24FunctionKey",
    "NSF25FunctionKey",
    "NSF26FunctionKey",
    "NSF27FunctionKey",
    "NSF28FunctionKey",
    "NSF29FunctionKey",
    "NSF30FunctionKey",
    "NSF31FunctionKey",
    "NSF32FunctionKey",
    "NSF33FunctionKey",
    "NSF34FunctionKey",
    "NSF35FunctionKey",
    "NSInsertFunctionKey",
    "NSDeleteFunctionKey",
    "NSHomeFunctionKey",
    "NSBeginFunctionKey",
    "NSEndFunctionKey",
    "NSPageUpFunctionKey",
    "NSPageDownFunctionKey",
    "NSPrintScreenFunctionKey",
    "NSScrollLockFunctionKey",
    "NSPauseFunctionKey",
    "NSSysReqFunctionKey",
    "NSBreakFunctionKey",
    "NSResetFunctionKey",
    "NSStopFunctionKey",
    "NSMenuFunctionKey",
    "NSUserFunctionKey",
    "NSSystemFunctionKey",
    "NSPrintFunctionKey",
    "NSClearLineFunctionKey",
    "NSClearDisplayFunctionKey",
    "NSInsertLineFunctionKey",
    "NSDeleteLineFunctionKey",
    "NSInsertCharFunctionKey",
    "NSDeleteCharFunctionKey",
    "NSPrevFunctionKey",
    "NSNextFunctionKey",
    "NSSelectFunctionKey",
    "NSExecuteFunctionKey",
    "NSUndoFunctionKey",
    "NSRedoFunctionKey",
    "NSFindFunctionKey",
    "NSHelpFunctionKey",
    "NSModeSwitchFunctionKey",
]:
    try:
        setattr(mod, nm, chr(getattr(mod, nm)))
    except AttributeError:
        pass

try:
    mod.NSImageNameApplicationIcon
except AttributeError:
    mod.NSImageNameApplicationIcon = "NSApplicationIcon"

if objc.arch == "arm64":
    # XXX: Temporary adjustment until the metadata
    #      is updated
    mod.NSImageResizingModeStretch = 1
    mod.NSImageResizingModeTile = 0

    mod.NSTextAlignmentCenter = 1
    mod.NSTextAlignmentRight = 2

mod.NSRightTextAlignment = mod.NSTextAlignmentRight
mod.NSCenterTextAlignment = mod.NSTextAlignmentCenter


del sys.modules["AppKit._metadata"]
