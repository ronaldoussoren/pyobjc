import CoreLocation
from PyObjCTools.TestSupport import TestCase, min_sdk_level


class TestCLBody(TestCase):
    @min_sdk_level("27.0")
    def test_protocols(self):
        self.assertProtocolExists("CLBody", CoreLocation)
