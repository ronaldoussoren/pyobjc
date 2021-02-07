from PyObjCTools.TestSupport import TestCase
import Intents


class TestINMessage(TestCase):
    def testConstants(self):
        self.assertEqual(Intents.INMessageTypeUnspecified, 0)
        self.assertEqual(Intents.INMessageTypeText, 1)
        self.assertEqual(Intents.INMessageTypeAudio, 2)
        self.assertEqual(Intents.INMessageTypeDigitalTouch, 3)
        self.assertEqual(Intents.INMessageTypeHandwriting, 4)
        self.assertEqual(Intents.INMessageTypeSticker, 5)
        self.assertEqual(Intents.INMessageTypeTapbackLiked, 6)
        self.assertEqual(Intents.INMessageTypeTapbackDisliked, 7)
        self.assertEqual(Intents.INMessageTypeTapbackEmphasized, 8)
        self.assertEqual(Intents.INMessageTypeTapbackLoved, 9)
        self.assertEqual(Intents.INMessageTypeTapbackQuestioned, 10)
        self.assertEqual(Intents.INMessageTypeTapbackLaughed, 11)
        self.assertEqual(Intents.INMessageTypeMediaCalendar, 12)
        self.assertEqual(Intents.INMessageTypeMediaLocation, 13)
        self.assertEqual(Intents.INMessageTypeMediaAddressCard, 14)
        self.assertEqual(Intents.INMessageTypeMediaImage, 15)
        self.assertEqual(Intents.INMessageTypeMediaVideo, 16)
        self.assertEqual(Intents.INMessageTypeMediaPass, 17)
        self.assertEqual(Intents.INMessageTypeMediaAudio, 18)

        self.assertEqual(Intents.INMessageTypePaymentSent, 19)
        self.assertEqual(Intents.INMessageTypePaymentRequest, 20)
        self.assertEqual(Intents.INMessageTypePaymentNote, 21)
        self.assertEqual(Intents.INMessageTypeAnimoji, 22)
        self.assertEqual(Intents.INMessageTypeActivitySnippet, 23)
        self.assertEqual(Intents.INMessageTypeFile, 24)
        self.assertEqual(Intents.INMessageTypeLink, 25)
