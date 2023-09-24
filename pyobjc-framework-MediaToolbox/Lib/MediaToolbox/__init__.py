"""
Python mapping for the MediaToolbox framework.

This module does not contain docstrings for the wrapped code, check Apple's
documentation for details on how to use these functions and classes.
"""


def _setup():
    import sys

    import Foundation
    import objc
    from . import _metadata, _MediaToolbox

    dir_func, getattr_func = objc.createFrameworkDirAndGetattr(
        name="MediaToolbox",
        frameworkIdentifier="com.apple.MediaToolbox",
        frameworkPath=objc.pathForFramework(
            "/System/Library/Frameworks/MediaToolbox.framework"
        ),
        globals_dict=globals(),
        inline_list=None,
        parents=(
            _MediaToolbox,
            Foundation,
        ),
        metadict=_metadata.__dict__,
    )

    globals()["__dir__"] = dir_func
    globals()["__getattr__"] = getattr_func

    del sys.modules["MediaToolbox._metadata"]


globals().pop("_setup")()
