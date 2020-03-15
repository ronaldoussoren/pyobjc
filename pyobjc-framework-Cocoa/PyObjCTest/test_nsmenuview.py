import AppKit
from PyObjCTools.TestSupport import TestCase, onlyOn32Bit


class TestNSMenuView(TestCase):
    @onlyOn32Bit
    def testMethods(self):
        self.assertResultIsBOOL(AppKit.NSMenuView.isHorizontal)
        self.assertArgIsBOOL(AppKit.NSMenuView.setHorizontal_, 0)
        self.assertResultIsBOOL(AppKit.NSMenuView.needsSizing)
        self.assertArgIsBOOL(AppKit.NSMenuView.setNeedsSizing_, 0)
        self.assertResultIsBOOL(AppKit.NSMenuView.isAttached)
        self.assertResultIsBOOL(AppKit.NSMenuView.isTornOff)
        self.assertResultIsBOOL(AppKit.NSMenuView.trackWithEvent_)
