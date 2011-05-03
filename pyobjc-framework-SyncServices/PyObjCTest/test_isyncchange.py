
from PyObjCTools.TestSupport import *
from SyncServices import *

class TestISyncChange (TestCase):
    def testConstants(self):
        self.assertEqual(ISyncChangeTypeNone, 0)
        self.assertEqual(ISyncChangeTypeAdd, 1)
        self.assertEqual(ISyncChangeTypeModify, 2)
        self.assertEqual(ISyncChangeTypeDelete, 3)

        self.assertIsInstance(ISyncChangePropertyActionKey, unicode)
        self.assertIsInstance(ISyncChangePropertySet, unicode)
        self.assertIsInstance(ISyncChangePropertyClear, unicode)
        self.assertIsInstance(ISyncChangePropertyNameKey, unicode)
        self.assertIsInstance(ISyncChangePropertyValueKey, unicode)

    @min_os_level('10.5')
    def testConstants10_5(self):
        self.assertIsInstance(ISyncChangePropertyValueIsDefaultKey, unicode)

if __name__ == "__main__":
    main()
