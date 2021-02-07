from PyObjCTools.TestSupport import TestCase, min_os_level
import CloudKit
import objc


class TestCKAsset(TestCase):
    @min_os_level("10.10")
    def testClasses(self):
        self.assertHasAttr(CloudKit, "CKAsset")
        self.assertIsInstance(CloudKit.CKAsset, objc.objc_class)
