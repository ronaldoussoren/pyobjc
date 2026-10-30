import Foundation
from PyObjCTools.TestSupport import TestCase, min_os_level


class TestNSDateInterval(TestCase):
    @min_os_level("10.12")
    def test_methods(self):
        self.assertResultIsBOOL(Foundation.NSDateInterval.isEqualToDateInterval_)
        self.assertResultIsBOOL(Foundation.NSDateInterval.intersectsDateInterval_)
        self.assertResultIsBOOL(Foundation.NSDateInterval.containsDate_)
