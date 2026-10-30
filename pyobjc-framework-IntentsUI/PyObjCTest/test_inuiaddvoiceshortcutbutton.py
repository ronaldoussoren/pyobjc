from PyObjCTools.TestSupport import TestCase
import IntentsUI


class TestINUIAddVoiceShortcutButton(TestCase):
    def test_enums(self):
        self.assertIsEnumType(IntentsUI.INUIAddVoiceShortcutButtonStyle)
        self.assertEqual(IntentsUI.INUIAddVoiceShortcutButtonStyleWhite, 0)
        self.assertEqual(IntentsUI.INUIAddVoiceShortcutButtonStyleWhiteOutline, 1)
        self.assertEqual(IntentsUI.INUIAddVoiceShortcutButtonStyleBlack, 2)
        self.assertEqual(IntentsUI.INUIAddVoiceShortcutButtonStyleBlackOutline, 3)
        self.assertEqual(IntentsUI.INUIAddVoiceShortcutButtonStyleAutomatic, 4)
        self.assertEqual(IntentsUI.INUIAddVoiceShortcutButtonStyleAutomaticOutline, 5)

    def test_protocols(self):
        self.assertProtocolExists("INUIAddVoiceShortcutButtonDelegate", IntentsUI)
