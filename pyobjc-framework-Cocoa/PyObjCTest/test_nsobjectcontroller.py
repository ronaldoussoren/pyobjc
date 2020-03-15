import AppKit
from PyObjCTools.TestSupport import TestCase


class TestNSObjectController(TestCase):
    def testMethods(self):
        self.assertResultIsBOOL(AppKit.NSObjectController.automaticallyPreparesContent)
        self.assertArgIsBOOL(
            AppKit.NSObjectController.setAutomaticallyPreparesContent_, 0
        )
        self.assertResultIsBOOL(AppKit.NSObjectController.isEditable)
        self.assertArgIsBOOL(AppKit.NSObjectController.setEditable_, 0)
        self.assertResultIsBOOL(AppKit.NSObjectController.canAdd)
        self.assertResultIsBOOL(AppKit.NSObjectController.canRemove)
        self.assertResultIsBOOL(AppKit.NSObjectController.validateUserInterfaceItem_)
        self.assertResultIsBOOL(AppKit.NSObjectController.fetchWithRequest_merge_error_)
        self.assertArgIsBOOL(AppKit.NSObjectController.fetchWithRequest_merge_error_, 1)
        self.assertArgIsOut(AppKit.NSObjectController.fetchWithRequest_merge_error_, 2)
        self.assertResultIsBOOL(AppKit.NSObjectController.usesLazyFetching)
        self.assertArgIsBOOL(AppKit.NSObjectController.setUsesLazyFetching_, 0)
