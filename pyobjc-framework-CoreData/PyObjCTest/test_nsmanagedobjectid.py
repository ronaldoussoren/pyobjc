import CoreData
from PyObjCTools.TestSupport import TestCase


class TestNSManagedObjectID(TestCase):
    def testMethods(self):
        self.assertResultIsBOOL(CoreData.NSManagedObjectID.isTemporaryID)
