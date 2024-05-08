"""
Python mapping for the CoreHaptics framework.

This module does not contain docstrings for the wrapped code, check Apple's
documentation for details on how to use these functions and classes.
"""


def _setup():
    import sys

    import Foundation
    import objc
    from . import _metadata

    dir_func, getattr_func = objc.createFrameworkDirAndGetattr(
        name="CoreHaptics",
        frameworkIdentifier="com.apple.CoreHaptics",
        frameworkPath=objc.pathForFramework(
            "/System/Library/Frameworks/CoreHaptics.framework"
        ),
        globals_dict=globals(),
        inline_list=None,
        parents=(Foundation,),
        metadict=_metadata.__dict__,
    )

    globals()["__dir__"] = dir_func
    globals()["__getattr__"] = getattr_func

    for cls, sel in (
        ("CHHapticPattern", b"init"),
        ("CHHapticEvent", b"init"),
        ("CHHapticEngine", b"init"),
        ("CHHapticEventParameter", b"init"),
        ("CHHapticDynamicParameter", b"init"),
        ("CHHapticParameterCurveControlPoint", b"init"),
        ("CHHapticParameterCurve", b"init"),
    ):
        objc.registerUnavailableMethod(cls, sel)

    del sys.modules["CoreHaptics._metadata"]


globals().pop("_setup")()
