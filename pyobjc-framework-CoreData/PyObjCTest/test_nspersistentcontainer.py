import CoreData
from PyObjCTools.TestSupport import TestCase, min_os_level


class TestNSPersistentContainer(TestCase):
    @min_os_level("10.12")
    def testMethods(self):
        self.assertArgIsBlock(
            CoreData.NSPersistentContainer.loadPersistentStoresWithCompletionHandler_,
            0,
            b"v@@",
        )
        self.assertArgIsBlock(
            CoreData.NSPersistentContainer.performBackgroundTask_, 0, b"v"
        )
