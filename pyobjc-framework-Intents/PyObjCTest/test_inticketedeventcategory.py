from PyObjCTools.TestSupport import TestCase
import Intents


class TestINTickeetedEventCategory(TestCase):
    def test_enum_types(self):
        self.assertIsEnumType(Intents.INTicketedEventCategory)

    def testConstants(self):
        self.assertEqual(Intents.INTicketedEventCategoryUnknown, 0)
        self.assertEqual(Intents.INTicketedEventCategoryMovie, 1)
