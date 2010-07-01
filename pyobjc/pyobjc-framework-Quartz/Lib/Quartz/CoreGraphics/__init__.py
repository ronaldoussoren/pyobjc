'''
Python mapping for the CoreGraphics framework.

This module does not contain docstrings for the wrapped code, check Apple's
documentation for details on how to use these functions and classes. 
'''

import objc as _objc
from CoreFoundation import *

from Quartz.CoreGraphics._inlines import _inline_list_

__bundle__ = _objc.initFrameworkWrapper("CoreGraphics",
    frameworkIdentifier="com.apple.CoreGraphics",
    frameworkPath=_objc.pathForFramework(
        "/System/Library/Frameworks/ApplicationServices.framework/Frameworks/CoreGraphics.framework"),
    globals=globals(), 
    inlineTab=_inline_list_,
    frameworkResourceName="Quartz.CoreGraphics",
    scan_classes=False)

from Quartz.CoreGraphics._callbacks import *
from Quartz.CoreGraphics._doubleindirect import *
from Quartz.CoreGraphics._sortandmap import *
from Quartz.CoreGraphics._coregraphics import *

setCGPathElement(CGPathElement)
del setCGPathElement

# a #define
kCGEventFilterMaskPermitAllEvents = (
                kCGEventFilterMaskPermitLocalMouseEvents | 
                kCGEventFilterMaskPermitLocalKeyboardEvents | 
                kCGEventFilterMaskPermitSystemDefinedEvents)

def CGEventMaskBit(eventType):
    return (1 << eventType)


# Some pseudo-constants
kCGBaseWindowLevel = CGWindowLevelForKey(kCGBaseWindowLevelKey)
kCGMinimumWindowLevel = CGWindowLevelForKey(kCGMinimumWindowLevelKey)
kCGDesktopWindowLevel = CGWindowLevelForKey(kCGDesktopWindowLevelKey)
kCGDesktopIconWindowLevel = CGWindowLevelForKey(kCGDesktopIconWindowLevelKey)
kCGBackstopMenuLevel = CGWindowLevelForKey(kCGBackstopMenuLevelKey)
kCGNormalWindowLevel = CGWindowLevelForKey(kCGNormalWindowLevelKey)
kCGFloatingWindowLevel = CGWindowLevelForKey(kCGFloatingWindowLevelKey)
kCGTornOffMenuWindowLevel = CGWindowLevelForKey(kCGTornOffMenuWindowLevelKey)
kCGDockWindowLevel = CGWindowLevelForKey(kCGDockWindowLevelKey)
kCGMainMenuWindowLevel = CGWindowLevelForKey(kCGMainMenuWindowLevelKey)
kCGStatusWindowLevel = CGWindowLevelForKey(kCGStatusWindowLevelKey)
kCGModalPanelWindowLevel = CGWindowLevelForKey(kCGModalPanelWindowLevelKey)
kCGPopUpMenuWindowLevel = CGWindowLevelForKey(kCGPopUpMenuWindowLevelKey)
kCGDraggingWindowLevel = CGWindowLevelForKey(kCGDraggingWindowLevelKey)
kCGScreenSaverWindowLevel = CGWindowLevelForKey(kCGScreenSaverWindowLevelKey)
kCGCursorWindowLevel = CGWindowLevelForKey(kCGCursorWindowLevelKey)
kCGOverlayWindowLevel = CGWindowLevelForKey(kCGOverlayWindowLevelKey)
kCGHelpWindowLevel = CGWindowLevelForKey(kCGHelpWindowLevelKey)
kCGUtilityWindowLevel = CGWindowLevelForKey(kCGUtilityWindowLevelKey)
kCGAssistiveTechHighWindowLevel = CGWindowLevelForKey(kCGAssistiveTechHighWindowLevelKey)
kCGMaximumWindowLevel = CGWindowLevelForKey(kCGMaximumWindowLevelKey)

CGSetLocalEventsFilterDuringSupressionState = CGSetLocalEventsFilterDuringSuppressionState

# Some useful tools
from Quartz.CoreGraphics._contextmanager import *   
