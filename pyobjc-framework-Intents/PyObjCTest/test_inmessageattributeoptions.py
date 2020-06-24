from PyObjCTools.TestSupport import TestCase, min_os_level
import Intents


class TestINMessageAttributeOptions(TestCase):
    @min_os_level("10.12")
    def testConstants(self):
        self.assertEqual(Intents.INMessageAttributeOptionRead, 1 << 0)
        self.assertEqual(Intents.INMessageAttributeOptionUnread, 1 << 1)
        self.assertEqual(Intents.INMessageAttributeOptionFlagged, 1 << 2)
        self.assertEqual(Intents.INMessageAttributeOptionUnflagged, 1 << 3)
        self.assertEqual(Intents.INMessageAttributeOptionPlayed, 1 << 4)
