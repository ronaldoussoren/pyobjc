"""
Python mapping for the FileProvider framework.

This module does not contain docstrings for the wrapped code, check Apple's
documentation for details on how to use these functions and classes.
"""


def _setup():
    import sys

    import Foundation
    import objc
    from . import _metadata, _FileProvider

    dir_func, getattr_func = objc.createFrameworkDirAndGetattr(
        name="FileProvider",
        frameworkIdentifier="com.apple.FileProvider",
        frameworkPath=objc.pathForFramework(
            "/System/Library/Frameworks/FileProvider.framework"
        ),
        globals_dict=globals(),
        inline_list=None,
        parents=(
            _FileProvider,
            Foundation,
        ),
        metadict=_metadata.__dict__,
    )

    globals()["__dir__"] = dir_func
    globals()["__getattr__"] = getattr_func

    for cls, sel in (("NSFileProviderManager", b"init"),):
        objc.registerUnavailableMethod(cls, sel)

    del sys.modules["FileProvider._metadata"]


globals().pop("_setup")()
