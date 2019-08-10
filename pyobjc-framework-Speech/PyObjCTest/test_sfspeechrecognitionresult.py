from PyObjCTools.TestSupport import *

import Speech


class TestSFSpeechRecognitionResult(TestCase):
    @min_os_level("10.15")
    def test_methods10_15(self):
        self.assertResultIsBOOL(Speech.SFSpeechRecognitionResult.isFinal)
