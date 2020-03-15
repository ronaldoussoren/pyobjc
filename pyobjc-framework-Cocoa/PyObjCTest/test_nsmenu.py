import AppKit
from PyObjCTools.TestSupport import TestCase, min_os_level, min_sdk_level
import objc


class TestNSMenuHelper(AppKit.NSObject):
    def validateMenuItem_(self, item):
        return 1

    def numberOfItemsInMenu_(self, menu):
        return 1

    def menu_updateItem_atIndex_shouldCancel_(self, m, i, d, s):
        return 1

    def menuHasKeyEquivalent_forEvent_target_action_(self, m, e, t, a):
        return 1

    def confinementRectForMenu_onScreen_(self, m, s):
        return 1


class TestNSMenu(TestCase):
    @min_sdk_level("10.6")
    def testProtocolObjects(self):
        objc.protocolNamed("NSMenuDelegate")

    def testProtocol(self):
        self.assertResultIsBOOL(TestNSMenuHelper.validateMenuItem_)
        self.assertResultHasType(
            TestNSMenuHelper.numberOfItemsInMenu_, objc._C_NSInteger
        )
        self.assertResultIsBOOL(TestNSMenuHelper.menu_updateItem_atIndex_shouldCancel_)
        self.assertArgHasType(
            TestNSMenuHelper.menu_updateItem_atIndex_shouldCancel_, 2, objc._C_NSInteger
        )
        self.assertArgIsBOOL(TestNSMenuHelper.menu_updateItem_atIndex_shouldCancel_, 3)
        self.assertResultIsBOOL(
            TestNSMenuHelper.menuHasKeyEquivalent_forEvent_target_action_
        )
        self.assertArgHasType(
            TestNSMenuHelper.menuHasKeyEquivalent_forEvent_target_action_, 2, b"o^@"
        )
        self.assertArgHasType(
            TestNSMenuHelper.menuHasKeyEquivalent_forEvent_target_action_, 3, b"o^:"
        )

    def testMethods(self):
        self.assertResultIsBOOL(AppKit.NSMenu.menuBarVisible)
        self.assertArgIsBOOL(AppKit.NSMenu.setMenuBarVisible_, 0)
        self.assertResultIsBOOL(AppKit.NSMenu.autoenablesItems)
        self.assertArgIsBOOL(AppKit.NSMenu.setAutoenablesItems_, 0)
        self.assertResultIsBOOL(AppKit.NSMenu.performKeyEquivalent_)
        self.assertResultIsBOOL(AppKit.NSMenu.autoenablesItems)
        self.assertArgIsBOOL(AppKit.NSMenu.setMenuChangedMessagesEnabled_, 0)
        self.assertResultIsBOOL(AppKit.NSMenu.isTornOff)
        self.assertResultIsBOOL(AppKit.NSMenu.isAttached)
        self.assertResultIsBOOL(AppKit.NSMenu.showsStateColumn)
        self.assertArgIsBOOL(AppKit.NSMenu.setShowsStateColumn_, 0)

        self.assertResultIsBOOL(AppKit.NSMenu.menuChangedMessagesEnabled)
        self.assertArgIsBOOL(AppKit.NSMenu.setMenuChangedMessagesEnabled_, 0)
        self.assertResultHasType(
            AppKit.NSMenu.locationForSubmenu_, AppKit.NSPoint.__typestr__
        )

    def testConstants(self):
        self.assertIsInstance(AppKit.NSMenuWillSendActionNotification, str)
        self.assertIsInstance(AppKit.NSMenuDidSendActionNotification, str)
        self.assertIsInstance(AppKit.NSMenuDidAddItemNotification, str)
        self.assertIsInstance(AppKit.NSMenuDidRemoveItemNotification, str)
        self.assertIsInstance(AppKit.NSMenuDidChangeItemNotification, str)
        self.assertIsInstance(AppKit.NSMenuDidBeginTrackingNotification, str)
        self.assertIsInstance(AppKit.NSMenuDidEndTrackingNotification, str)

    @min_os_level("10.6")
    def testMethods10_6(self):
        self.assertResultIsBOOL(
            AppKit.NSMenu.popUpMenuPositioningItem_atLocation_inView_
        )
        self.assertArgHasType(
            AppKit.NSMenu.popUpMenuPositioningItem_atLocation_inView_,
            1,
            AppKit.NSPoint.__typestr__,
        )
        self.assertResultHasType(AppKit.NSMenu.size, AppKit.NSSize.__typestr__)
        self.assertResultIsBOOL(AppKit.NSMenu.allowsContextMenuPlugIns)
        self.assertArgIsBOOL(AppKit.NSMenu.setAllowsContextMenuPlugIns_, 0)

        self.assertResultHasType(
            TestNSMenuHelper.confinementRectForMenu_onScreen_, AppKit.NSRect.__typestr__
        )

    @min_os_level("10.6")
    def testConstants10_6(self):
        self.assertEqual(AppKit.NSMenuPropertyItemTitle, 1 << 0)
        self.assertEqual(AppKit.NSMenuPropertyItemAttributedTitle, 1 << 1)
        self.assertEqual(AppKit.NSMenuPropertyItemKeyEquivalent, 1 << 2)
        self.assertEqual(AppKit.NSMenuPropertyItemImage, 1 << 3)
        self.assertEqual(AppKit.NSMenuPropertyItemEnabled, 1 << 4)
        self.assertEqual(AppKit.NSMenuPropertyItemAccessibilityDescription, 1 << 5)
