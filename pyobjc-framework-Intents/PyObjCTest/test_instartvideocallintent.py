from PyObjCTools.TestSupport import TestCase, min_sdk_level
import Intents


class TestINStartVideoCallIntentHelper(Intents.NSObject):
    def handleStartVideoCall_completion_(self, intent, completion):
        pass

    def confirmStartVideoCall_completion_(self, intent, completion):
        pass

    def resolveContactsForStartVideoCall_withCompletion_(self, intent, completion):
        pass


class TestINStartVideoCallIntent(TestCase):
    @min_sdk_level("10.12")
    def test_protocols(self):
        self.assertProtocolExists("INStartVideoCallIntentHandling", Intents)

    def test_protocol_methods(self):
        self.assertArgIsBlock(
            TestINStartVideoCallIntentHelper.handleStartVideoCall_completion_, 1, b"v@"
        )
        self.assertArgIsBlock(
            TestINStartVideoCallIntentHelper.confirmStartVideoCall_completion_, 1, b"v@"
        )
        self.assertArgIsBlock(
            TestINStartVideoCallIntentHelper.resolveContactsForStartVideoCall_withCompletion_,
            1,
            b"v@",
        )
