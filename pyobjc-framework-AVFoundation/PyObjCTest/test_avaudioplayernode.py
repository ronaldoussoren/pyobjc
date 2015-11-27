from PyObjCTools.TestSupport import *

import AVFoundation

AVAudioNodeCompletionHandler = b'v'

class TestAVAudioPlayerNode (TestCase):
    def testConstants(self):
        self.assertEqual(AVFoundation.AVAudioPlayerNodeBufferLoops,  1 << 0)
        self.assertEqual(AVFoundation.AVAudioPlayerNodeBufferInterrupts,  1 << 1)
        self.assertEqual(AVFoundation.AVAudioPlayerNodeBufferInterruptsAtLoop,  1 << 2)

    @min_os_level('10.10')
    def testMethods10_10(self):
        self.assertArgIsBlock(AVFoundation.AVAudioPlayerNode.scheduleBuffer_completionHandler_, 1, AVAudioNodeCompletionHandler)
        self.assertArgIsBlock(AVFoundation.AVAudioPlayerNode.scheduleBuffer_atTime_options_completionHandler_, 3, AVAudioNodeCompletionHandler)
        self.assertArgIsBlock(AVFoundation.AVAudioPlayerNode.scheduleFile_atTime_completionHandler_, 2, AVAudioNodeCompletionHandler)
        self.assertArgIsBlock(AVFoundation.AVAudioPlayerNode.scheduleSegment_startingFrame_frameCount_atTime_completionHandler_, 4, AVAudioNodeCompletionHandler)
        self.assertResultIsBOOL(AVFoundation.AVAudioPlayerNode.isPlaying)

if __name__ == "__main__":
    main()
