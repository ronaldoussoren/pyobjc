import CoreData
from PyObjCTools.TestSupport import TestCase, min_os_level


class TestNSRelationshipDescription(TestCase):
    def testConstants(self):
        self.assertEqual(CoreData.NSNoActionDeleteRule, 0)
        self.assertEqual(CoreData.NSNullifyDeleteRule, 1)
        self.assertEqual(CoreData.NSCascadeDeleteRule, 2)
        self.assertEqual(CoreData.NSDenyDeleteRule, 3)

    def testMethods(self):
        self.assertResultIsBOOL(CoreData.NSRelationshipDescription.isToMany)

    @min_os_level("10.7")
    def testMethods10_7(self):
        self.assertArgIsBOOL(CoreData.NSRelationshipDescription.setOrdered_, 0)
        self.assertResultIsBOOL(CoreData.NSRelationshipDescription.isOrdered)
