from PyObjCTools.TestSupport import TestCase, min_os_level
import Intents


class TestINCallRecordType(TestCase):
    @min_os_level("10.12")
    def testConstants(self):
        self.assertEqual(Intents.INCallRecordTypeUnknown, 0)
        self.assertEqual(Intents.INCallRecordTypeOutgoing, 1)
        self.assertEqual(Intents.INCallRecordTypeMissed, 2)
        self.assertEqual(Intents.INCallRecordTypeReceived, 3)

        self.assertEqual(Intents.INCallRecordTypeLatest, 4)
        self.assertEqual(Intents.INCallRecordTypeVoicemail, 5)
