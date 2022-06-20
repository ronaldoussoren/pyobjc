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

    @min_os_level("13.0")
    def testMethods13_0(self):
        self.assertArgIsOut(
            AVFoundation.AVSampleBufferGenerator.createSampleBufferForRequest_error_, 1
        )

        self.assertArgIsOut(
            AVFoundation.AVSampleBufferGenerator.createSampleBufferForRequest_addingToBatch_error_,
            2,
        )

        self.assertArgIsBlock(
            AVFoundation.AVSampleBufferGeneratorBatch.makeDataReadyWithCompletionHandler_,
            0,
            b"v@",
        )

    def testConstants(self):
        self.assertEqual(AVFoundation.AVSampleBufferRequestDirectionForward, +1)
        self.assertEqual(AVFoundation.AVSampleBufferRequestDirectionNone, 0)
        self.assertEqual(AVFoundation.AVSampleBufferRequestDirectionReverse, -1)

        self.assertEqual(AVFoundation.AVSampleBufferRequestModeImmediate, 0)
        self.assertEqual(AVFoundation.AVSampleBufferRequestModeScheduled, 1)
