from PyObjCTools.TestSupport import *
import sys

if sys.maxsize > 2**32:
    import MediaPlayer

    class TestMPContentItem (TestCase):
        @min_os_level('10.12')
        def testMethods(self):
            self.assertResultIsBOOL(MediaPlayer.MPContentItem.isContainer)
            self.assertArgIsBOOL(MediaPlayer.MPContentItem.setContainer_, 0)

            self.assertResultIsBOOL(MediaPlayer.MPContentItem.isPlayable)
            self.assertArgIsBOOL(MediaPlayer.MPContentItem.setPlayable_, 0)

            self.assertResultIsBOOL(MediaPlayer.MPContentItem.isStreamingContent)
            self.assertArgIsBOOL(MediaPlayer.MPContentItem.setStreamingContent_, 0)

            self.assertResultIsBOOL(MediaPlayer.MPContentItem.isExplicitContent)
            self.assertArgIsBOOL(MediaPlayer.MPContentItem.setExplicitContent_, 0)

if __name__ == "__main__":
    main()
