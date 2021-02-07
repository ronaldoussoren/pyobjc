import CoreData
from PyObjCTools.TestSupport import TestCase, min_os_level
import objc


class TestNSMergePolicy(TestCase):
    def testConstants(self):
        self.assertIsInstance(CoreData.NSErrorMergePolicy, objc.objc_object)
        self.assertIsInstance(
            CoreData.NSMergeByPropertyStoreTrumpMergePolicy, objc.objc_object
        )
        self.assertIsInstance(
            CoreData.NSMergeByPropertyObjectTrumpMergePolicy, objc.objc_object
        )
        self.assertIsInstance(CoreData.NSOverwriteMergePolicy, objc.objc_object)
        self.assertIsInstance(CoreData.NSRollbackMergePolicy, objc.objc_object)

        self.assertEqual(CoreData.NSErrorMergePolicyType, 0x00)
        self.assertEqual(CoreData.NSMergeByPropertyStoreTrumpMergePolicyType, 0x01)
        self.assertEqual(CoreData.NSMergeByPropertyObjectTrumpMergePolicyType, 0x02)
        self.assertEqual(CoreData.NSOverwriteMergePolicyType, 0x03)
        self.assertEqual(CoreData.NSRollbackMergePolicyType, 0x04)

    @min_os_level("10.7")
    def testMethods10_7(self):
        self.assertArgIsOut(CoreData.NSMergePolicy.resolveConflicts_error_, 1)
        self.assertResultIsBOOL(CoreData.NSMergePolicy.resolveConflicts_error_)

    @min_os_level("10.11")
    def testMethods10_11(self):
        self.assertArgIsOut(
            CoreData.NSMergePolicy.resolveOptimisticLockingVersionConflicts_error_, 1
        )
        self.assertResultIsBOOL(
            CoreData.NSMergePolicy.resolveOptimisticLockingVersionConflicts_error_
        )

        self.assertArgIsOut(CoreData.NSMergePolicy.resolveConstraintConflicts_error_, 1)
        self.assertResultIsBOOL(
            CoreData.NSMergePolicy.resolveConstraintConflicts_error_
        )
