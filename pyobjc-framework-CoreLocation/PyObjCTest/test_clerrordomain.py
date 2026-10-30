import CoreLocation
from PyObjCTools.TestSupport import TestCase


class TestCLErrorDomain(TestCase):
    def test_constants(self):
        self.assertIsInstance(CoreLocation.kCLErrorDomain, str)
