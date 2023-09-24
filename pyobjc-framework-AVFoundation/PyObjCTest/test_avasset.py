import AVFoundation
from PyObjCTools.TestSupport import TestCase, min_os_level, min_sdk_level


class TestAVAssetHelper(AVFoundation.NSObject):
    def isAssociatedWithFragmentMinder(self):
        return True


class TestAVAsset(TestCase):
    def test_enum_types(self):
        self.assertIsEnumType(AVFoundation.AVAssetReferenceRestrictions)

    @min_os_level("10.7")
    def testMethods(self):
        self.assertResultIsBOOL(AVFoundation.AVAsset.providesPreciseDurationAndTiming)
        self.assertResultIsBOOL(AVFoundation.AVAsset.hasProtectedContent)
        self.assertResultIsBOOL(AVFoundation.AVAsset.isPlayable)
        self.assertResultIsBOOL(AVFoundation.AVAsset.isExportable)
        self.assertResultIsBOOL(AVFoundation.AVAsset.isReadable)
        self.assertResultIsBOOL(AVFoundation.AVAsset.isComposable)

        self.assertResultIsBOOL(AVFoundation.AVURLAsset.isPlayableExtendedMIMEType_)

    @min_os_level("10.11")
    def testMethods10_11(self):
        self.assertResultIsBOOL(AVFoundation.AVAsset.canContainFragments)
        self.assertResultIsBOOL(AVFoundation.AVAsset.containsFragments)
        self.assertResultIsBOOL(AVFoundation.AVAsset.isCompatibleWithAirPlayVideo)

    @min_os_level("10.12.4")
    def testMethods10_12_4(self):
        self.assertResultIsBOOL(
            AVFoundation.AVURLAsset.mayRequireContentKeysForMediaDataProcessing
        )

    @min_os_level("12.0")
    def testMethods12_0(self):
        self.assertArgIsBlock(
            AVFoundation.AVAsset.loadTrackWithTrackID_completionHandler_, 1, b"v@@"
        )
        self.assertArgIsBlock(
            AVFoundation.AVAsset.loadTracksWithMediaType_completionHandler_, 1, b"v@@"
        )
        self.assertArgIsBlock(
            AVFoundation.AVAsset.loadTracksWithMediaCharacteristic_completionHandler_,
            1,
            b"v@@",
        )
        self.assertArgIsBlock(
            AVFoundation.AVAsset.loadMetadataForFormat_completionHandler_, 1, b"v@@"
        )
        self.assertArgIsBlock(
            AVFoundation.AVAsset.loadChapterMetadataGroupsWithTitleLocale_containingItemsWithCommonKeys_completionHandler_,
            2,
            b"v@@",
        )
        self.assertArgIsBlock(
            AVFoundation.AVAsset.loadChapterMetadataGroupsBestMatchingPreferredLanguages_completionHandler_,
            1,
            b"v@@",
        )
        self.assertArgIsBlock(
            AVFoundation.AVAsset.loadMediaSelectionGroupForMediaCharacteristic_completionHandler_,
            1,
            b"v@@",
        )
        self.assertArgIsBlock(
            AVFoundation.AVURLAsset.findCompatibleTrackForCompositionTrack_completionHandler_,
            1,
            b"v@@",
        )
        self.assertArgIsBlock(
            AVFoundation.AVURLAsset.loadTrackWithTrackID_completionHandler_, 1, b"v@@"
        )
        self.assertArgIsBlock(
            AVFoundation.AVURLAsset.loadTracksWithMediaType_completionHandler_,
            1,
            b"v@@",
        )
        self.assertArgIsBlock(
            AVFoundation.AVURLAsset.loadTracksWithMediaCharacteristic_completionHandler_,
            1,
            b"v@@",
        )

    @min_os_level("10.7")
    def testConstants(self):
        self.assertEqual(AVFoundation.AVAssetReferenceRestrictionForbidNone, 0)
        self.assertEqual(
            AVFoundation.AVAssetReferenceRestrictionForbidRemoteReferenceToLocal, 1 << 0
        )
        self.assertEqual(
            AVFoundation.AVAssetReferenceRestrictionForbidLocalReferenceToRemote, 1 << 1
        )
        self.assertEqual(
            AVFoundation.AVAssetReferenceRestrictionForbidCrossSiteReference, 1 << 2
        )
        self.assertEqual(
            AVFoundation.AVAssetReferenceRestrictionForbidLocalReferenceToLocal, 1 << 3
        )
        self.assertEqual(AVFoundation.AVAssetReferenceRestrictionForbidAll, 0xFFFF)
        self.assertEqual(
            AVFoundation.AVAssetReferenceRestrictionDefaultPolicy,
            AVFoundation.AVAssetReferenceRestrictionForbidLocalReferenceToRemote,
        )

        self.assertIsInstance(
            AVFoundation.AVURLAssetPreferPreciseDurationAndTimingKey, str
        )
        self.assertIsInstance(AVFoundation.AVURLAssetReferenceRestrictionsKey, str)

    @min_os_level("10.10")
    def testConstants10_10(self):
        self.assertIsInstance(
            AVFoundation.AVURLAssetShouldSupportAliasDataReferencesKey, str
        )

    @min_os_level("10.11")
    def testConstants10_11(self):
        self.assertIsInstance(AVFoundation.AVAssetDurationDidChangeNotification, str)
        self.assertIsInstance(
            AVFoundation.AVAssetContainsFragmentsDidChangeNotification, str
        )
        self.assertIsInstance(AVFoundation.AVAssetWasDefragmentedNotification, str)
        self.assertIsInstance(
            AVFoundation.AVAssetChapterMetadataGroupsDidChangeNotification, str
        )
        self.assertIsInstance(
            AVFoundation.AVAssetMediaSelectionGroupsDidChangeNotification, str
        )

    @min_os_level("10.15")
    def testConstants10_15(self):
        self.assertIsInstance(AVFoundation.AVURLAssetAllowsCellularAccessKey, str)
        self.assertIsInstance(
            AVFoundation.AVURLAssetAllowsExpensiveNetworkAccessKey, str
        )
        self.assertIsInstance(
            AVFoundation.AVURLAssetAllowsConstrainedNetworkAccessKey, str
        )

    @min_os_level("12.0")
    def testConstants12_0(self):
        self.assertIsInstance(AVFoundation.AVURLAssetURLRequestAttributionKey, str)

    @min_os_level("13.0")
    def testConstants13_0(self):
        self.assertIsInstance(AVFoundation.AVURLAssetHTTPUserAgentKey, str)
        self.assertIsInstance(AVFoundation.AVURLAssetPrimarySessionIdentifierKey, str)

    @min_os_level("14.0")
    def testConstants14_0(self):
        self.assertIsInstance(AVFoundation.AVURLAssetOverrideMIMETypeKey, str)

    @min_sdk_level("10.11")
    def testProtocols(self):
        self.assertProtocolExists("AVFragmentMinding")

    @min_sdk_level("10.11")
    def testProtocolMethods(self):
        self.assertResultIsBOOL(TestAVAssetHelper.isAssociatedWithFragmentMinder)
