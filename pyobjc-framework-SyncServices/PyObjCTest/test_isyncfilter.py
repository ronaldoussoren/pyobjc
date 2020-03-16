from PyObjCTools.TestSupport import TestCase
import SyncServices  # noqa: F401
import objc


class TestISyncFilterHelper(SyncServices.NSObject):
    def isEqual_(self, other):
        return True

    def shouldApplyRecord_withRecordIdentifier_(self, r, i):
        return False


class TestISyncFilter(TestCase):
    def testProtocols(self):
        objc.protocolNamed("ISyncFiltering")
        self.assertResultIsBOOL(TestISyncFilterHelper.isEqual_)
        self.assertResultIsBOOL(
            TestISyncFilterHelper.shouldApplyRecord_withRecordIdentifier_
        )
