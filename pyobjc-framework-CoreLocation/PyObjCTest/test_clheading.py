import CoreLocation
from PyObjCTools.TestSupport import TestCase


class TestCLHeading(TestCase):
    def test_constants(self):
        self.assertIsInstance(CoreLocation.kCLHeadingFilterNone, float)
