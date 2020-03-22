import CoreMotion
from PyObjCTools.TestSupport import TestCase, min_os_level


class TestCMErrorDomain(TestCase):
    @min_os_level("10.15")
    def test_constants(self):
        self.assertIsInstance(CoreMotion.CMErrorDomain, str)
