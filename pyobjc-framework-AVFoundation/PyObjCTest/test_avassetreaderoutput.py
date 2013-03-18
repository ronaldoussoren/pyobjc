from PyObjCTools.TestSupport import *

import AVFoundation

class TestAVAssetReaderOutput (TestCase):
    def test_methods(self):
        self.assertResultIsBOOL(AVFoundation.AVAssetReaderOutput.alwaysCopiesSampleData)
        self.assertArgIsBOOL(AVFoundation.AVAssetReaderOutput.setAlwaysCopiesSampleData_, 0)

if __name__ == "__main__":
    main()
