from PyObjCTools.TestSupport import TestCase
import IntentsUI  # noqa: F401
import objc


class TestINUIAddVoiceShortcutViewController(TestCase):
    def test_protocols(self):
        objc.protocolNamed("INUIAddVoiceShortcutViewControllerDelegate")
