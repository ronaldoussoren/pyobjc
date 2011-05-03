'''
Python mapping for the AppKit framework.

This module does not contain docstrings for the wrapped code, check Apple's
documentation for details on how to use these functions and classes. 
'''

import objc as _objc
from Foundation import *

from AppKit._inlines import _inline_list_
__bundle__ = _objc.initFrameworkWrapper("AppKit",
    frameworkIdentifier="com.apple.AppKit",
    frameworkPath=_objc.pathForFramework(
        "/System/Library/Frameworks/AppKit.framework"),
    globals=globals(),
    inlineTab=_inline_list_)

# NSApp is a global variable that can be changed in ObjC,
# somewhat emulate that (it is *not* possible to assign to
# NSApp in Python)
from AppKit._nsapp import NSApp

# Manually written wrappers:
from AppKit._AppKit import *

# Fix types for a number of character constants
NSEnterCharacter = unichr(NSEnterCharacter)
NSBackspaceCharacter = unichr(NSBackspaceCharacter)
NSTabCharacter = unichr(NSTabCharacter)
NSNewlineCharacter = unichr(NSNewlineCharacter)
NSFormFeedCharacter = unichr(NSFormFeedCharacter)
NSCarriageReturnCharacter = unichr(NSCarriageReturnCharacter)
NSBackTabCharacter = unichr(NSBackTabCharacter)
NSDeleteCharacter = unichr(NSDeleteCharacter)
NSLineSeparatorCharacter = unichr(NSLineSeparatorCharacter)
NSParagraphSeparatorCharacter = unichr(NSParagraphSeparatorCharacter)

try:
    NSImageNameApplicationIcon
except NameError:
    NSImageNameApplicationIcon = u"NSApplicationIcon"
