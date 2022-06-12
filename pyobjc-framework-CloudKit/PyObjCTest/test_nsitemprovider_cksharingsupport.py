from PyObjCTools.TestSupport import TestCase, min_os_level
import CloudKit

CKSharePreparationCompletionHandler = b"v@@"
CKSharePreparationHandler = b"v@@?"  # XXX: Block has type ^^^


class TestNSItemProvider_CKSharingSupport(TestCase):
    @min_os_level("13.0")
    def testMethods13_0(self):
        self.assertArgIsBlock(
            CloudKit.NSItemProvider.registerCKShareWithContainer_allowedSharingOptions_preparationHandler_,
            2,
            CKSharePreparationHandler,
        )

    def test_constants(self):
        self.assertIsEnumType(CloudKit.CKSharingOptions)
        self.assertEqual(CloudKit.CKSharingOptionsStandard, 0)
        self.assertEqual(CloudKit.CKSharingOptionsAllowPublic, 1 << 0)
        self.assertEqual(CloudKit.CKSharingOptionsAllowPrivate, 1 << 1)
        self.assertEqual(CloudKit.CKSharingOptionsAllowReadOnly, 1 << 4)
        self.assertEqual(CloudKit.CKSharingOptionsAllowReadWrite, 1 << 5)
