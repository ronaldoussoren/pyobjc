from AppKit import *
from PyObjCTools.TestSupport import *

class TestNSClipView (TestCase):
    def testMethods(self):
        self.assertResultIsBOOL(NSClipView.drawsBackground)
        self.assertArgIsBOOL(NSClipView.setDrawsBackground_, 0)
        self.assertResultIsBOOL(NSClipView.copiesOnScroll)
        self.assertArgIsBOOL(NSClipView.setCopiesOnScroll_, 0)
        self.assertResultIsBOOL(NSClipView.autoscroll_)

if __name__ == "__main__":
    main()
