import AVFoundation
from PyObjCTools.TestSupport import TestCase, min_os_level


class TestAVAudioUnitEQ(TestCase):
    def test_enum_types(self):
        self.assertIsEnumType(AVFoundation.AVAudioUnitEQFilterType)

    @min_os_level("10.7")
    def testConstants(self):
        self.assertEqual(AVFoundation.AVAudioUnitEQFilterTypeParametric, 0)
        self.assertEqual(AVFoundation.AVAudioUnitEQFilterTypeLowPass, 1)
        self.assertEqual(AVFoundation.AVAudioUnitEQFilterTypeHighPass, 2)
        self.assertEqual(AVFoundation.AVAudioUnitEQFilterTypeResonantLowPass, 3)
        self.assertEqual(AVFoundation.AVAudioUnitEQFilterTypeResonantHighPass, 4)
        self.assertEqual(AVFoundation.AVAudioUnitEQFilterTypeBandPass, 5)
        self.assertEqual(AVFoundation.AVAudioUnitEQFilterTypeBandStop, 6)
        self.assertEqual(AVFoundation.AVAudioUnitEQFilterTypeLowShelf, 7)
        self.assertEqual(AVFoundation.AVAudioUnitEQFilterTypeHighShelf, 8)
        self.assertEqual(AVFoundation.AVAudioUnitEQFilterTypeResonantLowShelf, 9)
        self.assertEqual(AVFoundation.AVAudioUnitEQFilterTypeResonantHighShelf, 10)

    @min_os_level("10.10")
    def testMethods10_10(self):
        self.assertResultIsBOOL(AVFoundation.AVAudioUnitEQFilterParameters.bypass)
        self.assertArgIsBOOL(AVFoundation.AVAudioUnitEQFilterParameters.setBypass_, 0)
