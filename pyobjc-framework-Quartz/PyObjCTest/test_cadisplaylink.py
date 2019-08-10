from PyObjCTools.TestSupport import *
from Quartz.QuartzCore import *


class TestCADisplayLink(TestCase):
    @min_os_level("10.15")
    def testMethods(self):
        self.assertArgIsSEL(CADisplayLink.displayLinkWithTarget_selector_, 1, b"v@:@")

        self.assertResultIsBOOL(CADisplayLink.isPaused)
        self.assertArgIsBOOL(CADisplayLink.setPaused_, 0)


if __name__ == "__main__":
    main()
