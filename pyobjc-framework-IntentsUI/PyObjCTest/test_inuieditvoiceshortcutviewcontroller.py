from PyObjCTools.TestSupport import TestCase
import IntentsUI  # noqa: F401


class TestINUIEditVoiceShortcutViewController(TestCase):
    def test_protocols(self):
        self.assertProtocolExists("INUIEditVoiceShortcutViewControllerDelegate")
