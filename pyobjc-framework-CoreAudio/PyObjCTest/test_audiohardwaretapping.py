import CoreAudio
from PyObjCTools.TestSupport import TestCase, min_os_level


class TesttAudioHardwareTapping(TestCase):
    @min_os_level("14.2")
    def testFunctions(self):
        self.assertArgIsOut(CoreAudio.AudioHardwareCreateProcessTap, 1)
        CoreAudio.AudioHardwareDestroyProcessTap
