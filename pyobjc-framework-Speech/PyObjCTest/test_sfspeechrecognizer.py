import Speech
from PyObjCTools.TestSupport import TestCase, min_os_level, min_sdk_level
import objc


class TestSFSpeechRecognizerHelper(Speech.NSObject):
    def speechRecognizer_availabilityDidChange_(self, a, b):
        pass


class TestSFSpeechRecognizer(TestCase):
    def test_constants(self):
        self.assertEqual(Speech.SFSpeechRecognizerAuthorizationStatusNotDetermined, 0)
        self.assertEqual(Speech.SFSpeechRecognizerAuthorizationStatusDenied, 1)
        self.assertEqual(Speech.SFSpeechRecognizerAuthorizationStatusRestricted, 2)
        self.assertEqual(Speech.SFSpeechRecognizerAuthorizationStatusAuthorized, 3)

    @min_sdk_level("10.15")
    def test_protocols(self):
        objc.protocolNamed("SFSpeechRecognizerDelegate")

    def test_methods(self):
        self.assertArgIsBOOL(
            TestSFSpeechRecognizerHelper.speechRecognizer_availabilityDidChange_, 1
        )

    @min_os_level("10.15")
    def test_methods10_15(self):
        self.assertArgIsBlock(
            Speech.SFSpeechRecognizer.requestAuthorization_, 0, b"v" + objc._C_NSInteger
        )

        self.assertResultIsBOOL(Speech.SFSpeechRecognizer.isAvailable)

        self.assertArgIsBlock(
            Speech.SFSpeechRecognizer.recognitionTaskWithRequest_resultHandler_,
            1,
            b"v@@",
        )
