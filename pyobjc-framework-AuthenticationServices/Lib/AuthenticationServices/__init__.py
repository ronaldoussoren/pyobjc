"""
Python mapping for the AuthenticationServices framework.

This module does not contain docstrings for the wrapped code, check Apple's
documentation for details on how to use these functions and classes.
"""


def _setup():
    import sys

    import Foundation
    import objc
    from . import _metadata, _AuthenticationServices

    dir_func, getattr_func = objc.createFrameworkDirAndGetattr(
        name="AuthenticationServices",
        frameworkIdentifier="com.apple.AuthenticationServices",
        frameworkPath=objc.pathForFramework(
            "/System/Library/Frameworks/AuthenticationServices.framework"
        ),
        globals_dict=globals(),
        inline_list=None,
        parents=(_AuthenticationServices, Foundation),
        metadict=_metadata.__dict__,
    )

    globals()["__dir__"] = dir_func
    globals()["__getattr__"] = getattr_func

    for cls, sel in (
        ("ASAuthorizationProviderExtensionLoginManager", b"init"),
        ("ASAuthorizationProviderExtensionLoginManager", b"new"),
        ("ASAuthorizationPublicKeyCredentialLargeBlobRegistrationInput", b"init"),
        ("ASAuthorizationPublicKeyCredentialLargeBlobRegistrationInput", b"new"),
        ("ASAuthorizationSecurityKeyPublicKeyCredentialAssertion", b"init"),
        ("ASAuthorizationSecurityKeyPublicKeyCredentialAssertion", b"new"),
        ("ASAuthorizationPlatformPublicKeyCredentialAssertion", b"init"),
        ("ASAuthorizationPlatformPublicKeyCredentialAssertion", b"new"),
        ("ASPasskeyCredentialIdentity", b"init"),
        (
            "ASCredentialProviderExtensionContext",
            b"completeRequestReturningItems:completionHandler:",
        ),
        ("ASAuthorizationWebBrowserPlatformPublicKeyCredential", b"init"),
        ("ASAuthorizationWebBrowserPlatformPublicKeyCredential", b"new"),
        ("ASAuthorization", b"init"),
        ("ASAuthorization", b"new"),
        ("ASAuthorizationPlatformPublicKeyCredentialRegistrationRequest", b"init"),
        ("ASAuthorizationPlatformPublicKeyCredentialRegistrationRequest", b"new"),
        ("ASAuthorizationPublicKeyCredentialLargeBlobAssertionInput", b"init"),
        ("ASAuthorizationPublicKeyCredentialLargeBlobAssertionInput", b"new"),
        ("ASAuthorizationSecurityKeyPublicKeyCredentialProvider", b"init"),
        ("ASAuthorizationSecurityKeyPublicKeyCredentialProvider", b"new"),
        ("ASAuthorizationPlatformPublicKeyCredentialAssertionRequest", b"init"),
        ("ASAuthorizationPlatformPublicKeyCredentialAssertionRequest", b"new"),
        ("ASPasskeyCredentialRequest", b"init"),
        ("ASPublicKeyCredentialClientData", b"init"),
        ("ASPublicKeyCredentialClientData", b"new"),
        ("ASWebAuthenticationSessionCallback", b"init"),
        ("ASWebAuthenticationSessionCallback", b"new"),
        ("ASSettingsHelper", b"init"),
        ("ASSettingsHelper", b"new"),
        ("ASCredentialIdentityStore", b"init"),
        ("ASAuthorizationRequest", b"init"),
        ("ASAuthorizationRequest", b"new"),
        ("ASPasskeyCredentialRequestParameters", b"init"),
        ("ASPasswordCredentialRequest", b"init"),
        ("ASAuthorizationAppleIDCredential", b"init"),
        ("ASAuthorizationAppleIDCredential", b"new"),
        ("ASAuthorizationController", b"init"),
        ("ASAuthorizationController", b"new"),
        ("ASAuthorizationSecurityKeyPublicKeyCredentialRegistrationRequest", b"init"),
        ("ASAuthorizationSecurityKeyPublicKeyCredentialRegistrationRequest", b"new"),
        ("ASWebAuthenticationSession", b"init"),
        ("ASWebAuthenticationSession", b"new"),
        ("ASAuthorizationSingleSignOnProvider", b"init"),
        ("ASAuthorizationSingleSignOnProvider", b"new"),
        ("ASAuthorizationPlatformPublicKeyCredentialProvider", b"init"),
        ("ASAuthorizationPlatformPublicKeyCredentialProvider", b"new"),
        ("ASWebAuthenticationSessionRequest", b"init"),
        ("ASWebAuthenticationSessionRequest", b"new"),
        ("ASAuthorizationProviderExtensionLoginConfiguration", b"init"),
        ("ASAuthorizationProviderExtensionLoginConfiguration", b"new"),
        ("ASAuthorizationPlatformPublicKeyCredentialDescriptor", b"init"),
        ("ASAuthorizationPlatformPublicKeyCredentialDescriptor", b"new"),
        ("ASAuthorizationSecurityKeyPublicKeyCredentialDescriptor", b"init"),
        ("ASAuthorizationSecurityKeyPublicKeyCredentialDescriptor", b"new"),
        ("ASAuthorizationProviderExtensionUserLoginConfiguration", b"init"),
        ("ASAuthorizationProviderExtensionUserLoginConfiguration", b"new"),
        ("ASAuthorizationSingleSignOnCredential", b"init"),
        ("ASAuthorizationSingleSignOnCredential", b"new"),
        ("ASPasswordCredentialIdentity", b"init"),
        ("ASAuthorizationPlatformPublicKeyCredentialRegistration", b"init"),
        ("ASAuthorizationPlatformPublicKeyCredentialRegistration", b"new"),
        ("ASAuthorizationPublicKeyCredentialLargeBlobAssertionOutput", b"init"),
        ("ASAuthorizationPublicKeyCredentialLargeBlobAssertionOutput", b"new"),
        ("ASAuthorizationPublicKeyCredentialParameters", b"init"),
        ("ASAuthorizationPublicKeyCredentialParameters", b"new"),
    ):
        objc.registerUnavailableMethod(cls, sel)

    del sys.modules["AuthenticationServices._metadata"]


globals().pop("_setup")()
