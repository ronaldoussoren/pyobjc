from PyObjCTools.TestSupport import *

import AVFoundation

class TestAVAudioFormat (TestCase):
    @min_os_level('10.10')
    def testConstants(self):
        self.assertEqual(AVFoundation.AVAudioOtherFormat, 0)
        self.assertEqual(AVFoundation.AVAudioPCMFormatFloat32, 1)
        self.assertEqual(AVFoundation.AVAudioPCMFormatFloat64, 2)
        self.assertEqual(AVFoundation.AVAudioPCMFormatInt16, 3)
        self.assertEqual(AVFoundation.AVAudioPCMFormatInt32, 4)

    @min_os_level('10.10')
    def testMethods(self):
        self.assertArgIsIn(AVFoundation.AVAudioFormat.initWithStreamDescription_, 0)
        self.assertArgIsIn(AVFoundation.AVAudioFormat.initWithStreamDescription_channelLayout_, 0)
        self.assertArgIsIn(AVFoundation.AVAudioFormat.initWithStreamDescription_channelLayout_, 0)
        self.assertArgIsBOOL(AVFoundation.AVAudioFormat.initWithCommonFormat_sampleRate_channels_interleaved_, 3)
        self.assertArgIsBOOL(AVFoundation.AVAudioFormat.initWithCommonFormat_sampleRate_interleaved_channelLayout_, 2)
        self.assertResultIsBOOL(AVFoundation.AVAudioFormat.isEqual_)
        self.assertResultIsBOOL(AVFoundation.AVAudioFormat.isStandard)
        self.assertResultIsBOOL(AVFoundation.AVAudioFormat.isInterleaved)

        self.assertResultIsFixedSize(AVFoundation.AVAudioFormat.streamDescription, 1)


if __name__ == "__main__":
    main()
