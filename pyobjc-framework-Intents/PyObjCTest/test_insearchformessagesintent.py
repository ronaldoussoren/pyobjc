from PyObjCTools.TestSupport import TestCase, min_os_level, min_sdk_level
import Intents


class TestINSearchForMessagesIntentHelper(Intents.NSObject):
    def handleSearchForMessages_completion_(self, intent, completion):
        pass

    def confirmSearchForMessages_completion_(self, intent, completion):
        pass

    def resolveRecipientsForSearchForMessages_withCompletion_(self, intent, completion):
        pass

    def resolveSendersForSearchForMessages_withCompletion_(self, intent, completion):
        pass

    def resolveSearchTermsForSearchForMessages_withCompletion_(
        self, intent, completion
    ):
        pass

    def resolveAttributesForSearchForMessages_withCompletion_(self, intent, completion):
        pass

    def resolveDateTimeRangeForSearchForMessages_withCompletion_(
        self, intent, completion
    ):
        pass

    def resolveIdentifiersForSearchForMessages_withCompletion_(
        self, intent, completion
    ):
        pass

    def resolveNotificationIdentifiersForSearchForMessages_withCompletion_(
        self, intent, completion
    ):
        pass

    def resolveGroupNamesForSearchForMessages_withCompletion_(self, intent, completion):
        pass

    def resolveSpeakableGroupNamesForSearchForMessages_withCompletion_(
        self, intent, completion
    ):
        pass


class TestINSearchForMessagesIntent(TestCase):
    @min_os_level("10.12")
    def testMethods(self):
        self.assertArgIsBlock(
            TestINSearchForMessagesIntentHelper.handleSearchForMessages_completion_,
            1,
            b"v@",
        )
        self.assertArgIsBlock(
            TestINSearchForMessagesIntentHelper.confirmSearchForMessages_completion_,
            1,
            b"v@",
        )

        self.assertArgIsBlock(
            TestINSearchForMessagesIntentHelper.resolveRecipientsForSearchForMessages_withCompletion_,
            1,
            b"v@",
        )
        self.assertArgIsBlock(
            TestINSearchForMessagesIntentHelper.resolveSendersForSearchForMessages_withCompletion_,
            1,
            b"v@",
        )
        # self.assertArgIsBlock(TestINSearchForMessagesIntentHelper.resolveSearchTermsForSearchForMessages_withCompletion_, 1, b'v@')  # noqa: B950
        self.assertArgIsBlock(
            TestINSearchForMessagesIntentHelper.resolveAttributesForSearchForMessages_withCompletion_,
            1,
            b"v@",
        )
        self.assertArgIsBlock(
            TestINSearchForMessagesIntentHelper.resolveDateTimeRangeForSearchForMessages_withCompletion_,
            1,
            b"v@",
        )
        # self.assertArgIsBlock(TestINSearchForMessagesIntentHelper.resolveIdentifiersForSearchForMessages_withCompletion_, 1, b'v@')  # noqa: B950
        # self.assertArgIsBlock(TestINSearchForMessagesIntentHelper.resolveNotificationIdentifiersForSearchForMessages_withCompletion_, 1, b'v@')  # noqa: B950
        self.assertArgIsBlock(
            TestINSearchForMessagesIntentHelper.resolveGroupNamesForSearchForMessages_withCompletion_,
            1,
            b"v@",
        )
        self.assertArgIsBlock(
            TestINSearchForMessagesIntentHelper.resolveSpeakableGroupNamesForSearchForMessages_withCompletion_,
            1,
            b"v@",
        )

    @min_sdk_level("10.12")
    def testProtocols(self):
        self.assertProtocolExists("INSearchForMessagesIntentHandling")
