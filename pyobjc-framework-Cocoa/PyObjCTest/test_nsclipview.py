from AppKit import *
from PyObjCTools.TestSupport import *

class TestNSClipView (TestCase):
    def testMethods(self):
        self.failUnlessResultIsBOOL(NSClipView.drawsBackground)
        self.failUnlessArgIsBOOL(NSClipView.setDrawsBackground_, 0)
        self.failUnlessResultIsBOOL(NSClipView.copiesOnScroll)
        self.failUnlessArgIsBOOL(NSClipView.setCopiesOnScroll_, 0)
        self.failUnlessResultIsBOOL(NSClipView.autoscroll_)

if __name__ == "__main__":
    main()
