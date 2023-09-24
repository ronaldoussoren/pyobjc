"""
Python mapping for the AVFoundation framework.

This module does not contain docstrings for the wrapped code, check Apple's
documentation for details on how to use these functions and classes.
"""


def _setup():
    import sys

    import CoreAudio
    import CoreMedia
    import Foundation
    import objc
    from . import _AVFoundation, _metadata
    from ._inlines import _inline_list_

    dir_func, getattr_func = objc.createFrameworkDirAndGetattr(
        name="AVFoundation",
        frameworkIdentifier="com.apple.avfoundation",
        frameworkPath=objc.pathForFramework(
            "/System/Library/Frameworks/AVFoundation.framework"
        ),
        globals_dict=globals(),
        inline_list=_inline_list_,
        parents=(_AVFoundation, CoreAudio, CoreMedia, Foundation),
        metadict=_metadata.__dict__,
    )

    globals()["__dir__"] = dir_func
    globals()["__getattr__"] = getattr_func

    del sys.modules["AVFoundation._metadata"]


globals().pop("_setup")()
