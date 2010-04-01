
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

if __name__ == "__main__":
    main()
