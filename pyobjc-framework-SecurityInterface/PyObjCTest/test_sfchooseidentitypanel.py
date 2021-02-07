import SecurityInterface
from PyObjCTools.TestSupport import TestCase
import objc


class TestSFChooseIdentityPanelHelper(SecurityInterface.NSObject):
    def chooseIdentityPanelShowHelp_(self, v):
        return 1


class TestSFChooseIdentityPanel(TestCase):
    def test_classes(self):
        SecurityInterface.SFChooseIdentityPanel

    def test_methods(self):
        self.assertArgIsSEL(
            SecurityInterface.SFChooseIdentityPanel.beginSheetForWindow_modalDelegate_didEndSelector_contextInfo_identities_message_,  # noqa: B950
            2,
            b"v@:@" + objc._C_NSInteger + b"^v",
        )

        self.assertArgIsBOOL(SecurityInterface.SFChooseIdentityPanel.setShowsHelp_, 0)
        self.assertResultIsBOOL(SecurityInterface.SFChooseIdentityPanel.showsHelp)

        self.assertResultIsBOOL(
            TestSFChooseIdentityPanelHelper.chooseIdentityPanelShowHelp_
        )
