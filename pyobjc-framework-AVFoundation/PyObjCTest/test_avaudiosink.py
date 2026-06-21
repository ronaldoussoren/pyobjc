import AVFoundation
from PyObjCTools.TestSupport import TestCase, min_os_level

AVAudioSinkNodeReceiverBlock = b"in^{AudioTimeStamp=dQdQ{SMPTETime=ssIIIssss}II}In^^{AudioBufferList=I[1{AudioBuffer=II^v}]}"  # noqa: B950
AVAudioSinkNodeReceiverBlockRealtimeSafe = b"in^{AudioTimeStamp=dQdQ{SMPTETime=ssIIIssss}II}In^^{AudioBufferList=I[1{AudioBuffer=II^v}]}"  # noqa: B950


class TestAVAudioSink(TestCase):
    @min_os_level("10.15")
    def test_methods(self):
        self.assertArgIsBlock(
            AVFoundation.AVAudioSinkNode.initWithReceiverBlock_,
            0,
            AVAudioSinkNodeReceiverBlock,
        )

    @min_os_level("27.0")
    def test_methods27_0(self):
        self.assertArgIsBlock(
            AVFoundation.AVAudioSinkNode.initWithRealtimeSafeReceiverBlock_,
            0,
            AVAudioSinkNodeReceiverBlockRealtimeSafe,
        )
