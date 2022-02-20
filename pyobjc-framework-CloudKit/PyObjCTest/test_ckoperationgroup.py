from PyObjCTools.TestSupport import TestCase
import CloudKit


class TestCKOperationGroup(TestCase):
    def test_enum_types(self):
        self.assertIsEnumType(CloudKit.CKOperationGroupTransferSize)

    def testConstants(self):
        self.assertEqual(CloudKit.CKOperationGroupTransferSizeUnknown, 0)
        self.assertEqual(CloudKit.CKOperationGroupTransferSizeKilobytes, 1)
        self.assertEqual(CloudKit.CKOperationGroupTransferSizeMegabytes, 2)
        self.assertEqual(CloudKit.CKOperationGroupTransferSizeTensOfMegabytes, 3)
        self.assertEqual(CloudKit.CKOperationGroupTransferSizeHundredsOfMegabytes, 4)
        self.assertEqual(CloudKit.CKOperationGroupTransferSizeGigabytes, 5)
        self.assertEqual(CloudKit.CKOperationGroupTransferSizeTensOfGigabytes, 6)
        self.assertEqual(CloudKit.CKOperationGroupTransferSizeHundredsOfGigabytes, 7)
