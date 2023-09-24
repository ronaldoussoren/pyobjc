"""
Python mapping for the GameplayKit framework.

This module does not contain docstrings for the wrapped code, check Apple's
documentation for details on how to use these functions and classes.
"""


def _setup():
    import sys

    import AppKit
    import SpriteKit
    import objc
    from . import _metadata, _GameplayKit

    dir_func, getattr_func = objc.createFrameworkDirAndGetattr(
        name="GameplayKit",
        frameworkIdentifier="com.apple.GameplayKit",
        frameworkPath=objc.pathForFramework(
            "/System/Library/Frameworks/GameplayKit.framework"
        ),
        globals_dict=globals(),
        inline_list=None,
        parents=(
            _GameplayKit,
            AppKit,
            SpriteKit,
        ),
        metadict=_metadata.__dict__,
    )

    globals()["__dir__"] = dir_func
    globals()["__getattr__"] = getattr_func

    del sys.modules["GameplayKit._metadata"]


globals().pop("_setup")()
