import AVFoundation
from PyObjCTools.TestSupport import TestCase, min_os_level

AVAudioNodeTapBlock = b"v@@"


class TestAVAudioNode(TestCase):
    @min_os_level("10.10")
    def testMethods10_10(self):
        self.assertArgIsBlock(
            AVFoundation.AVAudioNode.installTapOnBus_bufferSize_format_block_,
            3,
            AVAudioNodeTapBlock,
        )
