import sys
from PyObjCTools.TestSupport import *

if sys.maxsize > 2 ** 32:
    import Intents

    class TestINSendMessageRecipientResolutionResult (TestCase):
        def testConstants(self):
            self.assertEqual(Intents.INSendMessageRecipientUnsupportedReasonNoAccount, 1)
            self.assertEqual(Intents.INSendMessageRecipientUnsupportedReasonOffline, 2)
            self.assertEqual(Intents.INSendMessageRecipientUnsupportedReasonMessagingServiceNotEnabledForRecipient, 3)

            self.assertEqual(Intents.INSendMessageRecipientUnsupportedReasonNoValidHandle, 4)
            self.assertEqual(Intents.INSendMessageRecipientUnsupportedReasonRequestedHandleInvalid, 5)
            self.assertEqual(Intents.INSendMessageRecipientUnsupportedReasonNoHandleForLabel, 6)


if __name__ == "__main__":
    main()
