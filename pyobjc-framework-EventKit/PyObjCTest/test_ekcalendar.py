from PyObjCTools.TestSupport import TestCase

import EventKit


class TestEKCalendar(TestCase):
    def test_methods(self):
        self.assertResultIsBOOL(EventKit.EKCalendar.allowsContentModifications)
        self.assertResultIsBOOL(EventKit.EKCalendar.isImmutable)
        self.assertResultIsBOOL(EventKit.EKCalendar.isSubscribed)
