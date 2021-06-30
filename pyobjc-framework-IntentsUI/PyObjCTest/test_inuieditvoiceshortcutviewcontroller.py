from PyObjCTools.TestSupport import TestCase
import IntentsUI  # noqa: F401
import objc


class TestINUIEditVoiceShortcutViewController(TestCase):
    def test_protocols(self):
        objc.protocolNamed("INUIEditVoiceShortcutViewControllerDelegate")
