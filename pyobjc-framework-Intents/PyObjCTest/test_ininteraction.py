from PyObjCTools.TestSupport import TestCase, min_os_level
import Intents


class TestINInteraction(TestCase):
    def test_enum_types(self):
        self.assertIsEnumType(Intents.INIntentHandlingStatus)
        self.assertIsEnumType(Intents.INInteractionDirection)

    @min_os_level("10.12")
    def testConstants(self):
        self.assertEqual(Intents.INIntentHandlingStatusUnspecified, 0)
        self.assertEqual(Intents.INIntentHandlingStatusReady, 1)
        self.assertEqual(Intents.INIntentHandlingStatusInProgress, 2)
        self.assertEqual(Intents.INIntentHandlingStatusSuccess, 3)
        self.assertEqual(Intents.INIntentHandlingStatusFailure, 4)
        self.assertEqual(Intents.INIntentHandlingStatusDeferredToApplication, 5)
        self.assertEqual(Intents.INIntentHandlingStatusUserConfirmationRequired, 6)

        self.assertEqual(Intents.INInteractionDirectionUnspecified, 0)
        self.assertEqual(Intents.INInteractionDirectionOutgoing, 1)
        self.assertEqual(Intents.INInteractionDirectionIncoming, 2)

    @min_os_level("11.0")
    def test_methods11_0(self):
        self.assertArgIsBlock(
            Intents.INInteraction.donateInteractionWithCompletion_, 0, b"v@"
        )
        self.assertArgIsBlock(
            Intents.INInteraction.deleteAllInteractionsWithCompletion_, 0, b"v@"
        )
        self.assertArgIsBlock(
            Intents.INInteraction.deleteInteractionsWithIdentifiers_completion_,
            1,
            b"v@",
        )
        self.assertArgIsBlock(
            Intents.INInteraction.deleteInteractionsWithGroupIdentifier_completion_,
            1,
            b"v@",
        )
