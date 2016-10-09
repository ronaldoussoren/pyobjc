from PyObjCTools.TestSupport import *
from CoreData import *

class TestNSPersistentStoreDescription (TestCase):
    @min_os_level('10.12')
    def testMethods(self):
        self.assertArgIsBOOL(NSPersistentStoreDescription.setReadOnly_, 0)
        self.assertResultIsBOOL(NSPersistentStoreDescription.isReadOnly)

        self.assertArgIsBOOL(NSPersistentStoreDescription.setShouldAddStoreAsynchronously_, 0)
        self.assertResultIsBOOL(NSPersistentStoreDescription.shouldAddStoreAsynchronously)

        self.assertArgIsBOOL(NSPersistentStoreDescription.setShouldMigrateStoreAutomatically_, 0)
        self.assertResultIsBOOL(NSPersistentStoreDescription.shouldMigrateStoreAutomatically)

        self.assertArgIsBOOL(NSPersistentStoreDescription.setShouldInferMappingModelAutomatically_, 0)
        self.assertResultIsBOOL(NSPersistentStoreDescription.shouldInferMappingModelAutomatically)



if __name__ == "__main__":
    main()
