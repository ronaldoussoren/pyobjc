from PyObjCTools.TestSupport import TestCase

import FSKit


class TestFSMessageConnectionHelper(FSKit.NSObject):
    def prompt_replyHandler_(self, a, b):
        pass

    def promptTrueFalse_replyHandler_(self, a, b):
        pass

    def completed_replyHandler_(self, a, b):
        pass


class TestFSMessageConnection(TestCase):
    def test_protocols(self):
        self.assertProtocolExists("FSTaskMessageOperations")

    def test_protocol_methods(self):
        self.assertArgIsBlock(
            TestFSMessageConnectionHelper.prompt_replyHandler_, 1, b"v@@"
        )
        self.assertArgIsBlock(
            TestFSMessageConnectionHelper.promptTrueFalse_replyHandler_, 1, b"vZ@"
        )
        self.assertArgIsBlock(
            TestFSMessageConnectionHelper.completed_replyHandler_, 1, b"vi@"
        )

    def test_methods(self):
        self.assertArgIsBlock(FSKit.FSMessageConnection.connect_, 0, b"v@")

        self.assertArgIsPrintf(
            FSKit.FSMessageConnection.logLocalizedMessage_table_bundle_, 0
        )
        self.assertArgIsPrintf(
            FSKit.FSMessageConnection.localizedMessage_table_bundle_, 0
        )
