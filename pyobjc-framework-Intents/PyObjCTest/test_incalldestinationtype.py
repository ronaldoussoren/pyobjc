from PyObjCTools.TestSupport import TestCase
import Intents


class TestINCallDestinationType(TestCase):
    def test_enums(self):
        self.assertIsEnumType(Intents.INCallDestinationType)
        self.assertEqual(Intents.INCallDestinationTypeUnknown, 0)
        self.assertEqual(Intents.INCallDestinationTypeNormal, 1)
        self.assertEqual(Intents.INCallDestinationTypeEmergency, 2)
        self.assertEqual(Intents.INCallDestinationTypeVoicemail, 3)
        self.assertEqual(Intents.INCallDestinationTypeRedial, 4)
        self.assertEqual(Intents.INCallDestinationTypeCallBack, 5)
        self.assertEqual(Intents.INCallDestinationTypeNormalDestination, 1)
        self.assertEqual(Intents.INCallDestinationTypeEmergencyDestination, 2)
        self.assertEqual(Intents.INCallDestinationTypeVoicemailDestination, 3)
        self.assertEqual(Intents.INCallDestinationTypeRedialDestination, 4)

        # Old aliases:
        self.assertEqual(Intents.INCallDestinationTypeNormalDestination, 1)
