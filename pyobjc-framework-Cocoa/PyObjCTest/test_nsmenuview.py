from AppKit import *
from PyObjCTools.TestSupport import *

class TestNSMenuView (TestCase):
    @onlyOn32Bit
    def testMethods(self):
        self.assertResultIsBOOL(NSMenuView.isHorizontal)
        self.assertArgIsBOOL(NSMenuView.setHorizontal_, 0)
        self.assertResultIsBOOL(NSMenuView.needsSizing)
        self.assertArgIsBOOL(NSMenuView.setNeedsSizing_, 0)
        self.assertResultIsBOOL(NSMenuView.isAttached)
        self.assertResultIsBOOL(NSMenuView.isTornOff)
        self.assertResultIsBOOL(NSMenuView.trackWithEvent_)

if __name__ == "__main__":
    main()
