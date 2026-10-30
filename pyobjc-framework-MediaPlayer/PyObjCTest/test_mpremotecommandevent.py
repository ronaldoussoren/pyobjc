from PyObjCTools.TestSupport import TestCase, min_os_level
import MediaPlayer


class TestMPRemoteCommandEvent(TestCase):
    def test_enums(self):
        self.assertIsEnumType(MediaPlayer.MPSeekCommandEventType)
        self.assertEqual(MediaPlayer.MPSeekCommandEventTypeBeginSeeking, 0)
        self.assertEqual(MediaPlayer.MPSeekCommandEventTypeEndSeeking, 1)

    @min_os_level("10.12")
    def test_methods(self):
        self.assertResultIsBOOL(MediaPlayer.MPFeedbackCommandEvent.isNegative)
        self.assertResultIsBOOL(
            MediaPlayer.MPChangeShuffleModeCommandEvent.preservesShuffleMode
        )
        self.assertResultIsBOOL(
            MediaPlayer.MPChangeRepeatModeCommandEvent.preservesRepeatMode
        )
