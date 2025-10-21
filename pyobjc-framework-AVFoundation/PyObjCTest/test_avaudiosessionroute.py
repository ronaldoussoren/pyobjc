import AVFoundation
from PyObjCTools.TestSupport import TestCase, min_os_level


class TestAVAudioSessionRoute(TestCase):
    @min_os_level("26.0")
    def test_methods26_0(self):
        self.assertResultIsBOOL(AVFoundation.AVAudioSessionCapability.isSupported)
        self.assertResultIsBOOL(AVFoundation.AVAudioSessionCapability.isEnabled)
