
from PyObjCTools.TestSupport import *
from AppKit import *

class TestNSProgressIndicator (TestCase):
    def testConstants(self):
        self.failUnlessEqual(NSProgressIndicatorPreferredThickness, 14)
        self.failUnlessEqual(NSProgressIndicatorPreferredSmallThickness, 10)
        self.failUnlessEqual(NSProgressIndicatorPreferredLargeThickness, 18)
        self.failUnlessEqual(NSProgressIndicatorPreferredAquaThickness, 12)
        self.failUnlessEqual(NSProgressIndicatorBarStyle, 0)
        self.failUnlessEqual(NSProgressIndicatorSpinningStyle, 1)

    def testMethods(self):
        self.failUnlessResultIsBOOL(NSProgressIndicator.isIndeterminate)
        self.failUnlessArgIsBOOL(NSProgressIndicator.setIndeterminate_, 0)
        self.failUnlessResultIsBOOL(NSProgressIndicator.isBezeled)
        self.failUnlessArgIsBOOL(NSProgressIndicator.setBezeled_, 0)
        self.failUnlessResultIsBOOL(NSProgressIndicator.usesThreadedAnimation)
        self.failUnlessArgIsBOOL(NSProgressIndicator.setUsesThreadedAnimation_, 0)
        self.failUnlessResultIsBOOL(NSProgressIndicator.isDisplayedWhenStopped)
        self.failUnlessArgIsBOOL(NSProgressIndicator.setDisplayedWhenStopped_, 0)


if __name__ == "__main__":
    main()
