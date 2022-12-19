from PyObjCTools.TestSupport import TestCase, min_sdk_level
import Intents


class TestINAnswerCallIntentHelper(Intents.NSObject):
    def handleAnswerCall_completion_(self, a, b):
        pass

    def confirmAnswerCall_completion_(self, a, b):
        pass


class TestINAnswerCallIntent(TestCase):
    @min_sdk_level("13.1")
    def test_protocols(self):
        self.assertProtocolExists("INAnswerCallIntentHandling")

    def test_protocol_methods(self):
        self.assertArgIsBlock(
            TestINAnswerCallIntentHelper.handleAnswerCall_completion_, 1, b"v@"
        )
        self.assertArgIsBlock(
            TestINAnswerCallIntentHelper.confirmAnswerCall_completion_, 1, b"v@"
        )
