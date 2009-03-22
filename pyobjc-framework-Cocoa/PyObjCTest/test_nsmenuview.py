from AppKit import *
from PyObjCTools.TestSupport import *

class TestNSMenuView (TestCase):
    @onlyOn32Bit
    def testMethods(self):
        self.failUnlessResultIsBOOL(NSMenuView.isHorizontal)
        self.failUnlessArgIsBOOL(NSMenuView.setHorizontal_, 0)
        self.failUnlessResultIsBOOL(NSMenuView.needsSizing)
        self.failUnlessArgIsBOOL(NSMenuView.setNeedsSizing_, 0)
        self.failUnlessResultIsBOOL(NSMenuView.isAttached)
        self.failUnlessResultIsBOOL(NSMenuView.isTornOff)
        self.failUnlessResultIsBOOL(NSMenuView.trackWithEvent_)

if __name__ == "__main__":
    main()
