from PyObjCTools.TestSupport import TestCase
import Intents


class TestINMessageReactionType(TestCase):

    def test_enum(self):
        self.assertIsEnumType(Intents.INMessageReactionType)
        self.assertEqual(Intents.INMessageReactionTypeUnknown, 0)
        self.assertEqual(Intents.INMessageReactionTypeEmojiReaction, 1)
        self.assertEqual(Intents.INMessageReactionTypeEmoji, 2)
        self.assertEqual(Intents.INMessageReactionTypeGeneric, 3)
