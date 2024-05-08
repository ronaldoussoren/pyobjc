"""
Python mapping for the SystemExtensions framework.

This module does not contain docstrings for the wrapped code, check Apple's
documentation for details on how to use these functions and classes.
"""


def _setup():
    import sys

    import Foundation
    import objc
    from . import _metadata, _SystemExtensions

    dir_func, getattr_func = objc.createFrameworkDirAndGetattr(
        name="SystemExtensions",
        frameworkIdentifier="com.apple.SystemExtensions",
        frameworkPath=objc.pathForFramework(
            "/System/Library/Frameworks/SystemExtensions.framework"
        ),
        globals_dict=globals(),
        inline_list=None,
        parents=(
            _SystemExtensions,
            Foundation,
        ),
        metadict=_metadata.__dict__,
    )

    globals()["__dir__"] = dir_func
    globals()["__getattr__"] = getattr_func

    for cls, sel in (
        ("OSSystemExtensionManager", b"init"),
        ("OSSystemExtensionManager", b"new"),
    ):
        objc.registerUnavailableMethod(cls, sel)

    del sys.modules["SystemExtensions._metadata"]


globals().pop("_setup")()
