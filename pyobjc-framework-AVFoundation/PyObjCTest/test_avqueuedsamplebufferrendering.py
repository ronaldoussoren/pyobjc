from PyObjCTools.TestSupport import *

import AVFoundation

class TestAVQueuedSampleBufferRenderingHelper (AVFoundation.NSObject):
    def isReadyForMoreMediaData(self): return 0
    def requestMediaDataWhenReadyOnQueue_usingBlock_(self, q, b): pass

class TestAVQueuedSampleBufferRendering (TestCase):
    def testConstants(self):
        self.assertEqual(AVFoundation.AVQueuedSampleBufferRenderingStatusUnknown, 0)
        self.assertEqual(AVFoundation.AVQueuedSampleBufferRenderingStatusRendering, 1)
        self.assertEqual(AVFoundation.AVQueuedSampleBufferRenderingStatusFailed, 2)

    @min_sdk_level('10.13')
    def testProtocols(self):
        objc.protocolNamed('AVQueuedSampleBufferRendering')

    def testMethods(self):
        self.assertResultIsBOOL(TestAVQueuedSampleBufferRenderingHelper.isReadyForMoreMediaData)
        self.assertArgIsBlock(TestAVQueuedSampleBufferRenderingHelper.requestMediaDataWhenReadyOnQueue_usingBlock_, 1, b'v')

if __name__ == "__main__":
    main()
