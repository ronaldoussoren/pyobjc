from PyObjCTools.TestSupport import *
import sys

if sys.maxsize > 2**32:
    import MediaPlayer

    class TestMPPlayableContentManagerContext (TestCase):
        @min_os_level('10.12')
        def testMethods(self):
            self.assertResultIsBOOL(MediaPlayer.MPPlayableContentManagerContext.contentLimitsEnforced)
            self.assertResultIsBOOL(MediaPlayer.MPPlayableContentManagerContext.contentLimitsEnabled)
            self.assertResultIsBOOL(MediaPlayer.MPPlayableContentManagerContext.endpointAvailable)

if __name__ == "__main__":
    main()
