
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
        self.assertResultIsBOOL(TestNSMenuHelper.validateMenuItem_)
        self.assertResultHasType(TestNSMenuHelper.numberOfItemsInMenu_, objc._C_NSInteger)
        self.assertResultIsBOOL(TestNSMenuHelper.menu_updateItem_atIndex_shouldCancel_)
        self.assertArgHasType(TestNSMenuHelper.menu_updateItem_atIndex_shouldCancel_, 2, objc._C_NSInteger)
        self.assertArgIsBOOL(TestNSMenuHelper.menu_updateItem_atIndex_shouldCancel_, 3)
        self.assertResultIsBOOL(TestNSMenuHelper.menuHasKeyEquivalent_forEvent_target_action_)
        self.assertArgHasType(TestNSMenuHelper.menuHasKeyEquivalent_forEvent_target_action_, 2, b'o^@')
        self.assertArgHasType(TestNSMenuHelper.menuHasKeyEquivalent_forEvent_target_action_, 3, b'o^:')

    def testMethods(self):
        self.assertResultIsBOOL(NSMenu.menuBarVisible)
        self.assertArgIsBOOL(NSMenu.setMenuBarVisible_, 0)
        self.assertResultIsBOOL(NSMenu.autoenablesItems)
        self.assertArgIsBOOL(NSMenu.setAutoenablesItems_, 0)
        self.assertResultIsBOOL(NSMenu.performKeyEquivalent_)
        self.assertResultIsBOOL(NSMenu.autoenablesItems)
        self.assertArgIsBOOL(NSMenu.setMenuChangedMessagesEnabled_, 0)
        self.assertResultIsBOOL(NSMenu.isTornOff)
        self.assertResultIsBOOL(NSMenu.isAttached)
        self.assertResultIsBOOL(NSMenu.showsStateColumn)
        self.assertArgIsBOOL(NSMenu.setShowsStateColumn_, 0)

        self.assertResultIsBOOL(NSMenu.menuChangedMessagesEnabled)
        self.assertArgIsBOOL(NSMenu.setMenuChangedMessagesEnabled_, 0)
        self.assertResultHasType(NSMenu.locationForSubmenu_, NSPoint.__typestr__)

    def testConstants(self):
        self.assertIsInstance(NSMenuWillSendActionNotification, unicode)
        self.assertIsInstance(NSMenuDidSendActionNotification, unicode)
        self.assertIsInstance(NSMenuDidAddItemNotification, unicode)
        self.assertIsInstance(NSMenuDidRemoveItemNotification, unicode)
        self.assertIsInstance(NSMenuDidChangeItemNotification, unicode)
        self.assertIsInstance(NSMenuDidBeginTrackingNotification, unicode)
        self.assertIsInstance(NSMenuDidEndTrackingNotification, unicode)

    @min_os_level('10.6')
    def testMethods10_6(self):
        self.assertResultIsBOOL(NSMenu.popUpMenuPositioningItem_atLocation_inView_)
        self.assertArgHasType(NSMenu.popUpMenuPositioningItem_atLocation_inView_, 1, NSPoint.__typestr__)
        self.assertResultHasType(NSMenu.size, NSSize.__typestr__)
        self.assertResultIsBOOL(NSMenu.allowsContextMenuPlugIns)
        self.assertArgIsBOOL(NSMenu.setAllowsContextMenuPlugIns_, 0)

        self.assertResultHasType(TestNSMenuHelper.confinementRectForMenu_onScreen_, NSRect.__typestr__)

    @min_os_level('10.6')
    def testConstants10_6(self):
        self.assertEqual(NSMenuPropertyItemTitle, 1 << 0)
        self.assertEqual(NSMenuPropertyItemAttributedTitle, 1 << 1)
        self.assertEqual(NSMenuPropertyItemKeyEquivalent, 1 << 2)
        self.assertEqual(NSMenuPropertyItemImage, 1 << 3)
        self.assertEqual(NSMenuPropertyItemEnabled, 1 << 4)
        self.assertEqual(NSMenuPropertyItemAccessibilityDescription, 1 << 5)



if __name__ == "__main__":
    main()
