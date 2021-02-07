from PyObjCTools.TestSupport import TestCase, expectedFailure
import Quartz  # noqa: F401


class TestCGGLContext(TestCase):
    @expectedFailure
    def testIncomplete(self):
        self.fail("Add header tests for <CoreGraphics/CGGLContext.h>")
