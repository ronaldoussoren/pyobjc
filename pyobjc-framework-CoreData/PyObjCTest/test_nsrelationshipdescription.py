
from PyObjCTools.TestSupport import *
from CoreData import *

class TestNSRelationshipDescription (TestCase):
    def testConstants(self):
        self.assertEqual(NSNoActionDeleteRule, 0)
        self.assertEqual(NSNullifyDeleteRule, 1)
        self.assertEqual(NSCascadeDeleteRule, 2)
        self.assertEqual(NSDenyDeleteRule, 3)

    def testMethods(self):
        self.assertResultIsBOOL(NSRelationshipDescription.isToMany)

    @min_os_level('10.7')
    def testMethods10_7(self):
        self.assertArgIsBOOL(NSRelationshipDescription.setOrdered_, 0)
        self.assertResultIsBOOL(NSRelationshipDescription.isOrdered)

if __name__ == "__main__":
    main()
