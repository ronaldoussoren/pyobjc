from PyObjCTools.TestSupport import *

import AVFoundation

class TestAVAssetReader (TestCase):
    @min_os_level('10.7')
    def testConstants(self):
        self.assertEqual(AVFoundation.AVAssetReaderStatusUnknown, 0)
        self.assertEqual(AVFoundation.AVAssetReaderStatusReading, 1)
        self.assertEqual(AVFoundation.AVAssetReaderStatusCompleted, 2)
        self.assertEqual(AVFoundation.AVAssetReaderStatusFailed, 3)
        self.assertEqual(AVFoundation.AVAssetReaderStatusCancelled, 4)

    @min_os_level('10.7')
    def testMethods(self):
        self.assertArgIsOut(AVFoundation.AVAssetReader.assetReaderWithAsset_error_, 1)
        self.assertArgIsOut(AVFoundation.AVAssetReader.initWithAsset_error_, 1)
        self.assertResultIsBOOL(AVFoundation.AVAssetReader.canAddOutput_)
        self.assertResultIsBOOL(AVFoundation.AVAssetReader.startReading)

if __name__ == "__main__":
    main()
