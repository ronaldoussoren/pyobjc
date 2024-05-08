"""
Python mapping for the LocalAuthenticationEmbeddedUI framework.

This module does not contain docstrings for the wrapped code, check Apple's
documentation for details on how to use these functions and classes.
"""


def _setup():
    import sys

    import AppKit
    import LocalAuthentication
    import objc
    from . import _metadata

    dir_func, getattr_func = objc.createFrameworkDirAndGetattr(
        name="LocalAuthenticationEmbeddedUI",
        frameworkIdentifier="com.apple.LocalAuthenticationEmbeddedUI",
        frameworkPath=objc.pathForFramework(
            "/System/Library/Frameworks/LocalAuthenticationEmbeddedUI.framework"
        ),
        globals_dict=globals(),
        inline_list=None,
        parents=(
            LocalAuthentication,
            AppKit,
        ),
        metadict=_metadata.__dict__,
    )

    globals()["__dir__"] = dir_func
    globals()["__getattr__"] = getattr_func

    for cls, sel in (
        ("LAAuthenticationView", b"initWithFrame:"),
        ("LAAuthenticationView", b"initWithCoder:"),
    ):
        objc.registerUnavailableMethod(cls, sel)

    del sys.modules["LocalAuthenticationEmbeddedUI._metadata"]


globals().pop("_setup")()
