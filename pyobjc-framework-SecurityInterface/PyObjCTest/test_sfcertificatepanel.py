import SecurityInterface
from PyObjCTools.TestSupport import TestCase
import objc


class TestSFCertificatePanelHelper(SecurityInterface.NSObject):
    def certificatePanelShowHelp_(self, v):
        return 1


class TestSFCertificatePanel(TestCase):
    def test_classes(self):
        SecurityInterface.SFCertificatePanel

    def test_methods(self):
        self.assertArgIsBOOL(
            SecurityInterface.SFCertificatePanel.runModalForTrust_showGroup_, 1
        )
        self.assertArgIsBOOL(
            SecurityInterface.SFCertificatePanel.runModalForCertificates_showGroup_, 1
        )

        self.assertArgIsSEL(
            SecurityInterface.SFCertificatePanel.beginSheetForWindow_modalDelegate_didEndSelector_contextInfo_trust_showGroup_,
            2,
            b"v@:@" + objc._C_NSInteger + b"^v",
        )
        self.assertArgIsBOOL(
            SecurityInterface.SFCertificatePanel.beginSheetForWindow_modalDelegate_didEndSelector_contextInfo_trust_showGroup_,
            5,
        )

        self.assertArgIsSEL(
            SecurityInterface.SFCertificatePanel.beginSheetForWindow_modalDelegate_didEndSelector_contextInfo_certificates_showGroup_,  # noqa: B950
            2,
            b"v@:@" + objc._C_NSInteger + b"^v",
        )
        self.assertArgIsBOOL(
            SecurityInterface.SFCertificatePanel.beginSheetForWindow_modalDelegate_didEndSelector_contextInfo_certificates_showGroup_,  # noqa: B950
            5,
        )

        self.assertArgIsBOOL(SecurityInterface.SFCertificatePanel.setShowsHelp_, 0)
        self.assertResultIsBOOL(SecurityInterface.SFCertificatePanel.showsHelp)

        self.assertResultIsBOOL(TestSFCertificatePanelHelper.certificatePanelShowHelp_)
