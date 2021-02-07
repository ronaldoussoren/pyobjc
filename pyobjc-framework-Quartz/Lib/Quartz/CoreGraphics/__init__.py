"""
Python mapping for the CoreGraphics framework.

This module does not contain docstrings for the wrapped code, check Apple's
documentation for details on how to use these functions and classes.
"""
import sys

import CoreFoundation
import objc
import os
from Quartz.CoreGraphics import _metadata
from Quartz.CoreGraphics._inlines import _inline_list_

if os.path.exists("/System/Library/Frameworks/CoreGraphics.framework"):
    framework_path = "/System/Library/Frameworks/CoreGraphics.framework"
else:
    framework_path = "/System/Library/Frameworks/ApplicationServices.framework/Frameworks/CoreGraphics.framework"  # noqa: B950

sys.modules["Quartz.CoreGraphics"] = mod = objc.ObjCLazyModule(
    "Quartz.CoreGraphics",
    "com.apple.CoreGraphics",
    objc.pathForFramework(framework_path),
    _metadata.__dict__,
    _inline_list_,
    {
        "__doc__": __doc__,
        "__path__": __path__,
        "__loader__": globals().get("__loader__", None),
        "objc": objc,
    },
    (CoreFoundation,),
)


del sys.modules["Quartz.CoreGraphics._metadata"]


def _load(mod):
    import Quartz

    Quartz.CoreGraphics = mod

    # XXX: CGFLOAT_MIN is a #define for FLT_MIN or DBL_MIN, which isn't detected properly
    # by the metadata script.
    import sys

    if sys.maxsize > 1 << 32:
        mod.CGFLOAT_MIN = 1.175_494_350_822_287_5e-38
        mod.CGFLOAT_MAX = 3.402_823_466_385_288_6e38
    else:
        mod.CGFLOAT_MIN = 2.225_073_858_507_201_4e-308
        mod.CGFLOAT_MAX = 1.797_693_134_862_315_7e308

    import Quartz.CoreGraphics._callbacks as m

    for nm in dir(m):
        if nm.startswith("_"):
            continue
        setattr(mod, nm, getattr(m, nm))
    import Quartz.CoreGraphics._doubleindirect as m

    for nm in dir(m):
        if nm.startswith("_"):
            continue
        setattr(mod, nm, getattr(m, nm))
    import Quartz.CoreGraphics._sortandmap as m

    for nm in dir(m):
        if nm.startswith("_"):
            continue
        setattr(mod, nm, getattr(m, nm))
    import Quartz.CoreGraphics._coregraphics as m

    for nm in dir(m):
        if nm.startswith("_"):
            continue
        setattr(mod, nm, getattr(m, nm))
    import Quartz.CoreGraphics._contextmanager as m

    for nm in dir(m):
        if nm.startswith("_"):
            continue
        setattr(mod, nm, getattr(m, nm))

    mod.setCGPathElement(mod.CGPathElement)
    del mod.setCGPathElement

    # a #define
    mod.kCGEventFilterMaskPermitAllEvents = (
        mod.kCGEventFilterMaskPermitLocalMouseEvents
        | mod.kCGEventFilterMaskPermitLocalKeyboardEvents
        | mod.kCGEventFilterMaskPermitSystemDefinedEvents
    )

    def CGEventMaskBit(eventType):
        return 1 << eventType

    mod.CGEventMaskBit = CGEventMaskBit

    mod.kCGColorSpaceUserGray = "kCGColorSpaceUserGray"
    mod.kCGColorSpaceUserRGB = "kCGColorSpaceUserRGB"
    mod.kCGColorSpaceUserCMYK = "kCGColorSpaceUserCMYK"

    # Some pseudo-constants
    mod.kCGBaseWindowLevel = mod.CGWindowLevelForKey(mod.kCGBaseWindowLevelKey)
    mod.kCGMinimumWindowLevel = mod.CGWindowLevelForKey(mod.kCGMinimumWindowLevelKey)
    mod.kCGDesktopWindowLevel = mod.CGWindowLevelForKey(mod.kCGDesktopWindowLevelKey)
    mod.kCGDesktopIconWindowLevel = mod.CGWindowLevelForKey(
        mod.kCGDesktopIconWindowLevelKey
    )
    mod.kCGBackstopMenuLevel = mod.CGWindowLevelForKey(mod.kCGBackstopMenuLevelKey)
    mod.kCGNormalWindowLevel = mod.CGWindowLevelForKey(mod.kCGNormalWindowLevelKey)
    mod.kCGFloatingWindowLevel = mod.CGWindowLevelForKey(mod.kCGFloatingWindowLevelKey)
    mod.kCGTornOffMenuWindowLevel = mod.CGWindowLevelForKey(
        mod.kCGTornOffMenuWindowLevelKey
    )
    mod.kCGDockWindowLevel = mod.CGWindowLevelForKey(mod.kCGDockWindowLevelKey)
    mod.kCGMainMenuWindowLevel = mod.CGWindowLevelForKey(mod.kCGMainMenuWindowLevelKey)
    mod.kCGStatusWindowLevel = mod.CGWindowLevelForKey(mod.kCGStatusWindowLevelKey)
    mod.kCGModalPanelWindowLevel = mod.CGWindowLevelForKey(
        mod.kCGModalPanelWindowLevelKey
    )
    mod.kCGPopUpMenuWindowLevel = mod.CGWindowLevelForKey(
        mod.kCGPopUpMenuWindowLevelKey
    )
    mod.kCGDraggingWindowLevel = mod.CGWindowLevelForKey(mod.kCGDraggingWindowLevelKey)
    mod.kCGScreenSaverWindowLevel = mod.CGWindowLevelForKey(
        mod.kCGScreenSaverWindowLevelKey
    )
    mod.kCGCursorWindowLevel = mod.CGWindowLevelForKey(mod.kCGCursorWindowLevelKey)
    mod.kCGOverlayWindowLevel = mod.CGWindowLevelForKey(mod.kCGOverlayWindowLevelKey)
    mod.kCGHelpWindowLevel = mod.CGWindowLevelForKey(mod.kCGHelpWindowLevelKey)
    mod.kCGUtilityWindowLevel = mod.CGWindowLevelForKey(mod.kCGUtilityWindowLevelKey)
    mod.kCGAssistiveTechHighWindowLevel = mod.CGWindowLevelForKey(
        mod.kCGAssistiveTechHighWindowLevelKey
    )
    mod.kCGMaximumWindowLevel = mod.CGWindowLevelForKey(mod.kCGMaximumWindowLevelKey)

    mod.CGSetLocalEventsFilterDuringSupressionState = (
        mod.CGSetLocalEventsFilterDuringSuppressionState
    )

    mod.kCGAnyInputEventType = 0xFFFFFFFF


_load(mod)
