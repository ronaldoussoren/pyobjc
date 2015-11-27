from PyObjCTools.TestSupport import *

import AVFoundation

AVAudioNodeTapBlock = b'v@@'

class TestAVAudioNode (TestCase):
    @min_os_level('10.10')
    def testMethods10_10(self):
        self.assertArgIsBlock(AVFoundation.AVAudioNode.installTapOnBus_bufferSize_format_block_, 3, AVAudioNodeTapBlock)

if __name__ == "__main__":
    main()
