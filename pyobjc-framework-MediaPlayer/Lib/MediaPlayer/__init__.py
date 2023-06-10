"""
Python mapping for the MediaPlayer framework.

This module does not contain docstrings for the wrapped code, check Apple's
documentation for details on how to use these functions and classes.
"""


def _setup():
    import sys

    import AVFoundation
    import objc
    from . import _metadata

    dir_func, getattr_func = objc.createFrameworkDirAndGetattr(
        name="MediaPlayer",
        frameworkIdentifier="com.apple.MediaPlayer",
        frameworkPath=objc.pathForFramework(
            "/System/Library/Frameworks/MediaPlayer.framework"
        ),
        globals_dict=globals(),
        inline_list=None,
        parents=(AVFoundation,),
        metadict=_metadata.__dict__,
    )

    globals()["__dir__"] = dir_func
    globals()["__getattr__"] = getattr_func

    del sys.modules["MediaPlayer._metadata"]


globals().pop("_setup")()
