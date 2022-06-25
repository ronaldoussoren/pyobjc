from PyObjCTools.TestSupport import TestCase
import ShazamKit


class TestSHSession(TestCase):
    def test_classes(self):
        ShazamKit.SHSession

    def test_protocols(self):
        self.assertProtocolExists("SHSessionDelegate")
