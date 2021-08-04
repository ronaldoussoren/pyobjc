from PyObjCTools.TestSupport import TestCase, min_os_level
import Quartz


class TestPDFDestination(TestCase):
    @min_os_level("10.13")
    def testConstants(self):
        self.assertIsInstance(Quartz.kPDFDestinationUnspecifiedValue, float)
