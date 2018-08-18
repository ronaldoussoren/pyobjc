from PyObjCTools.TestSupport import *

import AVFoundation

class TestAVAssetTrack (TestCase):
    @min_os_level('10.7')
    def testMethods10_7(self):
        self.assertResultIsBOOL(AVFoundation.AVAssetTrack.isEnabled)
        self.assertResultIsBOOL(AVFoundation.AVAssetTrack.isSelfContained)
        self.assertResultIsBOOL(AVFoundation.AVAssetTrack.hasMediaCharacteristic_)

    @min_os_level('10.8')
    def testMethods10_8(self):
        self.assertResultIsBOOL(AVFoundation.AVAssetTrack.isPlayable)

    @min_os_level('10.10')
    def testMethods10_10(self):
        self.assertResultIsBOOL(AVFoundation.AVAssetTrack.requiresFrameReordering)
        self.assertResultIsBOOL(AVFoundation.AVAssetTrack.canProvideSampleCursors)

    @min_os_level('10.13')
    def testMethods10_13(self):
        self.assertResultIsBOOL(AVFoundation.AVAssetTrack.isDecodable)

    @min_os_level('10.9')
    def testConstants10_9(self):
        self.assertIsInstance(AVFoundation.AVTrackAssociationTypeAudioFallback, unicode)
        self.assertIsInstance(AVFoundation.AVTrackAssociationTypeChapterList, unicode)
        self.assertIsInstance(AVFoundation.AVTrackAssociationTypeForcedSubtitlesOnly, unicode)
        self.assertIsInstance(AVFoundation.AVTrackAssociationTypeSelectionFollower, unicode)
        self.assertIsInstance(AVFoundation.AVTrackAssociationTypeTimecode, unicode)

    @min_os_level('10.10')
    def testConstants10_10(self):
        self.assertIsInstance(AVFoundation.AVTrackAssociationTypeMetadataReferent, unicode)

    @min_os_level('10.11')
    def testConstants10_11(self):
        self.assertIsInstance(AVFoundation.AVAssetTrackTimeRangeDidChangeNotification, unicode)
        self.assertIsInstance(AVFoundation.AVAssetTrackSegmentsDidChangeNotification, unicode)
        self.assertIsInstance(AVFoundation.AVAssetTrackTrackAssociationsDidChangeNotification, unicode)

if __name__ == "__main__":
    main()
