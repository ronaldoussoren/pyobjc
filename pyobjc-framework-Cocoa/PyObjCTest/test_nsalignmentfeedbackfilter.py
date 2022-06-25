import AppKit  # noqa: F401
from PyObjCTools.TestSupport import TestCase, min_os_level


class TestNSAlignmentFeedbackFilter(TestCase):
    @min_os_level("10.11")
    def testProtocols(self):
        self.assertProtocolExists("NSAlignmentFeedbackToken")
