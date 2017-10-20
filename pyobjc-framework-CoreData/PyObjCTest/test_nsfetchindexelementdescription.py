from PyObjCTools.TestSupport import *
from CoreData import *

class TestNSFetchIndexElementDescription (TestCase):

    def testConstants(self):
        self.assertEqual(NSFetchIndexElementTypeBinary, 0)
        self.assertEqual(NSFetchIndexElementTypeRTree, 1)

    @min_os_level('10.13')
    def testMethods(self):
        self.assertResultIsBOOL(NSFetchIndexElementDescription.isAscending)
        self.assertArgIsBOOL(NSFetchIndexElementDescription.setAscending_, 0)


if __name__ == "__main__":
    main()
