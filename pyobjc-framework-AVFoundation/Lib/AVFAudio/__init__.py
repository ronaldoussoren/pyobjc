"""
Python mapping for the AVFAudio framework.

This module does not contain docstrings for the wrapped code, check Apple's
documentation for details on how to use these functions and classes.
"""


def _setup():
    import sys

    import CoreAudio
    import CoreMedia
    import Foundation
    import objc
    from . import _metadata
    from ._inlines import _inline_list_

    if objc.macos_available(11, 3):
        dir_func, getattr_func = objc.createFrameworkDirAndGetattr(
            name="AVFAudio",
            frameworkIdentifier="com.apple.audio.AVFAudio",
            frameworkPath=objc.pathForFramework(
                "/System/Library/Frameworks/AVFAudio.framework"
            ),
            globals_dict=globals(),
            inline_list=_inline_list_,
            parents=(CoreAudio, CoreMedia, Foundation),
            metadict=_metadata.__dict__,
        )
    else:
        dir_func, getattr_func = objc.createFrameworkDirAndGetattr(
            name="AVFoundation",
            frameworkIdentifier="com.apple.avfoundation",
            frameworkPath=objc.pathForFramework(
                "/System/Library/Frameworks/AVFoundation.framework"
            ),
            globals_dict=globals(),
            inline_list=_inline_list_,
            parents=(CoreAudio, CoreMedia, Foundation),
            metadict=_metadata.__dict__,
        )

    globals()["__dir__"] = dir_func
    globals()["__getattr__"] = getattr_func

    for cls, sel in ():
        objc.registerUnavailableMethod(cls, sel)

    del sys.modules["AVFAudio._metadata"]


globals().pop("_setup")()
