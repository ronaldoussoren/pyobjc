import sys
from PyObjCTools.TestSupport import *

if sys.maxsize > 2 ** 32:
    import Intents

    class TestINSearchForMessagesIntentResponse (TestCase):
        @min_os_level('10.12')
        def testConstants(self):
            self.assertEqual(Intent.INSearchForMessagesIntentResponseCodeUnspecified, 0)
            self.assertEqual(Intent.INSearchForMessagesIntentResponseCodeReady, 1)
            self.assertEqual(Intent.INSearchForMessagesIntentResponseCodeInProgress, 2)
            self.assertEqual(Intent.INSearchForMessagesIntentResponseCodeSuccess, 3)
            self.assertEqual(Intent.INSearchForMessagesIntentResponseCodeFailure, 4)
            self.assertEqual(Intent.INSearchForMessagesIntentResponseCodeFailureRequiringAppLaunch, 5)
            self.assertEqual(Intent.INSearchForMessagesIntentResponseCodeFailureMessageServiceNotAvailable, 6)


if __name__ == "__main__":
    main()
