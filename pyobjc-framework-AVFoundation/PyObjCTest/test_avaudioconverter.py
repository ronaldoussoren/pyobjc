import AVFoundation
import objc
from PyObjCTools.TestSupport import TestCase, min_os_level

AVAudioConverterInputBlock = b"@Io^" + objc._C_NSInteger


class TestAVAudioConverter(TestCase):
    def testConstants(self):
        self.assertEqual(AVFoundation.AVAudioConverterPrimeMethod_Pre, 0)
        self.assertEqual(AVFoundation.AVAudioConverterPrimeMethod_Normal, 1)
        self.assertEqual(AVFoundation.AVAudioConverterPrimeMethod_None, 2)

        self.assertEqual(AVFoundation.AVAudioConverterInputStatus_HaveData, 0)
        self.assertEqual(AVFoundation.AVAudioConverterInputStatus_NoDataNow, 1)
        self.assertEqual(AVFoundation.AVAudioConverterInputStatus_EndOfStream, 2)

        self.assertEqual(AVFoundation.AVAudioConverterOutputStatus_HaveData, 0)
        self.assertEqual(AVFoundation.AVAudioConverterOutputStatus_InputRanDry, 1)
        self.assertEqual(AVFoundation.AVAudioConverterOutputStatus_EndOfStream, 2)
        self.assertEqual(AVFoundation.AVAudioConverterOutputStatus_Error, 3)

    def testStructs(self):
        v = AVFoundation.AVAudioConverterPrimeInfo()
        self.assertEqual(v.leadingFrames, 0)
        self.assertEqual(v.trailingFrames, 0)

    @min_os_level("10.11")
    def testMethods(self):
        self.assertResultIsBOOL(AVFoundation.AVAudioConverter.downmix)
        self.assertArgIsBOOL(AVFoundation.AVAudioConverter.setDownmix_, 0)

        self.assertResultIsBOOL(AVFoundation.AVAudioConverter.dither)
        self.assertArgIsBOOL(AVFoundation.AVAudioConverter.setDither_, 0)

        self.assertResultIsBOOL(
            AVFoundation.AVAudioConverter.convertToBuffer_fromBuffer_error_
        )
        self.assertArgIsOut(
            AVFoundation.AVAudioConverter.convertToBuffer_fromBuffer_error_, 2
        )

        self.assertArgIsOut(
            AVFoundation.AVAudioConverter.convertToBuffer_error_withInputFromBlock_, 1
        )
        self.assertArgIsBlock(
            AVFoundation.AVAudioConverter.convertToBuffer_error_withInputFromBlock_,
            2,
            AVAudioConverterInputBlock,
        )
