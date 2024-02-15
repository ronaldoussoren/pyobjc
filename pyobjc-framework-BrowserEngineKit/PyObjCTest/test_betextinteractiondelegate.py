import BrowserEngineKit  # noqa: F401
from PyObjCTools.TestSupport import TestCase


class TestBETextInteractionDelegate(TestCase):
    def test_protocols(self):
        self.assertProtocolExists("BETextInteractionDelegate")
