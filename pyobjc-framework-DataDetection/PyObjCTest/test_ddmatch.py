from PyObjCTools.TestSupport import TestCase

import DataDetection


class TestDDMatch(TestCase):
    def test_methods(self):
        self.assertResultIsBOOL(DataDetection.DDMatchCalendarEvent.isAllDay)
