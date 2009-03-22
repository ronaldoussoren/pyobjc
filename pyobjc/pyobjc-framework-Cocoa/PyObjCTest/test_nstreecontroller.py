from AppKit import *
from PyObjCTools.TestSupport import *

class TestNSTreeController (TestCase):
    def testMethods(self):
        self.failUnlessResultIsBOOL(NSTreeController.canInsert)
        self.failUnlessResultIsBOOL(NSTreeController.canInsertChild)
        self.failUnlessResultIsBOOL(NSTreeController.canAddChild)
        self.failUnlessResultIsBOOL(NSTreeController.avoidsEmptySelection)
        self.failUnlessArgIsBOOL(NSTreeController.setAvoidsEmptySelection_, 0)
        self.failUnlessResultIsBOOL(NSTreeController.preservesSelection)
        self.failUnlessArgIsBOOL(NSTreeController.setPreservesSelection_, 0)
        self.failUnlessResultIsBOOL(NSTreeController.selectsInsertedObjects)
        self.failUnlessArgIsBOOL(NSTreeController.setSelectsInsertedObjects_, 0)
        self.failUnlessResultIsBOOL(NSTreeController.alwaysUsesMultipleValuesMarker)
        self.failUnlessArgIsBOOL(NSTreeController.setAlwaysUsesMultipleValuesMarker_, 0)
        self.failUnlessResultIsBOOL(NSTreeController.setSelectionIndexPaths_)
        self.failUnlessResultIsBOOL(NSTreeController.setSelectionIndexPath_)
        self.failUnlessResultIsBOOL(NSTreeController.addSelectionIndexPaths_)
        self.failUnlessResultIsBOOL(NSTreeController.removeSelectionIndexPaths_)

if __name__ == "__main__":
    main()
