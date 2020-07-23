from PyObjCTools.TestSupport import TestCase
import Intents


class TestINTickeetedEventCategory(TestCase):
    def testConstants(self):
        self.assertEqual(Intents.INTicketedEventCategoryUnknown, 0)
        self.assertEqual(Intents.INTicketedEventCategoryMovie, 1)
