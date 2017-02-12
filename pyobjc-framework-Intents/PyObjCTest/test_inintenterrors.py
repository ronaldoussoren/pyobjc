import sys
from PyObjCTools.TestSupport import *

if sys.maxsize > 2 ** 32:
    import Intents

    class TestINIntentErrors (TestCase):
        @min_os_level('10.12')
        def testConstants(self):
            self.assertEqual(Intents.INIntentErrorInteractionOperationNotSupported, 1900)
            self.assertEqual(Intents.INIntentErrorDonatingInteraction, 1901)
            self.assertEqual(Intents.INIntentErrorDeletingAllInteractions, 1902)
            self.assertEqual(Intents.INIntentErrorDeletingInteractionWithIdentifiers, 1903)
            self.assertEqual(Intents.INIntentErrorDeletingInteractionWithGroupIdentifier, 1904)
            self.assertEqual(Intents.INIntentErrorIntentSupportedByMultipleExtension, 2001)
            self.assertEqual(Intents.INIntentErrorRestrictedIntentsNotSupportedByExtension, 2002)
            self.assertEqual(Intents.INIntentErrorNoHandlerProvidedForIntent, 2003)
            self.assertEqual(Intents.INIntentErrorInvalidIntentName, 2004)
            self.assertEqual(Intents.INIntentErrorRequestTimedOut, 3001)
            self.assertEqual(Intents.INIntentErrorInvalidUserVocabularyFileLocation, 4000)

            self.assertEqual(Intents.INIntentErrorExtensionLaunchingTimeout, 5000)
            self.assertEqual(Intents.INIntentErrorExtensionBringUpFailed, 5001)


if __name__ == "__main__":
    main()
