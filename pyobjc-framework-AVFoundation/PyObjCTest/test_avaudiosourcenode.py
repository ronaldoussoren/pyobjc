from PyObjCTools.TestSupport import *

import AVFoundation

AVAudioSourceNodeRenderBlock = b"io^Zn^^{AudioTimeStamp=dQdQ{SMPTETime=ssIIIssss}II}Io^{AudioBufferList=I[1{AudioBuffer=II^v}]}"


class TestAVAudioSourceNode(TestCase):
    @min_os_level("10.15")
    def test_methods(self):
        self.assertArgIsBlock(
            AVFoundation.AVAudioSourceNode.initWithRenderBlock_,
            0,
            AVAudioSourceNodeRenderBlock,
        )


if __name__ == "__main__":
    main()
