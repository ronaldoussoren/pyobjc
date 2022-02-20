import AVFoundation
import objc
from PyObjCTools.TestSupport import TestCase, min_os_level

AVAudioNodeCompletionHandler = b"v"
AVAudioPlayerNodeCompletionHandler = b"v" + objc._C_NSInteger


class TestAVAudioPlayerNode(TestCase):
    def test_enum_types(self):
        self.assertIsEnumType(AVFoundation.AVAudioPlayerNodeBufferOptions)
        self.assertIsEnumType(AVFoundation.AVAudioPlayerNodeCompletionCallbackType)

    def testConstants(self):
        self.assertEqual(AVFoundation.AVAudioPlayerNodeBufferLoops, 1 << 0)
        self.assertEqual(AVFoundation.AVAudioPlayerNodeBufferInterrupts, 1 << 1)
        self.assertEqual(
            AVFoundation.AVAudioPlayerNodeBufferInterruptsAtLoop, 1 << 2
        )  # noqa: B950

        self.assertEqual(
            AVFoundation.AVAudioPlayerNodeCompletionDataConsumed, 0
        )  # noqa: B950
        self.assertEqual(
            AVFoundation.AVAudioPlayerNodeCompletionDataRendered, 1
        )  # noqa: B950
        self.assertEqual(
            AVFoundation.AVAudioPlayerNodeCompletionDataPlayedBack, 2
        )  # noqa: B950

    @min_os_level("10.10")
    def testMethods10_10(self):
        self.assertArgIsBlock(
            AVFoundation.AVAudioPlayerNode.scheduleBuffer_completionHandler_,
            1,
            AVAudioNodeCompletionHandler,
        )
        self.assertArgIsBlock(
            AVFoundation.AVAudioPlayerNode.scheduleBuffer_atTime_options_completionHandler_,  # noqa: B950
            3,
            AVAudioNodeCompletionHandler,
        )
        self.assertArgIsBlock(
            AVFoundation.AVAudioPlayerNode.scheduleFile_atTime_completionHandler_,  # noqa: B950
            2,
            AVAudioNodeCompletionHandler,
        )
        self.assertArgIsBlock(
            AVFoundation.AVAudioPlayerNode.scheduleSegment_startingFrame_frameCount_atTime_completionHandler_,  # noqa: B950
            4,
            AVAudioNodeCompletionHandler,
        )
        self.assertResultIsBOOL(AVFoundation.AVAudioPlayerNode.isPlaying)

    @min_os_level("10.13")
    def testMethods10_13(self):
        self.assertArgIsBlock(
            AVFoundation.AVAudioPlayerNode.scheduleBuffer_completionCallbackType_completionHandler_,  # noqa: B950
            2,
            AVAudioPlayerNodeCompletionHandler,
        )
        self.assertArgIsBlock(
            AVFoundation.AVAudioPlayerNode.scheduleBuffer_atTime_options_completionCallbackType_completionHandler_,  # noqa: B950
            4,
            AVAudioPlayerNodeCompletionHandler,
        )
        self.assertArgIsBlock(
            AVFoundation.AVAudioPlayerNode.scheduleFile_atTime_completionCallbackType_completionHandler_,  # noqa: B950
            3,
            AVAudioPlayerNodeCompletionHandler,
        )
        self.assertArgIsBlock(
            AVFoundation.AVAudioPlayerNode.scheduleSegment_startingFrame_frameCount_atTime_completionCallbackType_completionHandler_,  # noqa: B950
            5,
            AVAudioPlayerNodeCompletionHandler,
        )
