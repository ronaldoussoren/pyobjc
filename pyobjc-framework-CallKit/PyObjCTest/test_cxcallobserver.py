from PyObjCTools.TestSupport import TestCase
import CallKit  # noqa: F401
import objc


class TestCXCallObserver(TestCase):
    def test_protocols(self):
        objc.protocolNamed("CXCallObserverDelegate")
