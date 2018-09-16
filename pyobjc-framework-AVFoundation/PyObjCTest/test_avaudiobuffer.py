from PyObjCTools.TestSupport import *

import AVFoundation

class TestAVAudioBuffer (TestCase):
    @min_os_level('10.11')
    def testMethods(self):
        self.assertResultIsVariableSize(AVFoundation.AVAudioCompressedBuffer.packetDescriptions)
        self.assertResultIsVariableSize(AVFoundation.AVAudioCompressedBuffer.data)

    @expectedFailure
    def testMethods_manual(self):
        # Not quite sure how to test this
        self.fail("check floatChannelData,int16ChannelData, int32ChannelData")

if __name__ == "__main__":
    main()
