import AppKit
from PyObjCTools.TestSupport import TestCase


class TestNSArrayControler(TestCase):
    def testMethods(self):
        self.assertResultIsBOOL(AppKit.NSArrayController.automaticallyRearrangesObjects)

        self.assertResultIsBOOL(
            AppKit.NSArrayController.clearsFilterPredicateOnInsertion
        )
        self.assertArgIsBOOL(
            AppKit.NSArrayController.setClearsFilterPredicateOnInsertion_, 0
        )

        self.assertResultIsBOOL(AppKit.NSArrayController.avoidsEmptySelection)
        self.assertArgIsBOOL(AppKit.NSArrayController.setAvoidsEmptySelection_, 0)

        self.assertResultIsBOOL(AppKit.NSArrayController.preservesSelection)
        self.assertArgIsBOOL(AppKit.NSArrayController.setPreservesSelection_, 0)

        self.assertResultIsBOOL(AppKit.NSArrayController.selectsInsertedObjects)
        self.assertArgIsBOOL(AppKit.NSArrayController.setSelectsInsertedObjects_, 0)

        self.assertResultIsBOOL(AppKit.NSArrayController.alwaysUsesMultipleValuesMarker)
        self.assertArgIsBOOL(
            AppKit.NSArrayController.setAlwaysUsesMultipleValuesMarker_, 0
        )

        self.assertResultIsBOOL(AppKit.NSArrayController.setSelectionIndexes_)
        self.assertResultIsBOOL(AppKit.NSArrayController.setSelectionIndex_)
        self.assertResultIsBOOL(AppKit.NSArrayController.addSelectionIndexes_)
        self.assertResultIsBOOL(AppKit.NSArrayController.removeSelectionIndexes_)
        self.assertResultIsBOOL(AppKit.NSArrayController.setSelectedObjects_)
        self.assertResultIsBOOL(AppKit.NSArrayController.addSelectedObjects_)
        self.assertResultIsBOOL(AppKit.NSArrayController.removeSelectedObjects_)
        self.assertResultIsBOOL(AppKit.NSArrayController.canInsert)
        self.assertResultIsBOOL(AppKit.NSArrayController.canSelectNext)
        self.assertResultIsBOOL(AppKit.NSArrayController.canSelectPrevious)
