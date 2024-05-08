"""
Python mapping for the StoreKit framework.

This module does not contain docstrings for the wrapped code, check Apple's
documentation for details on how to use these functions and classes.
"""


def _setup():
    import sys

    import Foundation
    import objc
    from . import _metadata, _StoreKit

    dir_func, getattr_func = objc.createFrameworkDirAndGetattr(
        name="StoreKit",
        frameworkIdentifier="com.apple.StoreKit",
        frameworkPath=objc.pathForFramework(
            "/System/Library/Frameworks/StoreKit.framework"
        ),
        globals_dict=globals(),
        inline_list=None,
        parents=(
            _StoreKit,
            Foundation,
        ),
        metadict=_metadata.__dict__,
    )

    globals()["__dir__"] = dir_func
    globals()["__getattr__"] = getattr_func

    for cls, sel in (
        ("SKOverlayConfiguration", b"init"),
        ("SKOverlayConfiguration", b"new"),
        ("SKOverlayAppConfiguration", b"init"),
        ("SKOverlayAppConfiguration", b"new"),
        ("SKOverlayAppClipConfiguration", b"init"),
        ("SKOverlayAppClipConfiguration", b"new"),
        ("SKOverlayTransitionContext", b"init"),
        ("SKOverlayTransitionContext", b"new"),
        ("SKOverlay", b"init"),
        ("SKOverlay", b"new"),
    ):
        objc.registerUnavailableMethod(cls, sel)

    del sys.modules["StoreKit._metadata"]


globals().pop("_setup")()

from Foundation import NSLocalizedStringFromTableInBundle  # isort:skip  # noqa: E402


from . import StoreKitBundle  # isort:skip  # noqa: E402


def SKLocalizedString(x):
    return NSLocalizedStringFromTableInBundle(x, None, StoreKitBundle, "")
