import NetFS
from PyObjCTools.TestSupport import TestCase, min_os_level


class TestNetFS(TestCase):
    def testConstants(self):
        self.assertEqual(NetFS.kNetFSAuthenticationInfoKey, "AuthenticationInfo")
        self.assertEqual(NetFS.kNetFSServerDisplayNameKey, "ServerDisplayName")
        self.assertEqual(
            NetFS.kNetFSSupportsChangePasswordKey, "SupportsChangePassword"
        )
        self.assertEqual(NetFS.kNetFSSupportsGuestKey, "SupportsGuest")
        self.assertEqual(NetFS.kNetFSSupportsKerberosKey, "SupportsKerberos")
        self.assertEqual(NetFS.kNetFSGuestOnlyKey, "GuestOnly")
        self.assertEqual(NetFS.kNetFSNoMountAuthenticationKey, "NoMountAuthentication")
        self.assertEqual(
            NetFS.kNetFSConnectedWithAuthenticationInfoKey,
            "ConnectedWithAuthenticationInfo",
        )
        self.assertEqual(NetFS.kNetFSConnectedAsUserKey, "MountedByUser")
        self.assertEqual(NetFS.kNetFSConnectedAsGuestKey, "MountedByGuest")
        self.assertEqual(NetFS.kNetFSConnectedMultiUserKey, "ConnectedMultiUser")
        self.assertEqual(NetFS.kNetFSMechTypesSupportedKey, "MechTypesSupported")
        self.assertEqual(NetFS.kNAUIOptionKey, "UIOption")
        self.assertEqual(NetFS.kNAUIOptionNoUI, "NoUI")
        self.assertEqual(NetFS.kNAUIOptionAllowUI, "AllowUI")
        self.assertEqual(NetFS.kNAUIOptionForceUI, "ForceUI")
        self.assertEqual(NetFS.kNetFSSchemeKey, "Scheme")
        self.assertEqual(NetFS.kNetFSHostKey, "Host")
        self.assertEqual(NetFS.kNetFSAlternatePortKey, "AlternatePort")
        self.assertEqual(NetFS.kNetFSAuthorityParamsKey, "AuthorityParams")
        self.assertEqual(NetFS.kNetFSUserNameKey, "UserName")
        self.assertEqual(NetFS.kNetFSPasswordKey, "Password")
        self.assertEqual(NetFS.kNetFSPathKey, "Path")
        self.assertEqual(NetFS.kNetFSNoUserPreferencesKey, "NoUserPreferences")
        self.assertEqual(NetFS.kNetFSForceNewSessionKey, "ForceNewSession")
        self.assertEqual(NetFS.kNetFSUseAuthenticationInfoKey, "UseAuthenticationInfo")
        self.assertEqual(NetFS.kNetFSUseGuestKey, "Guest")
        self.assertEqual(NetFS.kNetFSChangePasswordKey, "ChangePassword")
        self.assertEqual(NetFS.kNetFSAllowLoopbackKey, "AllowLoopback")
        self.assertEqual(NetFS.kNetFSUseKerberosKey, "Kerberos")
        self.assertEqual(
            NetFS.kNetFSMountedWithAuthenticationInfoKey,
            "MountedWithAuthenticationInfo",
        )
        self.assertEqual(NetFS.kNetFSMountedByUserKey, "MountedByUser")
        self.assertEqual(NetFS.kNetFSMountedByGuestKey, "MountedByGuest")
        self.assertEqual(NetFS.kNetFSMountedMultiUserKey, "MountedMultiUser")
        self.assertEqual(NetFS.kNetFSMountedByKerberosKey, "MountedByKerberos")
        self.assertEqual(NetFS.ENETFSPWDNEEDSCHANGE, -5045)
        self.assertEqual(NetFS.ENETFSPWDPOLICY, -5046)
        self.assertEqual(NetFS.ENETFSACCOUNTRESTRICTED, -5999)
        self.assertEqual(NetFS.ENETFSNOSHARESAVAIL, -5998)
        self.assertEqual(NetFS.ENETFSNOAUTHMECHSUPP, -5997)
        self.assertEqual(NetFS.ENETFSNOPROTOVERSSUPP, -5996)
        self.assertEqual(NetFS.kNetFSGetAccessRightsKey, "GetAccessRights")
        self.assertEqual(NetFS.kNetFSAlreadyMountedKey, "AlreadyMounted")
        self.assertEqual(NetFS.kNetFSMountPathKey, "MountPath")
        self.assertEqual(NetFS.kNetFSHasPasswordKey, "HasPassword")
        self.assertEqual(NetFS.kNetFSIsHiddenKey, "IsHidden")
        self.assertEqual(NetFS.kNetFSPrinterShareKey, "PrinterShare")
        self.assertEqual(NetFS.kNetFSAccessRightsKey, "AccessRights")
        self.assertEqual(NetFS.kNetFSDisplayNameKey, "DisplayName")
        self.assertEqual(NetFS.kNetFSPasswordKey, "Password")
        self.assertEqual(NetFS.kNetFSSoftMountKey, "SoftMount")
        self.assertEqual(NetFS.kNetFSMountFlagsKey, "MountFlags")
        self.assertEqual(NetFS.kNetFSAllowSubMountsKey, "AllowSubMounts")
        self.assertEqual(NetFS.kNetFSMountAtMountDirKey, "MountAtMountDir")
        self.assertEqual(NetFS.kNetFSOpenURLMountKey, "OpenURLMount")
        self.assertEqual(NetFS.kNetFSMountedURLKey, "MountedURL")

    @min_os_level("10.8")
    def testFunctions10_8(self):
        self.assertArgIsOut(NetFS.NetFSMountURLSync, 6)

        NetFSMountURLBlock = b"vi^v@"

        self.assertArgIsOut(NetFS.NetFSMountURLAsync, 6)
        self.assertArgIsBlock(NetFS.NetFSMountURLAsync, 8, NetFSMountURLBlock)

        NetFS.NetFSMountURLCancel

    @min_os_level("10.9")
    def testFunctions10_9(self):
        NetFS.NetFSMountURLProbe

    @min_os_level("10.10")
    def testFunctions10_10(self):
        self.assertResultIsCFRetained(NetFS.NetFSCopyURLForRemountingVolume)
