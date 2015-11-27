from PyObjCTools.TestSupport import *

import OpenDirectory

class TestODConfiguration (TestCase):
    @min_os_level('10.9')
    def testConstants(self):
        self.assertEqual(OpenDirectory.ODPacketSigningDisabled, 0)
        self.assertEqual(OpenDirectory.ODPacketSigningAllow, 1)
        self.assertEqual(OpenDirectory.ODPacketSigningRequired, 2)

        self.assertEqual(OpenDirectory.ODPacketEncryptionDisabled, 0)
        self.assertEqual(OpenDirectory.ODPacketEncryptionAllow, 1)
        self.assertEqual(OpenDirectory.ODPacketEncryptionRequired, 2)
        self.assertEqual(OpenDirectory.ODPacketEncryptionSSL, 3)

        self.assertIsInstance(OpenDirectory.ODTrustTypeJoined, unicode)
        self.assertIsInstance(OpenDirectory.ODTrustTypeUsingCredentials, unicode)
        self.assertIsInstance(OpenDirectory.ODTrustTypeAnonymous, unicode)

    @min_os_level('10.9')
    def testMethods(self):
        self.assertResultIsBOOL(OpenDirectory.ODConfiguration.hideRegistration)
        self.assertArgIsBOOL(OpenDirectory.ODConfiguration.setHideRegistration_, 0)

        self.assertResultIsBOOL(OpenDirectory.ODConfiguration.trustUsesMutualAuthentication)

        self.assertResultIsBOOL(OpenDirectory.ODConfiguration.trustUsesKerberosKeytab)

        self.assertResultIsBOOL(OpenDirectory.ODConfiguration.trustUsesSystemKeychain)

        self.assertResultIsBOOL(OpenDirectory.ODConfiguration.manInTheMiddleProtection)
        self.assertArgIsBOOL(OpenDirectory.ODConfiguration.setManInTheMiddleProtection_, 0)

        self.assertResultIsBOOL(OpenDirectory.ODConfiguration.saveUsingAuthorization_error_)
        self.assertArgIsOut(OpenDirectory.ODConfiguration.saveUsingAuthorization_error_, 1)

        self.assertResultIsBOOL(OpenDirectory.ODConfiguration.addTrustType_trustAccount_trustPassword_username_password_joinExisting_error_)
        self.assertArgIsBOOL(OpenDirectory.ODConfiguration.addTrustType_trustAccount_trustPassword_username_password_joinExisting_error_, 5)
        self.assertArgIsOut(OpenDirectory.ODConfiguration.addTrustType_trustAccount_trustPassword_username_password_joinExisting_error_, 6)

        self.assertResultIsBOOL(OpenDirectory.ODConfiguration.removeTrustUsingUsername_password_deleteTrustAccount_error_)
        self.assertArgIsBOOL(OpenDirectory.ODConfiguration.removeTrustUsingUsername_password_deleteTrustAccount_error_, 2)
        self.assertArgIsOut(OpenDirectory.ODConfiguration.removeTrustUsingUsername_password_deleteTrustAccount_error_, 3)

if __name__ == "__main__":
    main()
