"""
Python mapping for the Symbols framework.

This module does not contain docstrings for the wrapped code, check Apple's
documentation for details on how to use these functions and classes.
"""


def _setup():
    import sys

    import objc
    import Foundation
    from . import _metadata

    dir_func, getattr_func = objc.createFrameworkDirAndGetattr(
        name="Symbols",
        frameworkIdentifier="com.apple.Symbols",
        frameworkPath=objc.pathForFramework(
            "/System/Library/Frameworks/Symbols.framework"
        ),
        globals_dict=globals(),
        inline_list=None,
        parents=(Foundation,),
        metadict=_metadata.__dict__,
    )

    globals()["__dir__"] = dir_func
    globals()["__getattr__"] = getattr_func

    for cls, sel in (
        ("NSSymbolEffectOptions", b"init"),
        ("NSSymbolEffectOptions", b"new"),
        ("NSSymbolEffect", b"init"),
        ("NSSymbolEffect", b"new"),
        ("NSSymbolContentTransition", b"init"),
        ("NSSymbolContentTransition", b"new"),
    ):
        objc.registerUnavailableMethod(cls, sel)

    del sys.modules["Symbols._metadata"]


globals().pop("_setup")()
