from PyObjCTools.TestSupport import TestCase
import Intents


class TestINStickerType(TestCase):
    def test_enum(self):
        self.assertIsEnumType(Intents.INStickerType)
        self.assertEqual(Intents.INStickerTypeUnknown, 0)
        self.assertEqual(Intents.INStickerTypeEmoji, 1)
        self.assertEqual(Intents.INStickerTypeGeneric, 2)
