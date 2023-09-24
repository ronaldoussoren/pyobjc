"""
Python mapping for the MetalKit framework.

This module does not contain docstrings for the wrapped code, check Apple's
documentation for details on how to use these functions and classes.
"""


def _setup():
    import sys

    import Foundation
    import Metal
    import objc
    from . import _metadata, _MetalKit

    dir_func, getattr_func = objc.createFrameworkDirAndGetattr(
        name="MetalKit",
        frameworkIdentifier="com.apple.MetalKit",
        frameworkPath=objc.pathForFramework(
            "/System/Library/Frameworks/MetalKit.framework"
        ),
        globals_dict=globals(),
        inline_list=None,
        parents=(
            _MetalKit,
            Metal,
            Foundation,
        ),
        metadict=_metadata.__dict__,
    )

    globals()["__dir__"] = dir_func
    globals()["__getattr__"] = getattr_func

    del sys.modules["MetalKit._metadata"]


globals().pop("_setup")()
