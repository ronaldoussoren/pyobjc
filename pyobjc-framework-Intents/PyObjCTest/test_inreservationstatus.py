from PyObjCTools.TestSupport import TestCase
import Intents


class TestINReservationStatus(TestCase):
    def test_enum_types(self):
        self.assertIsEnumType(Intents.INReservationStatus)

    def test_constants(self):
        self.assertEqual(Intents.INReservationStatusUnknown, 0)
        self.assertEqual(Intents.INReservationStatusCanceled, 1)
        self.assertEqual(Intents.INReservationStatusPending, 2)
        self.assertEqual(Intents.INReservationStatusHold, 3)
        self.assertEqual(Intents.INReservationStatusConfirmed, 4)
