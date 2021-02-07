# This file is generated by objective.metadata
#
# Last update: Sat Jun 27 17:31:20 2020
#
# flake8: noqa

import objc, sys

if sys.maxsize > 2 ** 32:

    def sel32or64(a, b):
        return b


else:

    def sel32or64(a, b):
        return a


misc = {}
misc.update(
    {
        "MDQueryBatchingParams": objc.createStructType(
            "MDQueryBatchingParams",
            b"{_MDQueryBatchingParams=QQQQQQ}",
            [
                "first_max_num",
                "first_max_ms",
                "progress_max_num",
                "progress_max_ms",
                "update_max_num",
                "update_max_ms",
            ],
        )
    }
)
constants = """$kMDAttributeAllValues@^{__CFString=}$kMDAttributeDisplayValues@^{__CFString=}$kMDAttributeMultiValued@^{__CFString=}$kMDAttributeName@^{__CFString=}$kMDAttributeReadOnlyValues@^{__CFString=}$kMDAttributeType@^{__CFString=}$kMDExporterAvaliable@^{__CFString=}$kMDItemAcquisitionMake@^{__CFString=}$kMDItemAcquisitionModel@^{__CFString=}$kMDItemAlbum@^{__CFString=}$kMDItemAltitude@^{__CFString=}$kMDItemAperture@^{__CFString=}$kMDItemAppleLoopDescriptors@^{__CFString=}$kMDItemAppleLoopsKeyFilterType@^{__CFString=}$kMDItemAppleLoopsLoopMode@^{__CFString=}$kMDItemAppleLoopsRootKey@^{__CFString=}$kMDItemApplicationCategories@^{__CFString=}$kMDItemAttributeChangeDate@^{__CFString=}$kMDItemAudiences@^{__CFString=}$kMDItemAudioBitRate@^{__CFString=}$kMDItemAudioChannelCount@^{__CFString=}$kMDItemAudioEncodingApplication@^{__CFString=}$kMDItemAudioSampleRate@^{__CFString=}$kMDItemAudioTrackNumber@^{__CFString=}$kMDItemAuthorAddresses@^{__CFString=}$kMDItemAuthorEmailAddresses@^{__CFString=}$kMDItemAuthors@^{__CFString=}$kMDItemBitsPerSample@^{__CFString=}$kMDItemCFBundleIdentifier@^{__CFString=}$kMDItemCameraOwner@^{__CFString=}$kMDItemCity@^{__CFString=}$kMDItemCodecs@^{__CFString=}$kMDItemColorSpace@^{__CFString=}$kMDItemComment@^{__CFString=}$kMDItemComposer@^{__CFString=}$kMDItemContactKeywords@^{__CFString=}$kMDItemContentCreationDate@^{__CFString=}$kMDItemContentModificationDate@^{__CFString=}$kMDItemContentType@^{__CFString=}$kMDItemContentTypeTree@^{__CFString=}$kMDItemContributors@^{__CFString=}$kMDItemCopyright@^{__CFString=}$kMDItemCountry@^{__CFString=}$kMDItemCoverage@^{__CFString=}$kMDItemCreator@^{__CFString=}$kMDItemDateAdded@^{__CFString=}$kMDItemDeliveryType@^{__CFString=}$kMDItemDescription@^{__CFString=}$kMDItemDirector@^{__CFString=}$kMDItemDisplayName@^{__CFString=}$kMDItemDownloadedDate@^{__CFString=}$kMDItemDueDate@^{__CFString=}$kMDItemDurationSeconds@^{__CFString=}$kMDItemEXIFGPSVersion@^{__CFString=}$kMDItemEXIFVersion@^{__CFString=}$kMDItemEditors@^{__CFString=}$kMDItemEmailAddresses@^{__CFString=}$kMDItemEncodingApplications@^{__CFString=}$kMDItemExecutableArchitectures@^{__CFString=}$kMDItemExecutablePlatform@^{__CFString=}$kMDItemExposureMode@^{__CFString=}$kMDItemExposureProgram@^{__CFString=}$kMDItemExposureTimeSeconds@^{__CFString=}$kMDItemExposureTimeString@^{__CFString=}$kMDItemFNumber@^{__CFString=}$kMDItemFSContentChangeDate@^{__CFString=}$kMDItemFSCreationDate@^{__CFString=}$kMDItemFSExists@^{__CFString=}$kMDItemFSHasCustomIcon@^{__CFString=}$kMDItemFSInvisible@^{__CFString=}$kMDItemFSIsExtensionHidden@^{__CFString=}$kMDItemFSIsReadable@^{__CFString=}$kMDItemFSIsStationery@^{__CFString=}$kMDItemFSIsWriteable@^{__CFString=}$kMDItemFSLabel@^{__CFString=}$kMDItemFSName@^{__CFString=}$kMDItemFSNodeCount@^{__CFString=}$kMDItemFSOwnerGroupID@^{__CFString=}$kMDItemFSOwnerUserID@^{__CFString=}$kMDItemFSSize@^{__CFString=}$kMDItemFinderComment@^{__CFString=}$kMDItemFlashOnOff@^{__CFString=}$kMDItemFocalLength@^{__CFString=}$kMDItemFocalLength35mm@^{__CFString=}$kMDItemFonts@^{__CFString=}$kMDItemGPSAreaInformation@^{__CFString=}$kMDItemGPSDOP@^{__CFString=}$kMDItemGPSDateStamp@^{__CFString=}$kMDItemGPSDestBearing@^{__CFString=}$kMDItemGPSDestDistance@^{__CFString=}$kMDItemGPSDestLatitude@^{__CFString=}$kMDItemGPSDestLongitude@^{__CFString=}$kMDItemGPSDifferental@^{__CFString=}$kMDItemGPSMapDatum@^{__CFString=}$kMDItemGPSMeasureMode@^{__CFString=}$kMDItemGPSProcessingMethod@^{__CFString=}$kMDItemGPSStatus@^{__CFString=}$kMDItemGPSTrack@^{__CFString=}$kMDItemGenre@^{__CFString=}$kMDItemHTMLContent@^{__CFString=}$kMDItemHasAlphaChannel@^{__CFString=}$kMDItemHeadline@^{__CFString=}$kMDItemISOSpeed@^{__CFString=}$kMDItemIdentifier@^{__CFString=}$kMDItemImageDirection@^{__CFString=}$kMDItemInformation@^{__CFString=}$kMDItemInstantMessageAddresses@^{__CFString=}$kMDItemInstructions@^{__CFString=}$kMDItemIsApplicationManaged@^{__CFString=}$kMDItemIsGeneralMIDISequence@^{__CFString=}$kMDItemIsLikelyJunk@^{__CFString=}$kMDItemKeySignature@^{__CFString=}$kMDItemKeywords@^{__CFString=}$kMDItemKind@^{__CFString=}$kMDItemLabelID@^{__CFString=}$kMDItemLabelIcon@^{__CFString=}$kMDItemLabelKind@^{__CFString=}$kMDItemLabelUUID@^{__CFString=}$kMDItemLanguages@^{__CFString=}$kMDItemLastUsedDate@^{__CFString=}$kMDItemLatitude@^{__CFString=}$kMDItemLayerNames@^{__CFString=}$kMDItemLensModel@^{__CFString=}$kMDItemLongitude@^{__CFString=}$kMDItemLyricist@^{__CFString=}$kMDItemMaxAperture@^{__CFString=}$kMDItemMediaTypes@^{__CFString=}$kMDItemMeteringMode@^{__CFString=}$kMDItemMusicalGenre@^{__CFString=}$kMDItemMusicalInstrumentCategory@^{__CFString=}$kMDItemMusicalInstrumentName@^{__CFString=}$kMDItemNamedLocation@^{__CFString=}$kMDItemNumberOfPages@^{__CFString=}$kMDItemOrganizations@^{__CFString=}$kMDItemOrientation@^{__CFString=}$kMDItemOriginalFormat@^{__CFString=}$kMDItemOriginalSource@^{__CFString=}$kMDItemPageHeight@^{__CFString=}$kMDItemPageWidth@^{__CFString=}$kMDItemParticipants@^{__CFString=}$kMDItemPath@^{__CFString=}$kMDItemPerformers@^{__CFString=}$kMDItemPhoneNumbers@^{__CFString=}$kMDItemPixelCount@^{__CFString=}$kMDItemPixelHeight@^{__CFString=}$kMDItemPixelWidth@^{__CFString=}$kMDItemProducer@^{__CFString=}$kMDItemProfileName@^{__CFString=}$kMDItemProjects@^{__CFString=}$kMDItemPublishers@^{__CFString=}$kMDItemRecipientAddresses@^{__CFString=}$kMDItemRecipientEmailAddresses@^{__CFString=}$kMDItemRecipients@^{__CFString=}$kMDItemRecordingDate@^{__CFString=}$kMDItemRecordingYear@^{__CFString=}$kMDItemRedEyeOnOff@^{__CFString=}$kMDItemResolutionHeightDPI@^{__CFString=}$kMDItemResolutionWidthDPI@^{__CFString=}$kMDItemRights@^{__CFString=}$kMDItemSecurityMethod@^{__CFString=}$kMDItemSpeed@^{__CFString=}$kMDItemStarRating@^{__CFString=}$kMDItemStateOrProvince@^{__CFString=}$kMDItemStreamable@^{__CFString=}$kMDItemSubject@^{__CFString=}$kMDItemSupportFileType@^{__CFString=}$kMDItemTempo@^{__CFString=}$kMDItemTextContent@^{__CFString=}$kMDItemTheme@^{__CFString=}$kMDItemTimeSignature@^{__CFString=}$kMDItemTimestamp@^{__CFString=}$kMDItemTitle@^{__CFString=}$kMDItemTotalBitRate@^{__CFString=}$kMDItemURL@^{__CFString=}$kMDItemVersion@^{__CFString=}$kMDItemVideoBitRate@^{__CFString=}$kMDItemWhereFroms@^{__CFString=}$kMDItemWhiteBalance@^{__CFString=}$kMDLabelAddedNotification@^{__CFString=}$kMDLabelBundleURL@^{__CFString=}$kMDLabelChangedNotification@^{__CFString=}$kMDLabelContentChangeDate@^{__CFString=}$kMDLabelDisplayName@^{__CFString=}$kMDLabelIconData@^{__CFString=}$kMDLabelIconUUID@^{__CFString=}$kMDLabelIsMutuallyExclusiveSetMember@^{__CFString=}$kMDLabelKind@^{__CFString=}$kMDLabelKindIsMutuallyExclusiveSetKey@^{__CFString=}$kMDLabelKindVisibilityKey@^{__CFString=}$kMDLabelRemovedNotification@^{__CFString=}$kMDLabelSetsFinderColor@^{__CFString=}$kMDLabelUUID@^{__CFString=}$kMDLabelVisibility@^{__CFString=}$kMDPrivateVisibility@^{__CFString=}$kMDPublicVisibility@^{__CFString=}$kMDQueryDidFinishNotification@^{__CFString=}$kMDQueryDidUpdateNotification@^{__CFString=}$kMDQueryProgressNotification@^{__CFString=}$kMDQueryResultContentRelevance@^{__CFString=}$kMDQueryScopeAllIndexed@^{__CFString=}$kMDQueryScopeComputer@^{__CFString=}$kMDQueryScopeComputerIndexed@^{__CFString=}$kMDQueryScopeHome@^{__CFString=}$kMDQueryScopeNetwork@^{__CFString=}$kMDQueryScopeNetworkIndexed@^{__CFString=}$kMDQueryUpdateAddedItems@^{__CFString=}$kMDQueryUpdateChangedItems@^{__CFString=}$kMDQueryUpdateRemovedItems@^{__CFString=}$"""
enums = """$kMDLabelLocalDomain@1$kMDLabelUserDomain@0$kMDQueryAllowFSTranslation@8$kMDQueryReverseSortOrderFlag@1$kMDQuerySynchronous@1$kMDQueryWantsUpdates@4$"""
misc.update({})
functions = {
    "MDQueryCreate": (
        b"^{__MDQuery=}^{__CFAllocator=}^{__CFString=}^{__CFArray=}^{__CFArray=}",
        "",
        {"retval": {"already_cfretained": True}},
    ),
    "MDItemCopyAttributes": (
        b"^{__CFDictionary=}^{__MDItem=}^{__CFArray=}",
        "",
        {"retval": {"already_cfretained": True}},
    ),
    "MDLabelCreate": (
        b"^{__MDLabel=}^{__CFAllocator=}^{__CFString=}^{__CFString=}I",
        "",
        {"retval": {"already_cfretained": True}},
    ),
    "MDLabelGetTypeID": (b"Q",),
    "MDQueryGetAttributeValueOfResultAtIndex": (b"@^{__MDQuery=}^{__CFString=}q",),
    "MDQueryCreateForItems": (
        b"^{__MDQuery=}^{__CFAllocator=}^{__CFString=}^{__CFArray=}^{__CFArray=}^{__CFArray=}",
        "",
        {"retval": {"already_cfretained": True}},
    ),
    "MDQueryCopyValueListAttributes": (
        b"^{__CFArray=}^{__MDQuery=}",
        "",
        {"retval": {"already_cfretained": True}},
    ),
    "MDLabelCopyAttributeName": (
        b"^{__CFString=}^{__MDLabel=}",
        "",
        {"retval": {"already_cfretained": True}},
    ),
    "MDCopyLabelsWithKind": (
        b"^{__CFArray=}^{__CFString=}",
        "",
        {"retval": {"already_cfretained": True}},
    ),
    "MDQueryGetIndexOfResult": (b"q^{__MDQuery=}@",),
    "MDLabelDelete": (b"Z^{__MDLabel=}",),
    "MDSchemaCopyDisplayNameForAttribute": (
        b"^{__CFString=}^{__CFString=}",
        "",
        {"retval": {"already_cfretained": True}},
    ),
    "MDItemCopyAttribute": (
        b"@^{__MDItem=}^{__CFString=}",
        "",
        {"retval": {"already_cfretained": True}},
    ),
    "MDQueryDisableUpdates": (b"v^{__MDQuery=}",),
    "MDItemCopyAttributeList": (
        b"^{__CFDictionary=}^{__MDItem=}",
        "",
        {"retval": {"already_cfretained": True}, "variadic": True},
    ),
    "MDItemCreate": (
        b"^{__MDItem=}^{__CFAllocator=}^{__CFString=}",
        "",
        {"retval": {"already_cfretained": True}},
    ),
    "MDQueryGetSortOptionFlagsForAttribute": (b"I^{__MDQuery=}^{__CFString=}",),
    "MDQueryGetBatchingParameters": (b"{_MDQueryBatchingParams=QQQQQQ}^{__MDQuery=}",),
    "MDCopyLabelWithUUID": (
        b"^{__MDLabel=}^{__CFUUID=}",
        "",
        {"retval": {"already_cfretained": True}},
    ),
    "MDQueryEnableUpdates": (b"v^{__MDQuery=}",),
    "MDQuerySetMaxCount": (b"v^{__MDQuery=}q",),
    "MDQueryCopyValuesOfAttribute": (
        b"^{__CFArray=}^{__MDQuery=}^{__CFString=}",
        "",
        {"retval": {"already_cfretained": True}},
    ),
    "MDItemsCreateWithURLs": (
        b"^{__CFArray=}^{__CFAllocator=}^{__CFArray=}",
        "",
        {"retval": {"already_cfretained": True}},
    ),
    "MDQuerySetCreateValueFunction": (
        b"v^{__MDQuery=}^?^v^{_CFArrayCallBacks=q^?^?^?^?}",
        "",
        {
            "retval": {"already_cfretained": True},
            "arguments": {
                1: {
                    "callable": {
                        "retval": {"type": b"^v"},
                        "arguments": {
                            0: {"type": b"^{__MDQuery=}"},
                            1: {"type": b"^{__CFString=}"},
                            2: {"type": b"@"},
                            3: {"type": b"^v"},
                        },
                    }
                }
            },
        },
    ),
    "MDSchemaCopyDisplayDescriptionForAttribute": (
        b"^{__CFString=}^{__CFString=}",
        "",
        {"retval": {"already_cfretained": True}},
    ),
    "MDCopyLabelsMatchingExpression": (
        b"^{__CFArray=}^{__CFString=}",
        "",
        {"retval": {"already_cfretained": True}},
    ),
    "MDQuerySetSortOrder": (b"Z^{__MDQuery=}^{__CFArray=}",),
    "MDQuerySetSortComparator": (
        b"v^{__MDQuery=}^?^v",
        "",
        {
            "arguments": {
                1: {
                    "callable": {
                        "retval": {"type": sel32or64(b"i", b"q")},
                        "arguments": {
                            0: {
                                "type": b"^@",
                                "type_modifier": "n",
                                "c_array_of_variable_length": True,
                            },
                            1: {
                                "type": b"^@",
                                "type_modifier": "n",
                                "c_array_of_variable_length": True,
                            },
                            2: {"type": b"^v"},
                        },
                    }
                }
            }
        },
    ),
    "MDSchemaCopyAllAttributes": (
        b"^{__CFArray=}",
        "",
        {"retval": {"already_cfretained": True}},
    ),
    "MDQueryStop": (b"v^{__MDQuery=}",),
    "MDQuerySetSearchScope": (b"v^{__MDQuery=}^{__CFArray=}I",),
    "MDQueryIsGatheringComplete": (b"Z^{__MDQuery=}",),
    "MDQuerySetCreateResultFunction": (
        b"v^{__MDQuery=}^?^v^{_CFArrayCallBacks=q^?^?^?^?}",
        "",
        {
            "retval": {"already_cfretained": True},
            "arguments": {
                1: {
                    "callable": {
                        "retval": {"type": b"^v"},
                        "arguments": {
                            0: {"type": b"^{__MDQuery=}"},
                            1: {"type": b"^{__MDItem=}"},
                            2: {"type": b"^v"},
                        },
                    }
                }
            },
        },
    ),
    "MDItemCopyLabels": (
        b"^{__CFArray=}^{__MDItem=}",
        "",
        {"retval": {"already_cfretained": True}},
    ),
    "MDSchemaCopyAttributesForContentType": (
        b"^{__CFDictionary=}^{__CFString=}",
        "",
        {"retval": {"already_cfretained": True}},
    ),
    "MDItemSetLabel": (b"Z^{__MDItem=}^{__MDLabel=}",),
    "MDQueryExecute": (b"Z^{__MDQuery=}Q",),
    "MDQuerySetDispatchQueue": (b"v^{__MDQuery=}@",),
    "MDLabelSetAttributes": (b"Z^{__MDLabel=}^{__CFDictionary=}",),
    "MDItemGetTypeID": (b"Q",),
    "MDQueryCopyQueryString": (
        b"^{__CFString=}^{__MDQuery=}",
        "",
        {"retval": {"already_cfretained": True}},
    ),
    "MDQueryCopySortingAttributes": (
        b"^{__CFArray=}^{__MDQuery=}",
        "",
        {"retval": {"already_cfretained": True}},
    ),
    "MDQuerySetSortOptionFlagsForAttribute": (b"Z^{__MDQuery=}^{__CFString=}I",),
    "MDQuerySetBatchingParameters": (b"v^{__MDQuery=}{_MDQueryBatchingParams=QQQQQQ}",),
    "MDQueryCreateSubset": (
        b"^{__MDQuery=}^{__CFAllocator=}^{__MDQuery=}^{__CFString=}^{__CFArray=}^{__CFArray=}",
        "",
        {"retval": {"already_cfretained": True}},
    ),
    "MDQueryGetTypeID": (b"Q",),
    "MDItemCreateWithURL": (
        b"^{__MDItem=}^{__CFAllocator=}^{__CFURL=}",
        "",
        {"retval": {"already_cfretained": True}},
    ),
    "MDQuerySetSortComparatorBlock": (
        b"v^{__MDQuery=}@?",
        "",
        {
            "arguments": {
                1: {
                    "callable": {
                        "retval": {"type": sel32or64(b"i", b"q")},
                        "arguments": {
                            0: {"type": "^v"},
                            1: {
                                "type": "^@",
                                "type_modifier": "n",
                                "c_array_of_variable_length": True,
                            },
                            2: {
                                "type": "^@",
                                "type_modifier": "n",
                                "c_array_of_variable_length": True,
                            },
                        },
                    },
                    "block": {
                        "retval": {"type": b"q"},
                        "arguments": {0: {"type": b"^@"}, 1: {"type": b"^@"}},
                    },
                }
            }
        },
    ),
    "MDItemCopyAttributeNames": (
        b"^{__CFArray=}^{__MDItem=}",
        "",
        {"retval": {"already_cfretained": True}},
    ),
    "MDQueryGetCountOfResultsWithAttributeValue": (b"q^{__MDQuery=}^{__CFString=}@",),
    "MDItemsCopyAttributes": (
        b"^{__CFArray=}^{__CFArray=}^{__CFArray=}",
        "",
        {"retval": {"already_cfretained": True}},
    ),
    "MDQueryGetResultCount": (b"q^{__MDQuery=}",),
    "MDCopyLabelKinds": (
        b"^{__CFArray=}",
        "",
        {"retval": {"already_cfretained": True}},
    ),
    "MDItemRemoveLabel": (b"Z^{__MDItem=}^{__MDLabel=}",),
    "MDQueryGetResultAtIndex": (b"@^{__MDQuery=}q",),
    "MDSchemaCopyMetaAttributesForAttribute": (
        b"^{__CFDictionary=}^{__CFString=}",
        "",
        {"retval": {"already_cfretained": True}},
    ),
    "MDLabelCopyAttribute": (
        b"@^{__MDLabel=}^{__CFString=}",
        "",
        {"retval": {"already_cfretained": True}},
    ),
}
aliases = {
    "MD_AVAIL": "AVAILABLE_MAC_OS_X_VERSION_10_4_AND_LATER",
    "MD_AVAIL_LEOPARD": "AVAILABLE_MAC_OS_X_VERSION_10_5_AND_LATER",
}
cftypes = [
    ("MDItemRef", b"^{__MDItem=}", None, None),
    ("MDLabelRef", b"^{__MDLabel=}", None, None),
    ("MDQueryRef", b"^{__MDQuery=}", None, None),
]
expressions = {}

# END OF FILE
