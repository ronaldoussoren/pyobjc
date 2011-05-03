
from PyObjCTools.TestSupport import *
from CoreData import *

class TestNSManagedObjectContext (TestCase):
    @min_os_level("10.5")
    def testConstants10_5(self):
        self.assertIsInstance(NSRefreshedObjectsKey, unicode)
        self.assertIsInstance(NSInvalidatedObjectsKey, unicode)
        self.assertIsInstance(NSInvalidatedAllObjectsKey, unicode)
        self.assertIsInstance(NSManagedObjectContextWillSaveNotification, unicode)

    def testConstants(self):
        self.assertIsInstance(NSManagedObjectContextDidSaveNotification, unicode)
        self.assertIsInstance(NSManagedObjectContextObjectsDidChangeNotification, unicode)
        self.assertIsInstance(NSInsertedObjectsKey, unicode)
        self.assertIsInstance(NSUpdatedObjectsKey, unicode)
        self.assertIsInstance(NSDeletedObjectsKey, unicode)


        self.assertIsInstance(NSErrorMergePolicy, NSObject)
        self.assertIsInstance(NSMergeByPropertyStoreTrumpMergePolicy, NSObject)
        self.assertIsInstance(NSMergeByPropertyObjectTrumpMergePolicy, NSObject)
        self.assertIsInstance(NSOverwriteMergePolicy, NSObject)
        self.assertIsInstance(NSRollbackMergePolicy, NSObject)

    def testMethods(self):
        self.assertResultIsBOOL(NSManagedObjectContext.hasChanges)
        self.assertArgIsOut(NSManagedObjectContext.executeFetchRequest_error_, 1)
        self.assertArgIsBOOL(NSManagedObjectContext.refreshObject_mergeChanges_, 1)
        self.assertResultIsBOOL(NSManagedObjectContext.save_)
        self.assertArgIsOut(NSManagedObjectContext.save_, 0)
        self.assertResultIsBOOL(NSManagedObjectContext.tryLock)
        self.assertResultIsBOOL(NSManagedObjectContext.propagatesDeletesAtEndOfEvent)
        self.assertArgIsBOOL(NSManagedObjectContext.setPropagatesDeletesAtEndOfEvent_, 0)
        self.assertResultIsBOOL(NSManagedObjectContext.retainsRegisteredObjects)
        self.assertArgIsBOOL(NSManagedObjectContext.setRetainsRegisteredObjects_, 0)


    @min_os_level('10.5')
    def testMethods10_5(self):
        self.assertArgIsOut(NSManagedObjectContext.countForFetchRequest_error_, 1)
        self.assertResultIsBOOL(NSManagedObjectContext.obtainPermanentIDsForObjects_error_)
        self.assertArgIsOut(NSManagedObjectContext.obtainPermanentIDsForObjects_error_, 1)

    @min_os_level('10.6')
    def testMethods10_6(self):
        self.assertArgIsOut(NSManagedObjectContext.existingObjectWithID_error_, 1)



if __name__ == "__main__":
    main()
