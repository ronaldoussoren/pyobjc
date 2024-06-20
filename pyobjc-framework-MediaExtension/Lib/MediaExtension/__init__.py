"""
Python mapping for the MediaExtension framework.

This module does not contain docstrings for the wrapped code, check Apple's
documentation for details on how to use these functions and classes.
"""


def _setup():
    import sys

    import AVFoundation
    import CoreMedia
    import Foundation
    import objc
    from . import _MediaExtension, _metadata

    dir_func, getattr_func = objc.createFrameworkDirAndGetattr(
        name="MediaExtension",
        frameworkIdentifier="com.apple.avfoundation",
        frameworkPath=objc.pathForFramework(
            "/System/Library/Frameworks/MediaExtension.framework"
        ),
        globals_dict=globals(),
        inline_list=None,
        parents=(_MediaExtension, CoreMedia, AVFoundation, Foundation),
        metadict=_metadata.__dict__,
    )

    globals()["__dir__"] = dir_func
    globals()["__getattr__"] = getattr_func

    del sys.modules["MediaExtension._metadata"]


globals().pop("_setup")()
