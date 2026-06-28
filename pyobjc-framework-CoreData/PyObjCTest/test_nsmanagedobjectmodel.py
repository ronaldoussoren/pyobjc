import CoreData
from PyObjCTools.TestSupport import TestCase, min_os_level


class TestNSManagedObjectModel(TestCase):
    def test_methods(self):
        self.assertResultIsBOOL(
            CoreData.NSManagedObjectModel.isConfiguration_compatibleWithStoreMetadata_
        )

    @min_os_level("14.0")
    def test_methods14_0(self):
        self.assertArgIsOut(
            CoreData.NSManagedObjectModel.checksumsForVersionedModelAtURL_error_, 1
        )
