from PyObjCTools.TestSupport import TestCase, expectedFailure
import Quartz  # noqa: F401


class TestCGPSConverter(TestCase):
    @expectedFailure
    def testIncomplete(self):
        self.fail("Add header tests for <CoreGraphics/CGPSConverter.h>")
