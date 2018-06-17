from PyObjCTools.TestSupport import *

import AVFoundation

class TestAVPlayerOutputHelper (AVFoundation.NSObject):
    def legibleOutput_didOutputAttributedStrings_nativeSampleBuffers_forItemTime_(self, a, b, c, d):
        pass

class TestAVPlayerOutput (TestCase):
    @min_os_level('10.8')
    def testMethods10_8(self):
        self.assertResultIsBOOL(AVFoundation.AVPlayerItemOutput.suppressesPlayerRendering)
        self.assertArgIsBOOL(AVFoundation.AVPlayerItemOutput.setSuppressesPlayerRendering_, 0)

        self.assertResultIsBOOL(AVFoundation.AVPlayerItemVideoOutput.hasNewPixelBufferForItemTime_)

        self.assertResultIsCFRetained(AVFoundation.AVPlayerItemVideoOutput.copyPixelBufferForItemTime_itemTimeForDisplay_)
        self.assertArgIsOut(AVFoundation.AVPlayerItemVideoOutput.copyPixelBufferForItemTime_itemTimeForDisplay_, 1)

        self.assertArgHasType(TestAVPlayerOutputHelper.legibleOutput_didOutputAttributedStrings_nativeSampleBuffers_forItemTime_,
                3, b'{_CMTime=qiIq}')

    def testProtocols(self):
        objc.protocolNamed('AVPlayerItemOutputPullDelegate')
        objc.protocolNamed('AVPlayerItemLegibleOutputPushDelegate')
        objc.protocolNamed('AVPlayerItemMetadataOutputPushDelegate')
        objc.protocolNamed('AVPlayerItemOutputPushDelegate')

    @min_os_level('10.9')
    def testConstants10_9(self):
        self.assertIsInstance(AVFoundation.AVPlayerItemLegibleOutputTextStylingResolutionDefault, unicode)
        self.assertIsInstance(AVFoundation.AVPlayerItemLegibleOutputTextStylingResolutionSourceAndRulesOnly, unicode)

if __name__ == "__main__":
    main()
