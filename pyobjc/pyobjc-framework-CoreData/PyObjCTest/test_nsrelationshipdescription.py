
from PyObjCTools.TestSupport import *
from CoreData import *

class TestNSRelationshipDescription (TestCase):
    def testConstants(self):
        self.failUnlessEqual(NSNoActionDeleteRule, 0)
        self.failUnlessEqual(NSNullifyDeleteRule, 1)
        self.failUnlessEqual(NSCascadeDeleteRule, 2)
        self.failUnlessEqual(NSDenyDeleteRule, 3)

    def testMethods(self):
        self.failUnlessResultIsBOOL(NSRelationshipDescription.isToMany)

if __name__ == "__main__":
    main()
