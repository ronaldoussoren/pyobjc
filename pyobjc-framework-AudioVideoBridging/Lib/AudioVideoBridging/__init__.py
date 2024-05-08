"""
Python mapping for the AudioVideoBridging framework.

This module does not contain docstrings for the wrapped code, check Apple's
documentation for details on how to use these functions and classes.
"""


def _setup():
    import sys

    import Foundation
    import objc
    from . import _metadata, _AudioVideoBridging

    dir_func, getattr_func = objc.createFrameworkDirAndGetattr(
        name="AudioVideoBridging",
        frameworkIdentifier="com.apple.AudioVideoBridging",
        frameworkPath=objc.pathForFramework(
            "/System/Library/Frameworks/AudioVideoBridging.framework"
        ),
        globals_dict=globals(),
        inline_list=None,
        parents=(
            _AudioVideoBridging,
            Foundation,
        ),
        metadict=_metadata.__dict__,
    )

    globals()["__dir__"] = dir_func
    globals()["__getattr__"] = getattr_func

    for cls, sel in (
        ("AVB1722ControlInterface", b"init"),
        ("AVBInterface", b"init"),
    ):
        objc.registerUnavailableMethod(cls, sel)

    del sys.modules["AudioVideoBridging._metadata"]


globals().pop("_setup")()
