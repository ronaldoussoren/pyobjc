from PyObjCTools.TestSupport import TestCase, min_os_level
import CloudKit


class TestCKFetchShareParticipantsOperation(TestCase):
    @min_os_level("12.0")
    def testMethods12_0(self):
        self.assertResultIsBlock(
            CloudKit.CKAcceptSharesOperation.perShareParticipantCompletionBlock, b"v@@@"
        )
        self.assertArgIsBlock(
            CloudKit.CKAcceptSharesOperation.setPerShareParticipantCompletionBlock_,
            0,
            b"v@@@",
        )

        self.assertResultIsBlock(
            CloudKit.CKAcceptSharesOperation.fetchShareParticipantsCompletionBlock,
            b"v@",
        )
        self.assertArgIsBlock(
            CloudKit.CKAcceptSharesOperation.setFetchShareParticipantsCompletionBlock_,
            0,
            b"v@",
        )
