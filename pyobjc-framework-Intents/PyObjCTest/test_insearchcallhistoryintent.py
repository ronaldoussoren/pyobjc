from PyObjCTools.TestSupport import TestCase, min_os_level, min_sdk_level
import Intents


class TestINSearchCallHistoryIntentHelper(Intents.NSObject):
    def handleSearchCallHistory_completion_(self, intent, completion):
        pass

    def confirmSearchCallHistory_completion_(self, intent, completion):
        pass

    def resolveCallTypeForSearchCallHistory_withCompletion_(self, intent, completion):
        pass

    def resolveRecipientForSearchCallHistory_withCompletion_(self, intent, completion):
        pass

    def resolveCallCapabilitiesForSearchCallHistory_withCompletion_(
        self, intent, completion
    ):
        pass

    def resolveCallTypesForSearchCallHistory_withCompletion_(self, intent, completion):
        pass

    def resolveUnseenForSearchCallHistory_withCompletion_(self, intent, completion):
        pass


class TestINSearchCallHistoryIntent(TestCase):
    @min_os_level("10.12")
    def testMethods(self):
        self.assertArgIsBlock(
            TestINSearchCallHistoryIntentHelper.handleSearchCallHistory_completion_,
            1,
            b"v@",
        )
        self.assertArgIsBlock(
            TestINSearchCallHistoryIntentHelper.confirmSearchCallHistory_completion_,
            1,
            b"v@",
        )
        self.assertArgIsBlock(
            TestINSearchCallHistoryIntentHelper.resolveCallTypeForSearchCallHistory_withCompletion_,
            1,
            b"v@",
        )
        self.assertArgIsBlock(
            TestINSearchCallHistoryIntentHelper.resolveRecipientForSearchCallHistory_withCompletion_,
            1,
            b"v@",
        )
        # Removed in Xcode 8.1
        # self.assertArgIsBlock(TestINSearchCallHistoryIntentHelper.resolveCallCapabilitiesForSearchCallHistory_withCompletion_, 1, b'v@')   # noqa: B950

    @min_os_level("10.13")
    def testMethods10_13(self):
        self.assertArgIsBlock(
            TestINSearchCallHistoryIntentHelper.resolveCallTypesForSearchCallHistory_withCompletion_,
            1,
            b"v@",
        )
        self.assertArgIsBlock(
            TestINSearchCallHistoryIntentHelper.resolveUnseenForSearchCallHistory_withCompletion_,
            1,
            b"v@",
        )

    @min_sdk_level("10.12")
    def testProtocols(self):
        self.assertProtocolExists("INSearchCallHistoryIntentHandling")
