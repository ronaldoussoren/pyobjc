import SecurityInterface
from PyObjCTools.TestSupport import TestCase
import objc


class TestSFKeychainSavePanel(TestCase):
    def test_classes(self):
        SecurityInterface.SFKeychainSavePanel

    def test_methods(self):
        self.assertArgIsSEL(
            SecurityInterface.SFKeychainSavePanel.beginSheetForDirectory_file_modalForWindow_modalDelegate_didEndSelector_contextInfo_,  # noqa: B950
            4,
            b"v@:@" + objc._C_NSInteger + b"^v",
        )
