import AVFoundation
from PyObjCTools.TestSupport import TestCase, min_os_level

AVAudioSourceNodeRenderBlock = b"io^Zn^^{AudioTimeStamp=dQdQ{SMPTETime=ssIIIssss}II}Io^{AudioBufferList=I[1{AudioBuffer=II^v}]}"  # noqa: B950
AVAudioSourceNodeRenderBlockRealtimeSafe = b"io^Zn^^{AudioTimeStamp=dQdQ{SMPTETime=ssIIIssss}II}Io^{AudioBufferList=I[1{AudioBuffer=II^v}]}"  # noqa: B950


class TestAVAudioSourceNode(TestCase):
    @min_os_level("10.15")
    def test_methods(self):
        self.assertArgIsBlock(
            AVFoundation.AVAudioSourceNode.initWithRenderBlock_,
            0,
            AVAudioSourceNodeRenderBlock,
        )

    @min_os_level("27.0")
    def test_methods27_0(self):
        self.assertArgIsBlock(
            AVFoundation.AVAudioSourceNode.initWithRealtimeSafeRenderBlock_,
            0,
            AVAudioSourceNodeRenderBlockRealtimeSafe,
        )
        self.assertArgIsBlock(
            AVFoundation.AVAudioSourceNode.initWithFormat_realtimeSafeRenderBlock_,
            1,
            AVAudioSourceNodeRenderBlockRealtimeSafe,
        )
