
from PyObjCTools.TestSupport import *
from AppKit import *

class TestNSProgressIndicator (TestCase):
    def testConstants(self):
        self.assertEqual(NSProgressIndicatorPreferredThickness, 14)
        self.assertEqual(NSProgressIndicatorPreferredSmallThickness, 10)
        self.assertEqual(NSProgressIndicatorPreferredLargeThickness, 18)
        self.assertEqual(NSProgressIndicatorPreferredAquaThickness, 12)
        self.assertEqual(NSProgressIndicatorBarStyle, 0)
        self.assertEqual(NSProgressIndicatorSpinningStyle, 1)

    def testMethods(self):
        self.assertResultIsBOOL(NSProgressIndicator.isIndeterminate)
        self.assertArgIsBOOL(NSProgressIndicator.setIndeterminate_, 0)
        self.assertResultIsBOOL(NSProgressIndicator.isBezeled)
        self.assertArgIsBOOL(NSProgressIndicator.setBezeled_, 0)
        self.assertResultIsBOOL(NSProgressIndicator.usesThreadedAnimation)
        self.assertArgIsBOOL(NSProgressIndicator.setUsesThreadedAnimation_, 0)
        self.assertResultIsBOOL(NSProgressIndicator.isDisplayedWhenStopped)
        self.assertArgIsBOOL(NSProgressIndicator.setDisplayedWhenStopped_, 0)


if __name__ == "__main__":
    main()
