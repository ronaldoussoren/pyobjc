import CoreData
from PyObjCTools.TestSupport import TestCase, min_os_level


class TestNSPersistentCloudKitContainerEvent(TestCase):
    def test_enum_types(self):
        self.assertIsEnumType(CoreData.NSPersistentCloudKitContainerEventType)

    def test_constants(self):
        self.assertEqual(CoreData.NSPersistentCloudKitContainerEventTypeSetup, 0)
        self.assertEqual(CoreData.NSPersistentCloudKitContainerEventTypeImport, 1)
        self.assertEqual(CoreData.NSPersistentCloudKitContainerEventTypeExport, 2)

    @min_os_level("11.0")
    def test_constants11_0(self):
        self.assertIsInstance(
            CoreData.NSPersistentCloudKitContainerEventChangedNotification, str
        )
        self.assertIsInstance(
            CoreData.NSPersistentCloudKitContainerEventUserInfoKey, str
        )
