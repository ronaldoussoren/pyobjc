from PyObjCTools.TestSupport import TestCase
import SyncServices


class TestISyncChange(TestCase):
    def test_enums(self):
        self.assertIsEnumType(SyncServices.ISyncChangeType)
        self.assertEqual(SyncServices.ISyncChangeTypeNone, 0)
        self.assertEqual(SyncServices.ISyncChangeTypeAdd, 1)
        self.assertEqual(SyncServices.ISyncChangeTypeModify, 2)
        self.assertEqual(SyncServices.ISyncChangeTypeDelete, 3)

    def test_constants(self):
        self.assertIsInstance(SyncServices.ISyncChangePropertyActionKey, str)
        self.assertIsInstance(SyncServices.ISyncChangePropertySet, str)
        self.assertIsInstance(SyncServices.ISyncChangePropertyClear, str)
        self.assertIsInstance(SyncServices.ISyncChangePropertyNameKey, str)
        self.assertIsInstance(SyncServices.ISyncChangePropertyValueKey, str)
        self.assertIsInstance(SyncServices.ISyncChangePropertyValueIsDefaultKey, str)
