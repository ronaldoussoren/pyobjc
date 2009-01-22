
from PyObjCTools.TestSupport import *
from SyncServices import *

class TestISyncFilterHelper (NSObject):
    def isEqual_(self, other):
        return True

    def shouldApplyRecord_withRecordIdentifier_(self, r, i):
        return False

class TestISyncFilter (TestCase):
    def testProtocols(self):
        self.failUnlessResultIsBOOL(TestISyncFilterHelper.isEqual_)
        self.failUnlessResultIsBOOL(TestISyncFilterHelper.shouldApplyRecord_withRecordIdentifier_)


if __name__ == "__main__":
    main()
