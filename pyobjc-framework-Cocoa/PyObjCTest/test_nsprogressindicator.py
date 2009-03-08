
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


if __name__ == "__main__":
    main()
