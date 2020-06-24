from PyObjCTools.TestSupport import TestCase, min_os_level
import EventKit


class TestEKAlarm(TestCase):
    @min_os_level("10.8")
    def testBasic(self):
        self.assertTrue(hasattr(EventKit, "EKAlarm"))

    @min_os_level("10.8")
    def testConstants10_8(self):
        self.assertEqual(EventKit.EKAlarmTypeDisplay, 0)
        self.assertEqual(EventKit.EKAlarmTypeAudio, 1)
        self.assertEqual(EventKit.EKAlarmTypeProcedure, 2)
        self.assertEqual(EventKit.EKAlarmTypeEmail, 3)

        self.assertEqual(EventKit.EKAlarmProximityNone, 0)
        self.assertEqual(EventKit.EKAlarmProximityEnter, 1)
        self.assertEqual(EventKit.EKAlarmProximityLeave, 2)
