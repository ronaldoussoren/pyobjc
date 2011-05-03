from AppKit import *
from PyObjCTools.TestSupport import *

class TestNSArrayControler (TestCase):
    def testMethods(self):
        self.assertResultIsBOOL(NSArrayController.automaticallyRearrangesObjects)

        self.assertResultIsBOOL(NSArrayController.clearsFilterPredicateOnInsertion)
        self.assertArgIsBOOL(NSArrayController.setClearsFilterPredicateOnInsertion_, 0)

        self.assertResultIsBOOL(NSArrayController.avoidsEmptySelection)
        self.assertArgIsBOOL(NSArrayController.setAvoidsEmptySelection_, 0)

        self.assertResultIsBOOL(NSArrayController.preservesSelection)
        self.assertArgIsBOOL(NSArrayController.setPreservesSelection_, 0)

        self.assertResultIsBOOL(NSArrayController.selectsInsertedObjects)
        self.assertArgIsBOOL(NSArrayController.setSelectsInsertedObjects_, 0)

        self.assertResultIsBOOL(NSArrayController.alwaysUsesMultipleValuesMarker)
        self.assertArgIsBOOL(NSArrayController.setAlwaysUsesMultipleValuesMarker_, 0)

        self.assertResultIsBOOL(NSArrayController.setSelectionIndexes_)
        self.assertResultIsBOOL(NSArrayController.setSelectionIndex_)
        self.assertResultIsBOOL(NSArrayController.addSelectionIndexes_)
        self.assertResultIsBOOL(NSArrayController.removeSelectionIndexes_)
        self.assertResultIsBOOL(NSArrayController.setSelectedObjects_)
        self.assertResultIsBOOL(NSArrayController.addSelectedObjects_)
        self.assertResultIsBOOL(NSArrayController.canInsert)
        self.assertResultIsBOOL(NSArrayController.canSelectNext)
        self.assertResultIsBOOL(NSArrayController.canSelectPrevious)

if __name__ == "__main__":
    main()
