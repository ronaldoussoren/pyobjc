from PyObjCTools.TestSupport import TestCase
import MailKit  # noqa: F401
import objc


class TestMEExtension(TestCase):
    def test_protocols(self):
        objc.protocolNamed("MEExtension")
