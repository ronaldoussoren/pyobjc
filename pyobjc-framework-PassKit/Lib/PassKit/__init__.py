"""
Python mapping for the PassKit framework.

This module does not contain docstrings for the wrapped code, check Apple's
documentation for details on how to use these functions and classes.
"""


def _setup():
    import sys

    import Foundation
    import objc
    from . import _metadata, _PassKit

    dir_func, getattr_func = objc.createFrameworkDirAndGetattr(
        name="PassKit",
        frameworkIdentifier="com.apple.PassKit",
        frameworkPath=objc.pathForFramework(
            "/System/Library/Frameworks/PassKit.framework"
        ),
        globals_dict=globals(),
        inline_list=None,
        parents=(
            _PassKit,
            Foundation,
        ),
        metadict=_metadata.__dict__,
    )

    globals()["__dir__"] = dir_func
    globals()["__getattr__"] = getattr_func

    for cls, sel in (
        ("PKIssuerProvisioningExtensionPassEntry", b"init"),
        ("PKPaymentOrderDetails", b"init"),
        ("PKPaymentOrderDetails", b"new"),
        ("PKPaymentTokenContext", b"init"),
        ("PKDeferredPaymentRequest", b"init"),
        ("PKPayLaterView", b"init"),
        ("PKPayLaterView", b"new"),
        ("PKPayLaterView", b"initWithFrame:"),
        ("PKPayLaterView", b"initWithCoder:"),
        ("PKIdentityButton", b"initWithFrame:"),
        ("PKIdentityButton", b"initWithFrame:primaryAction:"),
        ("PKIdentityElement", b"init"),
        ("PKIdentityElement", b"new"),
        ("PKAddSecureElementPassConfiguration", b"init"),
        ("PKAddSecureElementPassConfiguration", b"new"),
        ("PKDateComponentsRange", b"init"),
        ("PKStoredValuePassBalance", b"init"),
        ("PKStoredValuePassBalance", b"new"),
        ("PKIdentityDocument", b"init"),
        ("PKIdentityDocument", b"new"),
        ("PKIdentityIntentToStore", b"init"),
        ("PKIdentityIntentToStore", b"new"),
        ("PKAutomaticReloadPaymentRequest", b"init"),
        ("PKShareSecureElementPassViewController", b"init"),
        ("PKVehicleConnectionSession", b"init"),
        ("PKVehicleConnectionSession", b"new"),
        ("PKRecurringPaymentRequest", b"init"),
        ("PKShareablePassMetadataPreview", b"init"),
        ("PKShareablePassMetadataPreview", b"new"),
        ("PKIdentityDocumentMetadata", b"init"),
        ("PKIdentityDocumentMetadata", b"new"),
        ("PKIdentityAnyOfDescriptor", b"init"),
        ("PKIdentityAnyOfDescriptor", b"new"),
    ):
        objc.registerUnavailableMethod(cls, sel)

    del sys.modules["PassKit._metadata"]


globals().pop("_setup")()
