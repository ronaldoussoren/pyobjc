from AppKit import *
from PyObjCTools.TestSupport import *

class TestNSTreeController (TestCase):
    def testMethods(self):
        self.assertResultIsBOOL(NSTreeController.canInsert)
        self.assertResultIsBOOL(NSTreeController.canInsertChild)
        self.assertResultIsBOOL(NSTreeController.canAddChild)
        self.assertResultIsBOOL(NSTreeController.avoidsEmptySelection)
        self.assertArgIsBOOL(NSTreeController.setAvoidsEmptySelection_, 0)
        self.assertResultIsBOOL(NSTreeController.preservesSelection)
        self.assertArgIsBOOL(NSTreeController.setPreservesSelection_, 0)
        self.assertResultIsBOOL(NSTreeController.selectsInsertedObjects)
        self.assertArgIsBOOL(NSTreeController.setSelectsInsertedObjects_, 0)
        self.assertResultIsBOOL(NSTreeController.alwaysUsesMultipleValuesMarker)
        self.assertArgIsBOOL(NSTreeController.setAlwaysUsesMultipleValuesMarker_, 0)
        self.assertResultIsBOOL(NSTreeController.setSelectionIndexPaths_)
        self.assertResultIsBOOL(NSTreeController.setSelectionIndexPath_)
        self.assertResultIsBOOL(NSTreeController.addSelectionIndexPaths_)
        self.assertResultIsBOOL(NSTreeController.removeSelectionIndexPaths_)

if __name__ == "__main__":
    main()
