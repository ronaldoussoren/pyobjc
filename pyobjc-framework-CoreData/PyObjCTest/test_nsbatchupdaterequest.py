import CoreData
from PyObjCTools.TestSupport import TestCase, min_os_level


class TestNSBatchUpdateRequest(TestCase):
    @min_os_level("10.10")
    def testMethods(self):
        self.assertResultIsBOOL(CoreData.NSBatchUpdateRequest.includesSubentities)
        self.assertArgIsBOOL(CoreData.NSBatchUpdateRequest.setIncludesSubentities_, 0)
