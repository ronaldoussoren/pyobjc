"""
Python mapping for the DiscRecordingUI framework.

This module does not contain docstrings for the wrapped code, check Apple's
documentation for details on how to use these functions and classes.
"""


def _setup():
    import sys

    import DiscRecording
    import objc
    from . import _metadata

    dir_func, getattr_func = objc.createFrameworkDirAndGetattr(
        name="DiscRecordingUI",
        frameworkIdentifier="com.apple.DiscRecordingUI",
        frameworkPath=objc.pathForFramework(
            "/System/Library/Frameworks/DiscRecordingUI.framework"
        ),
        globals_dict=globals(),
        inline_list=None,
        parents=(DiscRecording,),
        metadict=_metadata.__dict__,
    )

    globals()["__dir__"] = dir_func
    globals()["__getattr__"] = getattr_func

    del sys.modules["DiscRecordingUI._metadata"]


globals().pop("_setup")()
