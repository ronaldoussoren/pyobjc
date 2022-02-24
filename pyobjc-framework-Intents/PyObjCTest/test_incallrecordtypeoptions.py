from PyObjCTools.TestSupport import TestCase, min_os_level
import Intents


class TestINCallRecordTypeOptions(TestCase):
    def test_enum_types(self):
        self.assertIsEnumType(Intents.INCallRecordTypeOptions)

    @min_os_level("10.12")
    def testConstants(self):
        self.assertEqual(Intents.INCallRecordTypeOptionOutgoing, 1 << 0)
        self.assertEqual(Intents.INCallRecordTypeOptionMissed, 1 << 1)
        self.assertEqual(Intents.INCallRecordTypeOptionReceived, 1 << 2)
        self.assertEqual(Intents.INCallRecordTypeOptionLatest, 1 << 3)
        self.assertEqual(Intents.INCallRecordTypeOptionVoicemail, 1 << 4)
        self.assertEqual(Intents.INCallRecordTypeOptionRinging, 1 << 5)
        self.assertEqual(Intents.INCallRecordTypeOptionInProgress, 1 << 6)
        self.assertEqual(Intents.INCallRecordTypeOptionOnHold, 1 << 7)
