"""
Python mapping for the SharedWithYou framework.

This module does not contain docstrings for the wrapped code, check Apple's
documentation for details on how to use these functions and classes.
"""


def _setup():
    import sys

    import SharedWithYouCore
    import objc
    from . import _metadata, _SharedWithYou

    dir_func, getattr_func = objc.createFrameworkDirAndGetattr(
        name="SharedWithYou",
        frameworkIdentifier="com.apple.SharedWithYou",
        frameworkPath=objc.pathForFramework(
            "/System/Library/Frameworks/SharedWithYou.framework"
        ),
        globals_dict=globals(),
        inline_list=None,
        parents=(
            _SharedWithYou,
            SharedWithYouCore,
        ),
        metadict=_metadata.__dict__,
    )

    globals()["__dir__"] = dir_func
    globals()["__getattr__"] = getattr_func

    del sys.modules["SharedWithYou._metadata"]


globals().pop("_setup")()
