import Speech
from PyObjCTools.TestSupport import TestCase


class TestPhoneticEmbedderEnums(TestCase):
    def test_constants(self):
        self.assertIsEnumType(Speech.PhoneticEncoderType)
        self.assertEqual(Speech.PhoneticEncoderTypeGrapheme, 0)
        self.assertEqual(Speech.PhoneticEncoderTypePhoneme, 1)

        self.assertIsEnumType(Speech.PhoneticEmbedderInitFlag)
        self.assertEqual(Speech.PhoneticEmbedderInitFlagAll, 0)
        self.assertEqual(Speech.PhoneticEmbedderInitFlagEmbedder, 1)
