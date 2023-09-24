"""
Python mapping for the CoreGraphics framework.

This module does not contain docstrings for the wrapped code, check Apple's
documentation for details on how to use these functions and classes.
"""


def _setup():
    import sys

    import CoreFoundation
    import objc
    import os
    from . import (
        _metadata,
        _callbacks,
        _doubleindirect,
        _sortandmap,
        _coregraphics,
        _contextmanager,
    )
    from ._inlines import _inline_list_

    if os.path.exists("/System/Library/Frameworks/CoreGraphics.framework"):
        frameworkPath = "/System/Library/Frameworks/CoreGraphics.framework"
        frameworkIdentifier = "com.apple.CoreGraphics"
    else:
        frameworkPath = "/System/Library/Frameworks/ApplicationServices.framework"
        frameworkIdentifier = "com.apple.ApplicationServices"

    dir_func, getattr_func = objc.createFrameworkDirAndGetattr(
        name="Quartz.CoreGraphics",
        frameworkIdentifier=frameworkIdentifier,
        frameworkPath=objc.pathForFramework(frameworkPath),
        globals_dict=globals(),
        inline_list=_inline_list_,
        parents=(
            _callbacks,
            _doubleindirect,
            _sortandmap,
            _coregraphics,
            _contextmanager,
            CoreFoundation,
        ),
        metadict=_metadata.__dict__,
    )

    globals()["__dir__"] = dir_func
    globals()["__getattr__"] = getattr_func

    del sys.modules["Quartz.CoreGraphics._metadata"]

    # XXX: To be verified
    from . import CGPathElement

    _sortandmap.setCGPathElement(CGPathElement)
    del _sortandmap.setCGPathElement

    # XXX: Move these to metadata!

    global CGFLOAT_MIN, CGFLOAT_MAX
    CGFLOAT_MIN = 1.175_494_350_822_287_5e-38
    CGFLOAT_MAX = 3.402_823_466_385_288_6e38

    global kCGAnyInputEventType
    kCGAnyInputEventType = 0xFFFFFFFF

    global CGEventMaskBit

    def CGEventMaskBit(eventType):
        return 1 << eventType

    global kCGColorSpaceUserGray, kCGColorSpaceUserRGB, kCGColorSpaceUserCMYK
    kCGColorSpaceUserGray = "kCGColorSpaceUserGray"
    kCGColorSpaceUserRGB = "kCGColorSpaceUserRGB"
    kCGColorSpaceUserCMYK = "kCGColorSpaceUserCMYK"


globals().pop("_setup")()
