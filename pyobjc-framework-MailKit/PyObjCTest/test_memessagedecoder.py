from PyObjCTools.TestSupport import TestCase
import MailKit  # noqa: F401


class TestMEMessageDecoder(TestCase):
    def test_protocols(self):
        self.assertProtocolExists("MEMessageDecoder")
