from PyObjCTools.TestSupport import TestCase, min_os_level
import MediaPlayer


class TestMPRemoteCommandEvent(TestCase):
    def test_enum_types(self):
        self.assertIsEnumType(MediaPlayer.MPSeekCommandEventType)

    @min_os_level("10.12")
    def testConstants(self):
        self.assertEqual(MediaPlayer.MPSeekCommandEventTypeBeginSeeking, 0)
        self.assertEqual(MediaPlayer.MPSeekCommandEventTypeEndSeeking, 1)

    @min_os_level("10.12")
    def testMethods(self):
        self.assertResultIsBOOL(MediaPlayer.MPFeedbackCommandEvent.isNegative)
        self.assertResultIsBOOL(
            MediaPlayer.MPChangeShuffleModeCommandEvent.preservesShuffleMode
        )
        self.assertResultIsBOOL(
            MediaPlayer.MPChangeRepeatModeCommandEvent.preservesRepeatMode
        )
