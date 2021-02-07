import CoreAudio
from PyObjCTools.TestSupport import TestCase, fourcc


class TestAudioSessionTypes(TestCase):
    def test_constants(self):
        self.assertEqual(CoreAudio.AVAudioSessionErrorCodeNone, 0)
        self.assertEqual(
            CoreAudio.AVAudioSessionErrorCodeMediaServicesFailed, fourcc(b"msrv")
        )
        self.assertEqual(CoreAudio.AVAudioSessionErrorCodeIsBusy, fourcc(b"!act"))
        self.assertEqual(
            CoreAudio.AVAudioSessionErrorCodeIncompatibleCategory, fourcc(b"!cat")
        )
        self.assertEqual(
            CoreAudio.AVAudioSessionErrorCodeCannotInterruptOthers, fourcc(b"!int")
        )
        self.assertEqual(
            CoreAudio.AVAudioSessionErrorCodeMissingEntitlement, fourcc(b"ent?")
        )
        self.assertEqual(
            CoreAudio.AVAudioSessionErrorCodeSiriIsRecording, fourcc(b"siri")
        )
        self.assertEqual(
            CoreAudio.AVAudioSessionErrorCodeCannotStartPlaying, fourcc(b"!pla")
        )
        self.assertEqual(
            CoreAudio.AVAudioSessionErrorCodeCannotStartRecording, fourcc(b"!rec")
        )
        self.assertEqual(CoreAudio.AVAudioSessionErrorCodeBadParam, -50)
        self.assertEqual(
            CoreAudio.AVAudioSessionErrorCodeInsufficientPriority, fourcc(b"!pri")
        )
        self.assertEqual(
            CoreAudio.AVAudioSessionErrorCodeResourceNotAvailable, fourcc(b"!res")
        )
        self.assertEqual(CoreAudio.AVAudioSessionErrorCodeUnspecified, fourcc(b"what"))
        self.assertEqual(
            CoreAudio.AVAudioSessionErrorCodeExpiredSession, fourcc(b"!ses")
        )
        self.assertEqual(
            CoreAudio.AVAudioSessionErrorCodeSessionNotActive, fourcc(b"inac")
        )
