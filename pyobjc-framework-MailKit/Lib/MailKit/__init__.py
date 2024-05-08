"""
Python mapping for the MailKit framework.

This module does not contain docstrings for the wrapped code, check Apple's
documentation for details on how to use these functions and classes.
"""


def _setup():
    import sys

    import AppKit
    import objc
    from . import _metadata

    dir_func, getattr_func = objc.createFrameworkDirAndGetattr(
        name="MailKit",
        frameworkIdentifier="com.apple.MailKit",
        frameworkPath=objc.pathForFramework(
            "/System/Library/Frameworks/MailKit.framework"
        ),
        globals_dict=globals(),
        inline_list=None,
        parents=(AppKit,),
        metadict=_metadata.__dict__,
    )

    globals()["__dir__"] = dir_func
    globals()["__getattr__"] = getattr_func

    for cls, sel in (
        ("MEComposeSession", b"init"),
        ("MEComposeSession", b"new"),
        ("MEDecodedMessage", b"init"),
        ("MEDecodedMessage", b"new"),
        ("MEMessageAction", b"init"),
        ("MEMessageAction", b"new"),
        ("MEMessageActionDecision", b"init"),
        ("MEMessageActionDecision", b"new"),
        ("MEExtensionManager", b"init"),
        ("MEExtensionManager", b"new"),
        ("MEMessage", b"init"),
        ("MEMessage", b"new"),
        ("MEMessageSecurityInformation", b"init"),
        ("MEMessageSecurityInformation", b"new"),
        ("MEMessageSigner", b"init"),
        ("MEMessageSigner", b"new"),
        ("MEEmailAddress", b"init"),
        ("MEEmailAddress", b"new"),
        ("MEMessageEncodingResult", b"init"),
        ("MEMessageEncodingResult", b"new"),
        ("MEOutgoingMessageEncodingStatus", b"init"),
        ("MEOutgoingMessageEncodingStatus", b"new"),
        ("MEAddressAnnotation", b"init"),
        ("MEAddressAnnotation", b"new"),
        ("MEDecodedMessageBanner", b"init"),
        ("MEDecodedMessageBanner", b"new"),
    ):
        objc.registerUnavailableMethod(cls, sel)

    del sys.modules["MailKit._metadata"]


globals().pop("_setup")()
