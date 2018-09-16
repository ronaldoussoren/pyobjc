from PyObjCTools.TestSupport import *

import AVFoundation

class TestAVSampleBufferRenderSynchronizer (TestCase):
    @min_os_level('10.13')
    def testMethods(self):
        self.assertArgIsBlock(AVFoundation.AVSampleBufferRenderSynchronizer.addPeriodicTimeObserverForInterval_queue_usingBlock_, 2, b'v{_CMTime=qiIq}')
        self.assertArgIsBlock(AVFoundation.AVSampleBufferRenderSynchronizer.addBoundaryTimeObserverForTimes_queue_usingBlock_, 2, b'v')

    @min_os_level('10.14')
    def test_constants10_14(self):
        self.assertIsInstance(AVFoundation.AVSampleBufferRenderSynchronizerRateDidChangeNotification, unicode)

if __name__ == "__main__":
    main()
