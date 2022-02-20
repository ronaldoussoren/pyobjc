from PyObjCTools.TestSupport import TestCase, min_os_level
import Intents


class TestINIntentErrors(TestCase):
    def test_enum_types(self):
        self.assertIsEnumType(Intents.INIntentErrorCode)

    def testConstants(self):
        self.assertEqual(Intents.INIntentErrorInteractionOperationNotSupported, 1900)
        self.assertEqual(Intents.INIntentErrorDonatingInteraction, 1901)
        self.assertEqual(Intents.INIntentErrorDeletingAllInteractions, 1902)
        self.assertEqual(Intents.INIntentErrorDeletingInteractionWithIdentifiers, 1903)
        self.assertEqual(
            Intents.INIntentErrorDeletingInteractionWithGroupIdentifier, 1904
        )
        self.assertEqual(Intents.INIntentErrorIntentSupportedByMultipleExtension, 2001)
        self.assertEqual(
            Intents.INIntentErrorRestrictedIntentsNotSupportedByExtension, 2002
        )
        self.assertEqual(Intents.INIntentErrorNoHandlerProvidedForIntent, 2003)
        self.assertEqual(Intents.INIntentErrorInvalidIntentName, 2004)
        self.assertEqual(Intents.INIntentErrorRequestTimedOut, 3001)
        self.assertEqual(Intents.INIntentErrorMissingInformation, 3002)
        self.assertEqual(Intents.INIntentErrorInvalidUserVocabularyFileLocation, 4000)

        self.assertEqual(Intents.INIntentErrorExtensionLaunchingTimeout, 5000)
        self.assertEqual(Intents.INIntentErrorExtensionBringUpFailed, 5001)

        self.assertEqual(Intents.INIntentErrorNoAppAvailable, 2005)
        self.assertEqual(Intents.INIntentErrorImageGeneric, 6000)
        self.assertEqual(Intents.INIntentErrorImageNoServiceAvailable, 6001)
        self.assertEqual(Intents.INIntentErrorImageStorageFailed, 6002)
        self.assertEqual(Intents.INIntentErrorImageLoadingFailed, 6003)
        self.assertEqual(Intents.INIntentErrorImageRetrievalFailed, 6004)
        self.assertEqual(Intents.INIntentErrorImageProxyLoop, 6005)
        self.assertEqual(Intents.INIntentErrorImageProxyInvalid, 6006)
        self.assertEqual(Intents.INIntentErrorImageProxyTimeout, 6007)
        self.assertEqual(Intents.INIntentErrorImageServiceFailure, 6008)
        self.assertEqual(Intents.INIntentErrorImageScalingFailed, 6009)
        self.assertEqual(Intents.INIntentErrorPermissionDenied, 6010)
        self.assertEqual(Intents.INIntentErrorVoiceShortcutCreationFailed, 7000)
        self.assertEqual(Intents.INIntentErrorVoiceShortcutGetFailed, 7001)
        self.assertEqual(Intents.INIntentErrorVoiceShortcutDeleteFailed, 7002)
        self.assertEqual(Intents.INIntentErrorEncodingGeneric, 8000)
        self.assertEqual(Intents.INIntentErrorEncodingFailed, 8001)
        self.assertEqual(Intents.INIntentErrorDecodingGeneric, 9000)

    @min_os_level("11.0")
    def testConstants11_0(self):
        self.assertIsInstance(Intents.INIntentErrorDomain, str)
