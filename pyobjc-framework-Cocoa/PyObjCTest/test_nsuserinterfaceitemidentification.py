import AppKit  # noqa: F401
import objc
from PyObjCTools.TestSupport import TestCase, min_os_level


class TestNSUserInterfaceItemIdentification(TestCase):
    @min_os_level("10.7")
    def testProtocols(self):
        objc.protocolNamed("NSUserInterfaceItemIdentification")
