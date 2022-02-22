import AVFoundation
from PyObjCTools.TestSupport import TestCase, min_os_level


class TestAVAssetTrack(TestCase):
    def test_typed_enum(self):
        self.assertIsTypedEnum(AVFoundation.AVTrackAssociationType, str)

    @min_os_level("10.7")
    def testMethods10_7(self):
        self.assertResultIsBOOL(AVFoundation.AVAssetTrack.isEnabled)
        self.assertResultIsBOOL(AVFoundation.AVAssetTrack.isSelfContained)
        self.assertResultIsBOOL(AVFoundation.AVAssetTrack.hasMediaCharacteristic_)

    @min_os_level("10.8")
    def testMethods10_8(self):
        self.assertResultIsBOOL(AVFoundation.AVAssetTrack.isPlayable)

    @min_os_level("10.10")
    def testMethods10_10(self):
        self.assertResultIsBOOL(AVFoundation.AVAssetTrack.requiresFrameReordering)
        self.assertResultIsBOOL(AVFoundation.AVAssetTrack.canProvideSampleCursors)

    @min_os_level("10.13")
    def testMethods10_13(self):
        self.assertResultIsBOOL(AVFoundation.AVAssetTrack.isDecodable)

    @min_os_level("12.0")
    def testMethods12_0(self):
        self.assertArgIsBlock(
            AVFoundation.AVAssetTrack.loadSegmentForTrackTime_completionHandler_,
            1,
            b"v@@",
        )
        self.assertArgIsBlock(
            AVFoundation.AVAssetTrack.loadSamplePresentationTimeForTrackTime_completionHandler_,
            1,
            b"v" + AVFoundation.CMTime.__typestr__ + b"@",
        )
        self.assertArgIsBlock(
            AVFoundation.AVAssetTrack.loadMetadataForFormat_completionHandler_,
            1,
            b"v@@",
        )
        self.assertArgIsBlock(
            AVFoundation.AVAssetTrack.loadAssociatedTracksOfType_completionHandler_,
            1,
            b"v@@",
        )

    @min_os_level("10.9")
    def testConstants10_9(self):
        self.assertIsInstance(AVFoundation.AVTrackAssociationTypeAudioFallback, str)
        self.assertIsInstance(AVFoundation.AVTrackAssociationTypeChapterList, str)
        self.assertIsInstance(
            AVFoundation.AVTrackAssociationTypeForcedSubtitlesOnly, str
        )
        self.assertIsInstance(AVFoundation.AVTrackAssociationTypeSelectionFollower, str)
        self.assertIsInstance(AVFoundation.AVTrackAssociationTypeTimecode, str)

    @min_os_level("10.10")
    def testConstants10_10(self):
        self.assertIsInstance(AVFoundation.AVTrackAssociationTypeMetadataReferent, str)

    @min_os_level("10.11")
    def testConstants10_11(self):
        self.assertIsInstance(
            AVFoundation.AVAssetTrackTimeRangeDidChangeNotification, str
        )
        self.assertIsInstance(
            AVFoundation.AVAssetTrackSegmentsDidChangeNotification, str
        )
        self.assertIsInstance(
            AVFoundation.AVAssetTrackTrackAssociationsDidChangeNotification, str
        )
