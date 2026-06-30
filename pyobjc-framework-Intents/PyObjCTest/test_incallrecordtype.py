from PyObjCTools.TestSupport import TestCase
import Intents


class TestINCallRecordType(TestCase):
    def test_enums(self):
        self.assertIsEnumType(Intents.INCallRecordType)
        self.assertEqual(Intents.INCallRecordTypeUnknown, 0)
        self.assertEqual(Intents.INCallRecordTypeOutgoing, 1)
        self.assertEqual(Intents.INCallRecordTypeMissed, 2)
        self.assertEqual(Intents.INCallRecordTypeReceived, 3)
        self.assertEqual(Intents.INCallRecordTypeLatest, 4)
        self.assertEqual(Intents.INCallRecordTypeVoicemail, 5)
        self.assertEqual(Intents.INCallRecordTypeRinging, 6)
        self.assertEqual(Intents.INCallRecordTypeInProgress, 7)
        self.assertEqual(Intents.INCallRecordTypeOnHold, 8)
