import sys

if sys.maxsize > 2 ** 32:
    from PyObjCTools.TestSupport import *
    import CloudKit

    class TestCKFetchShareParticipantsOperation (TestCase):
        @min_os_level("10.12")
        def testMethods10_12(self):
            self.assertArgIsBlock(CloudKit.CKFetchShareParticipantsOperation.setShareParticipantFetchedBlock_, 0, b"v@")
            self.assertResultIsBlock(CloudKit.CKFetchShareParticipantsOperation.shareParticipantFetchedBlock, b"v@")

            self.assertArgIsBlock(CloudKit.CKFetchShareParticipantsOperation.setFetchShareParticipantsCompletionBlock_, 0, b"v@")
            self.assertResultIsBlock(CloudKit.CKFetchShareParticipantsOperation.fetchShareParticipantsCompletionBlock, b"v@")

if __name__ == "__main__":
    main()
