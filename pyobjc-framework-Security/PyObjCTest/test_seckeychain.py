import sys

import Security
from PyObjCTools.TestSupport import TestCase, fourcc, NoObjCClass
import objc

SecKeychainCallback = (
    b"iI^{SecKeychainCallbackInfo=I^{__SecKeychainItem=}^{__SecKeychain=}i}^v"
)


class TestSecKeychain(TestCase):
    def test_structs(self):
        v = Security.SecKeychainSettings()
        self.assertEqual(v.version, 0)
        self.assertEqual(v.lockOnSleep, False)
        self.assertEqual(v.useLockInterval, False)
        self.assertEqual(v.lockInterval, 0)
        self.assertPickleRoundTrips(v)

        v = Security.SecKeychainCallbackInfo()
        self.assertEqual(v.version, 0)
        self.assertEqual(v.item, None)
        self.assertEqual(v.keychain, None)
        self.assertEqual(v.pid, 0)
        self.assertPickleRoundTrips(v)

    def test_constants(self):
        self.assertEqual(Security.kSecUnlockStateStatus, 1)
        self.assertEqual(Security.kSecReadPermStatus, 2)
        self.assertEqual(Security.kSecWritePermStatus, 4)

        if sys.byteorder == "little":

            def swap_int(v):
                import struct

                return struct.unpack("<I", struct.pack(">I", v))[0]

            self.assertEqual(
                Security.kSecAuthenticationTypeNTLM, swap_int(fourcc(b"ntlm"))
            )
            self.assertEqual(
                Security.kSecAuthenticationTypeMSN, swap_int(fourcc(b"msna"))
            )
            self.assertEqual(
                Security.kSecAuthenticationTypeDPA, swap_int(fourcc(b"dpaa"))
            )
            self.assertEqual(
                Security.kSecAuthenticationTypeRPA, swap_int(fourcc(b"rpaa"))
            )
            self.assertEqual(
                Security.kSecAuthenticationTypeHTTPBasic, swap_int(fourcc(b"http"))
            )
            self.assertEqual(
                Security.kSecAuthenticationTypeHTTPDigest, swap_int(fourcc(b"httd"))
            )
            self.assertEqual(
                Security.kSecAuthenticationTypeHTMLForm, swap_int(fourcc(b"form"))
            )
            self.assertEqual(
                Security.kSecAuthenticationTypeDefault, swap_int(fourcc(b"dflt"))
            )
            self.assertEqual(Security.kSecAuthenticationTypeAny, 0)

        else:
            self.assertEqual(Security.kSecAuthenticationTypeNTLM, fourcc(b"ntlm"))
            self.assertEqual(Security.kSecAuthenticationTypeMSN, fourcc(b"msna"))
            self.assertEqual(Security.kSecAuthenticationTypeDPA, fourcc(b"dpaa"))
            self.assertEqual(Security.kSecAuthenticationTypeRPA, fourcc(b"rpaa"))
            self.assertEqual(Security.kSecAuthenticationTypeHTTPBasic, fourcc(b"http"))
            self.assertEqual(Security.kSecAuthenticationTypeHTTPDigest, fourcc(b"httd"))
            self.assertEqual(Security.kSecAuthenticationTypeHTMLForm, fourcc(b"form"))
            self.assertEqual(Security.kSecAuthenticationTypeDefault, fourcc(b"dflt"))
            self.assertEqual(Security.kSecAuthenticationTypeAny, 0)

        self.assertEqual(Security.kSecProtocolTypeFTP, fourcc(b"ftp "))
        self.assertEqual(Security.kSecProtocolTypeFTPAccount, fourcc(b"ftpa"))
        self.assertEqual(Security.kSecProtocolTypeHTTP, fourcc(b"http"))
        self.assertEqual(Security.kSecProtocolTypeIRC, fourcc(b"irc "))
        self.assertEqual(Security.kSecProtocolTypeNNTP, fourcc(b"nntp"))
        self.assertEqual(Security.kSecProtocolTypePOP3, fourcc(b"pop3"))
        self.assertEqual(Security.kSecProtocolTypeSMTP, fourcc(b"smtp"))
        self.assertEqual(Security.kSecProtocolTypeSOCKS, fourcc(b"sox "))
        self.assertEqual(Security.kSecProtocolTypeIMAP, fourcc(b"imap"))
        self.assertEqual(Security.kSecProtocolTypeLDAP, fourcc(b"ldap"))
        self.assertEqual(Security.kSecProtocolTypeAppleTalk, fourcc(b"atlk"))
        self.assertEqual(Security.kSecProtocolTypeAFP, fourcc(b"afp "))
        self.assertEqual(Security.kSecProtocolTypeTelnet, fourcc(b"teln"))
        self.assertEqual(Security.kSecProtocolTypeSSH, fourcc(b"ssh "))
        self.assertEqual(Security.kSecProtocolTypeFTPS, fourcc(b"ftps"))
        self.assertEqual(Security.kSecProtocolTypeHTTPS, fourcc(b"htps"))
        self.assertEqual(Security.kSecProtocolTypeHTTPProxy, fourcc(b"htpx"))
        self.assertEqual(Security.kSecProtocolTypeHTTPSProxy, fourcc(b"htsx"))
        self.assertEqual(Security.kSecProtocolTypeFTPProxy, fourcc(b"ftpx"))
        self.assertEqual(Security.kSecProtocolTypeCIFS, fourcc(b"cifs"))
        self.assertEqual(Security.kSecProtocolTypeSMB, fourcc(b"smb "))
        self.assertEqual(Security.kSecProtocolTypeRTSP, fourcc(b"rtsp"))
        self.assertEqual(Security.kSecProtocolTypeRTSPProxy, fourcc(b"rtsx"))
        self.assertEqual(Security.kSecProtocolTypeDAAP, fourcc(b"daap"))
        self.assertEqual(Security.kSecProtocolTypeEPPC, fourcc(b"eppc"))
        self.assertEqual(Security.kSecProtocolTypeIPP, fourcc(b"ipp "))
        self.assertEqual(Security.kSecProtocolTypeNNTPS, fourcc(b"ntps"))
        self.assertEqual(Security.kSecProtocolTypeLDAPS, fourcc(b"ldps"))
        self.assertEqual(Security.kSecProtocolTypeTelnetS, fourcc(b"tels"))
        self.assertEqual(Security.kSecProtocolTypeIMAPS, fourcc(b"imps"))
        self.assertEqual(Security.kSecProtocolTypeIRCS, fourcc(b"ircs"))
        self.assertEqual(Security.kSecProtocolTypePOP3S, fourcc(b"pops"))
        self.assertEqual(Security.kSecProtocolTypeCVSpserver, fourcc(b"cvsp"))
        self.assertEqual(Security.kSecProtocolTypeSVN, fourcc(b"svn "))
        self.assertEqual(Security.kSecProtocolTypeAny, 0)

        self.assertEqual(Security.kSecLockEvent, 1)
        self.assertEqual(Security.kSecUnlockEvent, 2)
        self.assertEqual(Security.kSecAddEvent, 3)
        self.assertEqual(Security.kSecDeleteEvent, 4)
        self.assertEqual(Security.kSecUpdateEvent, 5)
        self.assertEqual(Security.kSecPasswordChangedEvent, 6)
        self.assertEqual(Security.kSecDefaultChangedEvent, 9)
        self.assertEqual(Security.kSecDataAccessEvent, 10)
        self.assertEqual(Security.kSecKeychainListChangedEvent, 11)
        self.assertEqual(Security.kSecTrustSettingsChangedEvent, 12)

        self.assertEqual(Security.kSecLockEventMask, 1 << Security.kSecLockEvent)
        self.assertEqual(Security.kSecUnlockEventMask, 1 << Security.kSecUnlockEvent)
        self.assertEqual(Security.kSecAddEventMask, 1 << Security.kSecAddEvent)
        self.assertEqual(Security.kSecDeleteEventMask, 1 << Security.kSecDeleteEvent)
        self.assertEqual(Security.kSecUpdateEventMask, 1 << Security.kSecUpdateEvent)
        self.assertEqual(
            Security.kSecPasswordChangedEventMask,
            1 << Security.kSecPasswordChangedEvent,
        )
        self.assertEqual(
            Security.kSecDefaultChangedEventMask, 1 << Security.kSecDefaultChangedEvent
        )
        self.assertEqual(
            Security.kSecDataAccessEventMask, 1 << Security.kSecDataAccessEvent
        )
        self.assertEqual(
            Security.kSecKeychainListChangedMask,
            1 << Security.kSecKeychainListChangedEvent,
        )
        self.assertEqual(
            Security.kSecTrustSettingsChangedEventMask,
            1 << Security.kSecTrustSettingsChangedEvent,
        )
        self.assertEqual(Security.kSecEveryEventMask, 0xFFFFFFFF)

        self.assertEqual(Security.kSecPreferencesDomainUser, 0)
        self.assertEqual(Security.kSecPreferencesDomainSystem, 1)
        self.assertEqual(Security.kSecPreferencesDomainCommon, 2)
        self.assertEqual(Security.kSecPreferencesDomainDynamic, 3)

    def test_functions(self):
        self.assertIsInstance(Security.SecKeychainGetTypeID(), int)

        self.assertResultHasType(Security.SecKeychainGetVersion, objc._C_INT)
        self.assertArgHasType(
            Security.SecKeychainGetVersion, 0, objc._C_OUT + objc._C_PTR + objc._C_UINT
        )

        self.assertResultHasType(Security.SecKeychainOpen, objc._C_INT)
        self.assertArgHasType(
            Security.SecKeychainOpen, 0, objc._C_IN + objc._C_PTR + objc._C_CHAR_AS_TEXT
        )
        self.assertArgIsNullTerminated(Security.SecKeychainOpen, 0)
        self.assertArgHasType(
            Security.SecKeychainOpen, 1, objc._C_OUT + objc._C_PTR + objc._C_ID
        )
        self.assertArgIsCFRetained(Security.SecKeychainOpen, 1)

        self.assertResultHasType(Security.SecKeychainCreate, objc._C_INT)
        self.assertArgHasType(
            Security.SecKeychainCreate,
            0,
            objc._C_IN + objc._C_PTR + objc._C_CHAR_AS_TEXT,
        )
        self.assertArgIsNullTerminated(Security.SecKeychainCreate, 0)
        self.assertArgHasType(Security.SecKeychainCreate, 1, objc._C_UINT)
        self.assertArgHasType(
            Security.SecKeychainCreate, 2, objc._C_IN + objc._C_PTR + objc._C_VOID
        )
        self.assertArgSizeInArg(Security.SecKeychainCreate, 2, 1)
        self.assertArgHasType(Security.SecKeychainCreate, 3, objc._C_NSBOOL)
        self.assertArgHasType(Security.SecKeychainCreate, 4, objc._C_ID)
        self.assertArgHasType(
            Security.SecKeychainCreate, 5, objc._C_OUT + objc._C_PTR + objc._C_ID
        )
        self.assertArgIsCFRetained(Security.SecKeychainCreate, 5)

        self.assertResultHasType(Security.SecKeychainDelete, objc._C_INT)
        self.assertArgHasType(Security.SecKeychainDelete, 0, objc._C_ID)

        self.assertResultHasType(Security.SecKeychainSetSettings, objc._C_INT)
        self.assertArgHasType(Security.SecKeychainSetSettings, 0, objc._C_ID)
        self.assertArgHasType(
            Security.SecKeychainSetSettings,
            1,
            objc._C_IN + objc._C_PTR + Security.SecKeychainSettings.__typestr__,
        )

        self.assertResultHasType(Security.SecKeychainCopySettings, objc._C_INT)
        self.assertArgHasType(Security.SecKeychainCopySettings, 0, objc._C_ID)
        self.assertArgHasType(
            Security.SecKeychainCopySettings,
            1,
            objc._C_OUT + objc._C_PTR + Security.SecKeychainSettings.__typestr__,
        )

        self.assertResultHasType(Security.SecKeychainUnlock, objc._C_INT)
        self.assertArgHasType(Security.SecKeychainUnlock, 0, objc._C_ID)
        self.assertArgHasType(Security.SecKeychainUnlock, 1, objc._C_UINT)
        self.assertArgHasType(
            Security.SecKeychainUnlock, 2, objc._C_IN + objc._C_PTR + objc._C_VOID
        )
        self.assertArgSizeInArg(Security.SecKeychainUnlock, 2, 1)
        self.assertArgHasType(Security.SecKeychainUnlock, 3, objc._C_NSBOOL)

        self.assertResultHasType(Security.SecKeychainLock, objc._C_INT)
        self.assertArgHasType(Security.SecKeychainLock, 0, objc._C_ID)

        self.assertResultHasType(Security.SecKeychainLockAll, objc._C_INT)

        self.assertResultHasType(Security.SecKeychainCopyDefault, objc._C_INT)
        self.assertArgHasType(
            Security.SecKeychainCopyDefault, 0, objc._C_OUT + objc._C_PTR + objc._C_ID
        )
        self.assertArgIsCFRetained(Security.SecKeychainCopyDefault, 0)

        self.assertResultHasType(Security.SecKeychainSetDefault, objc._C_INT)
        self.assertArgHasType(Security.SecKeychainSetDefault, 0, objc._C_ID)

        self.assertResultHasType(Security.SecKeychainCopySearchList, objc._C_INT)
        self.assertArgHasType(
            Security.SecKeychainCopySearchList,
            0,
            objc._C_OUT + objc._C_PTR + objc._C_ID,
        )
        self.assertArgIsCFRetained(Security.SecKeychainCopySearchList, 0)

        self.assertResultHasType(Security.SecKeychainSetSearchList, objc._C_INT)
        self.assertArgHasType(Security.SecKeychainSetSearchList, 0, objc._C_ID)

        self.assertResultHasType(Security.SecKeychainCopyDomainDefault, objc._C_INT)
        self.assertArgHasType(Security.SecKeychainCopyDomainDefault, 0, objc._C_INT)
        self.assertArgHasType(
            Security.SecKeychainCopyDomainDefault,
            1,
            objc._C_OUT + objc._C_PTR + objc._C_ID,
        )
        self.assertArgIsCFRetained(Security.SecKeychainCopyDomainDefault, 1)

        self.assertResultHasType(Security.SecKeychainSetDomainDefault, objc._C_INT)
        self.assertArgHasType(Security.SecKeychainSetDomainDefault, 0, objc._C_INT)
        self.assertArgHasType(Security.SecKeychainSetDomainDefault, 1, objc._C_ID)

        self.assertResultHasType(Security.SecKeychainCopyDomainSearchList, objc._C_INT)
        self.assertArgHasType(Security.SecKeychainCopyDomainSearchList, 0, objc._C_INT)
        self.assertArgHasType(
            Security.SecKeychainCopyDomainSearchList,
            1,
            objc._C_OUT + objc._C_PTR + objc._C_ID,
        )
        self.assertArgIsCFRetained(Security.SecKeychainCopyDomainSearchList, 1)

        self.assertResultHasType(Security.SecKeychainSetDomainSearchList, objc._C_INT)
        self.assertArgHasType(Security.SecKeychainSetDomainSearchList, 0, objc._C_INT)
        self.assertArgHasType(Security.SecKeychainSetDomainSearchList, 1, objc._C_ID)

        self.assertResultHasType(Security.SecKeychainSetPreferenceDomain, objc._C_INT)
        self.assertArgHasType(Security.SecKeychainSetPreferenceDomain, 0, objc._C_INT)

        self.assertResultHasType(Security.SecKeychainGetPreferenceDomain, objc._C_INT)
        self.assertArgHasType(
            Security.SecKeychainGetPreferenceDomain,
            0,
            objc._C_OUT + objc._C_PTR + objc._C_INT,
        )

        self.assertResultHasType(Security.SecKeychainGetStatus, objc._C_INT)
        self.assertArgHasType(Security.SecKeychainGetStatus, 0, objc._C_ID)
        self.assertArgHasType(
            Security.SecKeychainGetStatus, 1, objc._C_OUT + objc._C_PTR + objc._C_UINT
        )

        self.assertResultHasType(Security.SecKeychainGetPath, objc._C_INT)
        self.assertArgHasType(Security.SecKeychainGetPath, 0, objc._C_ID)
        self.assertArgHasType(
            Security.SecKeychainGetPath, 1, objc._C_INOUT + objc._C_PTR + objc._C_UINT
        )
        self.assertArgHasType(
            Security.SecKeychainGetPath,
            2,
            objc._C_OUT + objc._C_PTR + objc._C_CHAR_AS_TEXT,
        )
        self.assertArgSizeInArg(Security.SecKeychainGetPath, 2, 1)

        self.assertResultHasType(Security.SecKeychainAddCallback, objc._C_INT)
        self.assertArgIsFunction(
            Security.SecKeychainAddCallback, 0, SecKeychainCallback, True
        )
        self.assertArgHasType(Security.SecKeychainAddCallback, 1, objc._C_UINT)
        self.assertArgHasType(
            Security.SecKeychainAddCallback, 2, objc._C_PTR + objc._C_VOID
        )

        self.assertResultHasType(Security.SecKeychainRemoveCallback, objc._C_INT)
        self.assertArgIsFunction(
            Security.SecKeychainRemoveCallback, 0, SecKeychainCallback, True
        )

        self.assertResultHasType(Security.SecKeychainAddInternetPassword, objc._C_INT)
        self.assertArgHasType(Security.SecKeychainAddInternetPassword, 0, objc._C_ID)
        self.assertArgHasType(Security.SecKeychainAddInternetPassword, 1, objc._C_UINT)
        self.assertArgHasType(
            Security.SecKeychainAddInternetPassword,
            2,
            objc._C_IN + objc._C_PTR + objc._C_CHAR_AS_TEXT,
        )
        self.assertArgSizeInArg(Security.SecKeychainAddInternetPassword, 2, 1)
        self.assertArgHasType(Security.SecKeychainAddInternetPassword, 3, objc._C_UINT)
        self.assertArgHasType(
            Security.SecKeychainAddInternetPassword,
            4,
            objc._C_IN + objc._C_PTR + objc._C_CHAR_AS_TEXT,
        )
        self.assertArgSizeInArg(Security.SecKeychainAddInternetPassword, 4, 3)
        self.assertArgHasType(Security.SecKeychainAddInternetPassword, 5, objc._C_UINT)
        self.assertArgHasType(
            Security.SecKeychainAddInternetPassword,
            6,
            objc._C_IN + objc._C_PTR + objc._C_CHAR_AS_TEXT,
        )
        self.assertArgSizeInArg(Security.SecKeychainAddInternetPassword, 6, 5)
        self.assertArgHasType(Security.SecKeychainAddInternetPassword, 7, objc._C_UINT)
        self.assertArgHasType(
            Security.SecKeychainAddInternetPassword,
            8,
            objc._C_IN + objc._C_PTR + objc._C_CHAR_AS_TEXT,
        )
        self.assertArgSizeInArg(Security.SecKeychainAddInternetPassword, 8, 7)
        self.assertArgHasType(Security.SecKeychainAddInternetPassword, 9, objc._C_USHT)
        self.assertArgHasType(Security.SecKeychainAddInternetPassword, 10, objc._C_UINT)
        self.assertArgHasType(Security.SecKeychainAddInternetPassword, 11, objc._C_UINT)
        self.assertArgHasType(Security.SecKeychainAddInternetPassword, 12, objc._C_UINT)
        self.assertArgHasType(
            Security.SecKeychainAddInternetPassword,
            13,
            objc._C_IN + objc._C_PTR + objc._C_VOID,
        )
        self.assertArgSizeInArg(Security.SecKeychainAddInternetPassword, 13, 12)
        self.assertArgHasType(
            Security.SecKeychainAddInternetPassword,
            14,
            objc._C_OUT + objc._C_PTR + objc._C_ID,
        )
        self.assertArgIsCFRetained(Security.SecKeychainAddInternetPassword, 14)

        self.assertResultHasType(Security.SecKeychainAddGenericPassword, objc._C_INT)
        self.assertArgHasType(Security.SecKeychainAddGenericPassword, 0, objc._C_ID)
        self.assertArgHasType(Security.SecKeychainAddGenericPassword, 1, objc._C_UINT)
        self.assertArgHasType(
            Security.SecKeychainAddGenericPassword,
            2,
            objc._C_IN + objc._C_PTR + objc._C_CHAR_AS_TEXT,
        )
        self.assertArgSizeInArg(Security.SecKeychainAddGenericPassword, 2, 1)
        self.assertArgHasType(Security.SecKeychainAddGenericPassword, 3, objc._C_UINT)
        self.assertArgHasType(
            Security.SecKeychainAddGenericPassword,
            4,
            objc._C_IN + objc._C_PTR + objc._C_CHAR_AS_TEXT,
        )
        self.assertArgSizeInArg(Security.SecKeychainAddGenericPassword, 4, 3)
        self.assertArgHasType(Security.SecKeychainAddGenericPassword, 5, objc._C_UINT)
        self.assertArgHasType(
            Security.SecKeychainAddGenericPassword,
            6,
            objc._C_IN + objc._C_PTR + objc._C_VOID,
        )
        self.assertArgSizeInArg(Security.SecKeychainAddGenericPassword, 6, 5)
        self.assertArgHasType(
            Security.SecKeychainAddGenericPassword,
            7,
            objc._C_OUT + objc._C_PTR + objc._C_ID,
        )
        self.assertArgIsCFRetained(Security.SecKeychainAddGenericPassword, 7)

        self.assertResultHasType(
            Security.SecKeychainSetUserInteractionAllowed, objc._C_INT
        )
        self.assertArgHasType(
            Security.SecKeychainSetUserInteractionAllowed, 0, objc._C_NSBOOL
        )

        self.assertResultHasType(
            Security.SecKeychainGetUserInteractionAllowed, objc._C_INT
        )
        self.assertArgHasType(
            Security.SecKeychainGetUserInteractionAllowed,
            0,
            objc._C_OUT + objc._C_PTR + objc._C_NSBOOL,
        )

        self.assertResultHasType(Security.SecKeychainCopyAccess, objc._C_INT)
        self.assertArgHasType(Security.SecKeychainCopyAccess, 0, objc._C_ID)
        self.assertArgHasType(
            Security.SecKeychainCopyAccess, 1, objc._C_OUT + objc._C_PTR + objc._C_ID
        )
        self.assertArgIsCFRetained(Security.SecKeychainCopyAccess, 1)

        self.assertResultHasType(Security.SecKeychainSetAccess, objc._C_INT)
        self.assertArgHasType(Security.SecKeychainSetAccess, 0, objc._C_ID)
        self.assertArgHasType(Security.SecKeychainSetAccess, 1, objc._C_ID)

    def test_functions_manual_internet_password(self):
        server_name = b"invalid.python.org"
        security_domain = b"secdomain"
        account_name = b"pyobjc-test-user"
        path = b"/demo"
        password = b"secret-password"

        # XXX: This adds a dummy password item to the user keychain,
        #      which is not ideal.
        status, item = Security.SecKeychainAddInternetPassword(
            None,
            len(server_name),
            server_name,
            len(security_domain),
            security_domain,
            len(account_name),
            account_name,
            len(path),
            path,
            443,
            Security.kSecProtocolTypeHTTPS,
            Security.kSecAuthenticationTypeHTTPBasic,
            len(password),
            password,
            None,
        )
        self.assertIn(
            status,
            (
                0,
                Security.errSecDuplicateItem,
            ),
        )

        with self.assertRaisesRegex(TypeError, "expected 15 arguments, got 0"):
            Security.SecKeychainFindInternetPassword()

        with self.assertRaisesRegex(TypeError, "Cannot proxy"):
            Security.SecKeychainFindInternetPassword(
                NoObjCClass(),
                len(server_name),
                server_name,
                len(security_domain),
                security_domain,
                len(account_name),
                account_name,
                len(path),
                path,
                443,
                Security.kSecProtocolTypeHTTPS,
                Security.kSecAuthenticationTypeHTTPBasic,
                None,
                None,
                None,
            )

        with self.assertRaisesRegex(
            ValueError, "depythonifying 'long long', got 'str'"
        ):
            Security.SecKeychainFindInternetPassword(
                None,
                "len(server_name)",
                server_name,
                len(security_domain),
                security_domain,
                len(account_name),
                account_name,
                len(path),
                path,
                443,
                Security.kSecProtocolTypeHTTPS,
                Security.kSecAuthenticationTypeHTTPBasic,
                None,
                None,
                None,
            )

        with self.assertRaisesRegex(TypeError, "Expecting byte-buffer, got str"):
            Security.SecKeychainFindInternetPassword(
                None,
                len(server_name),
                server_name.decode(),
                len(security_domain),
                security_domain,
                len(account_name),
                account_name,
                len(path),
                path,
                443,
                Security.kSecProtocolTypeHTTPS,
                Security.kSecAuthenticationTypeHTTPBasic,
                None,
                None,
                None,
            )

        with self.assertRaisesRegex(
            ValueError, "depythonifying 'long long', got 'str'"
        ):
            Security.SecKeychainFindInternetPassword(
                None,
                len(server_name),
                server_name,
                "len(security_domain)",
                security_domain,
                len(account_name),
                account_name,
                len(path),
                path,
                443,
                Security.kSecProtocolTypeHTTPS,
                Security.kSecAuthenticationTypeHTTPBasic,
                None,
                None,
                None,
            )

        with self.assertRaisesRegex(TypeError, "Expecting byte-buffer, got str"):
            Security.SecKeychainFindInternetPassword(
                None,
                len(server_name),
                server_name,
                len(security_domain),
                security_domain.decode(),
                len(account_name),
                account_name,
                len(path),
                path,
                443,
                Security.kSecProtocolTypeHTTPS,
                Security.kSecAuthenticationTypeHTTPBasic,
                None,
                None,
                None,
            )

        with self.assertRaisesRegex(
            ValueError, "depythonifying 'long long', got 'str'"
        ):
            Security.SecKeychainFindInternetPassword(
                None,
                len(server_name),
                server_name,
                len(security_domain),
                security_domain,
                "len(account_name)",
                account_name,
                len(path),
                path,
                443,
                Security.kSecProtocolTypeHTTPS,
                Security.kSecAuthenticationTypeHTTPBasic,
                None,
                None,
                None,
            )

        with self.assertRaisesRegex(TypeError, "Expecting byte-buffer, got str"):
            Security.SecKeychainFindInternetPassword(
                None,
                len(server_name),
                server_name,
                len(security_domain),
                security_domain,
                len(account_name),
                account_name.decode(),
                len(path),
                path,
                443,
                Security.kSecProtocolTypeHTTPS,
                Security.kSecAuthenticationTypeHTTPBasic,
                None,
                None,
                None,
            )

        with self.assertRaisesRegex(
            ValueError, "depythonifying 'long long', got 'str'"
        ):
            Security.SecKeychainFindInternetPassword(
                None,
                len(server_name),
                server_name,
                len(security_domain),
                security_domain,
                len(account_name),
                account_name,
                "len(path)",
                path,
                443,
                Security.kSecProtocolTypeHTTPS,
                Security.kSecAuthenticationTypeHTTPBasic,
                None,
                None,
                None,
            )

        with self.assertRaisesRegex(TypeError, "Expecting byte-buffer, got str"):
            Security.SecKeychainFindInternetPassword(
                None,
                len(server_name),
                server_name,
                len(security_domain),
                security_domain,
                len(account_name),
                account_name,
                len(path),
                path.decode(),
                443,
                Security.kSecProtocolTypeHTTPS,
                Security.kSecAuthenticationTypeHTTPBasic,
                None,
                None,
                None,
            )

        with self.assertRaisesRegex(
            ValueError, "depythonifying 'unsigned short', got 'str'"
        ):
            Security.SecKeychainFindInternetPassword(
                None,
                len(server_name),
                server_name,
                len(security_domain),
                security_domain,
                len(account_name),
                account_name,
                len(path),
                path,
                "443",
                Security.kSecProtocolTypeHTTPS,
                Security.kSecAuthenticationTypeHTTPBasic,
                None,
                None,
                None,
            )

        with self.assertRaisesRegex(
            ValueError, "depythonifying 'unsigned int', got 'str'"
        ):
            Security.SecKeychainFindInternetPassword(
                None,
                len(server_name),
                server_name,
                len(security_domain),
                security_domain,
                len(account_name),
                account_name,
                len(path),
                path,
                443,
                "Security.kSecProtocolTypeHTTPS",
                Security.kSecAuthenticationTypeHTTPBasic,
                None,
                None,
                None,
            )
        with self.assertRaisesRegex(
            ValueError, "depythonifying 'unsigned int', got 'str'"
        ):
            Security.SecKeychainFindInternetPassword(
                None,
                len(server_name),
                server_name,
                len(security_domain),
                security_domain,
                len(account_name),
                account_name,
                len(path),
                path,
                443,
                Security.kSecProtocolTypeHTTPS,
                "Security.kSecAuthenticationTypeHTTPBasic",
                None,
                None,
                None,
            )
        with self.assertRaisesRegex(
            TypeError, "passwordLength must be None or objc.NULL"
        ):
            Security.SecKeychainFindInternetPassword(
                None,
                len(server_name),
                server_name,
                len(security_domain),
                security_domain,
                len(account_name),
                account_name,
                len(path),
                path,
                443,
                Security.kSecProtocolTypeHTTPS,
                Security.kSecAuthenticationTypeHTTPBasic,
                42,
                None,
                None,
            )
        with self.assertRaisesRegex(
            TypeError, "passwordData must be None or objc.NULL"
        ):
            Security.SecKeychainFindInternetPassword(
                None,
                len(server_name),
                server_name,
                len(security_domain),
                security_domain,
                len(account_name),
                account_name,
                len(path),
                path,
                443,
                Security.kSecProtocolTypeHTTPS,
                Security.kSecAuthenticationTypeHTTPBasic,
                None,
                42,
                None,
            )
        with self.assertRaisesRegex(TypeError, "item must be None or objc.NULL"):
            Security.SecKeychainFindInternetPassword(
                None,
                len(server_name),
                server_name,
                len(security_domain),
                security_domain,
                len(account_name),
                account_name,
                len(path),
                path,
                443,
                Security.kSecProtocolTypeHTTPS,
                Security.kSecAuthenticationTypeHTTPBasic,
                None,
                None,
                42,
            )

        status, password_length, password_data, item = (
            Security.SecKeychainFindInternetPassword(
                None,
                len(server_name),
                server_name,
                0,
                None,
                len(account_name),
                account_name,
                len(path),
                path,
                443,
                Security.kSecProtocolTypeHTTPS,
                Security.kSecAuthenticationTypeHTTPBasic,
                None,
                None,
                None,
            )
        )
        self.assertEqual(status, 0)
        self.assertIsNot(item, None)
        self.assertEqual(password_length, len(password))
        self.assertEqual(password_data, password)

        status, password_length, password_data, item = (
            Security.SecKeychainFindInternetPassword(
                None,
                len(server_name) * 2,
                server_name + server_name,
                0,
                None,
                len(account_name),
                account_name,
                len(path),
                path,
                443,
                Security.kSecProtocolTypeHTTPS,
                Security.kSecAuthenticationTypeHTTPBasic,
                None,
                None,
                None,
            )
        )
        self.assertEqual(status, Security.errSecItemNotFound)
        self.assertIs(item, None)
        self.assertEqual(password_length, 0)
        self.assertEqual(password_data, None)

        status, password_length, password_data, item = (
            Security.SecKeychainFindInternetPassword(
                None,
                len(server_name),
                server_name,
                0,
                None,
                0,
                None,
                0,
                None,
                443,
                Security.kSecProtocolTypeHTTPS,
                Security.kSecAuthenticationTypeHTTPBasic,
                None,
                None,
                None,
            )
        )
        self.assertEqual(status, 0)
        self.assertIsNot(item, None)
        self.assertEqual(password_length, len(password))
        self.assertEqual(password_data, password)

        status, password_length, password_data, item = (
            Security.SecKeychainFindInternetPassword(
                None,
                len(server_name),
                server_name,
                0,
                objc.NULL,
                0,
                objc.NULL,
                0,
                objc.NULL,
                443,
                Security.kSecProtocolTypeHTTPS,
                Security.kSecAuthenticationTypeHTTPBasic,
                None,
                None,
                None,
            )
        )
        self.assertEqual(status, 0)
        self.assertIsNot(item, None)
        self.assertEqual(password_length, len(password))
        self.assertEqual(password_data, password)

        status, password_length, password_data, item = (
            Security.SecKeychainFindInternetPassword(
                None,
                len(server_name),
                server_name,
                0,
                objc.NULL,
                0,
                objc.NULL,
                0,
                objc.NULL,
                443,
                Security.kSecProtocolTypeHTTPS,
                Security.kSecAuthenticationTypeHTTPBasic,
                objc.NULL,
                objc.NULL,
                objc.NULL,
            )
        )
        self.assertEqual(status, 0)
        self.assertIs(item, objc.NULL)
        self.assertEqual(password_length, 0)
        self.assertEqual(password_data, objc.NULL)

    def test_functions_manual_generic_password(self):
        server_name = b"generic-invalid.python.org"
        account_name = b"pyobjc-test-user"
        password = b"secret-password"

        # XXX: This adds a dummy password item to the user keychain,
        #      which is not ideal.
        status, item = Security.SecKeychainAddGenericPassword(
            None,
            len(server_name),
            server_name,
            len(account_name),
            account_name,
            len(password),
            password,
            None,
        )
        self.assertIn(
            status,
            (
                0,
                Security.errSecDuplicateItem,
            ),
        )

        with self.assertRaisesRegex(TypeError, "expected 8 arguments, got 0"):
            Security.SecKeychainFindGenericPassword()

        with self.assertRaisesRegex(TypeError, "Cannot proxy"):
            Security.SecKeychainFindGenericPassword(
                NoObjCClass(),
                len(server_name),
                server_name,
                len(account_name),
                account_name,
                None,
                None,
                None,
            )

        with self.assertRaisesRegex(
            ValueError, "depythonifying 'long long', got 'str'"
        ):
            Security.SecKeychainFindGenericPassword(
                None,
                "len(server_name)",
                server_name,
                len(account_name),
                account_name,
                None,
                None,
                None,
            )

        with self.assertRaisesRegex(TypeError, "Expecting byte-buffer, got str"):
            Security.SecKeychainFindGenericPassword(
                None,
                len(server_name),
                server_name.decode(),
                len(account_name),
                account_name,
                None,
                None,
                None,
            )

        with self.assertRaisesRegex(
            ValueError, "depythonifying 'long long', got 'str'"
        ):
            Security.SecKeychainFindGenericPassword(
                None,
                len(server_name),
                server_name,
                "len(account_name)",
                account_name,
                None,
                None,
                None,
            )

        with self.assertRaisesRegex(TypeError, "Expecting byte-buffer, got str"):
            Security.SecKeychainFindGenericPassword(
                None,
                len(server_name),
                server_name,
                len(account_name),
                account_name.decode(),
                None,
                None,
                None,
            )

        with self.assertRaisesRegex(
            TypeError, "passwordLength must be None or objc.NULL"
        ):
            Security.SecKeychainFindGenericPassword(
                None,
                len(server_name),
                server_name,
                len(account_name),
                account_name,
                42,
                None,
                None,
            )
        with self.assertRaisesRegex(
            TypeError, "passwordData must be None or objc.NULL"
        ):
            Security.SecKeychainFindGenericPassword(
                None,
                len(server_name),
                server_name,
                len(account_name),
                account_name,
                None,
                42,
                None,
            )
        with self.assertRaisesRegex(TypeError, "item must be None or objc.NULL"):
            Security.SecKeychainFindGenericPassword(
                None,
                len(server_name),
                server_name,
                len(account_name),
                account_name,
                None,
                None,
                42,
            )

        status, password_length, password_data, item = (
            Security.SecKeychainFindGenericPassword(
                None,
                len(server_name),
                server_name,
                len(account_name),
                account_name,
                None,
                None,
                None,
            )
        )
        self.assertEqual(status, 0)
        self.assertIsNot(item, None)
        self.assertEqual(password_length, len(password))
        self.assertEqual(password_data, password)

        status, password_length, password_data, item = (
            Security.SecKeychainFindGenericPassword(
                None,
                len(server_name) * 2,
                server_name + server_name,
                len(account_name),
                account_name,
                None,
                None,
                None,
            )
        )
        self.assertEqual(status, Security.errSecItemNotFound)
        self.assertIs(item, None)
        self.assertEqual(password_length, 0)
        self.assertEqual(password_data, None)

        status, password_length, password_data, item = (
            Security.SecKeychainFindGenericPassword(
                None,
                len(server_name),
                server_name,
                0,
                None,
                None,
                None,
                None,
            )
        )
        self.assertEqual(status, 0)
        self.assertIsNot(item, None)
        self.assertEqual(password_length, len(password))
        self.assertEqual(password_data, password)

        status, password_length, password_data, item = (
            Security.SecKeychainFindGenericPassword(
                None,
                len(server_name),
                server_name,
                0,
                objc.NULL,
                None,
                None,
                None,
            )
        )
        self.assertEqual(status, 0)
        self.assertIsNot(item, None)
        self.assertEqual(password_length, len(password))
        self.assertEqual(password_data, password)

        status, password_length, password_data, item = (
            Security.SecKeychainFindGenericPassword(
                None,
                len(server_name),
                server_name,
                0,
                objc.NULL,
                objc.NULL,
                objc.NULL,
                objc.NULL,
            )
        )
        self.assertEqual(status, 0)
        self.assertIs(item, objc.NULL)
        self.assertEqual(password_length, 0)
        self.assertEqual(password_data, objc.NULL)

    def test_functions_not_wrapped(self):
        self.assertFalse(hasattr(Security, "SecKeychainAttributeInfoForItemID"))
        self.assertFalse(hasattr(Security, "SecKeychainFreeAttributeInfo"))
