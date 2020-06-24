import CoreLocation
from PyObjCTools.TestSupport import TestCase, min_os_level


class TestCLHeading(TestCase):
    @min_os_level("10.7")
    def testConstants10_7(self):
        self.assertIsInstance(CoreLocation.kCLHeadingFilterNone, float)
