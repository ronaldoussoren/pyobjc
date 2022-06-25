import StoreKit  # noqa: F401
from PyObjCTools.TestSupport import TestCase


class TestSKRequest(TestCase):
    def test_protocols(self):
        self.assertProtocolExists("SKRequestDelegate")
