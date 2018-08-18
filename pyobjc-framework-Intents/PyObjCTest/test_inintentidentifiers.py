import sys
from PyObjCTools.TestSupport import *

if sys.maxsize > 2 ** 32:
    import Intents

    class TestINIntentIdentifiers (TestCase):
        @min_os_level('10.12')
        @expectedFailureIf(os_level_key(os_release()) < os_level_key('10.14')) # Documented to be available for 10.12, but not available
        def testConstants(self):
            self.assertIsInstance(Intents.INStartAudioCallIntentIdentifier, unicode)
            self.assertIsInstance(Intents.INStartVideoCallIntentIdentifier, unicode)
            self.assertIsInstance(Intents.INSearchCallHistoryIntentIdentifier, unicode)
            self.assertIsInstance(Intents.INSendMessageIntentIdentifier, unicode)
            self.assertIsInstance(Intents.INSearchForMessagesIntentIdentifier, unicode)
            self.assertIsInstance(Intents.INSetMessageAttributeIntentIdentifier, unicode)

if __name__ == "__main__":
    main()
