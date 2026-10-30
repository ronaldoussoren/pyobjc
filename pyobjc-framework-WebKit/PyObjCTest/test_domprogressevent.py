from PyObjCTools.TestSupport import TestCase
import WebKit


class TestDOMProgressEvent(TestCase):
    def test_methods(self):
        self.assertResultIsBOOL(WebKit.DOMProgressEvent.lengthComputable)
