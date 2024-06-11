# This file is generated by objective.metadata
#
# Last update: Tue Jun 11 10:09:37 2024
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
constants = """$CSActionIdentifier$CSIndexErrorDomain$CSMailboxArchive$CSMailboxDrafts$CSMailboxInbox$CSMailboxJunk$CSMailboxSent$CSMailboxTrash$CSQueryContinuationActionType$CSSearchQueryErrorDomain$CSSearchQueryString$CSSearchableItemActionType$CSSearchableItemActivityIdentifier$CSSuggestionHighlightAttributeName$CoreSpotlightVersionNumber@d$CoreSpotlightVersionString@*$"""
enums = """$CSIndexErrorCodeIndexUnavailableError@-1000$CSIndexErrorCodeIndexingUnsupported@-1005$CSIndexErrorCodeInvalidClientStateError@-1002$CSIndexErrorCodeInvalidItemError@-1001$CSIndexErrorCodeMismatchedClientState@-1006$CSIndexErrorCodeQuotaExceeded@-1004$CSIndexErrorCodeRemoteConnectionError@-1003$CSIndexErrorCodeUnknownError@-1$CSSearchQueryErrorCodeCancelled@-2003$CSSearchQueryErrorCodeIndexUnreachable@-2001$CSSearchQueryErrorCodeInvalidQuery@-2002$CSSearchQueryErrorCodeUnknown@-2000$CSSearchQuerySourceOptionAllowMail@1$CSSearchQuerySourceOptionDefault@0$CSSuggestionKindCustom@1$CSSuggestionKindDefault@2$CSSuggestionKindNone@0$CSUserInteractionDefault@0$CSUserInteractionFocus@1$CSUserInteractionSelect@0$"""
misc.update(
    {
        "CSSearchQuerySourceOptions": NewType("CSSearchQuerySourceOptions", int),
        "CSUserInteraction": NewType("CSUserInteraction", int),
        "CSIndexErrorCode": NewType("CSIndexErrorCode", int),
        "CSSuggestionKind": NewType("CSSuggestionKind", int),
        "CSSearchQueryErrorCode": NewType("CSSearchQueryErrorCode", int),
    }
)
misc.update({})
misc.update({})
aliases = {
    "CSUserInteractionDefault": "CSUserInteractionSelect",
    "CS_TVOS_UNAVAILABLE": "__TVOS_PROHIBITED",
}
r = objc.registerMetaDataForSelector
objc._updatingMetadata(True)
try:
    r(
        b"CSCustomAttributeKey",
        b"initWithKeyName:searchable:searchableByDefault:unique:multiValued:",
        {
            "arguments": {
                3: {"type": "Z"},
                4: {"type": "Z"},
                5: {"type": "Z"},
                6: {"type": "Z"},
            }
        },
    )
    r(b"CSCustomAttributeKey", b"isMultiValued", {"retval": {"type": "Z"}})
    r(b"CSCustomAttributeKey", b"isSearchable", {"retval": {"type": "Z"}})
    r(b"CSCustomAttributeKey", b"isSearchableByDefault", {"retval": {"type": "Z"}})
    r(b"CSCustomAttributeKey", b"isUnique", {"retval": {"type": "Z"}})
    r(b"CSCustomAttributeKey", b"setMultiValued:", {"arguments": {2: {"type": "Z"}}})
    r(b"CSCustomAttributeKey", b"setSearchable:", {"arguments": {2: {"type": "Z"}}})
    r(
        b"CSCustomAttributeKey",
        b"setSearchableByDefault:",
        {"arguments": {2: {"type": "Z"}}},
    )
    r(b"CSCustomAttributeKey", b"setUnique:", {"arguments": {2: {"type": "Z"}}})
    r(
        b"CSImportExtension",
        b"updateAttributes:forFileAtURL:error:",
        {
            "retval": {"type": "Z"},
            "arguments": {3: {"type_modifier": b"o"}, 4: {"type_modifier": b"o"}},
        },
    )
    r(
        b"CSSearchQuery",
        b"completionHandler",
        {
            "retval": {
                "callable": {
                    "retval": {"type": b"v"},
                    "arguments": {0: {"type": b"^v"}, 1: {"type": b"@"}},
                }
            }
        },
    )
    r(
        b"CSSearchQuery",
        b"foundItemsHandler",
        {
            "retval": {
                "callable": {
                    "retval": {"type": b"v"},
                    "arguments": {0: {"type": b"^v"}, 1: {"type": b"@"}},
                }
            }
        },
    )
    r(b"CSSearchQuery", b"isCancelled", {"retval": {"type": "Z"}})
    r(
        b"CSSearchQuery",
        b"setCompletionHandler:",
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
        b"CSSearchQuery",
        b"setFoundItemsHandler:",
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
        b"CSSearchableIndex",
        b"deleteAllSearchableItemsWithCompletionHandler:",
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
        b"CSSearchableIndex",
        b"deleteSearchableItemsWithDomainIdentifiers:completionHandler:",
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
        b"CSSearchableIndex",
        b"deleteSearchableItemsWithIdentifiers:completionHandler:",
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
        b"CSSearchableIndex",
        b"endIndexBatchWithClientState:completionHandler:",
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
        b"CSSearchableIndex",
        b"endIndexBatchWithExpectedClientState:newClientState:completionHandler:",
        {
            "arguments": {
                4: {
                    "callable": {
                        "retval": {"type": b"v"},
                        "arguments": {0: {"type": b"^v"}, 1: {"type": b"@"}},
                    }
                }
            }
        },
    )
    r(
        b"CSSearchableIndex",
        b"fetchDataForBundleIdentifier:itemIdentifier:contentType:completionHandler:",
        {
            "arguments": {
                5: {
                    "callable": {
                        "retval": {"type": b"v"},
                        "arguments": {
                            0: {"type": b"^v"},
                            1: {"type": b"@"},
                            2: {"type": b"@"},
                        },
                    }
                }
            }
        },
    )
    r(
        b"CSSearchableIndex",
        b"fetchLastClientStateWithCompletionHandler:",
        {
            "arguments": {
                2: {
                    "callable": {
                        "retval": {"type": b"v"},
                        "arguments": {
                            0: {"type": b"^v"},
                            1: {"type": b"@"},
                            2: {"type": b"@"},
                        },
                    }
                }
            }
        },
    )
    r(
        b"CSSearchableIndex",
        b"indexSearchableItems:completionHandler:",
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
    r(b"CSSearchableIndex", b"isIndexingAvailable", {"retval": {"type": b"Z"}})
    r(b"CSSearchableItem", b"isUpdate", {"retval": {"type": b"Z"}})
    r(b"CSSearchableItem", b"setIsUpdate:", {"arguments": {2: {"type": b"Z"}}})
    r(
        b"CSUserQuery",
        b"foundSuggestionsHandler",
        {
            "retval": {
                "callable": {
                    "retval": {"type": b"v"},
                    "arguments": {0: {"type": b"^v"}, 1: {"type": b"@"}},
                }
            }
        },
    )
    r(
        b"CSUserQuery",
        b"setFoundSuggestionsHandler:",
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
    r(b"CSUserQueryContext", b"disableSemanticSearch", {"retval": {"type": b"Z"}})
    r(b"CSUserQueryContext", b"enableRankedResults", {"retval": {"type": b"Z"}})
    r(
        b"CSUserQueryContext",
        b"setDisableSemanticSearch:",
        {"arguments": {2: {"type": b"Z"}}},
    )
    r(
        b"CSUserQueryContext",
        b"setEnableRankedResults:",
        {"arguments": {2: {"type": b"Z"}}},
    )
    r(
        b"NSObject",
        b"dataForSearchableIndex:itemIdentifier:typeIdentifier:error:",
        {
            "required": False,
            "retval": {"type": b"@"},
            "arguments": {
                2: {"type": b"@"},
                3: {"type": b"@"},
                4: {"type": b"@"},
                5: {"type": "^@", "type_modifier": b"o"},
            },
        },
    )
    r(
        b"NSObject",
        b"fileURLForSearchableIndex:itemIdentifier:typeIdentifier:inPlace:error:",
        {
            "required": False,
            "retval": {"type": b"@"},
            "arguments": {
                2: {"type": b"@"},
                3: {"type": b"@"},
                4: {"type": b"@"},
                5: {"type": "Z"},
                6: {"type": "^@", "type_modifier": b"o"},
            },
        },
    )
    r(
        b"NSObject",
        b"searchableIndex:reindexAllSearchableItemsWithAcknowledgementHandler:",
        {
            "required": True,
            "retval": {"type": b"v"},
            "arguments": {
                2: {"type": b"@"},
                3: {
                    "callable": {
                        "retval": {"type": b"v"},
                        "arguments": {0: {"type": b"^v"}},
                    },
                    "type": "@?",
                },
            },
        },
    )
    r(
        b"NSObject",
        b"searchableIndex:reindexSearchableItemsWithIdentifiers:acknowledgementHandler:",
        {
            "required": True,
            "retval": {"type": b"v"},
            "arguments": {
                2: {"type": b"@"},
                3: {"type": b"@"},
                4: {
                    "callable": {
                        "retval": {"type": b"v"},
                        "arguments": {0: {"type": b"^v"}},
                    },
                    "type": "@?",
                },
            },
        },
    )
    r(
        b"NSObject",
        b"searchableIndexDidFinishThrottle:",
        {"required": False, "retval": {"type": b"v"}, "arguments": {2: {"type": b"@"}}},
    )
    r(
        b"NSObject",
        b"searchableIndexDidThrottle:",
        {"required": False, "retval": {"type": b"v"}, "arguments": {2: {"type": b"@"}}},
    )
finally:
    objc._updatingMetadata(False)

objc.registerNewKeywordsFromSelector("CSCustomAttributeKey", b"initWithKeyName:")
objc.registerNewKeywordsFromSelector(
    "CSCustomAttributeKey",
    b"initWithKeyName:searchable:searchableByDefault:unique:multiValued:",
)
objc.registerNewKeywordsFromSelector("CSLocalizedString", b"initWithLocalizedStrings:")
objc.registerNewKeywordsFromSelector(
    "CSPerson", b"initWithDisplayName:handles:handleIdentifier:"
)
objc.registerNewKeywordsFromSelector(
    "CSSearchQuery", b"initWithQueryString:attributes:"
)
objc.registerNewKeywordsFromSelector(
    "CSSearchQuery", b"initWithQueryString:queryContext:"
)
objc.registerNewKeywordsFromSelector("CSSearchableIndex", b"initWithName:")
objc.registerNewKeywordsFromSelector(
    "CSSearchableIndex", b"initWithName:protectionClass:"
)
objc.registerNewKeywordsFromSelector(
    "CSSearchableItem", b"initWithUniqueIdentifier:domainIdentifier:attributeSet:"
)
objc.registerNewKeywordsFromSelector(
    "CSSearchableItemAttributeSet", b"initWithContentType:"
)
objc.registerNewKeywordsFromSelector(
    "CSSearchableItemAttributeSet", b"initWithItemContentType:"
)
objc.registerNewKeywordsFromSelector(
    "CSUserQuery", b"initWithUserQueryString:userQueryContext:"
)
expressions = {}

# END OF FILE
