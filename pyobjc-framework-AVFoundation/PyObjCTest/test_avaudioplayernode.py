from PyObjCTools.TestSupport import *

import AVFoundation

AVAudioNodeCompletionHandler = b'v'
AVAudioPlayerNodeCompletionHandler = b'v' + objc._C_NSInteger

class TestAVAudioPlayerNode (TestCase):
    def testConstants(self):
        self.assertEqual(AVFoundation.AVAudioPlayerNodeBufferLoops,  1 << 0)
        self.assertEqual(AVFoundation.AVAudioPlayerNodeBufferInterrupts,  1 << 1)
        self.assertEqual(AVFoundation.AVAudioPlayerNodeBufferInterruptsAtLoop,  1 << 2)

        self.assertEqual(AVFoundation.AVAudioPlayerNodeCompletionDataConsumed, 0)
        self.assertEqual(AVFoundation.AVAudioPlayerNodeCompletionDataRendered, 1)
        self.assertEqual(AVFoundation.AVAudioPlayerNodeCompletionDataPlayedBack, 2)

    @min_os_level('10.10')
    def testMethods10_10(self):
        self.assertArgIsBlock(AVFoundation.AVAudioPlayerNode.scheduleBuffer_completionHandler_, 1, AVAudioNodeCompletionHandler)
        self.assertArgIsBlock(AVFoundation.AVAudioPlayerNode.scheduleBuffer_atTime_options_completionHandler_, 3, AVAudioNodeCompletionHandler)
        self.assertArgIsBlock(AVFoundation.AVAudioPlayerNode.scheduleFile_atTime_completionHandler_, 2, AVAudioNodeCompletionHandler)
        self.assertArgIsBlock(AVFoundation.AVAudioPlayerNode.scheduleSegment_startingFrame_frameCount_atTime_completionHandler_, 4, AVAudioNodeCompletionHandler)
        self.assertResultIsBOOL(AVFoundation.AVAudioPlayerNode.isPlaying)

    @min_os_level('10.13')
    def testMethods10_13(self):
        self.assertArgIsBlock(AVFoundation.AVAudioPlayerNode.scheduleBuffer_completionCallbackType_completionHandler_, 2, AVAudioPlayerNodeCompletionHandler)
        self.assertArgIsBlock(AVFoundation.AVAudioPlayerNode.scheduleBuffer_atTime_options_completionCallbackType_completionHandler_, 4, AVAudioPlayerNodeCompletionHandler)
        self.assertArgIsBlock(AVFoundation.AVAudioPlayerNode.scheduleFile_atTime_completionCallbackType_completionHandler_, 3, AVAudioPlayerNodeCompletionHandler)
        self.assertArgIsBlock(AVFoundation.AVAudioPlayerNode.scheduleSegment_startingFrame_frameCount_atTime_completionCallbackType_completionHandler_, 5, AVAudioPlayerNodeCompletionHandler)


if __name__ == "__main__":
    main()
