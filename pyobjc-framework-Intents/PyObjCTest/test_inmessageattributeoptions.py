from PyObjCTools.TestSupport import TestCase
import Intents


class TestINMessageAttributeOptions(TestCase):
    def test_enums(self):
        self.assertIsEnumType(Intents.INMessageAttributeOptions)
        self.assertEqual(Intents.INMessageAttributeOptionRead, 1 << 0)
        self.assertEqual(Intents.INMessageAttributeOptionUnread, 1 << 1)
        self.assertEqual(Intents.INMessageAttributeOptionFlagged, 1 << 2)
        self.assertEqual(Intents.INMessageAttributeOptionUnflagged, 1 << 3)
        self.assertEqual(Intents.INMessageAttributeOptionPlayed, 1 << 4)
