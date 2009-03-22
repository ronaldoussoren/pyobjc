
from PyObjCTools.TestSupport import *
from AppKit import *

class TestNSMenuHelper (NSObject):
    def validateMenuItem_(self, item): return 1
    def numberOfItemsInMenu_(self, menu): return 1
    def menu_updateItem_atIndex_shouldCancel_(self, m, i, d, s): return 1
    def menuHasKeyEquivalent_forEvent_target_action_(self, m, e, t, a): return 1


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


    def testConstants(self):
        self.failUnlessIsInstance(NSMenuWillSendActionNotification, unicode)
        self.failUnlessIsInstance(NSMenuDidSendActionNotification, unicode)
        self.failUnlessIsInstance(NSMenuDidAddItemNotification, unicode)
        self.failUnlessIsInstance(NSMenuDidRemoveItemNotification, unicode)
        self.failUnlessIsInstance(NSMenuDidChangeItemNotification, unicode)
        self.failUnlessIsInstance(NSMenuDidBeginTrackingNotification, unicode)
        self.failUnlessIsInstance(NSMenuDidEndTrackingNotification, unicode)



if __name__ == "__main__":
    main()
