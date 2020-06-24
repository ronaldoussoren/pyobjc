from PyObjCTools.TestSupport import TestCase, min_os_level
import MediaPlayer


class TestMPPlayableContentManagerContext(TestCase):
    @min_os_level("10.12")
    def testMethods(self):
        self.assertResultIsBOOL(
            MediaPlayer.MPPlayableContentManagerContext.contentLimitsEnforced
        )
        self.assertResultIsBOOL(
            MediaPlayer.MPPlayableContentManagerContext.contentLimitsEnabled
        )
        self.assertResultIsBOOL(
            MediaPlayer.MPPlayableContentManagerContext.endpointAvailable
        )
