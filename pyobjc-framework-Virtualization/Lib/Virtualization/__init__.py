"""
Python mapping for the Virtualization framework.

This module does not contain docstrings for the wrapped code, check Apple's
documentation for details on how to use these functions and classes.
"""


def _setup():
    import sys

    import Foundation
    import objc
    from . import _metadata, _Virtualization

    dir_func, getattr_func = objc.createFrameworkDirAndGetattr(
        name="Virtualization",
        frameworkIdentifier="com.apple.Virtualization",
        frameworkPath=objc.pathForFramework(
            "/System/Library/Frameworks/Virtualization.framework"
        ),
        globals_dict=globals(),
        inline_list=None,
        parents=(
            _Virtualization,
            Foundation,
        ),
        metadict=_metadata.__dict__,
    )

    globals()["__dir__"] = dir_func
    globals()["__getattr__"] = getattr_func

    del sys.modules["Virtualization._metadata"]


globals().pop("_setup")()
