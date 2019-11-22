from PyObjCTools.TestSupport import *

import AVFoundation

# OSStatus (^AVAudioSinkNodeReceiverBlock)(const AudioTimeStamp *timestamp, AVAudioFrameCount frameCount, const AudioBufferList *inputData)
AVAudioSinkNodeReceiverBlock = b"in^{AudioTimeStamp=dQdQ{SMPTETime=ssIIIssss}II}In^^{AudioBufferList=I[1{AudioBuffer=II^v}]}"


class TestAVAudioSink(TestCase):
    @min_os_level("10.15")
    def test_methods(self):
        self.assertArgIsBlock(
            AVFoundation.AVAudioSinkNode.initWithReceiverBlock_,
            0,
            AVAudioSinkNodeReceiverBlock,
        )


if __name__ == "__main__":
    main()
