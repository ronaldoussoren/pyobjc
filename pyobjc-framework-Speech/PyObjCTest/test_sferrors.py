import Speech
from PyObjCTools.TestSupport import TestCase


class TestSFErrors(TestCase):
    def test_constants(self):
        self.assertIsInstance(Speech.SFSpeechErrorDomain, str)

        self.assertIsEnumType(Speech.SFSpeechErrorCode)
        self.assertEqual(Speech.SFSpeechErrorCodeInternalServiceError, 1)
        self.assertEqual(Speech.SFSpeechErrorCodeAudioDisordered, 2)
        self.assertEqual(Speech.SFSpeechErrorCodeUnexpectedAudioFormat, 3)
        self.assertEqual(Speech.SFSpeechErrorCodeNoModel, 4)
        self.assertEqual(Speech.SFSpeechErrorCodeIncompatibleAudioFormats, 5)
        self.assertEqual(Speech.SFSpeechErrorCodeInvalidJitProfile, 6)
        self.assertEqual(Speech.SFSpeechErrorCodeUndefinedTemplateClassName, 7)
        self.assertEqual(Speech.SFSpeechErrorCodeMalformedSupplementalModel, 8)
        self.assertEqual(Speech.SFSpeechErrorCodeUnimplementedFunctionality, 9)
        self.assertEqual(Speech.SFSpeechErrorCodeModuleOutputFailed, 10)
