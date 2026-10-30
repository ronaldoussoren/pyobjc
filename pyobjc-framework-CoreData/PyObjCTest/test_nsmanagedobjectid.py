import CoreData
from PyObjCTools.TestSupport import TestCase


class TestNSManagedObjectID(TestCase):
    def test_methods(self):
        self.assertResultIsBOOL(CoreData.NSManagedObjectID.isTemporaryID)
