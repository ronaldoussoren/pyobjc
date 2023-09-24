"""
Python mapping for the CoreAudioKit framework.

This module does not contain docstrings for the wrapped code, check Apple's
documentation for details on how to use these functions and classes.
"""


def _setup():
    import sys

    import CoreAudio
    import Foundation
    import objc
    from . import _metadata

    dir_func, getattr_func = objc.createFrameworkDirAndGetattr(
        name="CoreAudioKit",
        frameworkIdentifier="com.apple.audio.CoreAudioKit",
        frameworkPath=objc.pathForFramework(
            "/System/Library/Frameworks/CoreAudioKit.framework"
        ),
        globals_dict=globals(),
        inline_list=None,
        parents=(
            CoreAudio,
            Foundation,
        ),
        metadict=_metadata.__dict__,
    )

    globals()["__dir__"] = dir_func
    globals()["__getattr__"] = getattr_func

    del sys.modules["CoreAudioKit._metadata"]


globals().pop("_setup")()
