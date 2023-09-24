from PyObjCTools.TestSupport import TestCase
import Intents


class TestINSendMessageRecipientResolutionResult(TestCase):
    def test_enum_types(self):
        self.assertIsEnumType(Intents.INSendMessageRecipientUnsupportedReason)

    def testConstants(self):
        self.assertEqual(Intents.INSendMessageRecipientUnsupportedReasonNoAccount, 1)
        self.assertEqual(Intents.INSendMessageRecipientUnsupportedReasonOffline, 2)
        self.assertEqual(
            Intents.INSendMessageRecipientUnsupportedReasonMessagingServiceNotEnabledForRecipient,
            3,
        )

        self.assertEqual(
            Intents.INSendMessageRecipientUnsupportedReasonNoValidHandle, 4
        )
        self.assertEqual(
            Intents.INSendMessageRecipientUnsupportedReasonRequestedHandleInvalid, 5
        )
        self.assertEqual(
            Intents.INSendMessageRecipientUnsupportedReasonNoHandleForLabel, 6
        )
        self.assertEqual(
            Intents.INSendMessageRecipientUnsupportedReasonRequiringInAppAuthentication,
            7,
        )
