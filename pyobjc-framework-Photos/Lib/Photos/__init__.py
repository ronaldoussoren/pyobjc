"""
Python mapping for the Photos framework.

This module does not contain docstrings for the wrapped code, check Apple's
documentation for details on how to use these functions and classes.
"""


def _setup():
    import sys

    import Foundation
    import objc
    from . import _metadata, _Photos

    if objc.macos_available(10, 15):
        identifier = "com.apple.Photos"
    else:
        identifier = "com.apple.PhotoKit.Photos"

    dir_func, getattr_func = objc.createFrameworkDirAndGetattr(
        name="Photos",
        frameworkIdentifier=identifier,
        frameworkPath=objc.pathForFramework(
            "/System/Library/Frameworks/Photos.framework"
        ),
        globals_dict=globals(),
        inline_list=None,
        parents=(
            _Photos,
            Foundation,
        ),
        metadict=_metadata.__dict__,
    )

    globals()["__dir__"] = dir_func
    globals()["__getattr__"] = getattr_func

    for cls, sel in (
        ("PHPersistentChangeToken", b"init"),
        ("PHPersistentChangeToken", b"new"),
        ("PHLivePhoto", b"init"),
        ("PHPersistentObjectChangeDetails", b"init"),
        ("PHPersistentObjectChangeDetails", b"new"),
        ("PHLivePhotoEditingContext", b"init"),
        ("PHPersistentChangeFetchResult", b"init"),
        ("PHPersistentChangeFetchResult", b"new"),
        ("PHPersistentChange", b"init"),
        ("PHPersistentChange", b"new"),
    ):
        objc.registerUnavailableMethod(cls, sel)

    del sys.modules["Photos._metadata"]


globals().pop("_setup")()
