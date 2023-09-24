"""
Python mapping for the AppKit framework.

This module does not contain docstrings for the wrapped code, check Apple's
documentation for details on how to use these functions and classes.
"""


def _setup():
    import sys

    import Foundation
    import objc
    from . import _metadata, _nsapp, _AppKit
    from ._inlines import _inline_list_

    dir_func, getattr_func = objc.createFrameworkDirAndGetattr(
        name="AppKit",
        frameworkIdentifier="com.apple.AppKit",
        frameworkPath=objc.pathForFramework(
            "/System/Library/Frameworks/AppKit.framework"
        ),
        globals_dict=globals(),
        inline_list=_inline_list_,
        parents=(
            _nsapp,
            _AppKit,
            Foundation,
        ),
        metadict=_metadata.__dict__,
    )

    globals()["__dir__"] = dir_func
    globals()["__getattr__"] = getattr_func

    del sys.modules["AppKit._metadata"]

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

    # Fix types for a number of character constants
    # XXX: Move this to metadata
    globals_dict = globals()
    for nm in [
        "NSEnterCharacter",
        "NSBackspaceCharacter",
        "NSTabCharacter",
        "NSNewlineCharacter",
        "NSFormFeedCharacter",
        "NSCarriageReturnCharacter",
        "NSBackTabCharacter",
        "NSDeleteCharacter",
        "NSLineSeparatorCharacter",
        "NSParagraphSeparatorCharacter",
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
            globals_dict[nm] = chr(__getattr__(nm))  # noqa: F821
        except AttributeError:
            pass


globals().pop("_setup")()


def NSDictionaryOfVariableBindings(*names):
    """
    Return a dictionary with the given names and there values.
    """
    import sys

    variables = sys._getframe(1).f_locals

    return {nm: variables[nm] for nm in names}
