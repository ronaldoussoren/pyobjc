from PyObjCTools.TestSupport import TestCase, min_os_level
import CloudKit


class TestCKFetchShareParticipantsOperation(TestCase):
    @min_os_level("10.12")
    def testMethods10_12(self):
        self.assertArgIsBlock(
            CloudKit.CKFetchShareParticipantsOperation.setShareParticipantFetchedBlock_,
            0,
            b"v@",
        )
        self.assertResultIsBlock(
            CloudKit.CKFetchShareParticipantsOperation.shareParticipantFetchedBlock,
            b"v@",
        )

        self.assertArgIsBlock(
            CloudKit.CKFetchShareParticipantsOperation.setFetchShareParticipantsCompletionBlock_,  # noqa: B950
            0,
            b"v@",
        )
        self.assertResultIsBlock(
            CloudKit.CKFetchShareParticipantsOperation.fetchShareParticipantsCompletionBlock,  # noqa: B950
            b"v@",
        )
