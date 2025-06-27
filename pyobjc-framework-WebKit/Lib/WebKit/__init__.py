"""
Python mapping for the WebKit framework.

This module does not contain docstrings for the wrapped code, check Apple's
documentation for details on how to use these functions and classes.
"""


def _setup():
    import sys

    import Foundation
    import objc
    from . import _metadata, _WebKit

    dir_func, getattr_func = objc.createFrameworkDirAndGetattr(
        name="WebKit",
        frameworkIdentifier="com.apple.WebKit",
        frameworkPath=objc.pathForFramework(
            "/System/Library/Frameworks/WebKit.framework"
        ),
        globals_dict=globals(),
        inline_list=None,
        parents=(
            _WebKit,
            Foundation,
        ),
        metadict=_metadata.__dict__,
    )

    globals()["__dir__"] = dir_func
    globals()["__getattr__"] = getattr_func

    for cls, sel in (
        ("WKContentWorld", b"init"),
        ("WKContentWorld", b"new"),
        ("WKHTTPCookieStore", b"init"),
        ("WKSecurityOrigin", b"init"),
        ("WKFindResult", b"init"),
        ("WKBackForwardListItem", b"init"),
        ("WKWebsiteDataStore", b"init"),
        ("WKWebsiteDataStore", b"new"),
        ("DOMObject", b"init"),
        ("WKContextMenuElementInfo", b"init"),
        ("WKWebExtension", b"init"),
        ("WKWebExtension", b"new"),
        ("WKWebExtensionAction", b"init"),
        ("WKWebExtensionAction", b"new"),
        ("WKWebExtensionCommand", b"init"),
        ("WKWebExtensionCommand", b"new"),
        ("WKWebExtensionContext", b"init"),
        ("WKWebExtensionContext", b"new"),
        ("WKWebExtensionControllerConfiguration", b"init"),
        ("WKWebExtensionControllerConfiguration", b"new"),
        ("WKWebExtensionDataRecord", b"init"),
        ("WKWebExtensionDataRecord", b"new"),
        ("WKWebExtensionMatchPattern", b"init"),
        ("WKWebExtensionMatchPattern", b"new"),
        ("WKWebExtensionMessagePort", b"init"),
        ("WKWebExtensionMessagePort", b"new"),
        ("WKWebExtensionTabConfiguration", b"init"),
        ("WKWebExtensionTabConfiguration", b"new"),
        ("WKWebExtensionWindowConfiguration", b"init"),
        ("WKWebExtensionWindowConfiguration", b"new"),
    ):
        objc.registerUnavailableMethod(cls, sel)

    del sys.modules["WebKit._metadata"]

    objc.addConvenienceForBasicSequence("WebScriptObject", True)


globals().pop("_setup")()
