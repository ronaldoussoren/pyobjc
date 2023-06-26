import Speech
from PyObjCTools.TestSupport import TestCase


class TestSFErrors(TestCase):
    def test_constants(self):
        self.assertIsInstance(Speech.SFSpeechErrorDomain)

        self.assertIsEnumType(Speech.SFSpeechErrorCode)
        self.assertEqual(Speech.SFSpeechErrorCodeInternalServiceError, 0)
        self.assertEqual(Speech.SFSpeechErrorCodeAudioDisordered, 1)
        self.assertEqual(Speech.SFSpeechErrorCodeUnexpectedAudioFormat, 2)
        self.assertEqual(Speech.SFSpeechErrorCodeNoModel, 3)
        self.assertEqual(Speech.SFSpeechErrorCodeIncompatibleAudioFormats, 4)
        self.assertEqual(Speech.SFSpeechErrorCodeInvalidJitProfile, 5)
        self.assertEqual(Speech.SFSpeechErrorCodeUndefinedTemplateClassName, 6)
        self.assertEqual(Speech.SFSpeechErrorCodeMalformedSupplementalModel, 7)
        self.assertEqual(Speech.SFSpeechErrorCodeUnimplementedFunctionality, 8)
        self.assertEqual(Speech.SFSpeechErrorCodeModuleOutputFailed, 9)
