from PyObjCTools.TestSupport import TestCase
import WebKit  # noqa: F401


class TestDOMEventTargetHelper(WebKit.NSObject):
    def addEventListener_listener_useCapture_(self, a, b, c):
        pass

    def removeEventListener_listener_useCapture_(self, a, b, c):
        pass

    def dispatchEvent_(self, a):
        return 1

    def addEventListener___(self, a, b, c):
        pass

    def removeEventListener___(self, a, b, c):
        pass


class TestDOMEventTarget(TestCase):
    def test_protocols(self):
        self.assertProtocolExists("DOMEventTarget", WebKit)

    def test_protocol_methods(self):
        self.assertArgIsBOOL(
            TestDOMEventTargetHelper.addEventListener_listener_useCapture_, 2
        )
        self.assertArgIsBOOL(
            TestDOMEventTargetHelper.removeEventListener_listener_useCapture_, 2
        )
        self.assertArgIsBOOL(TestDOMEventTargetHelper.addEventListener___, 2)
        self.assertArgIsBOOL(TestDOMEventTargetHelper.removeEventListener___, 2)
        self.assertResultIsBOOL(TestDOMEventTargetHelper.dispatchEvent_)
