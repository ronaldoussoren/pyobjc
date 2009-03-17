from AppKit import *
from PyObjCTools.TestSupport import *

class TestNSArrayControler (TestCase):
    def testMethods(self):
        self.failUnlessResultIsBOOL(NSArrayController.automaticallyRearrangesObjects)

        self.failUnlessResultIsBOOL(NSArrayController.clearsFilterPredicateOnInsertion)
        self.failUnlessArgIsBOOL(NSArrayController.setClearsFilterPredicateOnInsertion_, 0)

        self.failUnlessResultIsBOOL(NSArrayController.avoidsEmptySelection)
        self.failUnlessArgIsBOOL(NSArrayController.setAvoidsEmptySelection_, 0)

        self.failUnlessResultIsBOOL(NSArrayController.preservesSelection)
        self.failUnlessArgIsBOOL(NSArrayController.setPreservesSelection_, 0)

        self.failUnlessResultIsBOOL(NSArrayController.selectsInsertedObjects)
        self.failUnlessArgIsBOOL(NSArrayController.setSelectsInsertedObjects_, 0)

        self.failUnlessResultIsBOOL(NSArrayController.alwaysUsesMultipleValuesMarker)
        self.failUnlessArgIsBOOL(NSArrayController.setAlwaysUsesMultipleValuesMarker_, 0)

        self.failUnlessResultIsBOOL(NSArrayController.setSelectionIndexes_)
        self.failUnlessResultIsBOOL(NSArrayController.setSelectionIndex_)
        self.failUnlessResultIsBOOL(NSArrayController.addSelectionIndexes_)
        self.failUnlessResultIsBOOL(NSArrayController.removeSelectionIndexes_)
        self.failUnlessResultIsBOOL(NSArrayController.setSelectedObjects_)
        self.failUnlessResultIsBOOL(NSArrayController.addSelectedObjects_)
        self.failUnlessResultIsBOOL(NSArrayController.canInsert)
        self.failUnlessResultIsBOOL(NSArrayController.canSelectNext)
        self.failUnlessResultIsBOOL(NSArrayController.canSelectPrevious)

if __name__ == "__main__":
    main()
