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

    @min_os_level("12.0")
    def testMethods12_0(self):
        # No special handling is needed for the audiobufferlist, this type has
        # special handling in the CoreAudio bindings
        self.assertArgIsBlock(
            AVFoundation.AVAudioPCMBuffer.initWithPCMFormat_bufferListNoCopy_deallocator_,
            2,
            b"v^{AudioBufferList=I[1{AudioBuffer=II^v}]}",
        )
