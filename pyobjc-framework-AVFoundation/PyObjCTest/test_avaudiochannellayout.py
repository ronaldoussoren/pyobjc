import AVFoundation
from PyObjCTools.TestSupport import TestCase, min_os_level


class TestAVAudioChannelLayout(TestCase):
    @min_os_level("10.10")
    def testMethods10_10(self):
        self.assertResultIsBOOL(AVFoundation.AVAudioChannelLayout.isEqual_)
