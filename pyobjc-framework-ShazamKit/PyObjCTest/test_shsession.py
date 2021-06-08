from PyObjCTools.TestSupport import TestCase
import ShazamKit
import objc


class TestSHSession(TestCase):
    def test_classes(self):
        ShazamKit.SHSession

    def test_protocols(self):
        objc.protocolNamed("SHSessionDelegate")
