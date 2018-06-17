from PyObjCTools.TestSupport import *

import AVFoundation

class TestAVSampleBufferRenderSynchronizer (TestCase):
    def testMethods(self):
        self.assertArgIsBlock(AVFoundation.AVSampleBufferRenderSynchronizer.addPeriodicTimeObserverForInterval_queue_usingBlock_, 2, b'v{_CMTime=qiIq}')
        self.assertArgIsBlock(AVFoundation.AVSampleBufferRenderSynchronizer.addBoundaryTimeObserverForTimes_queue_usingBlock_, 2, b'v')

if __name__ == "__main__":
    main()
