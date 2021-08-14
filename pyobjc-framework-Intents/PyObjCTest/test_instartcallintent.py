from PyObjCTools.TestSupport import TestCase, min_sdk_level
import Intents
import objc


class TestINStartCallIntentHelper(Intents.NSObject):
    def handleStartCall_completion_(self, a, b):
        pass

    def confirmStartCall_completion_(self, a, b):
        pass

    def resolveCallRecordToCallBackForStartCall_withCompletion_(self, a, b):
        pass

    def resolveDestinationTypeForStartCall_withCompletion_(self, a, b):
        pass

    def resolveContactsForStartCall_withCompletion_(self, a, b):
        pass

    def resolveCallCapabilityForStartCall_withCompletion_(self, a, b):
        pass


class TestINStartCallIntent(TestCase):
    @min_sdk_level("12.0")
    def test_protocols12_0(self):
        objc.protocolNamed("INStartCallIntentHandling")

    def test_methods(self):
        self.assertArgIsBlock(
            TestINStartCallIntentHelper.handleStartCall_completion_, 1, b"v@"
        )
        self.assertArgIsBlock(
            TestINStartCallIntentHelper.confirmStartCall_completion_, 1, b"v@"
        )
        self.assertArgIsBlock(
            TestINStartCallIntentHelper.resolveCallRecordToCallBackForStartCall_withCompletion_,
            1,
            b"v@",
        )
        self.assertArgIsBlock(
            TestINStartCallIntentHelper.resolveDestinationTypeForStartCall_withCompletion_,
            1,
            b"v@",
        )
        self.assertArgIsBlock(
            TestINStartCallIntentHelper.resolveContactsForStartCall_withCompletion_,
            1,
            b"v@",
        )
        self.assertArgIsBlock(
            TestINStartCallIntentHelper.resolveCallCapabilityForStartCall_withCompletion_,
            1,
            b"v@",
        )
