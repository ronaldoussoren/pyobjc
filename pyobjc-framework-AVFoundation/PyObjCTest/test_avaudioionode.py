from PyObjCTools.TestSupport import *

import AVFoundation

AVAudioIONodeInputBlock = b'^{AudioBufferList=L[1{AudioBuffer=LL^v}]}I'


class TestAVAudioIONode (TestCase):
    @min_os_level('10.7')
    def testConstants(self):
        self.assertIsInstance(AVFoundation.AVCoreAnimationBeginTimeAtZero, float)
        self.assertIsInstance(AVFoundation.AVLayerVideoGravityResizeAspect, unicode)
        self.assertIsInstance(AVFoundation.AVLayerVideoGravityResizeAspectFill, unicode)
        self.assertIsInstance(AVFoundation.AVLayerVideoGravityResize, unicode)

    @min_os_level('10.13')
    def testMethods10_13(self):
        self.assertResultIsBOOL(AVFoundation.AVAudioInputNode.setManualRenderingInputPCMFormat_inputBlock_)
        self.assertArgIsBlock(AVFoundation.AVAudioInputNode.setManualRenderingInputPCMFormat_inputBlock_, 1, AVAudioIONodeInputBlock)

if __name__ == "__main__":
    main()
