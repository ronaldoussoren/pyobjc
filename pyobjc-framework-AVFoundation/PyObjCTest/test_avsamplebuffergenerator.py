import AVFoundation
from PyObjCTools.TestSupport import TestCase, min_os_level


class TestAVSampleBufferGenerator(TestCase):
    @min_os_level("10.10")
    def testMethods(self):
        self.assertArgIsBlock(
            AVFoundation.AVSampleBufferGenerator.notifyOfDataReadyForSampleBuffer_completionHandler_,  # noqa: B950
            1,
            b"vZ@",
        )

    def testConstants(self):
        self.assertEqual(AVFoundation.AVSampleBufferRequestDirectionForward, +1)
        self.assertEqual(AVFoundation.AVSampleBufferRequestDirectionNone, 0)
        self.assertEqual(AVFoundation.AVSampleBufferRequestDirectionReverse, -1)

        self.assertEqual(AVFoundation.AVSampleBufferRequestModeImmediate, 0)
        self.assertEqual(AVFoundation.AVSampleBufferRequestModeScheduled, 1)
