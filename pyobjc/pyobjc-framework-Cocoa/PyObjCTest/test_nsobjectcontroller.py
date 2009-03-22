from AppKit import *
from PyObjCTools.TestSupport import *

class TestNSObjectController (TestCase):
    def testMethods(self):
        self.failUnlessResultIsBOOL(NSObjectController.automaticallyPreparesContent)
        self.failUnlessArgIsBOOL(NSObjectController.setAutomaticallyPreparesContent_, 0)
        self.failUnlessResultIsBOOL(NSObjectController.isEditable)
        self.failUnlessArgIsBOOL(NSObjectController.setEditable_, 0)
        self.failUnlessResultIsBOOL(NSObjectController.canAdd)
        self.failUnlessResultIsBOOL(NSObjectController.canRemove)
        self.failUnlessResultIsBOOL(NSObjectController.validateUserInterfaceItem_)
        self.failUnlessResultIsBOOL(NSObjectController.fetchWithRequest_merge_error_)
        self.failUnlessArgIsBOOL(NSObjectController.fetchWithRequest_merge_error_, 1)
        self.failUnlessArgIsOut(NSObjectController.fetchWithRequest_merge_error_, 2)
        self.failUnlessResultIsBOOL(NSObjectController.usesLazyFetching)
        self.failUnlessArgIsBOOL(NSObjectController.setUsesLazyFetching_, 0)


if __name__ == "__main__":
    main()
