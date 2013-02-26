from PyObjCTools.TestSupport import *

import AVFoundation

try:
    unicode
except NameError:
    unicode = str

class TestAVAssetExportSession (TestCase):
    def test_constants(self):
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
        self.assertIsInstance(AVFoundation.AVAssetExportPresetAppleM4V1080pHD, unicode)
        self.assertIsInstance(AVFoundation.AVAssetExportPresetAppleProRes422LPCM, unicode)

        self.assertEqual(AVFoundation.AVAssetExportSessionStatusUnknown, 0)
        self.assertEqual(AVFoundation.AVAssetExportSessionStatusWaiting 1),
        self.assertEqual(AVFoundation.AVAssetExportSessionStatusExporting, 2)
        self.assertEqual(AVFoundation.AVAssetExportSessionStatusCompleted, 3)
        self.assertEqual(AVFoundation.AVAssetExportSessionStatusFailed, 4)
        self.assertEqual(AVFoundation.AVAssetExportSessionStatusCancelled, 5)


    def test_methods(self):
        self.assertResultIsBOOL(AVFoundation.AVAssetExportSession.shouldOptimizeForNetworkUse)
        self.assertArgIsBOOL(AVFoundation.AVAssetExportSession.setShouldOptimizeForNetworkUse_, 0)

        self.assertArgIsBlock(AVFoundation.AVAssetExportSession.exportAsynchronouslyWithCompletionHandler_, b'v')


if __name__ == "__main__":
    main()
