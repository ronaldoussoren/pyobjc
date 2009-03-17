
from PyObjCTools.TestSupport import *
from AppKit import *

class TestNSBox (TestCase):
    def testConstants(self):
        self.failUnlessEqual(NSNoTitle, 0)
        self.failUnlessEqual(NSAboveTop, 1)
        self.failUnlessEqual(NSAtTop, 2)
        self.failUnlessEqual(NSBelowTop, 3)
        self.failUnlessEqual(NSAboveBottom, 4)
        self.failUnlessEqual(NSAtBottom, 5)
        self.failUnlessEqual(NSBelowBottom, 6)
        self.failUnlessEqual(NSBoxPrimary, 0)
        self.failUnlessEqual(NSBoxSecondary, 1)
        self.failUnlessEqual(NSBoxSeparator, 2)
        self.failUnlessEqual(NSBoxOldStyle, 3)
        self.failUnlessEqual(NSBoxCustom, 4)

    def testMethods(self):
        self.failUnlessResultIsBOOL(NSBox.isTransparent)
        self.failUnlessArgIsBOOL(NSBox.setTransparent_, 0)


if __name__ == "__main__":
    main()
