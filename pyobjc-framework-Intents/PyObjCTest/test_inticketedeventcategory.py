from PyObjCTools.TestSupport import TestCase
import Intents


class TestINTickeetedEventCategory(TestCase):
    def test_enums(self):
        self.assertIsEnumType(Intents.INTicketedEventCategory)
        self.assertEqual(Intents.INTicketedEventCategoryUnknown, 0)
        self.assertEqual(Intents.INTicketedEventCategoryMovie, 1)
