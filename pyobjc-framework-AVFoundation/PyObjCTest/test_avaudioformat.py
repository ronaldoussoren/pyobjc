from PyObjCTools.TestSupport import *

import AVFoundation

try:
    unicode
except NameError:
    unicode = str


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
        self.assertArgIsIn(AVFoundation.AVAudioFormat.initWithStreamDescription, 0)
        self.assertArgIsIn(AVFoundation.AVAudioFormat.initWithStreamDescription_channelLayout_, 0)
        self.assertArgIsIn(AVFoundation.AVAudioFormat.initWithStreamDescription_channelLayout_, 1)
        self.assertArgIsIn(AVFoundation.AVAudioFormat.initStandardFormatWithSampleRate_channelLayout_, 1)
        self.assertArgIsBOOL(AVFoundation.AVAudioFormat.initWithCommonFormat_sampleRate_channels_interleaved_, 3)
        self.assertArgIsBOOL(AVFoundation.AVAudioFormat.initWithCommonFormat_sampleRate_interleaved_channelLayout_, 2)
        self.assertArgIsIn(AVFoundation.AVAudioFormat.initWithCommonFormat_sampleRate_interleaved_channelLayout_, 3)
        self.assertResultIsBOOL(AVFoundation.AVAudioFormat.isEqual_)
        self.assertResultIsBOOL(AVFoundation.AVAudioFormat.isStandard)
        self.assertResultIsBOOL(AVFoundation.AVAudioFormat.isInterleaved)

        self.fail("streamDescription")


if __name__ == "__main__":
    main()
