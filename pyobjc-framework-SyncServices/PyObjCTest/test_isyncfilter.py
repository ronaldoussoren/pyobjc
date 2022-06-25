from PyObjCTools.TestSupport import TestCase
import SyncServices  # noqa: F401


class TestISyncFilterHelper(SyncServices.NSObject):
    def isEqual_(self, other):
        return True

    def shouldApplyRecord_withRecordIdentifier_(self, r, i):
        return False


class TestISyncFilter(TestCase):
    def testProtocols(self):
        self.assertProtocolExists("ISyncFiltering")

    def test_protocol_methods(self):
        self.assertResultIsBOOL(TestISyncFilterHelper.isEqual_)
        self.assertResultIsBOOL(
            TestISyncFilterHelper.shouldApplyRecord_withRecordIdentifier_
        )
