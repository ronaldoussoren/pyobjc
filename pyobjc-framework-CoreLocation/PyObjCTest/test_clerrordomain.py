import CoreLocation
from PyObjCTools.TestSupport import TestCase


class TestCLErrorDomain(TestCase):
    def testConstants(self):
        self.assertIsInstance(CoreLocation.kCLErrorDomain, str)
