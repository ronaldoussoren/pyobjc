from PyObjCTools.TestSupport import TestCase
import CallKit  # noqa: F401


class TestCXCallObserver(TestCase):
    def test_protocols(self):
        self.assertProtocolExists("CXCallObserverDelegate")
