
from PyObjCTools.TestSupport import *
from Quartz.CoreGraphics import *

class TestCGDisplayFade (TestCase):
    def testConstants(self):
        self.failUnlessEqual(kCGDisplayFadeReservationInvalidToken, 0)
        self.failUnlessEqual(kCGDisplayBlendNormal, 0.0)
        self.failUnlessEqual(kCGDisplayBlendSolidColor, 1.0)
        self.failUnlessEqual(kCGMaxDisplayReservationInterval, 15.0)

    def testIncomplete(self):
        self.fail("Add header tests for <CoreGraphics/CGDisplayFade.h>")

if __name__ == "__main__":
    main()
