import AppKit
from PyObjCTools.TestSupport import TestCase


class TestNSTreeController(TestCase):
    def testMethods(self):
        self.assertResultIsBOOL(AppKit.NSTreeController.canInsert)
        self.assertResultIsBOOL(AppKit.NSTreeController.canInsertChild)
        self.assertResultIsBOOL(AppKit.NSTreeController.canAddChild)
        self.assertResultIsBOOL(AppKit.NSTreeController.avoidsEmptySelection)
        self.assertArgIsBOOL(AppKit.NSTreeController.setAvoidsEmptySelection_, 0)
        self.assertResultIsBOOL(AppKit.NSTreeController.preservesSelection)
        self.assertArgIsBOOL(AppKit.NSTreeController.setPreservesSelection_, 0)
        self.assertResultIsBOOL(AppKit.NSTreeController.selectsInsertedObjects)
        self.assertArgIsBOOL(AppKit.NSTreeController.setSelectsInsertedObjects_, 0)
        self.assertResultIsBOOL(AppKit.NSTreeController.alwaysUsesMultipleValuesMarker)
        self.assertArgIsBOOL(
            AppKit.NSTreeController.setAlwaysUsesMultipleValuesMarker_, 0
        )
        self.assertResultIsBOOL(AppKit.NSTreeController.setSelectionIndexPaths_)
        self.assertResultIsBOOL(AppKit.NSTreeController.setSelectionIndexPath_)
        self.assertResultIsBOOL(AppKit.NSTreeController.addSelectionIndexPaths_)
        self.assertResultIsBOOL(AppKit.NSTreeController.removeSelectionIndexPaths_)
