from PyObjCTools.TestSupport import TestCase
import IntentsUI  # noqa: F401


class TestINUIAddVoiceShortcutViewController(TestCase):
    def test_protocols(self):
        self.assertProtocolExists("INUIAddVoiceShortcutViewControllerDelegate")
