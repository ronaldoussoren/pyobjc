import sys
from PyObjCTools.TestSupport import *

if sys.maxsize > 2 ** 32:
    import Intents

    class TestINSearchForMessagesIntentResponse (TestCase):
        @min_os_level('10.12')
        def testConstants(self):
            self.assertEqual(Intents.INSearchForMessagesIntentResponseCodeUnspecified, 0)
            self.assertEqual(Intents.INSearchForMessagesIntentResponseCodeReady, 1)
            self.assertEqual(Intents.INSearchForMessagesIntentResponseCodeInProgress, 2)
            self.assertEqual(Intents.INSearchForMessagesIntentResponseCodeSuccess, 3)
            self.assertEqual(Intents.INSearchForMessagesIntentResponseCodeFailure, 4)
            self.assertEqual(Intents.INSearchForMessagesIntentResponseCodeFailureRequiringAppLaunch, 5)
            self.assertEqual(Intents.INSearchForMessagesIntentResponseCodeFailureMessageServiceNotAvailable, 6)
            self.assertEqual(Intents.INSearchForMessagesIntentResponseCodeFailureMessageTooManyResults, 7)


if __name__ == "__main__":
    main()
