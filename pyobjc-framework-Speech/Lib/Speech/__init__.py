"""
Python mapping for the Speech framework.

This module does not contain docstrings for the wrapped code, check Apple's
documentation for details on how to use these functions and classes.
"""


def _setup():
    import sys

    import Foundation
    import objc
    from . import _metadata, _Speech

    dir_func, getattr_func = objc.createFrameworkDirAndGetattr(
        name="Speech",
        frameworkIdentifier="com.apple.Speech",
        frameworkPath=objc.pathForFramework(
            "/System/Library/Frameworks/Speech.framework"
        ),
        globals_dict=globals(),
        inline_list=None,
        parents=(
            _Speech,
            Foundation,
        ),
        metadict=_metadata.__dict__,
    )

    globals()["__dir__"] = dir_func
    globals()["__getattr__"] = getattr_func

    del sys.modules["Speech._metadata"]


globals().pop("_setup")()
