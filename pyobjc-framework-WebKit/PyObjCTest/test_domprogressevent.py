from PyObjCTools.TestSupport import TestCase, min_os_level
import WebKit


class TestDOMProgressEvent(TestCase):
    @min_os_level("10.6")
    def test_methods10_6(self):
        self.assertResultIsBOOL(WebKit.DOMProgressEvent.lengthComputable)
