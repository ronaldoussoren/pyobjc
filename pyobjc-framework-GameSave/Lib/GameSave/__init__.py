"""
Python mapping for the GameSave framework.

This module does not contain docstrings for the wrapped code, check Apple's
documentation for details on how to use these functions and classes.
"""


def _setup():
    import sys

    import objc
    import Foundation
    from . import _metadata

    dir_func, getattr_func = objc.createFrameworkDirAndGetattr(
        name="GameSave",
        frameworkIdentifier="com.apple.gamesave",
        frameworkPath=objc.pathForFramework(
            "/System/Library/Frameworks/GameSave.framework"
        ),
        globals_dict=globals(),
        inline_list=None,
        parents=(Foundation,),
        metadict=_metadata.__dict__,
    )

    globals()["__dir__"] = dir_func
    globals()["__getattr__"] = getattr_func

    for cls, sel in (
        ("GSSyncedDirectoryVersion", b"init"),
        ("GSSyncedDirectoryVersion", b"new"),
        ("GSSyncedDirectoryState", b"init"),
        ("GSSyncedDirectoryState", b"new"),
        ("GSSyncedDirectory", b"init"),
        ("GSSyncedDirectory", b"new"),
    ):
        objc.registerUnavailableMethod(cls, sel)

    del sys.modules["GameSave._metadata"]


globals().pop("_setup")()
