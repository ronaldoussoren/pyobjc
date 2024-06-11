# This file is generated by objective.metadata
#
# Last update: Tue Jun 11 10:13:57 2024
#
# flake8: noqa

import objc, sys
from typing import NewType

if sys.maxsize > 2**32:

    def sel32or64(a, b):
        return b

else:

    def sel32or64(a, b):
        return a


if objc.arch == "arm64":

    def selAorI(a, b):
        return a

else:

    def selAorI(a, b):
        return b


misc = {}
constants = """$MEComposeSessionErrorDomain$MEMessageSecurityErrorDomain$"""
enums = """$MEComposeSessionErrorCodeInvalidBody@2$MEComposeSessionErrorCodeInvalidHeaders@1$MEComposeSessionErrorCodeInvalidRecipients@0$MEComposeUserActionForward@4$MEComposeUserActionNewMessage@1$MEComposeUserActionReply@2$MEComposeUserActionReplyAll@3$MEMessageActionFlagBlue@6$MEMessageActionFlagDefaultColor@1$MEMessageActionFlagGray@8$MEMessageActionFlagGreen@5$MEMessageActionFlagNone@0$MEMessageActionFlagOrange@3$MEMessageActionFlagPurple@7$MEMessageActionFlagRed@2$MEMessageActionFlagYellow@4$MEMessageActionMessageColorBlue@6$MEMessageActionMessageColorGray@7$MEMessageActionMessageColorGreen@1$MEMessageActionMessageColorNone@0$MEMessageActionMessageColorOrange@3$MEMessageActionMessageColorPurple@5$MEMessageActionMessageColorRed@4$MEMessageActionMessageColorYellow@2$MEMessageEncryptionStateEncrypted@2$MEMessageEncryptionStateNotEncrypted@1$MEMessageEncryptionStateUnknown@0$MEMessageSecurityDecodingError@1$MEMessageSecurityEncodingError@0$MEMessageStateDraft@1$MEMessageStateReceived@0$MEMessageStateSending@2$"""
misc.update(
    {
        "MEMessageSecurityErrorCode": NewType("MEMessageSecurityErrorCode", int),
        "MEMessageActionFlag": NewType("MEMessageActionFlag", int),
        "MEComposeSessionErrorCode": NewType("MEComposeSessionErrorCode", int),
        "MEMessageActionMessageColor": NewType("MEMessageActionMessageColor", int),
        "MEMessageEncryptionState": NewType("MEMessageEncryptionState", int),
        "MEMessageState": NewType("MEMessageState", int),
        "MEComposeUserAction": NewType("MEComposeUserAction", int),
    }
)
misc.update({})
misc.update({})
r = objc.registerMetaDataForSelector
objc._updatingMetadata(True)
try:
    r(b"MEComposeContext", b"isEncrypted", {"retval": {"type": b"Z"}})
    r(b"MEComposeContext", b"isSigned", {"retval": {"type": b"Z"}})
    r(b"MEComposeContext", b"shouldEncrypt", {"retval": {"type": b"Z"}})
    r(b"MEComposeContext", b"shouldSign", {"retval": {"type": b"Z"}})
    r(
        b"MEDecodedMessageBanner",
        b"initWithTitle:primaryActionTitle:dismissable:",
        {"arguments": {4: {"type": b"Z"}}},
    )
    r(b"MEDecodedMessageBanner", b"isDismissable", {"retval": {"type": b"Z"}})
    r(
        b"MEEncodedOutgoingMessage",
        b"initWithRawData:isSigned:isEncrypted:",
        {"arguments": {3: {"type": b"Z"}, 4: {"type": b"Z"}}},
    )
    r(b"MEEncodedOutgoingMessage", b"isEncrypted", {"retval": {"type": b"Z"}})
    r(b"MEEncodedOutgoingMessage", b"isSigned", {"retval": {"type": b"Z"}})
    r(
        b"MEExtensionManager",
        b"reloadContentBlockerWithIdentifier:completionHandler:",
        {
            "arguments": {
                3: {
                    "callable": {
                        "retval": {"type": b"v"},
                        "arguments": {0: {"type": b"^v"}, 1: {"type": b"@"}},
                    }
                }
            }
        },
    )
    r(
        b"MEExtensionManager",
        b"reloadVisibleMessagesWithCompletionHandler:",
        {
            "arguments": {
                2: {
                    "callable": {
                        "retval": {"type": b"v"},
                        "arguments": {0: {"type": b"^v"}, 1: {"type": b"@"}},
                    }
                }
            }
        },
    )
    r(
        b"MEMessageSecurityInformation",
        b"initWithSigners:isEncrypted:signingError:encryptionError:",
        {"arguments": {3: {"type": b"Z"}}},
    )
    r(
        b"MEMessageSecurityInformation",
        b"initWithSigners:isEncrypted:signingError:encryptionError:shouldBlockRemoteContent:localizedRemoteContentBlockingReason:",
        {"arguments": {3: {"type": b"Z"}, 6: {"type": b"Z"}}},
    )
    r(b"MEMessageSecurityInformation", b"isEncrypted", {"retval": {"type": b"Z"}})
    r(
        b"MEMessageSecurityInformation",
        b"shouldBlockRemoteContent",
        {"retval": {"type": b"Z"}},
    )
    r(b"MEOutgoingMessageEncodingStatus", b"canEncrypt", {"retval": {"type": b"Z"}})
    r(b"MEOutgoingMessageEncodingStatus", b"canSign", {"retval": {"type": b"Z"}})
    r(
        b"MEOutgoingMessageEncodingStatus",
        b"initWithCanSign:canEncrypt:securityError:addressesFailingEncryption:",
        {"arguments": {2: {"type": b"Z"}, 3: {"type": b"Z"}}},
    )
    r(
        b"NSObject",
        b"additionalHeadersForSession:",
        {"required": False, "retval": {"type": b"@"}, "arguments": {2: {"type": b"@"}}},
    )
    r(b"NSObject", b"contentRulesJSON", {"required": True, "retval": {"type": b"@"}})
    r(
        b"NSObject",
        b"decideActionForMessage:completionHandler:",
        {
            "required": True,
            "retval": {"type": b"v"},
            "arguments": {
                2: {"type": b"@"},
                3: {
                    "callable": {
                        "retval": {"type": b"v"},
                        "arguments": {0: {"type": b"^v"}, 1: {"type": b"@"}},
                    },
                    "type": b"@?",
                },
            },
        },
    )
    r(
        b"NSObject",
        b"decodedMessageForMessageData:",
        {"required": True, "retval": {"type": b"@"}, "arguments": {2: {"type": b"@"}}},
    )
    r(
        b"NSObject",
        b"encodeMessage:composeContext:completionHandler:",
        {
            "required": True,
            "retval": {"type": b"v"},
            "arguments": {
                2: {"type": b"@"},
                3: {"type": b"@"},
                4: {
                    "callable": {
                        "retval": {"type": b"v"},
                        "arguments": {0: {"type": b"^v"}, 1: {"type": b"@"}},
                    },
                    "type": b"@?",
                },
            },
        },
    )
    r(
        b"NSObject",
        b"extensionViewControllerForMessageContext:",
        {"required": True, "retval": {"type": b"@"}, "arguments": {2: {"type": b"@"}}},
    )
    r(
        b"NSObject",
        b"extensionViewControllerForMessageSigners:",
        {"required": True, "retval": {"type": b"@"}, "arguments": {2: {"type": b"@"}}},
    )
    r(
        b"NSObject",
        b"getEncodingStatusForMessage:composeContext:completionHandler:",
        {
            "required": True,
            "retval": {"type": b"v"},
            "arguments": {
                2: {"type": b"@"},
                3: {"type": b"@"},
                4: {
                    "callable": {
                        "retval": {"type": b"v"},
                        "arguments": {0: {"type": b"^v"}, 1: {"type": b"@"}},
                    },
                    "type": b"@?",
                },
            },
        },
    )
    r(
        b"NSObject",
        b"handlerForComposeSession:",
        {"required": False, "retval": {"type": b"@"}, "arguments": {2: {"type": b"@"}}},
    )
    r(
        b"NSObject",
        b"handlerForContentBlocker",
        {"required": False, "retval": {"type": b"@"}},
    )
    r(
        b"NSObject",
        b"handlerForMessageActions",
        {"required": False, "retval": {"type": b"@"}},
    )
    r(
        b"NSObject",
        b"handlerForMessageSecurity",
        {"required": False, "retval": {"type": b"@"}},
    )
    r(
        b"NSObject",
        b"mailComposeSessionDidBegin:",
        {"required": True, "retval": {"type": b"v"}, "arguments": {2: {"type": b"@"}}},
    )
    r(
        b"NSObject",
        b"mailComposeSessionDidEnd:",
        {"required": True, "retval": {"type": b"v"}, "arguments": {2: {"type": b"@"}}},
    )
    r(
        b"NSObject",
        b"primaryActionClickedForMessageContext:completionHandler:",
        {
            "required": True,
            "retval": {"type": b"v"},
            "arguments": {
                2: {"type": b"@"},
                3: {
                    "callable": {
                        "retval": {"type": b"v"},
                        "arguments": {0: {"type": b"^v"}, 1: {"type": b"@"}},
                    },
                    "type": b"@?",
                },
            },
        },
    )
    r(b"NSObject", b"requiredHeaders", {"required": False, "retval": {"type": b"@"}})
    r(
        b"NSObject",
        b"session:annotateAddressesWithCompletionHandler:",
        {
            "required": False,
            "retval": {"type": b"v"},
            "arguments": {
                2: {"type": b"@"},
                3: {
                    "callable": {
                        "retval": {"type": b"v"},
                        "arguments": {0: {"type": b"^v"}, 1: {"type": b"@"}},
                    },
                    "type": b"@?",
                },
            },
        },
    )
    r(
        b"NSObject",
        b"session:canSendMessageWithCompletionHandler:",
        {
            "required": False,
            "retval": {"type": b"v"},
            "arguments": {
                2: {"type": b"@"},
                3: {
                    "callable": {
                        "retval": {"type": b"v"},
                        "arguments": {0: {"type": b"^v"}, 1: {"type": b"@"}},
                    },
                    "type": b"@?",
                },
            },
        },
    )
    r(
        b"NSObject",
        b"viewControllerForSession:",
        {"required": True, "retval": {"type": b"@"}, "arguments": {2: {"type": b"@"}}},
    )
