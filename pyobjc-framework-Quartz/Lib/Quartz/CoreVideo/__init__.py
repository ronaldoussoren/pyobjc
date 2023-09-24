"""
Python mapping for the CoreVideo framework.

This module does not contain docstrings for the wrapped code, check Apple's
documentation for details on how to use these functions and classes.
"""


def _setup():
    import sys

    import CoreFoundation
    import objc
    from . import _metadata, _CVPixelBuffer

    dir_func, getattr_func = objc.createFrameworkDirAndGetattr(
        name="Quartz.CoreVideo",
        frameworkIdentifier="com.apple.CoreVideo",
        frameworkPath=objc.pathForFramework(
            "/System/Library/Frameworks/CoreVideo.framework"
        ),
        globals_dict=globals(),
        inline_list=None,
        parents=(
            _CVPixelBuffer,
            CoreFoundation,
        ),
        metadict=_metadata.__dict__,
    )

    globals()["__dir__"] = dir_func
    globals()["__getattr__"] = getattr_func

    del sys.modules["Quartz.CoreVideo._metadata"]


globals().pop("_setup")()
