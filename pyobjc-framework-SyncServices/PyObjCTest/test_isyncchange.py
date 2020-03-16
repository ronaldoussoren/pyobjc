from PyObjCTools.TestSupport import TestCase, min_os_level
import SyncServices


class TestISyncChange(TestCase):
    def testConstants(self):
        self.assertEqual(SyncServices.ISyncChangeTypeNone, 0)
        self.assertEqual(SyncServices.ISyncChangeTypeAdd, 1)
        self.assertEqual(SyncServices.ISyncChangeTypeModify, 2)
        self.assertEqual(SyncServices.ISyncChangeTypeDelete, 3)

        self.assertIsInstance(SyncServices.ISyncChangePropertyActionKey, str)
        self.assertIsInstance(SyncServices.ISyncChangePropertySet, str)
        self.assertIsInstance(SyncServices.ISyncChangePropertyClear, str)
        self.assertIsInstance(SyncServices.ISyncChangePropertyNameKey, str)
        self.assertIsInstance(SyncServices.ISyncChangePropertyValueKey, str)

    @min_os_level("10.6")
    def testConstants10_5(self):
        # Document for 10.5, but not actually present there
        self.assertIsInstance(SyncServices.ISyncChangePropertyValueIsDefaultKey, str)
