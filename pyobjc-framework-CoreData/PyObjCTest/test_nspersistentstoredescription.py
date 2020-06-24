import CoreData
from PyObjCTools.TestSupport import TestCase, min_os_level


class TestNSPersistentStoreDescription(TestCase):
    @min_os_level("10.12")
    def testMethods(self):
        self.assertArgIsBOOL(CoreData.NSPersistentStoreDescription.setReadOnly_, 0)
        self.assertResultIsBOOL(CoreData.NSPersistentStoreDescription.isReadOnly)

        self.assertArgIsBOOL(
            CoreData.NSPersistentStoreDescription.setShouldAddStoreAsynchronously_, 0
        )
        self.assertResultIsBOOL(
            CoreData.NSPersistentStoreDescription.shouldAddStoreAsynchronously
        )

        self.assertArgIsBOOL(
            CoreData.NSPersistentStoreDescription.setShouldMigrateStoreAutomatically_, 0
        )
        self.assertResultIsBOOL(
            CoreData.NSPersistentStoreDescription.shouldMigrateStoreAutomatically
        )

        self.assertArgIsBOOL(
            CoreData.NSPersistentStoreDescription.setShouldInferMappingModelAutomatically_,
            0,
        )
        self.assertResultIsBOOL(
            CoreData.NSPersistentStoreDescription.shouldInferMappingModelAutomatically
        )
