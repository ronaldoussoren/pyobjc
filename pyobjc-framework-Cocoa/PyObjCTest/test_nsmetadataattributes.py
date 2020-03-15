import Foundation
from PyObjCTools.TestSupport import TestCase, min_os_level


class TestNSMetaDataAttributes(TestCase):
    @min_os_level("10.7")
    def testConstants10_7(self):
        self.assertIsInstance(Foundation.NSMetadataItemFSNameKey, str)
        self.assertIsInstance(Foundation.NSMetadataItemDisplayNameKey, str)
        self.assertIsInstance(Foundation.NSMetadataItemURLKey, str)
        self.assertIsInstance(Foundation.NSMetadataItemPathKey, str)
        self.assertIsInstance(Foundation.NSMetadataItemFSSizeKey, str)
        self.assertIsInstance(Foundation.NSMetadataItemFSCreationDateKey, str)
        self.assertIsInstance(Foundation.NSMetadataItemFSContentChangeDateKey, str)
        self.assertIsInstance(Foundation.NSMetadataItemIsUbiquitousKey, str)
        self.assertIsInstance(
            Foundation.NSMetadataUbiquitousItemHasUnresolvedConflictsKey, str
        )
        self.assertIsInstance(Foundation.NSMetadataUbiquitousItemIsDownloadedKey, str)
        self.assertIsInstance(Foundation.NSMetadataUbiquitousItemIsDownloadingKey, str)
        self.assertIsInstance(Foundation.NSMetadataUbiquitousItemIsUploadedKey, str)
        self.assertIsInstance(Foundation.NSMetadataUbiquitousItemIsUploadingKey, str)
        self.assertIsInstance(
            Foundation.NSMetadataUbiquitousItemPercentDownloadedKey, str
        )
        self.assertIsInstance(
            Foundation.NSMetadataUbiquitousItemPercentUploadedKey, str
        )

    @min_os_level("10.9")
    def testConstants10_9(self):
        self.assertIsInstance(Foundation.NSMetadataItemContentTypeKey, str)
        self.assertIsInstance(Foundation.NSMetadataItemContentTypeTreeKey, str)
        self.assertIsInstance(
            Foundation.NSMetadataUbiquitousItemDownloadingStatusKey, str
        )
        self.assertIsInstance(
            Foundation.NSMetadataUbiquitousItemDownloadingStatusDownloaded, str
        )
        self.assertIsInstance(
            Foundation.NSMetadataUbiquitousItemDownloadingStatusCurrent, str
        )
        self.assertIsInstance(
            Foundation.NSMetadataUbiquitousItemDownloadingErrorKey, str
        )
        self.assertIsInstance(Foundation.NSMetadataUbiquitousItemUploadingErrorKey, str)
        self.assertIsInstance(Foundation.NSMetadataItemAttributeChangeDateKey, str)
        self.assertIsInstance(Foundation.NSMetadataItemKeywordsKey, str)
        self.assertIsInstance(Foundation.NSMetadataItemTitleKey, str)
        self.assertIsInstance(Foundation.NSMetadataItemAuthorsKey, str)
        self.assertIsInstance(Foundation.NSMetadataItemEditorsKey, str)
        self.assertIsInstance(Foundation.NSMetadataItemParticipantsKey, str)
        self.assertIsInstance(Foundation.NSMetadataItemProjectsKey, str)
        self.assertIsInstance(Foundation.NSMetadataItemDownloadedDateKey, str)
        self.assertIsInstance(Foundation.NSMetadataItemWhereFromsKey, str)
        self.assertIsInstance(Foundation.NSMetadataItemCommentKey, str)
        self.assertIsInstance(Foundation.NSMetadataItemCopyrightKey, str)
        self.assertIsInstance(Foundation.NSMetadataItemLastUsedDateKey, str)
        self.assertIsInstance(Foundation.NSMetadataItemContentCreationDateKey, str)
        self.assertIsInstance(Foundation.NSMetadataItemContentModificationDateKey, str)
        self.assertIsInstance(Foundation.NSMetadataItemDateAddedKey, str)
        self.assertIsInstance(Foundation.NSMetadataItemDurationSecondsKey, str)
        self.assertIsInstance(Foundation.NSMetadataItemContactKeywordsKey, str)
        self.assertIsInstance(Foundation.NSMetadataItemVersionKey, str)
        self.assertIsInstance(Foundation.NSMetadataItemPixelHeightKey, str)
        self.assertIsInstance(Foundation.NSMetadataItemPixelWidthKey, str)
        self.assertIsInstance(Foundation.NSMetadataItemPixelCountKey, str)
        self.assertIsInstance(Foundation.NSMetadataItemColorSpaceKey, str)
        self.assertIsInstance(Foundation.NSMetadataItemBitsPerSampleKey, str)
        self.assertIsInstance(Foundation.NSMetadataItemFlashOnOffKey, str)
        self.assertIsInstance(Foundation.NSMetadataItemFocalLengthKey, str)
        self.assertIsInstance(Foundation.NSMetadataItemAcquisitionMakeKey, str)
        self.assertIsInstance(Foundation.NSMetadataItemAcquisitionModelKey, str)
        self.assertIsInstance(Foundation.NSMetadataItemISOSpeedKey, str)
        self.assertIsInstance(Foundation.NSMetadataItemOrientationKey, str)
        self.assertIsInstance(Foundation.NSMetadataItemLayerNamesKey, str)
        self.assertIsInstance(Foundation.NSMetadataItemWhiteBalanceKey, str)
        self.assertIsInstance(Foundation.NSMetadataItemApertureKey, str)
        self.assertIsInstance(Foundation.NSMetadataItemProfileNameKey, str)
        self.assertIsInstance(Foundation.NSMetadataItemResolutionWidthDPIKey, str)
        self.assertIsInstance(Foundation.NSMetadataItemResolutionHeightDPIKey, str)
        self.assertIsInstance(Foundation.NSMetadataItemExposureModeKey, str)
        self.assertIsInstance(Foundation.NSMetadataItemExposureTimeSecondsKey, str)
        self.assertIsInstance(Foundation.NSMetadataItemEXIFVersionKey, str)
        self.assertIsInstance(Foundation.NSMetadataItemCameraOwnerKey, str)
        self.assertIsInstance(Foundation.NSMetadataItemFocalLength35mmKey, str)
        self.assertIsInstance(Foundation.NSMetadataItemLensModelKey, str)
        self.assertIsInstance(Foundation.NSMetadataItemEXIFGPSVersionKey, str)
        self.assertIsInstance(Foundation.NSMetadataItemAltitudeKey, str)
        self.assertIsInstance(Foundation.NSMetadataItemLatitudeKey, str)
        self.assertIsInstance(Foundation.NSMetadataItemLongitudeKey, str)
        self.assertIsInstance(Foundation.NSMetadataItemSpeedKey, str)
        self.assertIsInstance(Foundation.NSMetadataItemTimestampKey, str)
        self.assertIsInstance(Foundation.NSMetadataItemGPSTrackKey, str)
        self.assertIsInstance(Foundation.NSMetadataItemImageDirectionKey, str)
        self.assertIsInstance(Foundation.NSMetadataItemGPSStatusKey, str)
        self.assertIsInstance(Foundation.NSMetadataItemGPSMeasureModeKey, str)
        self.assertIsInstance(Foundation.NSMetadataItemGPSDOPKey, str)
        self.assertIsInstance(Foundation.NSMetadataItemGPSMapDatumKey, str)
        self.assertIsInstance(Foundation.NSMetadataItemGPSDestLatitudeKey, str)
        self.assertIsInstance(Foundation.NSMetadataItemGPSDestLongitudeKey, str)
        self.assertIsInstance(Foundation.NSMetadataItemGPSDestBearingKey, str)
        self.assertIsInstance(Foundation.NSMetadataItemGPSProcessingMethodKey, str)
        self.assertIsInstance(Foundation.NSMetadataItemGPSAreaInformationKey, str)
        self.assertIsInstance(Foundation.NSMetadataItemGPSDateStampKey, str)
        self.assertIsInstance(Foundation.NSMetadataItemGPSDifferentalKey, str)
        self.assertIsInstance(Foundation.NSMetadataItemCodecsKey, str)
        self.assertIsInstance(Foundation.NSMetadataItemMediaTypesKey, str)
        self.assertIsInstance(Foundation.NSMetadataItemStreamableKey, str)
        self.assertIsInstance(Foundation.NSMetadataItemTotalBitRateKey, str)
        self.assertIsInstance(Foundation.NSMetadataItemVideoBitRateKey, str)
        self.assertIsInstance(Foundation.NSMetadataItemAudioBitRateKey, str)
        self.assertIsInstance(Foundation.NSMetadataItemDeliveryTypeKey, str)
        self.assertIsInstance(Foundation.NSMetadataItemAlbumKey, str)
        self.assertIsInstance(Foundation.NSMetadataItemHasAlphaChannelKey, str)
        self.assertIsInstance(Foundation.NSMetadataItemRedEyeOnOffKey, str)
        self.assertIsInstance(Foundation.NSMetadataItemMeteringModeKey, str)
        self.assertIsInstance(Foundation.NSMetadataItemMaxApertureKey, str)
        self.assertIsInstance(Foundation.NSMetadataItemFNumberKey, str)
        self.assertIsInstance(Foundation.NSMetadataItemExposureProgramKey, str)
        self.assertIsInstance(Foundation.NSMetadataItemExposureTimeStringKey, str)
        self.assertIsInstance(Foundation.NSMetadataItemHeadlineKey, str)
        self.assertIsInstance(Foundation.NSMetadataItemInstructionsKey, str)
        self.assertIsInstance(Foundation.NSMetadataItemCityKey, str)
        self.assertIsInstance(Foundation.NSMetadataItemStateOrProvinceKey, str)
        self.assertIsInstance(Foundation.NSMetadataItemCountryKey, str)
        self.assertIsInstance(Foundation.NSMetadataItemTextContentKey, str)
        self.assertIsInstance(Foundation.NSMetadataItemAudioSampleRateKey, str)
        self.assertIsInstance(Foundation.NSMetadataItemAudioChannelCountKey, str)
        self.assertIsInstance(Foundation.NSMetadataItemTempoKey, str)
        self.assertIsInstance(Foundation.NSMetadataItemKeySignatureKey, str)
        self.assertIsInstance(Foundation.NSMetadataItemTimeSignatureKey, str)
        self.assertIsInstance(Foundation.NSMetadataItemAudioEncodingApplicationKey, str)
        self.assertIsInstance(Foundation.NSMetadataItemComposerKey, str)
        self.assertIsInstance(Foundation.NSMetadataItemLyricistKey, str)
        self.assertIsInstance(Foundation.NSMetadataItemAudioTrackNumberKey, str)
        self.assertIsInstance(Foundation.NSMetadataItemRecordingDateKey, str)
        self.assertIsInstance(Foundation.NSMetadataItemMusicalGenreKey, str)
        self.assertIsInstance(Foundation.NSMetadataItemIsGeneralMIDISequenceKey, str)
        self.assertIsInstance(Foundation.NSMetadataItemRecordingYearKey, str)
        self.assertIsInstance(Foundation.NSMetadataItemOrganizationsKey, str)
        self.assertIsInstance(Foundation.NSMetadataItemLanguagesKey, str)
        self.assertIsInstance(Foundation.NSMetadataItemRightsKey, str)
        self.assertIsInstance(Foundation.NSMetadataItemPublishersKey, str)
        self.assertIsInstance(Foundation.NSMetadataItemContributorsKey, str)
        self.assertIsInstance(Foundation.NSMetadataItemCoverageKey, str)
        self.assertIsInstance(Foundation.NSMetadataItemSubjectKey, str)
        self.assertIsInstance(Foundation.NSMetadataItemThemeKey, str)
        self.assertIsInstance(Foundation.NSMetadataItemDescriptionKey, str)
        self.assertIsInstance(Foundation.NSMetadataItemIdentifierKey, str)
        self.assertIsInstance(Foundation.NSMetadataItemAudiencesKey, str)
        self.assertIsInstance(Foundation.NSMetadataItemNumberOfPagesKey, str)
        self.assertIsInstance(Foundation.NSMetadataItemPageWidthKey, str)
        self.assertIsInstance(Foundation.NSMetadataItemPageHeightKey, str)
        self.assertIsInstance(Foundation.NSMetadataItemSecurityMethodKey, str)
        self.assertIsInstance(Foundation.NSMetadataItemCreatorKey, str)
        self.assertIsInstance(Foundation.NSMetadataItemEncodingApplicationsKey, str)
        self.assertIsInstance(Foundation.NSMetadataItemDueDateKey, str)
        self.assertIsInstance(Foundation.NSMetadataItemStarRatingKey, str)
        self.assertIsInstance(Foundation.NSMetadataItemPhoneNumbersKey, str)
        self.assertIsInstance(Foundation.NSMetadataItemEmailAddressesKey, str)
        self.assertIsInstance(Foundation.NSMetadataItemInstantMessageAddressesKey, str)
        self.assertIsInstance(Foundation.NSMetadataItemKindKey, str)
        self.assertIsInstance(Foundation.NSMetadataItemRecipientsKey, str)
        self.assertIsInstance(Foundation.NSMetadataItemFinderCommentKey, str)
        self.assertIsInstance(Foundation.NSMetadataItemFontsKey, str)
        self.assertIsInstance(Foundation.NSMetadataItemAppleLoopsRootKeyKey, str)
        self.assertIsInstance(Foundation.NSMetadataItemAppleLoopsKeyFilterTypeKey, str)
        self.assertIsInstance(Foundation.NSMetadataItemAppleLoopsLoopModeKey, str)
        self.assertIsInstance(Foundation.NSMetadataItemAppleLoopDescriptorsKey, str)
        self.assertIsInstance(
            Foundation.NSMetadataItemMusicalInstrumentCategoryKey, str
        )
        self.assertIsInstance(Foundation.NSMetadataItemMusicalInstrumentNameKey, str)
        self.assertIsInstance(Foundation.NSMetadataItemCFBundleIdentifierKey, str)
        self.assertIsInstance(Foundation.NSMetadataItemInformationKey, str)
        self.assertIsInstance(Foundation.NSMetadataItemDirectorKey, str)
        self.assertIsInstance(Foundation.NSMetadataItemProducerKey, str)
        self.assertIsInstance(Foundation.NSMetadataItemGenreKey, str)
        self.assertIsInstance(Foundation.NSMetadataItemPerformersKey, str)
        self.assertIsInstance(Foundation.NSMetadataItemOriginalFormatKey, str)
        self.assertIsInstance(Foundation.NSMetadataItemOriginalSourceKey, str)
        self.assertIsInstance(Foundation.NSMetadataItemAuthorEmailAddressesKey, str)
        self.assertIsInstance(Foundation.NSMetadataItemRecipientEmailAddressesKey, str)
        self.assertIsInstance(Foundation.NSMetadataItemAuthorAddressesKey, str)
        self.assertIsInstance(Foundation.NSMetadataItemRecipientAddressesKey, str)
        self.assertIsInstance(Foundation.NSMetadataItemIsLikelyJunkKey, str)
        self.assertIsInstance(Foundation.NSMetadataItemExecutableArchitecturesKey, str)
        self.assertIsInstance(Foundation.NSMetadataItemExecutablePlatformKey, str)
        self.assertIsInstance(Foundation.NSMetadataItemApplicationCategoriesKey, str)
        self.assertIsInstance(Foundation.NSMetadataItemIsApplicationManagedKey, str)

    @min_os_level("10.10")
    def testConstants10_10(self):
        self.assertIsInstance(
            Foundation.NSMetadataUbiquitousItemDownloadRequestedKey, str
        )
        self.assertIsInstance(
            Foundation.NSMetadataUbiquitousItemIsExternalDocumentKey, str
        )
        self.assertIsInstance(
            Foundation.NSMetadataUbiquitousItemContainerDisplayNameKey, str
        )
        self.assertIsInstance(
            Foundation.NSMetadataUbiquitousItemURLInLocalContainerKey, str
        )

    @min_os_level("10.12")
    def testConstants10_12(self):
        self.assertIsInstance(
            Foundation.NSMetadataUbiquitousSharedItemCurrentUserRoleKey, str
        )
        self.assertIsInstance(
            Foundation.NSMetadataUbiquitousSharedItemCurrentUserPermissionsKey, str
        )
        self.assertIsInstance(
            Foundation.NSMetadataUbiquitousSharedItemOwnerNameComponentsKey, str
        )
        self.assertIsInstance(
            Foundation.NSMetadataUbiquitousSharedItemMostRecentEditorNameComponentsKey,
            str,
        )
        self.assertIsInstance(Foundation.NSMetadataUbiquitousSharedItemRoleOwner, str)
        self.assertIsInstance(
            Foundation.NSMetadataUbiquitousSharedItemRoleParticipant, str
        )
        self.assertIsInstance(
            Foundation.NSMetadataUbiquitousSharedItemPermissionsReadOnly, str
        )
        self.assertIsInstance(
            Foundation.NSMetadataUbiquitousSharedItemPermissionsReadWrite, str
        )
