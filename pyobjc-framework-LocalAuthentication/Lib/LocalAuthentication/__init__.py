"""
Python mapping for the CloudKit framework.

This module does not contain docstrings for the wrapped code, check Apple's
documentation for details on how to use these functions and classes.
"""


def _setup():
    import sys

    import Foundation
    import objc
    from . import _metadata, _LocalAuthentication

    dir_func, getattr_func = objc.createFrameworkDirAndGetattr(
        name="LocalAuthentication",
        frameworkIdentifier="com.apple.LocalAuthentication",
        frameworkPath=objc.pathForFramework(
            "/System/Library/Frameworks/LocalAuthentication.framework"
        ),
        globals_dict=globals(),
        inline_list=None,
        parents=(
            _LocalAuthentication,
            Foundation,
        ),
        metadict=_metadata.__dict__,
    )

    globals()["__dir__"] = dir_func
    globals()["__getattr__"] = getattr_func

    for cls, sel in (
        ("LARightStore", b"init"),
        ("LARightStore", b"new"),
        ("LAPrivateKey", b"init"),
        ("LAPrivateKey", b"new"),
        ("LAPublicKey", b"init"),
        ("LAPublicKey", b"new"),
        ("LASecret", b"init"),
        ("LASecret", b"new"),
        ("LAPersistedRight", b"init"),
        ("LAPersistedRight", b"new"),
    ):
        objc.registerUnavailableMethod(cls, sel)

    del sys.modules["LocalAuthentication._metadata"]


globals().pop("_setup")()
