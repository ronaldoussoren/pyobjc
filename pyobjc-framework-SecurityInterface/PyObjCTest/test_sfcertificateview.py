import SecurityInterface
from PyObjCTools.TestSupport import TestCase, expectedFailure


class TestSFCertificateView(TestCase):
    @expectedFailure
    def test_constants(self):
        # Constant is not present on 10.12
        self.assertHasAttr(
            SecurityInterface, "SFCertificateViewDisclosureStateDidChange"
        )
        self.assertIsInstance(
            SecurityInterface.SFCertificateViewDisclosureStateDidChange, str
        )

    def test_classes(self):
        SecurityInterface.SFCertificateView

    def test_methods(self):
        self.assertArgIsBOOL(SecurityInterface.SFCertificateView.setEditableTrust_, 0)
        self.assertResultIsBOOL(SecurityInterface.SFCertificateView.isEditable)
        self.assertArgIsBOOL(SecurityInterface.SFCertificateView.setDisplayTrust_, 0)
        self.assertResultIsBOOL(SecurityInterface.SFCertificateView.isTrustDisplayed)
        self.assertArgIsBOOL(SecurityInterface.SFCertificateView.setDisplayDetails_, 0)
        self.assertResultIsBOOL(SecurityInterface.SFCertificateView.detailsDisplayed)
        self.assertArgIsBOOL(
            SecurityInterface.SFCertificateView.setDetailsDisclosed_, 0
        )
        self.assertResultIsBOOL(SecurityInterface.SFCertificateView.detailsDisclosed)
        self.assertArgIsBOOL(
            SecurityInterface.SFCertificateView.setPoliciesDisclosed_, 0
        )
        self.assertResultIsBOOL(SecurityInterface.SFCertificateView.policiesDisclosed)
