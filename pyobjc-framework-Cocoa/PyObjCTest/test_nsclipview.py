from AppKit import *
from PyObjCTools.TestSupport import *

class TestNSClipView (TestCase):
    def testMethods(self):
        self.assertResultIsBOOL(NSClipView.drawsBackground)
        self.assertArgIsBOOL(NSClipView.setDrawsBackground_, 0)
        self.assertResultIsBOOL(NSClipView.copiesOnScroll)
        self.assertArgIsBOOL(NSClipView.setCopiesOnScroll_, 0)
        self.assertResultIsBOOL(NSClipView.autoscroll_)

    @min_os_level('10.10')
    def testMethods10_10(self):
        self.assertResultIsBOOL(NSClipView.automaticallyAdjustsContentInsets)
        self.assertArgIsBOOL(NSClipView.setAutomaticallyAdjustsContentInsets_, 0)

if __name__ == "__main__":
    main()
