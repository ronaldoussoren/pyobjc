import CoreData
from PyObjCTools.TestSupport import TestCase, min_os_level


class TestNSManagedObjectModel(TestCase):
    @min_os_level("10.5")
    def testMethods(self):
        self.assertResultIsBOOL(
            CoreData.NSManagedObjectModel.isConfiguration_compatibleWithStoreMetadata_
        )
