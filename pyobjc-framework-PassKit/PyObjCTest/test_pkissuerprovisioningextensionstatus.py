from PyObjCTools.TestSupport import TestCase

import PassKit


class TestPKIssuerProvisioningExtensionStatus(TestCase):
    def test_methods(self):
        self.assertResultIsBOOL(
            PassKit.PKIssuerProvisioningExtensionStatus.requiresAuthentication
        )
        self.assertArgIsBOOL(
            PassKit.PKIssuerProvisioningExtensionStatus.setRequiresAuthentication_, 0
        )
        self.assertResultIsBOOL(
            PassKit.PKIssuerProvisioningExtensionStatus.passEntriesAvailable
        )
        self.assertArgIsBOOL(
            PassKit.PKIssuerProvisioningExtensionStatus.setPassEntriesAvailable_, 0
        )
        self.assertResultIsBOOL(
            PassKit.PKIssuerProvisioningExtensionStatus.remotePassEntriesAvailable
        )
        self.assertArgIsBOOL(
            PassKit.PKIssuerProvisioningExtensionStatus.setRemotePassEntriesAvailable_,
            0,
        )
