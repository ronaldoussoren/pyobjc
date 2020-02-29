import AVFoundation
from PyObjCTools.TestSupport import *


class TestAVPlayerLayer(TestCase):
    @min_os_level("10.7")
    def testMethods10_7(self):
        self.assertResultIsBOOL(AVFoundation.AVPlayerLayer.isReadyForDisplay)


if __name__ == "__main__":
    main()
