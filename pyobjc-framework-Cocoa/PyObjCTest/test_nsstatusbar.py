
from PyObjCTools.TestSupport import *
from AppKit import *

class TestNSStatusBar (TestCase):
    def testConstants(self):
        self.failUnlessEqual(NSVariableStatusItemLength, -1)
        self.failUnlessEqual(NSSquareStatusItemLength, -2)

    def testMethods(self):
        self.failUnlessResultIsBOOL(NSStatusBar.isVertical)

if __name__ == "__main__":
    main()
