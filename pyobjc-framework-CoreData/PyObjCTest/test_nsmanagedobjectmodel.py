import CoreData
from PyObjCTools.TestSupport import TestCase, min_os_level


class TestNSManagedObjectModel(TestCase):
    @min_os_level("10.5")
    def testMethods(self):
        self.assertResultIsBOOL(
            CoreData.NSManagedObjectModel.isConfiguration_compatibleWithStoreMetadata_
        )

    @min_os_level("14.0")
    def test_methods14_0(self):
        self.assertArgIsOut(
            CoreData.NSManagedObjectModel.checksumsForVersionedModelAtURL_error_, 1
        )
