import Speech
from PyObjCTools.TestSupport import TestCase, min_os_level


class TestSFSpeechRecognitionResult(TestCase):
    @min_os_level("10.15")
    def test_methods10_15(self):
        self.assertResultIsBOOL(Speech.SFSpeechRecognitionResult.isFinal)
