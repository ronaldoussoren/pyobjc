"""
Python mapping for the NetworkExtension framework.

This module does not contain docstrings for the wrapped code, check Apple's
documentation for details on how to use these functions and classes.
"""


def _setup():
    import sys

    import Foundation
    import objc
    from . import _metadata, _NetworkExtension

    dir_func, getattr_func = objc.createFrameworkDirAndGetattr(
        name="NetworkExtension",
        frameworkIdentifier="com.apple.NetworkExtension",
        frameworkPath=objc.pathForFramework(
            "/System/Library/Frameworks/NetworkExtension.framework"
        ),
        globals_dict=globals(),
        inline_list=None,
        parents=(
            _NetworkExtension,
            Foundation,
        ),
        metadict=_metadata.__dict__,
    )

    for cls, sel in (
        ("NEURLFilter", b"init"),
        ("NEURLFilter", b"new"),
    ):
        objc.registerUnavailableMethod(cls, sel)

    globals()["__dir__"] = dir_func
    globals()["__getattr__"] = getattr_func

    del sys.modules["NetworkExtension._metadata"]


globals().pop("_setup")()
