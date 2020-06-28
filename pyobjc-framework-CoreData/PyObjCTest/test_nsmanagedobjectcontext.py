import CoreData
from PyObjCTools.TestSupport import TestCase, min_os_level


class TestNSManagedObjectContext(TestCase):
    @min_os_level("10.12.4")
    def testConstants10_12_4(self):
        self.assertIsInstance(
            CoreData.NSManagedObjectContextDidSaveObjectIDsNotification, str
        )
        self.assertIsInstance(
            CoreData.NSManagedObjectContextDidMergeChangesObjectIDsNotification, str
        )
        self.assertIsInstance(CoreData.NSInsertedObjectIDsKey, str)
        self.assertIsInstance(CoreData.NSUpdatedObjectIDsKey, str)
        self.assertIsInstance(CoreData.NSDeletedObjectIDsKey, str)

    @min_os_level("10.12")
    def testConstants10_12(self):
        self.assertIsInstance(CoreData.NSManagedObjectContextQueryGenerationKey, str)

    @min_os_level("10.5")
    def testConstants10_5(self):
        self.assertIsInstance(CoreData.NSRefreshedObjectsKey, str)
        self.assertIsInstance(CoreData.NSInvalidatedObjectsKey, str)
        self.assertIsInstance(CoreData.NSInvalidatedAllObjectsKey, str)
        self.assertIsInstance(CoreData.NSManagedObjectContextWillSaveNotification, str)

    def testConstants(self):
        self.assertIsInstance(CoreData.NSManagedObjectContextDidSaveNotification, str)
        self.assertIsInstance(
            CoreData.NSManagedObjectContextObjectsDidChangeNotification, str
        )
        self.assertIsInstance(CoreData.NSInsertedObjectsKey, str)
        self.assertIsInstance(CoreData.NSUpdatedObjectsKey, str)
        self.assertIsInstance(CoreData.NSDeletedObjectsKey, str)

        self.assertIsInstance(CoreData.NSErrorMergePolicy, CoreData.NSObject)
        self.assertIsInstance(
            CoreData.NSMergeByPropertyStoreTrumpMergePolicy, CoreData.NSObject
        )
        self.assertIsInstance(
            CoreData.NSMergeByPropertyObjectTrumpMergePolicy, CoreData.NSObject
        )
        self.assertIsInstance(CoreData.NSOverwriteMergePolicy, CoreData.NSObject)
        self.assertIsInstance(CoreData.NSRollbackMergePolicy, CoreData.NSObject)

        self.assertEqual(CoreData.NSConfinementConcurrencyType, 0)
        self.assertEqual(CoreData.NSPrivateQueueConcurrencyType, 1)
        self.assertEqual(CoreData.NSMainQueueConcurrencyType, 2)

    def testMethods(self):
        self.assertResultIsBOOL(CoreData.NSManagedObjectContext.hasChanges)
        self.assertArgIsOut(
            CoreData.NSManagedObjectContext.executeFetchRequest_error_, 1
        )
        self.assertArgIsBOOL(
            CoreData.NSManagedObjectContext.refreshObject_mergeChanges_, 1
        )
        self.assertResultIsBOOL(CoreData.NSManagedObjectContext.save_)
        self.assertArgIsOut(CoreData.NSManagedObjectContext.save_, 0)
        self.assertResultIsBOOL(CoreData.NSManagedObjectContext.tryLock)
        self.assertResultIsBOOL(
            CoreData.NSManagedObjectContext.propagatesDeletesAtEndOfEvent
        )
        self.assertArgIsBOOL(
            CoreData.NSManagedObjectContext.setPropagatesDeletesAtEndOfEvent_, 0
        )
        self.assertResultIsBOOL(
            CoreData.NSManagedObjectContext.retainsRegisteredObjects
        )
        self.assertArgIsBOOL(
            CoreData.NSManagedObjectContext.setRetainsRegisteredObjects_, 0
        )

    @min_os_level("10.5")
    def testMethods10_5(self):
        self.assertArgIsOut(
            CoreData.NSManagedObjectContext.countForFetchRequest_error_, 1
        )
        self.assertResultIsBOOL(
            CoreData.NSManagedObjectContext.obtainPermanentIDsForObjects_error_
        )
        self.assertArgIsOut(
            CoreData.NSManagedObjectContext.obtainPermanentIDsForObjects_error_, 1
        )

    @min_os_level("10.6")
    def testMethods10_6(self):
        self.assertArgIsOut(
            CoreData.NSManagedObjectContext.existingObjectWithID_error_, 1
        )

    @min_os_level("10.7")
    def testMethods10_7(self):
        self.assertArgIsBlock(CoreData.NSManagedObjectContext.performBlock_, 0, b"v")
        self.assertArgIsBlock(
            CoreData.NSManagedObjectContext.performBlockAndWait_, 0, b"v"
        )

    @min_os_level("10.10")
    def testMethods10_10(self):
        self.assertArgIsOut(CoreData.NSManagedObjectContext.executeRequest_error_, 1)

    @min_os_level("10.11")
    def testMethods10_11(self):
        self.assertResultIsBOOL(
            CoreData.NSManagedObjectContext.shouldDeleteInaccessibleFaults
        )
        self.assertArgIsBOOL(
            CoreData.NSManagedObjectContext.setShouldDeleteInaccessibleFaults_, 0
        )

        self.assertResultIsBOOL(
            CoreData.NSManagedObjectContext.shouldHandleInaccessibleFault_forObjectID_triggeredByProperty_
        )

    @min_os_level("10.12")
    def testMethods10_12(self):
        self.assertResultIsBOOL(
            CoreData.NSManagedObjectContext.setQueryGenerationFromToken_error_
        )
        self.assertArgIsOut(
            CoreData.NSManagedObjectContext.setQueryGenerationFromToken_error_, 1
        )
        self.assertResultIsBOOL(
            CoreData.NSManagedObjectContext.automaticallyMergesChangesFromParent
        )
        self.assertArgIsBOOL(
            CoreData.NSManagedObjectContext.setAutomaticallyMergesChangesFromParent_, 0
        )
