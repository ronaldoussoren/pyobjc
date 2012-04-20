'''
Python mapping for the AppKit framework.

This module does not contain docstrings for the wrapped code, check Apple's
documentation for details on how to use these functions and classes. 
'''
import sys
import objc
import Foundation

from AppKit import _metadata
from AppKit._inlines import _inline_list_

sys.modules['AppKit'] = mod = objc.ObjCLazyModule('AppKit',
        "com.apple.AppKit", objc.pathForFramework("/System/Library/Frameworks/AppKit.framework"),
        _metadata.__dict__, _inline_list_, {
            '__doc__': __doc__,
            'objc': objc,
            '__path__': __path__,
        }, (Foundation,))

# NSApp is a global variable that can be changed in ObjC,
# somewhat emulate that (it is *not* possible to assign to
# NSApp in Python)
from AppKit._nsapp import NSApp
mod.NSApp = NSApp

# Manually written wrappers:
import AppKit._AppKit
for nm in dir(AppKit._AppKit):
    setattr(mod, nm, getattr(AppKit._AppKit, nm))

# Fix types for a number of character constants
mod.NSEnterCharacter = unichr(mod.NSEnterCharacter)
mod.NSBackspaceCharacter = unichr(mod.NSBackspaceCharacter)
mod.NSTabCharacter = unichr(mod.NSTabCharacter)
mod.NSNewlineCharacter = unichr(mod.NSNewlineCharacter)
mod.NSFormFeedCharacter = unichr(mod.NSFormFeedCharacter)
mod.NSCarriageReturnCharacter = unichr(mod.NSCarriageReturnCharacter)
mod.NSBackTabCharacter = unichr(mod.NSBackTabCharacter)
mod.NSDeleteCharacter = unichr(mod.NSDeleteCharacter)
mod.NSLineSeparatorCharacter = unichr(mod.NSLineSeparatorCharacter)
mod.NSParagraphSeparatorCharacter = unichr(mod.NSParagraphSeparatorCharacter)

try:
    mod.NSImageNameApplicationIcon
except AttributeError:
    mod.NSImageNameApplicationIcon = u"NSApplicationIcon"

