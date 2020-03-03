import AVFoundation
from PyObjCTools.TestSupport import TestCase, min_os_level, expectedFailure


class TestAVAudioBuffer(TestCase):
    @min_os_level("10.11")
    def testMethods(self):
        self.assertResultIsVariableSize(
            AVFoundation.AVAudioCompressedBuffer.packetDescriptions
        )
        self.assertResultIsVariableSize(AVFoundation.AVAudioCompressedBuffer.data)

    @expectedFailure
    def testMethods_manual(self):
        # Not quite sure how to test this
        self.fail("check floatChannelData,int16ChannelData, int32ChannelData")
