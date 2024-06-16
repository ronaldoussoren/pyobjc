from PyObjCTools.TestSupport import TestCase
import Intents


class TestINStickerType(TestCase):
    def test_enum(self):
        self.assertIsEnumType(Intents.INStickerType)
        self.assettEqual(Intents.INStickerTypeUnknown, 0)
        self.assettEqual(Intents.INStickerTypeEmoji, 1)
        self.assettEqual(Intents.INStickerTypeGeneric, 2)
