from PyObjCTools.TestSupport import TestCase
import Intents


class TestINReservationActionType(TestCase):
    def test_enum_types(self):
        self.assertIsEnumType(Intents.INReservationActionType)

    def test_constants(self):
        self.assertEqual(Intents.INReservationActionTypeUnknown, 0)
        self.assertEqual(Intents.INReservationActionTypeCheckIn, 1)
