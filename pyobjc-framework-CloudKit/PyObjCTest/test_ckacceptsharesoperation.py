import sys

if sys.maxsize > 2 ** 32:
    from PyObjCTools.TestSupport import *
    import CloudKit

    class TestCKAcceptSharesOperation (TestCase):
        @min_os_level("10.12")
        def testMethods10_12(self):
            self.assertArgIsBlock(CloudKit.CKAcceptSharesOperation.setPerShareCompletionBlock_, 0, b"v@@@")
            self.assertResultIsBlock(CloudKit.CKAcceptSharesOperation.perShareCompletionBlock, b"v@@@")

            self.assertArgIsBlock(CloudKit.CKAcceptSharesOperation.setAcceptSharesCompletionBlock_, 0, b"v@")
            self.assertResultIsBlock(CloudKit.CKAcceptSharesOperation.acceptSharesCompletionBlock, b"v@")

if __name__ == "__main__":
    main()
