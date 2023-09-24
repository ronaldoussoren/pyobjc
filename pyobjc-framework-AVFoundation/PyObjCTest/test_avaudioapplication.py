import AVFoundation
from PyObjCTools.TestSupport import TestCase, fourcc, min_os_level


class TestAVAudioApplication(TestCase):
    def test_constants(self):
        self.assertIsEnumType(AVFoundation.AVAudioApplicationRecordPermission)
        self.assertEqual(
            AVFoundation.AVAudioApplicationRecordPermissionUndetermined, fourcc(b"undt")
        )
        self.assertEqual(
            AVFoundation.AVAudioApplicationRecordPermissionDenied, fourcc(b"deny")
        )
        self.assertEqual(
            AVFoundation.AVAudioApplicationRecordPermissionGranted, fourcc(b"grnt")
        )

    @min_os_level("14.0")
    def test_constants14_0(self):
        self.assertIsInstance(
            AVFoundation.AVAudioApplicationInputMuteStateChangeNotification, str
        )
        self.assertIsInstance(AVFoundation.AVAudioApplicationMuteStateKey, str)

    @min_os_level("14.0")
    def test_methods14_0(self):
        self.assertResultIsBOOL(AVFoundation.AVAudioApplication.isInputMuted)

        self.assertResultIsBOOL(
            AVFoundation.AVAudioApplication.setInputMuteStateChangeHandler_error_
        )
        self.assertArgIsBlock(
            AVFoundation.AVAudioApplication.setInputMuteStateChangeHandler_error_,
            0,
            b"ZZ",
        )
        self.assertArgIsOut(
            AVFoundation.AVAudioApplication.setInputMuteStateChangeHandler_error_, 1
        )

        self.assertArgIsBlock(
            AVFoundation.AVAudioApplication.requestRecordPermissionWithCompletionHandler_,
            0,
            b"vZ",
        )
