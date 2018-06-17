from PyObjCTools.TestSupport import *

import AVFoundation


class TestAVSampleBufferGenerator (TestCase):
    @min_os_level('10.10')
    def testMethods(self):
        self.assertArgIsBlock(AVFoundation.AVSampleBufferGenerator.notifyOfDataReadyForSampleBuffer_completionHandler_, 1, b'vZ@')

    def testConstants(self):
        self.assertEqual(AVFoundation.AVSampleBufferRequestDirectionForward, +1)
        self.assertEqual(AVFoundation.AVSampleBufferRequestDirectionNone, 0)
        self.assertEqual(AVFoundation.AVSampleBufferRequestDirectionReverse, -1)

        self.assertEqual(AVFoundation.AVSampleBufferRequestModeImmediate, 0)
        self.assertEqual(AVFoundation.AVSampleBufferRequestModeScheduled, 1)

if __name__ == "__main__":
    main()
