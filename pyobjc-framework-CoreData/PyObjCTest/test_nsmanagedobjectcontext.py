
from PyObjCTools.TestSupport import *
from CoreData import *

class TestNSManagedObjectContext (TestCase):
    @min_os_level("10.5")
    def testConstants10_5(self):
        self.failUnlessIsInstance(NSRefreshedObjectsKey, unicode)
        self.failUnlessIsInstance(NSInvalidatedObjectsKey, unicode)
        self.failUnlessIsInstance(NSInvalidatedAllObjectsKey, unicode)

    def testConstants(self):
        self.failUnlessIsInstance(NSManagedObjectContextDidSaveNotification, unicode)
        self.failUnlessIsInstance(NSManagedObjectContextObjectsDidChangeNotification, unicode)
        self.failUnlessIsInstance(NSInsertedObjectsKey, unicode)
        self.failUnlessIsInstance(NSUpdatedObjectsKey, unicode)
        self.failUnlessIsInstance(NSDeletedObjectsKey, unicode)


        self.failUnlessIsInstance(NSErrorMergePolicy, NSObject)
        self.failUnlessIsInstance(NSMergeByPropertyStoreTrumpMergePolicy, NSObject)
        self.failUnlessIsInstance(NSMergeByPropertyObjectTrumpMergePolicy, NSObject)
        self.failUnlessIsInstance(NSOverwriteMergePolicy, NSObject)
        self.failUnlessIsInstance(NSRollbackMergePolicy, NSObject)

    def testMethods(self):
        self.failUnlessResultIsBOOL(NSManagedObjectContext.hasChanges)
        self.failUnlessArgIsOut(NSManagedObjectContext.executeFetchRequest_error_, 1)
        self.failUnlessArgIsBOOL(NSManagedObjectContext.refreshObject_mergeChanges_, 1)
        self.failUnlessResultIsBOOL(NSManagedObjectContext.save_)
        self.failUnlessArgIsOut(NSManagedObjectContext.save_, 0)
        self.failUnlessResultIsBOOL(NSManagedObjectContext.tryLock)
        self.failUnlessResultIsBOOL(NSManagedObjectContext.propagatesDeletesAtEndOfEvent)
        self.failUnlessArgIsBOOL(NSManagedObjectContext.setPropagatesDeletesAtEndOfEvent_, 0)
        self.failUnlessResultIsBOOL(NSManagedObjectContext.retainsRegisteredObjects)
        self.failUnlessArgIsBOOL(NSManagedObjectContext.setRetainsRegisteredObjects_, 0)


    @min_os_level('10.5')
    def testMethods10_5(self):
        self.failUnlessArgIsOut(NSManagedObjectContext.countForFetchRequest_error_, 1)
        self.failUnlessResultIsBOOL(NSManagedObjectContext.obtainPermanentIDsForObjects_error_)
        self.failUnlessArgIsOut(NSManagedObjectContext.obtainPermanentIDsForObjects_error_, 1)



if __name__ == "__main__":
    main()
