import CoreData
from PyObjCTools.TestSupport import TestCase, min_os_level


class TestNSFetchIndexElementDescription(TestCase):
    def testConstants(self):
        self.assertEqual(CoreData.NSFetchIndexElementTypeBinary, 0)
        self.assertEqual(CoreData.NSFetchIndexElementTypeRTree, 1)

    @min_os_level("10.13")
    def testMethods(self):
        self.assertResultIsBOOL(CoreData.NSFetchIndexElementDescription.isAscending)
        self.assertArgIsBOOL(CoreData.NSFetchIndexElementDescription.setAscending_, 0)
