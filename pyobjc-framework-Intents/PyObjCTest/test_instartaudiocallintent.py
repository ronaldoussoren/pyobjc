from PyObjCTools.TestSupport import TestCase, min_sdk_level
import Intents


class TestINStartAudioCallIntentHelper(Intents.NSObject):
    def handleStartAudioCall_completion_(self, intent, completion):
        pass

    def confirmStartAudioCall_completion_(self, intent, completion):
        pass

    def resolveContactsForStartAudioCall_withCompletion_(self, intent, completion):
        pass

    def resolveDestinationTypeForStartAudioCall_withCompletion_(
        self, intent, completion
    ):
        pass


class TestINStartAudioCallIntent(TestCase):
    @min_sdk_level("10.12")
    def test_protocols(self):
        self.assertProtocolExists("INStartAudioCallIntentHandling", Intents)

    def test_protocol_methods(self):
        self.assertArgIsBlock(
            TestINStartAudioCallIntentHelper.handleStartAudioCall_completion_, 1, b"v@"
        )
        self.assertArgIsBlock(
            TestINStartAudioCallIntentHelper.confirmStartAudioCall_completion_, 1, b"v@"
        )
        self.assertArgIsBlock(
            TestINStartAudioCallIntentHelper.resolveContactsForStartAudioCall_withCompletion_,
            1,
            b"v@",
        )
        self.assertArgIsBlock(
            TestINStartAudioCallIntentHelper.resolveDestinationTypeForStartAudioCall_withCompletion_,
            1,
            b"v@",
        )
