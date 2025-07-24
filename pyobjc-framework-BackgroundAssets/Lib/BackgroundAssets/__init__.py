"""
Python mapping for the BackgroundAssets framework.

This module does not contain docstrings for the wrapped code, check Apple's
documentation for details on how to use these functions and classes.
"""


def _setup():
    import sys

    import Foundation
    import objc
    from . import _metadata, _BackgroundAssets

    dir_func, getattr_func = objc.createFrameworkDirAndGetattr(
        name="BackgroundAssets",
        frameworkIdentifier="com.apple.mobileasset.BackgroundAssets",
        frameworkPath=objc.pathForFramework(
            "/System/Library/Frameworks/BackgroundAssets.framework"
        ),
        globals_dict=globals(),
        inline_list=None,
        parents=(_BackgroundAssets, Foundation),
        metadict=_metadata.__dict__,
    )

    globals()["__dir__"] = dir_func
    globals()["__getattr__"] = getattr_func

    for cls, sel in (
        ("BADownloadManager", b"init"),
        ("BADownloadManager", b"new"),
        ("BAURLDownload", b"init"),
        ("BAURLDownload", b"new"),
        ("BAAppExtensionInfo", b"init"),
        ("BAAppExtensionInfo", b"new"),
        ("BADownload", b"init"),
        ("BADownload", b"new"),
        ("BAAssetPack", b"init"),
        ("BAAssetPack", b"new"),
        ("BAAssetPackManager", b"init"),
        ("BAAssetPackManager", b"new"),
        ("BAAssetPackManifest", b"init"),
        ("BAAssetPackManifest", b"new"),
    ):
        objc.registerUnavailableMethod(cls, sel)

    del sys.modules["BackgroundAssets._metadata"]


globals().pop("_setup")()