finally:
    objc._updatingMetadata(False)

objc.registerNewKeywordsFromSelector(
    "MEDecodedMessage", b"initWithData:securityInformation:context:"
)
objc.registerNewKeywordsFromSelector(
    "MEDecodedMessage", b"initWithData:securityInformation:context:banner:"
)
objc.registerNewKeywordsFromSelector(
    "MEDecodedMessageBanner", b"initWithTitle:primaryActionTitle:dismissable:"
)
objc.registerNewKeywordsFromSelector("MEEmailAddress", b"initWithRawString:")
objc.registerNewKeywordsFromSelector(
    "MEEncodedOutgoingMessage", b"initWithRawData:isSigned:isEncrypted:"
)
objc.registerNewKeywordsFromSelector(
    "MEMessageEncodingResult", b"initWithEncodedMessage:signingError:encryptionError:"
)
objc.registerNewKeywordsFromSelector(
    "MEMessageSecurityInformation",
    b"initWithSigners:isEncrypted:signingError:encryptionError:",
)
objc.registerNewKeywordsFromSelector(
    "MEMessageSecurityInformation",
    b"initWithSigners:isEncrypted:signingError:encryptionError:shouldBlockRemoteContent:localizedRemoteContentBlockingReason:",
)
objc.registerNewKeywordsFromSelector(
    "MEMessageSigner", b"initWithEmailAddresses:signatureLabel:context:"
)
objc.registerNewKeywordsFromSelector(
    "MEOutgoingMessageEncodingStatus",
    b"initWithCanSign:canEncrypt:securityError:addressesFailingEncryption:",
)
expressions = {}

# END OF FILE
