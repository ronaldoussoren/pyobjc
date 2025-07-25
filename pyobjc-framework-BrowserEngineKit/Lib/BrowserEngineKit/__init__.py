"""
Python mapping for the BrowserEngineKit framework.

This module does not contain docstrings for the wrapped code, check Apple's
documentation for details on how to use these functions and classes.
"""


def _setup():
    import sys

    import Foundation
    import objc
    from . import _BrowserEngineKit, _metadata

    dir_func, getattr_func = objc.createFrameworkDirAndGetattr(
        name="BrowserEngineKit",
        frameworkIdentifier="com.apple.BrowserEngineKit",
        frameworkPath=objc.pathForFramework(
            "/System/Library/Frameworks/BrowserEngineKit.framework"
        ),
        globals_dict=globals(),
        inline_list=None,
        parents=(_BrowserEngineKit, Foundation),
        metadict=_metadata.__dict__,
    )

    globals()["__dir__"] = dir_func
    globals()["__getattr__"] = getattr_func

    for cls, sel in (
        ("BETextDocumentRequest", b"init"),
        ("BETextDocumentRequest", b"new"),
        ("BELayerHierarchyHandle", b"init"),
        ("BELayerHierarchyHandle", b"new"),
        ("BEAutoFillTextSuggestion", b"init"),
        ("BEAutoFillTextSuggestion", b"new"),
        ("BEKeyEntryContext", b"init"),
        ("BEKeyEntryContext", b"new"),
        (
            "BEContextMenuConfiguration",
            b"configurationWithIdentifier:previewProvider:actionProvider:",
        ),
        ("BETextAlternatives", b"init"),
        ("BETextAlternatives", b"new"),
        ("BEWebAppManifest", b"init"),
        ("BEMediaEnvironment", b"init"),
        ("BEMediaEnvironment", b"new"),
        ("BERenderingProcess", b"init"),
        ("BERenderingProcess", b"new"),
        ("BETextSuggestion", b"init"),
        ("BETextSuggestion", b"new"),
        ("BELayerHierarchyHostingTransactionCoordinator", b"init"),
        ("BELayerHierarchyHostingTransactionCoordinator", b"new"),
        ("BELayerHierarchy", b"init"),
        ("BELayerHierarchy", b"new"),
        ("BENetworkingProcess", b"init"),
        ("BENetworkingProcess", b"new"),
        ("BEScrollViewScrollUpdate", b"init"),
        ("BEScrollViewScrollUpdate", b"new"),
        ("BEKeyEntry", b"init"),
        ("BEKeyEntry", b"new"),
        ("BEWebContentProcess", b"init"),
        ("BEWebContentProcess", b"new"),
        ("BETextDocumentContext", b"init"),
        ("BETextDocumentContext", b"new"),
        ("BEAccessibilityRemoteHostElement", b"init"),
        ("BEAccessibilityRemoteHostElement", b"new"),
        ("BEAccessibilityRemoteElement", b"init"),
        ("BEAccessibilityRemoteElement", b"new"),
    ):
        objc.registerUnavailableMethod(cls, sel)

    del sys.modules["BrowserEngineKit._metadata"]


globals().pop("_setup")()
