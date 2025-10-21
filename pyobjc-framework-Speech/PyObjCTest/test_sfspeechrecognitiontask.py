import Speech
import objc
from PyObjCTools.TestSupport import TestCase, min_os_level, min_sdk_level


class TestSFSpeechRecognitionTaskHelper(Speech.NSObject):
    def speechRecognitionTask_didFinishSuccessfully_(self, a, b):
        pass

    def speechRecognitionTask_didProcessAudioDuration_(self, a, b):
        pass


class TestSFSpeechRecognitionTask(TestCase):

    def test_constants(self):
        self.assertIsEnumType(Speech.SFSpeechRecognitionTaskState)
        self.assertEqual(Speech.SFSpeechRecognitionTaskStateStarting, 0)
        self.assertEqual(Speech.SFSpeechRecognitionTaskStateRunning, 1)
        self.assertEqual(Speech.SFSpeechRecognitionTaskStateFinishing, 2)
        self.assertEqual(Speech.SFSpeechRecognitionTaskStateCanceling, 3)
        self.assertEqual(Speech.SFSpeechRecognitionTaskStateCompleted, 4)

    @min_sdk_level("10.15")
    def test_protocols(self):
        self.assertProtocolExists("SFSpeechRecognitionTaskDelegate")

    def test_methods(self):
        self.assertArgIsBOOL(
            TestSFSpeechRecognitionTaskHelper.speechRecognitionTask_didFinishSuccessfully_,
            1,
        )

        self.assertArgHasType(
            TestSFSpeechRecognitionTaskHelper.speechRecognitionTask_didProcessAudioDuration_,
            1,
            objc._C_DBL,
        )

    @min_os_level("10.15")
    def test_methods10_15(self):
        self.assertResultIsBOOL(Speech.SFSpeechRecognitionTask.isFinishing)

        self.assertResultIsBOOL(Speech.SFSpeechRecognitionTask.isCancelled)
