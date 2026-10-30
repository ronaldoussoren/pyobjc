from PyObjCTools.TestSupport import TestCase, min_os_level
import EventKit


class TestEKSource(TestCase):
    def test_enums(self):
        self.assertIsEnumType(EventKit.EKSourceType)
        self.assertEqual(EventKit.EKSourceTypeLocal, 0)
        self.assertEqual(EventKit.EKSourceTypeExchange, 1)
        self.assertEqual(EventKit.EKSourceTypeCalDAV, 2)
        self.assertEqual(EventKit.EKSourceTypeMobileMe, 3)
        self.assertEqual(EventKit.EKSourceTypeSubscribed, 4)
        self.assertEqual(EventKit.EKSourceTypeBirthdays, 5)

        self.assertIsEnumType(EventKit.EKEntityType)
        self.assertEqual(EventKit.EKEntityTypeEvent, 0)
        self.assertEqual(EventKit.EKEntityTypeReminder, 1)

        self.assertEqual(EventKit.EKEntityMaskEvent, (1 << EventKit.EKEntityTypeEvent))
        self.assertEqual(
            EventKit.EKEntityMaskReminder, (1 << EventKit.EKEntityTypeReminder)
        )

    @min_os_level("13.0")
    def test_methods13_0(self):
        self.assertResultIsBOOL(EventKit.EKSource.isDelegate)
