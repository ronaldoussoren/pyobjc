"""
Python mapping for the CryptoTokenKit framework.

This module does not contain docstrings for the wrapped code, check Apple's
documentation for details on how to use these functions and classes.
"""


def _setup():
    import sys

    import Foundation
    import objc
    from . import _metadata, _CryptoTokenKit

    dir_func, getattr_func = objc.createFrameworkDirAndGetattr(
        name="CryptoTokenKit",
        frameworkIdentifier="com.apple.CryptoTokenKit",
        frameworkPath=objc.pathForFramework(
            "/System/Library/Frameworks/CryptoTokenKit.framework"
        ),
        globals_dict=globals(),
        inline_list=None,
        parents=(
            _CryptoTokenKit,
            Foundation,
        ),
        metadict=_metadata.__dict__,
    )

    globals()["__dir__"] = dir_func
    globals()["__getattr__"] = getattr_func

    for cls, sel in (
        ("TKSmartCardToken", b"initWithTokenDriver:instanceID:"),
        ("TKTokenWatcherTokenInfo", b"init"),
        ("TKTokenWatcherTokenInfo", b"new"),
        ("TKTokenKeychainItem", b"init"),
        ("TKTokenKeychainCertificate", b"initWithTokenDriver:instanceID:"),
        ("TKTokenKeychainKey", b"initWithTokenDriver:instanceID:"),
        ("TKTokenKeychainContents", b"init"),
        ("TKTokenDriverConfiguration", b"init"),
        ("TKTokenDriverConfiguration", b"new"),
        ("TKTokenConfiguration", b"init"),
        ("TKTokenConfiguration", b"new"),
        ("TKTokenKeyAlgorithm", b"init"),
        ("TKTokenSession", b"init"),
        ("TKToken", b"init"),
        ("TKToken", b"new"),
        ("TKTLVRecord", b"init"),
        ("TKTLVRecord", b"new"),
        ("TKSmartCardTokenRegistrationManager", b"init"),
        ("TKSmartCardTokenRegistrationManager", b"new"),
    ):
        objc.registerUnavailableMethod(cls, sel)

    del sys.modules["CryptoTokenKit._metadata"]


globals().pop("_setup")()
