import CoreData
from PyObjCTools.TestSupport import TestCase, min_os_level


class TestNSPersistentCloudKitContainerEvent(TestCase):
    def test_constants(self):
        self.assertEqual(CoreData.NSPersistentCloudKitContainerEventTypeSetup, 0)
        self.assertEqual(CoreData.NSPersistentCloudKitContainerEventTypeImport, 1)
        self.assertEqual(CoreData.NSPersistentCloudKitContainerEventTypeExport, 2)

    @min_os_level("10.16")
    def test_constants10_16(self):
        self.assertIsInstance(
            CoreData.NSPersistentCloudKitContainerEventChangedNotification, str
        )
        self.assertIsInstance(
            CoreData.NSPersistentCloudKitContainerEventUserInfoKey, str
        )
