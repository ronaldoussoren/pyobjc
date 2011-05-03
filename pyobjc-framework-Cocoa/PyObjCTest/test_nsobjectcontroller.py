from AppKit import *
from PyObjCTools.TestSupport import *

class TestNSObjectController (TestCase):
    def testMethods(self):
        self.assertResultIsBOOL(NSObjectController.automaticallyPreparesContent)
        self.assertArgIsBOOL(NSObjectController.setAutomaticallyPreparesContent_, 0)
        self.assertResultIsBOOL(NSObjectController.isEditable)
        self.assertArgIsBOOL(NSObjectController.setEditable_, 0)
        self.assertResultIsBOOL(NSObjectController.canAdd)
        self.assertResultIsBOOL(NSObjectController.canRemove)
        self.assertResultIsBOOL(NSObjectController.validateUserInterfaceItem_)
        self.assertResultIsBOOL(NSObjectController.fetchWithRequest_merge_error_)
        self.assertArgIsBOOL(NSObjectController.fetchWithRequest_merge_error_, 1)
        self.assertArgIsOut(NSObjectController.fetchWithRequest_merge_error_, 2)
        self.assertResultIsBOOL(NSObjectController.usesLazyFetching)
        self.assertArgIsBOOL(NSObjectController.setUsesLazyFetching_, 0)


if __name__ == "__main__":
    main()
