import sys

if sys.maxsize > 2 ** 32:
    from PyObjCTools.TestSupport import *
    import CloudKit

    class TestCKOperationGroup (TestCase):
        def testConstants(self):
            self.assertEqual(CloudKit.CKOperationGroupTransferSizeUnknown, 0)
            self.assertEqual(CloudKit.CKOperationGroupTransferSizeKilobytes, 1)
            self.assertEqual(CloudKit.CKOperationGroupTransferSizeMegabytes, 2)
            self.assertEqual(CloudKit.CKOperationGroupTransferSizeTensOfMegabytes, 3)
            self.assertEqual(CloudKit.CKOperationGroupTransferSizeHundredsOfMegabytes, 4)
            self.assertEqual(CloudKit.CKOperationGroupTransferSizeGigabytes, 5)
            self.assertEqual(CloudKit.CKOperationGroupTransferSizeTensOfGigabytes, 6)
            self.assertEqual(CloudKit.CKOperationGroupTransferSizeHundredsOfGigabytes, 7)

if __name__ == "__main__":
    main()
