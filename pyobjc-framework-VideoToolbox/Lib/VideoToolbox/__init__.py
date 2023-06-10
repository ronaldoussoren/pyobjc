"""
Python mapping for the VideoToolbox framework.

This module does not contain docstrings for the wrapped code, check Apple's
documentation for details on how to use these functions and classes.
"""


def _setup():
    import sys

    import Quartz
    import CoreMedia
    import Foundation
    import objc
    from . import _metadata, _VideoToolbox

    dir_func, getattr_func = objc.createFrameworkDirAndGetattr(
        name="VideoToolbox",
        frameworkIdentifier="com.apple.VideoToolbox",
        frameworkPath=objc.pathForFramework(
            "/System/Library/Frameworks/VideoToolbox.framework"
        ),
        globals_dict=globals(),
        inline_list=None,
        parents=(
            _VideoToolbox,
            Quartz,
            CoreMedia,
            Foundation,
        ),
        metadict=_metadata.__dict__,
    )

    globals()["__dir__"] = dir_func
    globals()["__getattr__"] = getattr_func

    del sys.modules["VideoToolbox._metadata"]


globals().pop("_setup")()
