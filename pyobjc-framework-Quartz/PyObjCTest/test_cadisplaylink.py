from PyObjCTools.TestSupport import TestCase, min_os_level
import Quartz


class TestCADisplayLink(TestCase):
    @min_os_level("10.15")
    def testMethods(self):
        self.assertArgIsSEL(
            Quartz.CADisplayLink.displayLinkWithTarget_selector_, 1, b"v@:@"
        )

        self.assertResultIsBOOL(Quartz.CADisplayLink.isPaused)
        self.assertArgIsBOOL(Quartz.CADisplayLink.setPaused_, 0)
