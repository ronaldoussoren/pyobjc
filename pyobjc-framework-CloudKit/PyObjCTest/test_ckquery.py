from PyObjCTools.TestSupport import TestCase, min_os_level
import CloudKit
import objc


class TestCKQuery(TestCase):
    @min_os_level("10.10")
    def testClasses(self):
        self.assertHasAttr(CloudKit, "CKQuery")
        self.assertIsInstance(CloudKit.CKQuery, objc.objc_class)
