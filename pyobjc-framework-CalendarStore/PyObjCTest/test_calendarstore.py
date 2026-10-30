import CalendarStore
import objc
from PyObjCTools.TestSupport import TestCase


class TestCalendarStore(TestCase):
    def test_classes(self):
        self.assertHasAttr(CalendarStore, "CalAlarm")
        self.assertIsInstance(CalendarStore.CalAlarm, objc.objc_class)
        self.assertHasAttr(CalendarStore, "CalNthWeekDay")
        self.assertIsInstance(CalendarStore.CalNthWeekDay, objc.objc_class)


class TestCallableMetadata(TestCase):
    def test_callable_metadata_is_sane(self):
        self.assertCallableMetadataIsSane(CalendarStore)
