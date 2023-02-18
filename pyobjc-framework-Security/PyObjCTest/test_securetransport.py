import Security
from PyObjCTools.TestSupport import TestCase, min_os_level
import objc

SSLReadFunc = b"i@o^vN^L"
SSLWriteFunc = b"i@n^vN^L"


class TestSecureTransport(TestCase):
    def test_types(self):
        self.assertIsCFType(Security.SSLContextRef)

    def test_constants(self):
        self.assertEqual(Security.kSSLCiphersuiteGroupDefault, 0)
        self.assertEqual(Security.kSSLCiphersuiteGroupCompatibility, 1)
        self.assertEqual(Security.kSSLCiphersuiteGroupLegacy, 2)
        self.assertEqual(Security.kSSLCiphersuiteGroupATS, 3)
        self.assertEqual(Security.kSSLCiphersuiteGroupATSCompatibility, 4)

        self.assertEqual(Security.kSSLProtocolUnknown, 0)
        self.assertEqual(Security.kSSLProtocol3, 2)
        self.assertEqual(Security.kTLSProtocol1, 4)
        self.assertEqual(Security.kTLSProtocol11, 7)
        self.assertEqual(Security.kTLSProtocol12, 8)
        self.assertEqual(Security.kDTLSProtocol1, 9)
        self.assertEqual(Security.kTLSProtocol13, 10)
        self.assertEqual(Security.kTLSProtocolMaxSupported, 999)
        self.assertEqual(Security.kSSLProtocol2, 1)
        self.assertEqual(Security.kSSLProtocol3Only, 3)
        self.assertEqual(Security.kTLSProtocol1Only, 5)
        self.assertEqual(Security.kSSLProtocolAll, 6)

        self.assertEqual(Security.kSSLSessionOptionBreakOnServerAuth, 0)
        self.assertEqual(Security.kSSLSessionOptionBreakOnCertRequested, 1)
        self.assertEqual(Security.kSSLSessionOptionBreakOnClientAuth, 2)
        self.assertEqual(Security.kSSLSessionOptionFalseStart, 3)
        self.assertEqual(Security.kSSLSessionOptionSendOneByteRecord, 4)
        self.assertEqual(Security.kSSLSessionOptionAllowServerIdentityChange, 5)
        self.assertEqual(Security.kSSLSessionOptionFallback, 6)
        self.assertEqual(Security.kSSLSessionOptionBreakOnClientHello, 7)
        self.assertEqual(Security.kSSLSessionOptionAllowRenegotiation, 8)
        self.assertEqual(Security.kSSLSessionOptionEnableSessionTickets, 9)

        self.assertEqual(Security.kSSLIdle, 0)
        self.assertEqual(Security.kSSLHandshake, 1)
        self.assertEqual(Security.kSSLConnected, 2)
        self.assertEqual(Security.kSSLClosed, 3)
        self.assertEqual(Security.kSSLAborted, 4)

        self.assertEqual(Security.kSSLClientCertNone, 0)
        self.assertEqual(Security.kSSLClientCertRequested, 1)
        self.assertEqual(Security.kSSLClientCertSent, 2)
        self.assertEqual(Security.kSSLClientCertRejected, 3)

        self.assertEqual(Security.errSSLProtocol, -9800)
        self.assertEqual(Security.errSSLNegotiation, -9801)
        self.assertEqual(Security.errSSLFatalAlert, -9802)
        self.assertEqual(Security.errSSLWouldBlock, -9803)
        self.assertEqual(Security.errSSLSessionNotFound, -9804)
        self.assertEqual(Security.errSSLClosedGraceful, -9805)
        self.assertEqual(Security.errSSLClosedAbort, -9806)
        self.assertEqual(Security.errSSLXCertChainInvalid, -9807)
        self.assertEqual(Security.errSSLBadCert, -9808)
        self.assertEqual(Security.errSSLCrypto, -9809)
        self.assertEqual(Security.errSSLInternal, -9810)
        self.assertEqual(Security.errSSLModuleAttach, -9811)
        self.assertEqual(Security.errSSLUnknownRootCert, -9812)
        self.assertEqual(Security.errSSLNoRootCert, -9813)
        self.assertEqual(Security.errSSLCertExpired, -9814)
        self.assertEqual(Security.errSSLCertNotYetValid, -9815)
        self.assertEqual(Security.errSSLClosedNoNotify, -9816)
        self.assertEqual(Security.errSSLBufferOverflow, -9817)
        self.assertEqual(Security.errSSLBadCipherSuite, -9818)
        self.assertEqual(Security.errSSLPeerUnexpectedMsg, -9819)
        self.assertEqual(Security.errSSLPeerBadRecordMac, -9820)
        self.assertEqual(Security.errSSLPeerDecryptionFail, -9821)
        self.assertEqual(Security.errSSLPeerRecordOverflow, -9822)
        self.assertEqual(Security.errSSLPeerDecompressFail, -9823)
        self.assertEqual(Security.errSSLPeerHandshakeFail, -9824)
        self.assertEqual(Security.errSSLPeerBadCert, -9825)
        self.assertEqual(Security.errSSLPeerUnsupportedCert, -9826)
        self.assertEqual(Security.errSSLPeerCertRevoked, -9827)
        self.assertEqual(Security.errSSLPeerCertExpired, -9828)
        self.assertEqual(Security.errSSLPeerCertUnknown, -9829)
        self.assertEqual(Security.errSSLIllegalParam, -9830)
        self.assertEqual(Security.errSSLPeerUnknownCA, -9831)
        self.assertEqual(Security.errSSLPeerAccessDenied, -9832)
        self.assertEqual(Security.errSSLPeerDecodeError, -9833)
        self.assertEqual(Security.errSSLPeerDecryptError, -9834)
        self.assertEqual(Security.errSSLPeerExportRestriction, -9835)
        self.assertEqual(Security.errSSLPeerProtocolVersion, -9836)
        self.assertEqual(Security.errSSLPeerInsufficientSecurity, -9837)
        self.assertEqual(Security.errSSLPeerInternalError, -9838)
        self.assertEqual(Security.errSSLPeerUserCancelled, -9839)
        self.assertEqual(Security.errSSLPeerNoRenegotiation, -9840)
        self.assertEqual(Security.errSSLPeerAuthCompleted, -9841)
        self.assertEqual(Security.errSSLClientCertRequested, -9842)
        self.assertEqual(Security.errSSLHostNameMismatch, -9843)
        self.assertEqual(Security.errSSLConnectionRefused, -9844)
        self.assertEqual(Security.errSSLDecryptionFail, -9845)
        self.assertEqual(Security.errSSLBadRecordMac, -9846)
        self.assertEqual(Security.errSSLRecordOverflow, -9847)
        self.assertEqual(Security.errSSLBadConfiguration, -9848)
        self.assertEqual(Security.errSSLUnexpectedRecord, -9849)
        self.assertEqual(Security.errSSLWeakPeerEphemeralDHKey, -9850)
        self.assertEqual(Security.errSSLClientHelloReceived, -9851)

        self.assertEqual(
            Security.errSSLServerAuthCompleted, Security.errSSLPeerAuthCompleted
        )
        self.assertEqual(
            Security.errSSLClientAuthCompleted, Security.errSSLPeerAuthCompleted
        )
        self.assertEqual(Security.errSSLLast, Security.errSSLUnexpectedRecord)

        self.assertEqual(Security.kSSLServerSide, 0)
        self.assertEqual(Security.kSSLClientSide, 1)

        self.assertEqual(Security.kSSLStreamType, 0)
        self.assertEqual(Security.kSSLDatagramType, 1)

        self.assertEqual(Security.kNeverAuthenticate, 0)
        self.assertEqual(Security.kAlwaysAuthenticate, 1)
        self.assertEqual(Security.kTryAuthenticate, 2)

        self.assertEqual(Security.errSSLTransportReset, -9852)
        self.assertEqual(Security.errSSLNetworkTimeout, -9853)
        self.assertEqual(Security.errSSLConfigurationFailed, -9854)
        self.assertEqual(Security.errSSLUnsupportedExtension, -9855)
        self.assertEqual(Security.errSSLUnexpectedMessage, -9856)
        self.assertEqual(Security.errSSLDecompressFail, -9857)
        self.assertEqual(Security.errSSLHandshakeFail, -9858)
        self.assertEqual(Security.errSSLDecodeError, -9859)
        self.assertEqual(Security.errSSLInappropriateFallback, -9860)
        self.assertEqual(Security.errSSLMissingExtension, -9861)
        self.assertEqual(Security.errSSLBadCertificateStatusResponse, -9862)
        self.assertEqual(Security.errSSLCertificateRequired, -9863)
        self.assertEqual(Security.errSSLUnknownPSKIdentity, -9864)
        self.assertEqual(Security.errSSLUnrecognizedName, -9865)

    @min_os_level("10.12")
    def test_constants_10_12(self):
        self.assertIsInstance(Security.kSSLSessionConfig_default, str)
        self.assertIsInstance(Security.kSSLSessionConfig_ATSv1, str)
        self.assertIsInstance(Security.kSSLSessionConfig_ATSv1_noPFS, str)
        self.assertIsInstance(Security.kSSLSessionConfig_standard, str)
        self.assertIsInstance(Security.kSSLSessionConfig_RC4_fallback, str)
        self.assertIsInstance(Security.kSSLSessionConfig_TLSv1_fallback, str)
        self.assertIsInstance(Security.kSSLSessionConfig_TLSv1_RC4_fallback, str)
        self.assertIsInstance(Security.kSSLSessionConfig_legacy, str)
        self.assertIsInstance(Security.kSSLSessionConfig_legacy_DHE, str)
        self.assertIsInstance(Security.kSSLSessionConfig_anonymous, str)
        self.assertIsInstance(Security.kSSLSessionConfig_3DES_fallback, str)
        self.assertIsInstance(Security.kSSLSessionConfig_TLSv1_3DES_fallback, str)

    def test_functions(self):
        self.assertIsInstance(Security.SSLContextGetTypeID(), int)

        self.assertFalse(hasattr(Security, "SSLNewContext"))
        self.assertFalse(hasattr(Security, "SSLDisposeContext"))

        self.assertResultHasType(Security.SSLGetSessionState, objc._C_INT)
        self.assertArgHasType(Security.SSLGetSessionState, 0, objc._C_ID)
        self.assertArgHasType(
            Security.SSLGetSessionState, 1, objc._C_OUT + objc._C_PTR + objc._C_INT
        )

        self.assertResultHasType(Security.SSLSetIOFuncs, objc._C_INT)
        self.assertArgHasType(Security.SSLSetIOFuncs, 0, objc._C_ID)
        self.assertArgIsFunction(Security.SSLSetIOFuncs, 1, SSLReadFunc, True)
        self.assertArgIsFunction(Security.SSLSetIOFuncs, 2, SSLWriteFunc, True)

        self.assertResultHasType(Security.SSLSetCertificate, objc._C_INT)
        self.assertArgHasType(Security.SSLSetCertificate, 0, objc._C_ID)
        self.assertArgHasType(Security.SSLSetCertificate, 1, objc._C_ID)

        self.assertResultHasType(Security.SSLSetConnection, objc._C_INT)
        self.assertArgHasType(Security.SSLSetConnection, 0, objc._C_ID)
        self.assertArgHasType(Security.SSLSetConnection, 1, objc._C_ID)

        self.assertResultHasType(Security.SSLGetConnection, objc._C_INT)
        self.assertArgHasType(Security.SSLGetConnection, 0, objc._C_ID)
        self.assertArgHasType(
            Security.SSLGetConnection, 1, objc._C_OUT + objc._C_PTR + objc._C_ID
        )

        self.assertResultHasType(Security.SSLSetPeerDomainName, objc._C_INT)
        self.assertArgHasType(Security.SSLSetPeerDomainName, 0, objc._C_ID)
        self.assertArgHasType(
            Security.SSLSetPeerDomainName,
            1,
            objc._C_IN + objc._C_PTR + objc._C_CHAR_AS_TEXT,
        )
        self.assertArgSizeInArg(Security.SSLSetPeerDomainName, 1, 2)
        self.assertArgHasType(Security.SSLSetPeerDomainName, 2, objc._C_ULNG)

        self.assertResultHasType(Security.SSLGetPeerDomainNameLength, objc._C_INT)
        self.assertArgHasType(Security.SSLGetPeerDomainNameLength, 0, objc._C_ID)
        self.assertArgHasType(
            Security.SSLGetPeerDomainNameLength,
            1,
            objc._C_OUT + objc._C_PTR + objc._C_ULNG,
        )

        self.assertResultHasType(Security.SSLGetPeerDomainName, objc._C_INT)
        self.assertArgHasType(Security.SSLGetPeerDomainName, 0, objc._C_ID)
        self.assertArgHasType(
            Security.SSLGetPeerDomainName,
            1,
            objc._C_OUT + objc._C_PTR + objc._C_CHAR_AS_TEXT,
        )
        self.assertArgSizeInArg(Security.SSLGetPeerDomainName, 1, 2)
        self.assertArgHasType(
            Security.SSLGetPeerDomainName, 2, objc._C_INOUT + objc._C_PTR + objc._C_ULNG
        )

        self.assertResultHasType(Security.SSLGetNegotiatedProtocolVersion, objc._C_INT)
        self.assertArgHasType(Security.SSLGetNegotiatedProtocolVersion, 0, objc._C_ID)
        self.assertArgHasType(
            Security.SSLGetNegotiatedProtocolVersion,
            1,
            objc._C_OUT + objc._C_PTR + objc._C_INT,
        )

        self.assertResultHasType(Security.SSLGetNumberSupportedCiphers, objc._C_INT)
        self.assertArgHasType(Security.SSLGetNumberSupportedCiphers, 0, objc._C_ID)
        self.assertArgHasType(
            Security.SSLGetNumberSupportedCiphers,
            1,
            objc._C_OUT + objc._C_PTR + objc._C_ULNG,
        )

        self.assertResultHasType(Security.SSLGetSupportedCiphers, objc._C_INT)
        self.assertArgHasType(Security.SSLGetSupportedCiphers, 0, objc._C_ID)
        self.assertArgHasType(
            Security.SSLGetSupportedCiphers, 1, objc._C_OUT + objc._C_PTR + objc._C_INT
        )
        self.assertArgSizeInArg(Security.SSLGetSupportedCiphers, 1, 2)
        self.assertArgHasType(
            Security.SSLGetSupportedCiphers,
            2,
            objc._C_INOUT + objc._C_PTR + objc._C_ULNG,
        )

        self.assertResultHasType(Security.SSLSetEnabledCiphers, objc._C_INT)
        self.assertArgHasType(Security.SSLSetEnabledCiphers, 0, objc._C_ID)
        self.assertArgHasType(
            Security.SSLSetEnabledCiphers, 1, objc._C_IN + objc._C_PTR + objc._C_INT
        )
        self.assertArgSizeInArg(Security.SSLSetEnabledCiphers, 1, 2)
        self.assertArgHasType(Security.SSLSetEnabledCiphers, 2, objc._C_ULNG)

        self.assertResultHasType(Security.SSLGetNumberEnabledCiphers, objc._C_INT)
        self.assertArgHasType(Security.SSLGetNumberEnabledCiphers, 0, objc._C_ID)
        self.assertArgHasType(
            Security.SSLGetNumberEnabledCiphers,
            1,
            objc._C_OUT + objc._C_PTR + objc._C_ULNG,
        )

        self.assertResultHasType(Security.SSLGetEnabledCiphers, objc._C_INT)
        self.assertArgHasType(Security.SSLGetEnabledCiphers, 0, objc._C_ID)
        self.assertArgHasType(
            Security.SSLGetEnabledCiphers, 1, objc._C_OUT + objc._C_PTR + objc._C_INT
        )
        self.assertArgSizeInArg(Security.SSLGetEnabledCiphers, 1, 2)
        self.assertArgHasType(
            Security.SSLGetEnabledCiphers, 2, objc._C_INOUT + objc._C_PTR + objc._C_ULNG
        )

        self.assertFalse(hasattr(Security, "SSLSetProtocolVersionEnabled"))
        self.assertFalse(hasattr(Security, "SSLGetProtocolVersionEnabled"))
        self.assertFalse(hasattr(Security, "SSLSetProtocolVersion"))
        self.assertFalse(hasattr(Security, "SSLGetProtocolVersion"))
        self.assertFalse(hasattr(Security, "SSLSetEnableCertVerify"))
        self.assertFalse(hasattr(Security, "SSLGetEnableCertVerify"))
        self.assertFalse(hasattr(Security, "SSLSetAllowsExpiredCerts"))
        self.assertFalse(hasattr(Security, "SSLGetAllowsExpiredCerts"))
        self.assertFalse(hasattr(Security, "SSLSetAllowsExpiredRoots"))
        self.assertFalse(hasattr(Security, "SSLGetAllowsExpiredRoots"))
        self.assertFalse(hasattr(Security, "SSLSetAllowsAnyRoot"))
        self.assertFalse(hasattr(Security, "SSLGetAllowsAnyRoot"))
        self.assertFalse(hasattr(Security, "SSLSetTrustedRoots"))
        self.assertFalse(hasattr(Security, "SSLCopyTrustedRoots"))
        self.assertFalse(hasattr(Security, "SSLCopyPeerCertificates"))

        self.assertResultHasType(Security.SSLSetPeerID, objc._C_INT)
        self.assertArgHasType(Security.SSLSetPeerID, 0, objc._C_ID)
        self.assertArgHasType(
            Security.SSLSetPeerID, 1, objc._C_IN + objc._C_PTR + objc._C_VOID
        )
        self.assertArgSizeInArg(Security.SSLSetPeerID, 1, 2)
        self.assertArgHasType(Security.SSLSetPeerID, 2, objc._C_ULNG)

        self.assertResultHasType(Security.SSLGetPeerID, objc._C_INT)
        self.assertArgHasType(Security.SSLGetPeerID, 0, objc._C_ID)
        self.assertArgHasType(
            Security.SSLGetPeerID, 1, objc._C_OUT + objc._C_PTR + objc._C_VOID
        )
        self.assertArgSizeInArg(Security.SSLGetPeerID, 1, 2)
        self.assertArgHasType(
            Security.SSLGetPeerID, 2, objc._C_INOUT + objc._C_PTR + objc._C_ULNG
        )

        self.assertResultHasType(Security.SSLGetNegotiatedCipher, objc._C_INT)
        self.assertArgHasType(Security.SSLGetNegotiatedCipher, 0, objc._C_ID)
        self.assertArgHasType(
            Security.SSLGetNegotiatedCipher, 1, objc._C_OUT + objc._C_PTR + objc._C_INT
        )

        self.assertResultHasType(Security.SSLSetClientSideAuthenticate, objc._C_INT)
        self.assertArgHasType(Security.SSLSetClientSideAuthenticate, 0, objc._C_ID)
        self.assertArgHasType(Security.SSLSetClientSideAuthenticate, 1, objc._C_INT)

        self.assertResultHasType(Security.SSLAddDistinguishedName, objc._C_INT)
        self.assertArgHasType(Security.SSLAddDistinguishedName, 0, objc._C_ID)
        self.assertArgHasType(
            Security.SSLAddDistinguishedName, 1, objc._C_IN + objc._C_PTR + objc._C_VOID
        )
        self.assertArgSizeInArg(Security.SSLAddDistinguishedName, 1, 2)
        self.assertArgHasType(Security.SSLAddDistinguishedName, 2, objc._C_ULNG)

        self.assertResultHasType(Security.SSLSetCertificateAuthorities, objc._C_INT)
        self.assertArgHasType(Security.SSLSetCertificateAuthorities, 0, objc._C_ID)
        self.assertArgHasType(Security.SSLSetCertificateAuthorities, 1, objc._C_ID)
        self.assertArgHasType(Security.SSLSetCertificateAuthorities, 2, objc._C_NSBOOL)

        self.assertResultHasType(Security.SSLCopyCertificateAuthorities, objc._C_INT)
        self.assertArgHasType(Security.SSLCopyCertificateAuthorities, 0, objc._C_ID)
        self.assertArgHasType(
            Security.SSLCopyCertificateAuthorities,
            1,
            objc._C_OUT + objc._C_PTR + objc._C_ID,
        )
        self.assertArgIsCFRetained(Security.SSLCopyCertificateAuthorities, 1)

        self.assertResultHasType(Security.SSLCopyDistinguishedNames, objc._C_INT)
        self.assertArgHasType(Security.SSLCopyDistinguishedNames, 0, objc._C_ID)
        self.assertArgHasType(
            Security.SSLCopyDistinguishedNames,
            1,
            objc._C_OUT + objc._C_PTR + objc._C_ID,
        )
        self.assertArgIsCFRetained(Security.SSLCopyDistinguishedNames, 1)

        self.assertResultHasType(Security.SSLGetClientCertificateState, objc._C_INT)
        self.assertArgHasType(Security.SSLGetClientCertificateState, 0, objc._C_ID)
        self.assertArgHasType(
            Security.SSLGetClientCertificateState,
            1,
            objc._C_OUT + objc._C_PTR + objc._C_INT,
        )

        self.assertResultHasType(Security.SSLSetDiffieHellmanParams, objc._C_INT)
        self.assertArgHasType(Security.SSLSetDiffieHellmanParams, 0, objc._C_ID)
        self.assertArgHasType(
            Security.SSLSetDiffieHellmanParams,
            1,
            objc._C_IN + objc._C_PTR + objc._C_VOID,
        )
        self.assertArgSizeInArg(Security.SSLSetDiffieHellmanParams, 1, 2)
        self.assertArgHasType(Security.SSLSetDiffieHellmanParams, 2, objc._C_ULNG)

        self.assertResultHasType(Security.SSLGetDiffieHellmanParams, objc._C_INT)
        self.assertArgHasType(Security.SSLGetDiffieHellmanParams, 0, objc._C_ID)
        self.assertArgHasType(
            Security.SSLGetDiffieHellmanParams,
            1,
            objc._C_OUT + objc._C_PTR + objc._C_VOID,
        )
        self.assertArgSizeInArg(Security.SSLGetDiffieHellmanParams, 1, 2)
        self.assertArgHasType(
            Security.SSLGetDiffieHellmanParams,
            2,
            objc._C_INOUT + objc._C_PTR + objc._C_ULNG,
        )

        self.assertFalse(hasattr(Security, "SSLSetRsaBlinding"))
        self.assertFalse(hasattr(Security, "SSLGetRsaBlinding"))

        self.assertResultHasType(Security.SSLHandshake, objc._C_INT)
        self.assertArgHasType(Security.SSLHandshake, 0, objc._C_ID)

        self.assertResultHasType(Security.SSLWrite, objc._C_INT)
        self.assertArgHasType(Security.SSLWrite, 0, objc._C_ID)
        self.assertArgHasType(
            Security.SSLWrite, 1, objc._C_IN + objc._C_PTR + objc._C_VOID
        )
        self.assertArgSizeInArg(Security.SSLWrite, 1, 2)
        self.assertArgHasType(Security.SSLWrite, 2, objc._C_ULNG)
        self.assertArgHasType(
            Security.SSLWrite, 3, objc._C_OUT + objc._C_PTR + objc._C_ULNG
        )

        self.assertResultHasType(Security.SSLRead, objc._C_INT)
        self.assertArgHasType(Security.SSLRead, 0, objc._C_ID)
        self.assertArgHasType(
            Security.SSLRead, 1, objc._C_OUT + objc._C_PTR + objc._C_VOID
        )
        self.assertArgSizeInArg(Security.SSLRead, 1, (2, 3))
        self.assertArgHasType(Security.SSLRead, 2, objc._C_ULNG)
        self.assertArgHasType(
            Security.SSLRead, 3, objc._C_OUT + objc._C_PTR + objc._C_ULNG
        )

        self.assertResultHasType(Security.SSLGetBufferedReadSize, objc._C_INT)
        self.assertArgHasType(Security.SSLGetBufferedReadSize, 0, objc._C_ID)
        self.assertArgHasType(
            Security.SSLGetBufferedReadSize, 1, objc._C_OUT + objc._C_PTR + objc._C_ULNG
        )

        self.assertResultHasType(Security.SSLClose, objc._C_INT)
        self.assertArgHasType(Security.SSLClose, 0, objc._C_ID)

    @min_os_level("10.6")
    def test_functions10_6(self):
        self.assertResultHasType(Security.SSLSetSessionOption, objc._C_INT)
        self.assertArgHasType(Security.SSLSetSessionOption, 0, objc._C_ID)
        self.assertArgHasType(Security.SSLSetSessionOption, 1, objc._C_INT)
        self.assertArgHasType(Security.SSLSetSessionOption, 2, objc._C_NSBOOL)

        self.assertResultHasType(Security.SSLGetSessionOption, objc._C_INT)
        self.assertArgHasType(Security.SSLGetSessionOption, 0, objc._C_ID)
        self.assertArgHasType(Security.SSLGetSessionOption, 1, objc._C_INT)
        self.assertArgHasType(
            Security.SSLGetSessionOption, 2, objc._C_OUT + objc._C_PTR + objc._C_NSBOOL
        )

        self.assertResultHasType(Security.SSLCopyPeerTrust, objc._C_INT)
        self.assertArgHasType(Security.SSLCopyPeerTrust, 0, objc._C_ID)
        self.assertArgHasType(
            Security.SSLCopyPeerTrust, 1, objc._C_OUT + objc._C_PTR + objc._C_ID
        )
        self.assertArgIsCFRetained(Security.SSLCopyPeerTrust, 1)

    @min_os_level("10.8")
    def test_functions10_8(self):
        self.assertResultHasType(Security.SSLCreateContext, objc._C_ID)
        self.assertResultIsCFRetained(Security.SSLCreateContext)
        self.assertArgHasType(Security.SSLCreateContext, 0, objc._C_ID)
        self.assertArgHasType(Security.SSLCreateContext, 1, objc._C_INT)
        self.assertArgHasType(Security.SSLCreateContext, 2, objc._C_INT)

        self.assertResultHasType(Security.SSLSetProtocolVersionMin, objc._C_INT)
        self.assertArgHasType(Security.SSLSetProtocolVersionMin, 0, objc._C_ID)
        self.assertArgHasType(Security.SSLSetProtocolVersionMin, 1, objc._C_INT)

        self.assertResultHasType(Security.SSLGetProtocolVersionMin, objc._C_INT)
        self.assertArgHasType(Security.SSLGetProtocolVersionMin, 0, objc._C_ID)
        self.assertArgHasType(
            Security.SSLGetProtocolVersionMin,
            1,
            objc._C_OUT + objc._C_PTR + objc._C_INT,
        )

        self.assertResultHasType(Security.SSLSetProtocolVersionMax, objc._C_INT)
        self.assertArgHasType(Security.SSLSetProtocolVersionMax, 0, objc._C_ID)
        self.assertArgHasType(Security.SSLSetProtocolVersionMax, 1, objc._C_INT)

        self.assertResultHasType(Security.SSLGetProtocolVersionMax, objc._C_INT)
        self.assertArgHasType(Security.SSLGetProtocolVersionMax, 0, objc._C_ID)
        self.assertArgHasType(
            Security.SSLGetProtocolVersionMax,
            1,
            objc._C_OUT + objc._C_PTR + objc._C_INT,
        )

        self.assertResultHasType(Security.SSLSetDatagramHelloCookie, objc._C_INT)
        self.assertArgHasType(Security.SSLSetDatagramHelloCookie, 0, objc._C_ID)
        self.assertArgHasType(
            Security.SSLSetDatagramHelloCookie,
            1,
            objc._C_IN + objc._C_PTR + objc._C_VOID,
        )
        self.assertArgSizeInArg(Security.SSLSetDatagramHelloCookie, 1, 2)
        self.assertArgHasType(Security.SSLSetDatagramHelloCookie, 2, objc._C_ULNG)

        self.assertResultHasType(Security.SSLSetMaxDatagramRecordSize, objc._C_INT)
        self.assertArgHasType(Security.SSLSetMaxDatagramRecordSize, 0, objc._C_ID)
        self.assertArgHasType(Security.SSLSetMaxDatagramRecordSize, 1, objc._C_ULNG)

        self.assertResultHasType(Security.SSLGetMaxDatagramRecordSize, objc._C_INT)
        self.assertArgHasType(Security.SSLGetMaxDatagramRecordSize, 0, objc._C_ID)
        self.assertArgHasType(
            Security.SSLGetMaxDatagramRecordSize,
            1,
            objc._C_OUT + objc._C_PTR + objc._C_ULNG,
        )

        self.assertResultHasType(Security.SSLGetDatagramWriteSize, objc._C_INT)
        self.assertArgHasType(Security.SSLGetDatagramWriteSize, 0, objc._C_ID)
        self.assertArgHasType(
            Security.SSLGetDatagramWriteSize,
            1,
            objc._C_OUT + objc._C_PTR + objc._C_ULNG,
        )

    @min_os_level("10.11")
    def test_functions_10_11(self):
        self.assertResultHasType(Security.SSLCopyRequestedPeerName, objc._C_INT)
        self.assertArgHasType(Security.SSLCopyRequestedPeerName, 0, objc._C_ID)
        self.assertArgHasType(
            Security.SSLCopyRequestedPeerName,
            1,
            objc._C_OUT + objc._C_PTR + objc._C_CHAR_AS_TEXT,
        )
        self.assertArgSizeInArg(Security.SSLCopyRequestedPeerName, 1, 2)
        self.assertArgHasType(
            Security.SSLGetPeerDomainName, 2, objc._C_INOUT + objc._C_PTR + objc._C_ULNG
        )

        self.assertResultHasType(Security.SSLCopyRequestedPeerNameLength, objc._C_INT)
        self.assertArgHasType(Security.SSLCopyRequestedPeerNameLength, 0, objc._C_ID)
        self.assertArgHasType(
            Security.SSLCopyRequestedPeerNameLength,
            1,
            objc._C_OUT + objc._C_PTR + objc._C_ULNG,
        )

    @min_os_level("10.12")
    def test_functions10_12(self):
        self.assertResultHasType(Security.SSLSetSessionConfig, objc._C_INT)
        self.assertArgHasType(Security.SSLSetSessionConfig, 0, objc._C_ID)
        self.assertArgHasType(Security.SSLSetSessionConfig, 1, objc._C_ID)

        self.assertResultHasType(Security.SSLReHandshake, objc._C_INT)
        self.assertArgHasType(Security.SSLReHandshake, 0, objc._C_ID)

    @min_os_level("10.13")
    def test_functions10_13(self):
        self.assertResultHasType(Security.SSLSetSessionTicketsEnabled, objc._C_INT)
        self.assertArgHasType(Security.SSLSetSessionTicketsEnabled, 0, objc._C_ID)
        self.assertArgHasType(Security.SSLSetSessionTicketsEnabled, 1, objc._C_NSBOOL)

        self.assertResultHasType(Security.SSLSetOCSPResponse, objc._C_INT)
        self.assertArgHasType(Security.SSLSetOCSPResponse, 0, objc._C_ID)
        self.assertArgHasType(Security.SSLSetOCSPResponse, 1, objc._C_ID)

        self.assertResultHasType(Security.SSLSetEncryptionCertificate, objc._C_INT)
        self.assertArgHasType(Security.SSLSetEncryptionCertificate, 0, objc._C_ID)
        self.assertArgHasType(Security.SSLSetEncryptionCertificate, 1, objc._C_ID)

        self.assertResultHasType(Security.SSLSetError, objc._C_INT)
        self.assertArgHasType(Security.SSLSetError, 0, objc._C_ID)
        self.assertArgHasType(Security.SSLSetError, 1, objc._C_INT)

    @min_os_level("10.13")
    def test_functions10_13_missing(self):
        self.assertResultHasType(Security.SSLSetALPNProtocols, objc._C_INT)
        self.assertArgHasType(Security.SSLSetALPNProtocols, 0, objc._C_ID)
        self.assertArgHasType(Security.SSLSetALPNProtocols, 1, objc._C_ID)

        self.assertResultHasType(Security.SSLCopyALPNProtocols, objc._C_INT)
        self.assertArgHasType(Security.SSLCopyALPNProtocols, 0, objc._C_ID)
        self.assertArgHasType(
            Security.SSLCopyALPNProtocols, 1, objc._C_OUT + objc._C_PTR + objc._C_ID
        )
        self.assertArgIsCFRetained(Security.SSLCopyALPNProtocols, 1)
