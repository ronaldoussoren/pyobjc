from PyObjCTools.TestSupport import TestCase
import Intents


class TestINReservationActionType(TestCase):
    def test_enums(self):
        self.assertIsEnumType(Intents.INReservationActionType)
        self.assertEqual(Intents.INReservationActionTypeUnknown, 0)
        self.assertEqual(Intents.INReservationActionTypeCheckIn, 1)
