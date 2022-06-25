from PyObjCTools.TestSupport import TestCase, min_sdk_level
import Intents


class TestINShareFocusStatusIntentHelper(Intents.NSObject):
    def handleShareFocusStatus_completion_(self, a, b):
        pass

    def confirmShareFocusStatus_completion_(self, a, b):
        pass


class TestINShareFocusStatusIntent(TestCase):
    @min_sdk_level("12.0")
    def test_protocols(self):
        self.assertProtocolExists("INShareFocusStatusIntentHandling")

    def test_methods(self):
        self.assertArgIsBlock(
            TestINShareFocusStatusIntentHelper.handleShareFocusStatus_completion_,
            1,
            b"v@",
        )
        self.assertArgIsBlock(
            TestINShareFocusStatusIntentHelper.confirmShareFocusStatus_completion_,
            1,
            b"v@",
        )
