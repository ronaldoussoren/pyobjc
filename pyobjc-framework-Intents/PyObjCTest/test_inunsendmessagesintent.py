from PyObjCTools.TestSupport import TestCase, min_sdk_level
import Intents


class TestINUnsendMessagesIntentHelper(Intents.NSObject):
    def handleUnsendMessages_completion_(self, a, b):
        pass

    def confirmUnsendMessages_completion_(self, a, b):
        pass


class TestINUnsendMessagesIntent(TestCase):
    @min_sdk_level("14.0")
    def test_protocols(self):
        self.assertProtocolExists("INUnsendMessagesIntentHandling")

    def test_protocol_methods(self):
        self.assertArgIsBlock(
            TestINUnsendMessagesIntentHelper.handleUnsendMessages_completion_, 1, b"v@"
        )
        self.assertArgIsBlock(
            TestINUnsendMessagesIntentHelper.confirmUnsendMessages_completion_, 1, b"v@"
        )
