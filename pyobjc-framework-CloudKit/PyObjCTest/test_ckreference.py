from PyObjCTools.TestSupport import TestCase, min_os_level
import CloudKit
import objc


class TestCKReference(TestCase):
    def test_enums(self):
        self.assertIsEnumType(CloudKit.CKReferenceAction)
        self.assertEqual(CloudKit.CKReferenceActionNone, 0)
        self.assertEqual(CloudKit.CKReferenceActionDeleteSelf, 1)

    @min_os_level("10.10")
    def test_classes(self):
        self.assertHasAttr(CloudKit, "CKReference")
        self.assertIsInstance(CloudKit.CKReference, objc.objc_class)
