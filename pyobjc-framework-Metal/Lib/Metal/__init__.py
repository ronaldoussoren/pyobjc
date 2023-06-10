"""
Python mapping for the Metal framework.

This module does not contain docstrings for the wrapped code, check Apple's
documentation for details on how to use these functions and classes.
"""


def _setup():
    import sys

    import AppKit
    import objc
    from . import _metadata, _Metal
    from ._inlines import _inline_list_

    dir_func, getattr_func = objc.createFrameworkDirAndGetattr(
        name="Metal",
        frameworkIdentifier="com.apple.Metal",
        frameworkPath=objc.pathForFramework(
            "/System/Library/Frameworks/Metal.framework"
        ),
        globals_dict=globals(),
        inline_list=_inline_list_,
        parents=(
            _Metal,
            AppKit,
        ),
        metadict=_metadata.__dict__,
    )

    globals()["__dir__"] = dir_func
    globals()["__getattr__"] = getattr_func

    del sys.modules["Metal._metadata"]


globals().pop("_setup")()
