from PyObjCTools.TestSupport import TestCase, min_os_level
import WebKit  # noqa: F401


class TestDOMEventListener(TestCase):
    @min_os_level("10.10")
    def testProtocols(self):
        self.assertProtocolExists("DOMEventListener")
