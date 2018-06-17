from PyObjCTools.TestSupport import *

import AVFoundation

class TestAVAssetExportSession (TestCase):
    @min_os_level('10.7')
    def testConstants(self):
        self.assertIsInstance(AVFoundation.AVAssetExportPreset640x480, unicode)
        self.assertIsInstance(AVFoundation.AVAssetExportPreset960x540, unicode)
        self.assertIsInstance(AVFoundation.AVAssetExportPreset1280x720, unicode)
        self.assertIsInstance(AVFoundation.AVAssetExportPreset1920x1080, unicode)
        self.assertIsInstance(AVFoundation.AVAssetExportPresetAppleM4A, unicode)
        self.assertIsInstance(AVFoundation.AVAssetExportPresetPassthrough, unicode)
        self.assertIsInstance(AVFoundation.AVAssetExportPresetAppleM4VCellular, unicode)
        self.assertIsInstance(AVFoundation.AVAssetExportPresetAppleM4ViPod, unicode)
        self.assertIsInstance(AVFoundation.AVAssetExportPresetAppleM4V480pSD, unicode)
        self.assertIsInstance(AVFoundation.AVAssetExportPresetAppleM4VAppleTV, unicode)
        self.assertIsInstance(AVFoundation.AVAssetExportPresetAppleM4VWiFi, unicode)
        self.assertIsInstance(AVFoundation.AVAssetExportPresetAppleM4V720pHD, unicode)
        self.assertIsInstance(AVFoundation.AVAssetExportPresetAppleProRes422LPCM, unicode)

        self.assertEqual(AVFoundation.AVAssetExportSessionStatusUnknown, 0)
        self.assertEqual(AVFoundation.AVAssetExportSessionStatusWaiting, 1)
        self.assertEqual(AVFoundation.AVAssetExportSessionStatusExporting, 2)
        self.assertEqual(AVFoundation.AVAssetExportSessionStatusCompleted, 3)
        self.assertEqual(AVFoundation.AVAssetExportSessionStatusFailed, 4)
        self.assertEqual(AVFoundation.AVAssetExportSessionStatusCancelled, 5)


    @min_os_level('10.8')
    def testConstants10_8(self):
        self.assertIsInstance(AVFoundation.AVAssetExportPresetAppleM4V1080pHD, unicode)

    @min_os_level('10.10')
    def testConstants10_10(self):
        self.assertIsInstance(AVFoundation.AVAssetExportPreset3840x2160, unicode)

    @min_os_level('10.11')
    def testConstants10_11(self):
        self.assertIsInstance(AVFoundation.AVAssetExportPresetLowQuality, unicode)
        self.assertIsInstance(AVFoundation.AVAssetExportPresetMediumQuality, unicode)
        self.assertIsInstance(AVFoundation.AVAssetExportPresetHighestQuality, unicode)

    @min_os_level('10.13')
    def testConstants10_13(self):
        self.assertIsInstance(AVFoundation.AVAssetExportPresetHEVCHighestQuality, unicode)
        self.assertIsInstance(AVFoundation.AVAssetExportPresetHEVC1920x1080, unicode)
        self.assertIsInstance(AVFoundation.AVAssetExportPresetHEVC3840x2160, unicode)

    @min_os_level('10.7')
    def testMethods(self):
        self.assertArgIsBlock(AVFoundation.AVAssetExportSession.determineCompatibilityOfExportPreset_withAsset_outputFileType_completionHandler_, 3, b'vZ')
        self.assertResultIsBOOL(AVFoundation.AVAssetExportSession.shouldOptimizeForNetworkUse)
        self.assertArgIsBOOL(AVFoundation.AVAssetExportSession.setShouldOptimizeForNetworkUse_, 0)
        self.assertArgIsBlock(AVFoundation.AVAssetExportSession.determineCompatibleFileTypesWithCompletionHandler_, 0, b'v@')
        self.assertArgIsBlock(AVFoundation.AVAssetExportSession.exportAsynchronouslyWithCompletionHandler_, 0, b'v')

    @min_os_level('10.10')
    def testMethods10_10(self):
        self.assertResultIsBOOL(AVFoundation.AVAssetExportSession.canPerformMultiplePassesOverSourceMediaData)
        self.assertArgIsBOOL(AVFoundation.AVAssetExportSession.setCanPerformMultiplePassesOverSourceMediaData_, 0)

if __name__ == "__main__":
    main()
