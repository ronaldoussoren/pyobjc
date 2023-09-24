import Speech
from PyObjCTools.TestSupport import TestCase


class TestSFErrors(TestCase):
    def test_constants(self):
        self.assertIsInstance(Speech.SFSpeechErrorDomain, str)

        self.assertIsEnumType(Speech.SFSpeechErrorCode)
        self.assertEqual(Speech.SFSpeechErrorCodeInternalServiceError, 1)
        self.assertEqual(Speech.SFSpeechErrorCodeUndefinedTemplateClassName, 7)
        self.assertEqual(Speech.SFSpeechErrorCodeMalformedSupplementalModel, 8)
