from PyObjCTools.TestSupport import TestCase, min_os_level
import CloudKit
import objc


class TestCKReference(TestCase):
    def test_enum_types(self):
        self.assertIsEnumType(CloudKit.CKReferenceAction)

    @min_os_level("10.10")
    def testClasses(self):
        self.assertHasAttr(CloudKit, "CKReference")
        self.assertIsInstance(CloudKit.CKReference, objc.objc_class)

    @min_os_level("10.10")
    def testConstants(self):
        self.assertEqual(CloudKit.CKReferenceActionNone, 0)
        self.assertEqual(CloudKit.CKReferenceActionDeleteSelf, 1)
