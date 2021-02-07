from PyObjCTools.TestSupport import TestCase, min_os_level
import Quartz
import objc


class TestPDFDestination(TestCase):
    @min_os_level("10.13")
    def testConstants(self):
        # XXX: In the 10.13 SDK this is een "extern" defintion istead of an
        # #define.
        self.assertEqual(Quartz.kPDFDestinationUnspecifiedValue, objc._FLT_MAX)
