import Foundation
from PyObjCTools.TestSupport import TestCase, min_os_level


class TestNSMeasurement(TestCase):
    @min_os_level("10.12")
    def test_methods(self):
        self.assertResultIsBOOL(Foundation.NSMeasurement.canBeConvertedToUnit_)
