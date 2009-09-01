
from PyObjCTools.TestSupport import *
from AppKit import *

class TestNSMenuHelper (NSObject):
    def validateMenuItem_(self, item): return 1
    def numberOfItemsInMenu_(self, menu): return 1
    def menu_updateItem_atIndex_shouldCancel_(self, m, i, d, s): return 1
    def menuHasKeyEquivalent_forEvent_target_action_(self, m, e, t, a): return 1
    def confinementRectForMenu_onScreen_(self, m, s): return 1


class TestNSMenu (TestCase):
    def testProtocol(self):
        self.failUnlessResultIsBOOL(TestNSMenuHelper.validateMenuItem_)
        self.failUnlessResultHasType(TestNSMenuHelper.numberOfItemsInMenu_, objc._C_NSInteger)
        self.failUnlessResultIsBOOL(TestNSMenuHelper.menu_updateItem_atIndex_shouldCancel_)
        self.failUnlessArgHasType(TestNSMenuHelper.menu_updateItem_atIndex_shouldCancel_, 2, objc._C_NSInteger)
        self.failUnlessArgIsBOOL(TestNSMenuHelper.menu_updateItem_atIndex_shouldCancel_, 3)
        self.failUnlessResultIsBOOL(TestNSMenuHelper.menuHasKeyEquivalent_forEvent_target_action_)
        self.failUnlessArgHasType(TestNSMenuHelper.menuHasKeyEquivalent_forEvent_target_action_, 2, 'o^@')
        self.failUnlessArgHasType(TestNSMenuHelper.menuHasKeyEquivalent_forEvent_target_action_, 3, 'o^:')

    def testMethods(self):
        self.failUnlessResultIsBOOL(NSMenu.menuBarVisible)
        self.failUnlessArgIsBOOL(NSMenu.setMenuBarVisible_, 0)
        self.failUnlessResultIsBOOL(NSMenu.autoenablesItems)
        self.failUnlessArgIsBOOL(NSMenu.setAutoenablesItems_, 0)
        self.failUnlessResultIsBOOL(NSMenu.performKeyEquivalent_)
        self.failUnlessResultIsBOOL(NSMenu.autoenablesItems)
        self.failUnlessArgIsBOOL(NSMenu.setMenuChangedMessagesEnabled_, 0)
        self.failUnlessResultIsBOOL(NSMenu.isTornOff)
        self.failUnlessResultIsBOOL(NSMenu.isAttached)
        self.failUnlessResultIsBOOL(NSMenu.showsStateColumn)
        self.failUnlessArgIsBOOL(NSMenu.setShowsStateColumn_, 0)

        self.failUnlessResultIsBOOL(NSMenu.menuChangedMessagesEnabled)
        self.failUnlessArgIsBOOL(NSMenu.setMenuChangedMessagesEnabled_, 0)
        self.failUnlessResultHasType(NSMenu.locationForSubmenu_, NSPoint.__typestr__)

    def testConstants(self):
        self.failUnlessIsInstance(NSMenuWillSendActionNotification, unicode)
        self.failUnlessIsInstance(NSMenuDidSendActionNotification, unicode)
        self.failUnlessIsInstance(NSMenuDidAddItemNotification, unicode)
        self.failUnlessIsInstance(NSMenuDidRemoveItemNotification, unicode)
        self.failUnlessIsInstance(NSMenuDidChangeItemNotification, unicode)
        self.failUnlessIsInstance(NSMenuDidBeginTrackingNotification, unicode)
        self.failUnlessIsInstance(NSMenuDidEndTrackingNotification, unicode)

    @min_os_level('10.6')
    def testMethods10_6(self):
        self.failUnlessResultIsBOOL(NSMenu.popUpMenuPositioningItem_atLocation_inView_)
        self.failUnlessArgHasType(NSMenu.popUpMenuPositioningItem_atLocation_inView_, 1, NSPoint.__typestr__)
        self.failUnlessResultHasType(NSMenu.size, NSSize.__typestr__)
        self.failUnlessResultIsBOOL(NSMenu.allowsContextMenuPlugIns)
        self.failUnlessArgIsBOOL(NSMenu.setAllowsContextMenuPlugIns_, 0)

        self.failUnlessResultHasType(TestNSMenuHelper.confinementRectForMenu_onScreen_, NSRect.__typestr__)

    @min_os_level('10.6')
    def testConstants10_6(self):
        self.failUnlessEqual(NSMenuPropertyItemTitle, 1 << 0)
        self.failUnlessEqual(NSMenuPropertyItemAttributedTitle, 1 << 1)
        self.failUnlessEqual(NSMenuPropertyItemKeyEquivalent, 1 << 2)
        self.failUnlessEqual(NSMenuPropertyItemImage, 1 << 3)
        self.failUnlessEqual(NSMenuPropertyItemEnabled, 1 << 4)
        self.failUnlessEqual(NSMenuPropertyItemAccessibilityDescription, 1 << 5)



if __name__ == "__main__":
    main()
