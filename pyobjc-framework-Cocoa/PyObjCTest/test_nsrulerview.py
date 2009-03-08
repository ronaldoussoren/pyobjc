
from PyObjCTools.TestSupport import *
from AppKit import *

class TestNSRulerView (TestCase):
    def testConstants(self):
        self.failUnlessEqual(NSHorizontalRuler, 0)
        self.failUnlessEqual(NSVerticalRuler, 1)

if __name__ == "__main__":
    main()
