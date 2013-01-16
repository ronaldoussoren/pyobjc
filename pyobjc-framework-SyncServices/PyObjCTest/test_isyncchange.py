
from PyObjCTools.TestSupport import *
from SyncServices import *

try:
    unicode
except NameError:
    unicode = str

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

    @min_os_level('10.6')
    def testConstants10_5(self):
        # Document for 10.5, but not actually present there
        self.assertIsInstance(ISyncChangePropertyValueIsDefaultKey, unicode)

if __name__ == "__main__":
    main()
