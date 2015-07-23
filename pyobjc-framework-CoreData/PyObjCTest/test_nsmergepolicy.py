from PyObjCTools.TestSupport import *
from CoreData import *

class TestNSMergePolicy (TestCase):
    def testConstants(self):
        self.assertIsInstance(NSErrorMergePolicy, objc.objc_object)
        self.assertIsInstance(NSMergeByPropertyStoreTrumpMergePolicy, objc.objc_object)
        self.assertIsInstance(NSMergeByPropertyObjectTrumpMergePolicy, objc.objc_object)
        self.assertIsInstance(NSOverwriteMergePolicy, objc.objc_object)
        self.assertIsInstance(NSRollbackMergePolicy, objc.objc_object)

        self.assertEqual(NSErrorMergePolicyType, 0x00)
        self.assertEqual(NSMergeByPropertyStoreTrumpMergePolicyType, 0x01)
        self.assertEqual(NSMergeByPropertyObjectTrumpMergePolicyType, 0x02)
        self.assertEqual(NSOverwriteMergePolicyType, 0x03)
        self.assertEqual(NSRollbackMergePolicyType, 0x04)

    @min_os_level('10.7')
    def testMethods10_7(self):
        self.assertArgIsOut(NSMergePolicy.resolveConflicts_error_, 1)
        self.assertResultIsBOOL(NSMergePolicy.resolveConflicts_error_)

    @min_os_level('10.11')
    def testMethods10_11(self):
        self.assertArgIsOut(NSMergePolicy.resolveOptimisticLockingVersionConflicts_error_, 1)
        self.assertResultIsBOOL(NSMergePolicy.resolveOptimisticLockingVersionConflicts_error_)

        self.assertArgIsOut(NSMergePolicy.resolveConstraintConflicts_error_, 1)
        self.assertResultIsBOOL(NSMergePolicy.resolveConstraintConflicts_error_)

if __name__ == "__main__":
    main()
