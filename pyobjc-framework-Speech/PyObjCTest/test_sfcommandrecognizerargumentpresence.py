import Speech
from PyObjCTools.TestSupport import TestCase


class TestSFCommandRecognizerArgumentPresence(TestCase):
    def test_constants(self):
        self.assertIsEnumType(Speech.SFCommandRecognizerArgumentPresence)
        self.assertEqual(
            Speech.SFCommandRecognizerArgumentPresencePresentAndDelimited, 0
        )
        self.assertEqual(
            Speech.SFCommandRecognizerArgumentPresencePresentMaybeIncomplete, 1
        )
        self.assertEqual(
            Speech.SFCommandRecognizerArgumentPresenceMissingMaybeExpected, 2
        )
        self.assertEqual(Speech.SFCommandRecognizerArgumentPresenceMissing, 3)
