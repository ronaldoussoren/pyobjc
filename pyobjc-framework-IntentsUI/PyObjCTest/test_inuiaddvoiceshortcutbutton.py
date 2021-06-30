from PyObjCTools.TestSupport import TestCase
import IntentsUI
import objc


class TestINUIAddVoiceShortcutButton(TestCase):
    def test_constants(self):
        self.assertEqual(IntentsUI.INUIAddVoiceShortcutButtonStyleWhite, 0)
        self.assertEqual(IntentsUI.INUIAddVoiceShortcutButtonStyleWhiteOutline, 1)
        self.assertEqual(IntentsUI.INUIAddVoiceShortcutButtonStyleBlack, 2)
        self.assertEqual(IntentsUI.INUIAddVoiceShortcutButtonStyleBlackOutline, 3)
        self.assertEqual(IntentsUI.INUIAddVoiceShortcutButtonStyleAutomatic, 4)
        self.assertEqual(IntentsUI.INUIAddVoiceShortcutButtonStyleAutomaticOutline, 5)

    def test_protocols(self):
        objc.protocolNamed("INUIAddVoiceShortcutButtonDelegate")
