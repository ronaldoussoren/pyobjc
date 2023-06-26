"""
Python mapping for the Cinematic framework.

This module does not contain docstrings for the wrapped code, check Apple's
documentation for details on how to use these functions and classes.
"""


def _setup():
    import sys

    import objc
    import Foundation
    import AVFoundation
    import CoreMedia
    import Metal

    from . import _metadata

    dir_func, getattr_func = objc.createFrameworkDirAndGetattr(
        name="Cinematic",
        frameworkIdentifier="com.apple.Cinematic",
        frameworkPath=objc.pathForFramework(
            "/System/Library/Frameworks/Cinematic.framework"
        ),
        globals_dict=globals(),
        inline_list=None,
        parents=(Foundation, AVFoundation, CoreMedia, Metal),
        metadict=_metadata.__dict__,
    )

    globals()["__dir__"] = dir_func
    globals()["__getattr__"] = getattr_func

    del sys.modules["Cinematic._metadata"]


globals().pop("_setup")()
