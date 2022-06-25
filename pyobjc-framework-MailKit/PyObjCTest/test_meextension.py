from PyObjCTools.TestSupport import TestCase
import MailKit  # noqa: F401


class TestMEExtension(TestCase):
    def test_protocols(self):
        self.assertProtocolExists("MEExtension")
