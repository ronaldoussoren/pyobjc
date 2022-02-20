import Speech
from PyObjCTools.TestSupport import TestCase


class TestSFSpeechRecognitionTaskHint(TestCase):
    def test_enum_types(self):
        self.assertIsEnumType(Speech.SFSpeechRecognitionTaskHint)

    def test_constants(self):
        self.assertEqual(Speech.SFSpeechRecognitionTaskHintUnspecified, 0)
        self.assertEqual(Speech.SFSpeechRecognitionTaskHintDictation, 1)
        self.assertEqual(Speech.SFSpeechRecognitionTaskHintSearch, 2)
        self.assertEqual(Speech.SFSpeechRecognitionTaskHintConfirmation, 3)
