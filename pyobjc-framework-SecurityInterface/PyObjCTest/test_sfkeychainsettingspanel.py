from PyObjCTools.TestSupport import *

import SecurityInterface

class TestSFKeychainSettingsPanel (TestCase):
    def test_classes(self):
        SecurityInterface.SFKeychainSettingsPanel

    def test_methods(self):
        self.assertArgIsSEL(SecurityInterface.SFKeychainSettingsPanel.beginSheetForWindow_modalDelegate_didEndSelector_contextInfo_settings_keychain_, 2, b'v@:@'+objc._C_NSInteger+b'^v')

if __name__ == "__main__":
    main()
