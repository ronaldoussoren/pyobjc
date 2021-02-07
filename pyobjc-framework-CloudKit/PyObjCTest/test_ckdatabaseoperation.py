from PyObjCTools.TestSupport import TestCase, min_os_level
import CloudKit
import objc


class TestCKDatabaseOperation(TestCase):
    @min_os_level("10.10")
    def testClasses(self):
        self.assertHasAttr(CloudKit, "CKDatabaseOperation")
        self.assertIsInstance(CloudKit.CKDatabaseOperation, objc.objc_class)
