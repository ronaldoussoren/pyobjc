from PyObjCTools.TestSupport import *

import AVFoundation


class TestAVAudioUnitReverb (TestCase):
    @min_os_level('10.7')
    def testConstants(self):
        self.assertEqual(AVFoundation.AVAudioUnitReverbPresetSmallRoom, 0)
        self.assertEqual(AVFoundation.AVAudioUnitReverbPresetMediumRoom, 1)
        self.assertEqual(AVFoundation.AVAudioUnitReverbPresetLargeRoom, 2)
        self.assertEqual(AVFoundation.AVAudioUnitReverbPresetMediumHall, 3)
        self.assertEqual(AVFoundation.AVAudioUnitReverbPresetLargeHall, 4)
        self.assertEqual(AVFoundation.AVAudioUnitReverbPresetPlate, 5)
        self.assertEqual(AVFoundation.AVAudioUnitReverbPresetMediumChamber, 6)
        self.assertEqual(AVFoundation.AVAudioUnitReverbPresetLargeChamber, 7)
        self.assertEqual(AVFoundation.AVAudioUnitReverbPresetCathedral, 8)
        self.assertEqual(AVFoundation.AVAudioUnitReverbPresetLargeRoom2, 9)
        self.assertEqual(AVFoundation.AVAudioUnitReverbPresetMediumHall2, 10)
        self.assertEqual(AVFoundation.AVAudioUnitReverbPresetMediumHall3, 11)
        self.assertEqual(AVFoundation.AVAudioUnitReverbPresetLargeHall2, 12)


if __name__ == "__main__":
    main()
