from PyObjCTools.TestSupport import TestCase
import MailKit  # noqa: F401


class TestMEContentBlocker(TestCase):
    def test_protocols(self):
        self.assertProtocolExists("MEContentBlocker")
