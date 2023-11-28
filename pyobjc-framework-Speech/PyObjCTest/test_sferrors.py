import Speech
from PyObjCTools.TestSupport import TestCase, min_os_level


class TestSFErrors(TestCase):
    def test_constants(self):
        self.assertIsEnumType(Speech.SFSpeechErrorCode)
        self.assertEqual(Speech.SFSpeechErrorCodeInternalServiceError, 1)
        self.assertEqual(Speech.SFSpeechErrorCodeUndefinedTemplateClassName, 7)
        self.assertEqual(Speech.SFSpeechErrorCodeMalformedSupplementalModel, 8)

    @min_os_level("14.0")
    def test_constants14_0(self):
        self.assertIsInstance(Speech.SFSpeechErrorDomain, str)
