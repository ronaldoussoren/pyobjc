import SecurityInterface
from PyObjCTools.TestSupport import TestCase
import objc


class TestSFKeychainSettingsPanel(TestCase):
    def test_classes(self):
        SecurityInterface.SFKeychainSettingsPanel

    def test_methods(self):
        self.assertArgIsSEL(
            SecurityInterface.SFKeychainSettingsPanel.beginSheetForWindow_modalDelegate_didEndSelector_contextInfo_settings_keychain_,  # noqa: B950
            2,
            b"v@:@" + objc._C_NSInteger + b"^v",
        )
