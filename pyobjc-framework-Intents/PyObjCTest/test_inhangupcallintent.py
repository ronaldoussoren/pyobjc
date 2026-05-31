from PyObjCTools.TestSupport import TestCase, min_sdk_level
import Intents


class TestINHangUpCallIntentHelper(Intents.NSObject):
    def handleHangUpCall_completion_(self, a, b):
        pass

    def confirmHangUpCall_completion_(self, a, b):
        pass


class TestINHangUpCallIntent(TestCase):
    @min_sdk_level("13.1")
    def test_protocols(self):
        self.assertProtocolExists("INHangUpCallIntentHandling")

    def test_protocol_methods(self):
        self.assertArgIsBlock(
            TestINHangUpCallIntentHelper.handleHangUpCall_completion_, 1, b"v@"
        )
        self.assertArgIsBlock(
            TestINHangUpCallIntentHelper.confirmHangUpCall_completion_, 1, b"v@"
        )
