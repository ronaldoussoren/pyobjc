from PyObjCTools.TestSupport import TestCase, min_os_level
import Intents


class TestINCallDestinationType(TestCase):
    def test_enum_types(self):
        self.assertIsEnumType(Intents.INCallDestinationType)

    @min_os_level("10.12")
    def testConstants(self):
        self.assertEqual(Intents.INCallDestinationTypeUnknown, 0)
        self.assertEqual(Intents.INCallDestinationTypeNormalDestination, 1)
        self.assertEqual(Intents.INCallDestinationTypeEmergencyDestination, 2)
        self.assertEqual(Intents.INCallDestinationTypeVoicemailDestination, 3)
        self.assertEqual(Intents.INCallDestinationTypeRedialDestination, 4)

        self.assertEqual(Intents.INCallDestinationTypeNormal, 1)
        self.assertEqual(Intents.INCallDestinationTypeEmergency, 2)
        self.assertEqual(Intents.INCallDestinationTypeVoicemail, 3)
        self.assertEqual(Intents.INCallDestinationTypeRedial, 4)

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
