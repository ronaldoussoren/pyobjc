from PyObjCTools.TestSupport import *
import sys

if sys.maxsize > 2**32:
    import MediaPlayer

    class TestMPRemoteCommandEvent (TestCase):
        @min_os_level('10.12')
        def testConstants(self):
            self.assertEqual(MediaPlayer.MPSeekCommandEventTypeBeginSeeking, 0)
            self.assertEqual(MediaPlayer.MPSeekCommandEventTypeEndSeeking, 1)


        @min_os_level('10.12')
        def testMethods(self):
            self.assertResultIsBOOL(MediaPlayer.MPFeedbackCommandEvent.isNegative)
            self.assertResultIsBOOL(MediaPlayer.MPChangeShuffleModeCommandEvent.preservesShuffleMode)
            self.assertResultIsBOOL(MediaPlayer.MPChangeRepeatModeCommandEvent.preservesRepeatMode)


if __name__ == "__main__":
    main()
