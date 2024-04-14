from PyObjCTools.TestSupport import TestCase, fourcc

import IOBluetooth

# XXX: Argument contains a union, hence need manual binding
# OBEXSessionEventCallback = b"vn^" + IOBluetooth.OBEXSessionEvent.__typestr__
OBEXSessionEventCallback = b"vn^v"


class TestOBEX(TestCase):
    def test_constants(self):
        self.assertIsEnumType(IOBluetooth.OBEXErrorCodes)

        self.assertEqual(IOBluetooth.kOBEXErrorRangeMin, -21850)
        self.assertEqual(IOBluetooth.kOBEXErrorRangeMax, -21899)
        self.assertEqual(IOBluetooth.kOBEXSuccess, 0)
        self.assertEqual(IOBluetooth.kOBEXGeneralError, -21850)
        self.assertEqual(IOBluetooth.kOBEXNoResourcesError, -21851)
        self.assertEqual(IOBluetooth.kOBEXUnsupportedError, -21852)
        self.assertEqual(IOBluetooth.kOBEXInternalError, -21853)
        self.assertEqual(IOBluetooth.kOBEXBadArgumentError, -21854)
        self.assertEqual(IOBluetooth.kOBEXTimeoutError, -21855)
        self.assertEqual(IOBluetooth.kOBEXBadRequestError, -21856)
        self.assertEqual(IOBluetooth.kOBEXCancelledError, -21857)
        self.assertEqual(IOBluetooth.kOBEXForbiddenError, -21858)
        self.assertEqual(IOBluetooth.kOBEXUnauthorizedError, -21859)
        self.assertEqual(IOBluetooth.kOBEXNotAcceptableError, -21860)
        self.assertEqual(IOBluetooth.kOBEXConflictError, -21861)
        self.assertEqual(IOBluetooth.kOBEXMethodNotAllowedError, -21862)
        self.assertEqual(IOBluetooth.kOBEXNotFoundError, -21863)
        self.assertEqual(IOBluetooth.kOBEXNotImplementedError, -21864)
        self.assertEqual(IOBluetooth.kOBEXPreconditionFailedError, -21865)
        self.assertEqual(IOBluetooth.kOBEXSessionBusyError, -21875)
        self.assertEqual(IOBluetooth.kOBEXSessionNotConnectedError, -21876)
        self.assertEqual(IOBluetooth.kOBEXSessionBadRequestError, -21877)
        self.assertEqual(IOBluetooth.kOBEXSessionBadResponseError, -21878)
        self.assertEqual(IOBluetooth.kOBEXSessionNoTransportError, -21879)
        self.assertEqual(IOBluetooth.kOBEXSessionTransportDiedError, -21880)
        self.assertEqual(IOBluetooth.kOBEXSessionTimeoutError, -21881)
        self.assertEqual(IOBluetooth.kOBEXSessionAlreadyConnectedError, -21882)

        self.assertIsEnumType(IOBluetooth.OBEXHeaderIdentifiers)
        self.assertEqual(IOBluetooth.kOBEXHeaderIDName, 0x01)
        self.assertEqual(IOBluetooth.kOBEXHeaderIDDescription, 0x05)
        self.assertEqual(IOBluetooth.kOBEXHeaderIDReservedRangeStart, 0x10)
        self.assertEqual(IOBluetooth.kOBEXHeaderIDReservedRangeEnd, 0x2F)
        self.assertEqual(IOBluetooth.kOBEXHeaderIDUserDefinedRangeStart, 0x30)
        self.assertEqual(IOBluetooth.kOBEXHeaderIDUserDefinedRangeEnd, 0x3F)
        self.assertEqual(IOBluetooth.kOBEXHeaderIDType, 0x42)
        self.assertEqual(IOBluetooth.kOBEXHeaderIDTimeISO, 0x44)
        self.assertEqual(IOBluetooth.kOBEXHeaderIDTarget, 0x46)
        self.assertEqual(IOBluetooth.kOBEXHeaderIDHTTP, 0x47)
        self.assertEqual(IOBluetooth.kOBEXHeaderIDBody, 0x48)
        self.assertEqual(IOBluetooth.kOBEXHeaderIDEndOfBody, 0x49)
        self.assertEqual(IOBluetooth.kOBEXHeaderIDWho, 0x4A)
        self.assertEqual(IOBluetooth.kOBEXHeaderIDAppParameters, 0x4C)
        self.assertEqual(IOBluetooth.kOBEXHeaderIDAuthorizationChallenge, 0x4D)
        self.assertEqual(IOBluetooth.kOBEXHeaderIDAuthorizationResponse, 0x4E)
        self.assertEqual(IOBluetooth.kOBEXHeaderIDObjectClass, 0x4F)
        self.assertEqual(IOBluetooth.kOBEXHeaderIDCount, 0xC0)
        self.assertEqual(IOBluetooth.kOBEXHeaderIDLength, 0xC3)
        self.assertEqual(IOBluetooth.kOBEXHeaderIDTime4Byte, 0xC4)
        self.assertEqual(IOBluetooth.kOBEXHeaderIDConnectionID, 0xCB)
        self.assertEqual(IOBluetooth.kOBEXHeaderIDOBEX13WANUUID, 0x50)
        self.assertEqual(IOBluetooth.kOBEXHeaderIDOBEX13ObjectClass, 0x51)
        self.assertEqual(IOBluetooth.kOBEXHeaderIDOBEX13SessionParameters, 0x52)
        self.assertEqual(IOBluetooth.kOBEXHeaderIDOBEX13SessionSequenceNumber, 0x93)
        self.assertEqual(IOBluetooth.kOBEXHeaderIDOBEX13CreatorID, 0xCF)

        self.assertIsEnumType(IOBluetooth.OBEXOpCodeResponseValues)
        self.assertEqual(IOBluetooth.kOBEXResponseCodeReservedRangeStart, 0x00)
        self.assertEqual(IOBluetooth.kOBEXResponseCodeReservedRangeEnd, 0x0F)
        self.assertEqual(IOBluetooth.kOBEXResponseCodeContinue, 0x10)
        self.assertEqual(IOBluetooth.kOBEXResponseCodeContinueWithFinalBit, 0x90)
        self.assertEqual(IOBluetooth.kOBEXResponseCodeSuccess, 0x20)
        self.assertEqual(IOBluetooth.kOBEXResponseCodeSuccessWithFinalBit, 0xA0)
        self.assertEqual(IOBluetooth.kOBEXResponseCodeCreated, 0x21)
        self.assertEqual(IOBluetooth.kOBEXResponseCodeCreatedWithFinalBit, 0xA1)
        self.assertEqual(IOBluetooth.kOBEXResponseCodeAccepted, 0x22)
        self.assertEqual(IOBluetooth.kOBEXResponseCodeAcceptedWithFinalBit, 0xA2)
        self.assertEqual(IOBluetooth.kOBEXResponseCodeNonAuthoritativeInfo, 0x23)
        self.assertEqual(
            IOBluetooth.kOBEXResponseCodeNonAuthoritativeInfoWithFinalBit, 0xA3
        )
        self.assertEqual(IOBluetooth.kOBEXResponseCodeNoContent, 0x24)
        self.assertEqual(IOBluetooth.kOBEXResponseCodeNoContentWithFinalBit, 0xA4)
        self.assertEqual(IOBluetooth.kOBEXResponseCodeResetContent, 0x25)
        self.assertEqual(IOBluetooth.kOBEXResponseCodeResetContentWithFinalBit, 0xA5)
        self.assertEqual(IOBluetooth.kOBEXResponseCodePartialContent, 0x26)
        self.assertEqual(IOBluetooth.kOBEXResponseCodePartialContentWithFinalBit, 0xA6)
        self.assertEqual(IOBluetooth.kOBEXResponseCodeMultipleChoices, 0x30)
        self.assertEqual(IOBluetooth.kOBEXResponseCodeMultipleChoicesWithFinalBit, 0xB0)
        self.assertEqual(IOBluetooth.kOBEXResponseCodeMovedPermanently, 0x31)
        self.assertEqual(
            IOBluetooth.kOBEXResponseCodeMovedPermanentlyWithFinalBit, 0xB1
        )
        self.assertEqual(IOBluetooth.kOBEXResponseCodeMovedTemporarily, 0x32)
        self.assertEqual(
            IOBluetooth.kOBEXResponseCodeMovedTemporarilyWithFinalBit, 0xB2
        )
        self.assertEqual(IOBluetooth.kOBEXResponseCodeSeeOther, 0x33)
        self.assertEqual(IOBluetooth.kOBEXResponseCodeSeeOtherWithFinalBit, 0xB3)
        self.assertEqual(IOBluetooth.kOBEXResponseCodeNotModified, 0x34)
        self.assertEqual(IOBluetooth.kOBEXResponseCodeNotModifiedWithFinalBit, 0xB4)
        self.assertEqual(IOBluetooth.kOBEXResponseCodeUseProxy, 0x35)
        self.assertEqual(IOBluetooth.kOBEXResponseCodeUseProxyWithFinalBit, 0xB5)
        self.assertEqual(IOBluetooth.kOBEXResponseCodeBadRequest, 0x40)
        self.assertEqual(IOBluetooth.kOBEXResponseCodeBadRequestWithFinalBit, 0xC0)
        self.assertEqual(IOBluetooth.kOBEXResponseCodeUnauthorized, 0x41)
        self.assertEqual(IOBluetooth.kOBEXResponseCodeUnauthorizedWithFinalBit, 0xC1)
        self.assertEqual(IOBluetooth.kOBEXResponseCodePaymentRequired, 0x42)
        self.assertEqual(IOBluetooth.kOBEXResponseCodePaymentRequiredWithFinalBit, 0xC2)
        self.assertEqual(IOBluetooth.kOBEXResponseCodeForbidden, 0x43)
        self.assertEqual(IOBluetooth.kOBEXResponseCodeForbiddenWithFinalBit, 0xC3)
        self.assertEqual(IOBluetooth.kOBEXResponseCodeNotFound, 0x44)
        self.assertEqual(IOBluetooth.kOBEXResponseCodeNotFoundWithFinalBit, 0xC4)
        self.assertEqual(IOBluetooth.kOBEXResponseCodeMethodNotAllowed, 0x45)
        self.assertEqual(
            IOBluetooth.kOBEXResponseCodeMethodNotAllowedWithFinalBit, 0xC5
        )
        self.assertEqual(IOBluetooth.kOBEXResponseCodeNotAcceptable, 0x46)
        self.assertEqual(IOBluetooth.kOBEXResponseCodeNotAcceptableWithFinalBit, 0xC6)
        self.assertEqual(IOBluetooth.kOBEXResponseCodeProxyAuthenticationRequired, 0x47)
        self.assertEqual(
            IOBluetooth.kOBEXResponseCodeProxyAuthenticationRequiredWithFinalBit, 0xC7
        )
        self.assertEqual(IOBluetooth.kOBEXResponseCodeRequestTimeOut, 0x48)
        self.assertEqual(IOBluetooth.kOBEXResponseCodeRequestTimeOutWithFinalBit, 0xC8)
        self.assertEqual(IOBluetooth.kOBEXResponseCodeConflict, 0x49)
        self.assertEqual(IOBluetooth.kOBEXResponseCodeConflictWithFinalBit, 0xC9)
        self.assertEqual(IOBluetooth.kOBEXResponseCodeGone, 0x4A)
        self.assertEqual(IOBluetooth.kOBEXResponseCodeGoneWithFinalBit, 0xCA)
        self.assertEqual(IOBluetooth.kOBEXResponseCodeLengthRequired, 0x4B)
        self.assertEqual(IOBluetooth.kOBEXResponseCodeLengthRequiredFinalBit, 0xCB)
        self.assertEqual(IOBluetooth.kOBEXResponseCodePreconditionFailed, 0x4C)
        self.assertEqual(
            IOBluetooth.kOBEXResponseCodePreconditionFailedWithFinalBit, 0xCC
        )
        self.assertEqual(IOBluetooth.kOBEXResponseCodeRequestedEntityTooLarge, 0x4D)
        self.assertEqual(
            IOBluetooth.kOBEXResponseCodeRequestedEntityTooLargeWithFinalBit, 0xCD
        )
        self.assertEqual(IOBluetooth.kOBEXResponseCodeRequestURLTooLarge, 0x4E)
        self.assertEqual(
            IOBluetooth.kOBEXResponseCodeRequestURLTooLargeWithFinalBit, 0xCE
        )
        self.assertEqual(IOBluetooth.kOBEXResponseCodeUnsupportedMediaType, 0x4F)
        self.assertEqual(
            IOBluetooth.kOBEXResponseCodeUnsupportedMediaTypeWithFinalBit, 0xCF
        )
        self.assertEqual(IOBluetooth.kOBEXResponseCodeInternalServerError, 0x50)
        self.assertEqual(
            IOBluetooth.kOBEXResponseCodeInternalServerErrorWithFinalBit, 0xD0
        )
        self.assertEqual(IOBluetooth.kOBEXResponseCodeNotImplemented, 0x51)
        self.assertEqual(IOBluetooth.kOBEXResponseCodeNotImplementedWithFinalBit, 0xD1)
        self.assertEqual(IOBluetooth.kOBEXResponseCodeBadGateway, 0x52)
        self.assertEqual(IOBluetooth.kOBEXResponseCodeBadGatewayWithFinalBit, 0xD2)
        self.assertEqual(IOBluetooth.kOBEXResponseCodeServiceUnavailable, 0x53)
        self.assertEqual(
            IOBluetooth.kOBEXResponseCodeServiceUnavailableWithFinalBit, 0xD3
        )
        self.assertEqual(IOBluetooth.kOBEXResponseCodeGatewayTimeout, 0x54)
        self.assertEqual(IOBluetooth.kOBEXResponseCodeGatewayTimeoutWithFinalBit, 0xD4)
        self.assertEqual(IOBluetooth.kOBEXResponseCodeHTTPVersionNotSupported, 0x55)
        self.assertEqual(
            IOBluetooth.kOBEXResponseCodeHTTPVersionNotSupportedWithFinalBit, 0xD5
        )
        self.assertEqual(IOBluetooth.kOBEXResponseCodeDatabaseFull, 0x60)
        self.assertEqual(IOBluetooth.kOBEXResponseCodeDatabaseFullWithFinalBit, 0xE0)
        self.assertEqual(IOBluetooth.kOBEXResponseCodeDatabaseLocked, 0x61)
        self.assertEqual(IOBluetooth.kOBEXResponseCodeDatabaseLockedWithFinalBit, 0xE1)

        self.assertIsEnumType(IOBluetooth.OBEXOpCodeCommandValues)
        self.assertEqual(IOBluetooth.kOBEXOpCodeReserved, 0x04)
        self.assertEqual(IOBluetooth.kOBEXOpCodeConnect, 0x80)
        self.assertEqual(IOBluetooth.kOBEXOpCodeDisconnect, 0x81)
        self.assertEqual(IOBluetooth.kOBEXOpCodePut, 0x02)
        self.assertEqual(IOBluetooth.kOBEXOpCodePutWithHighBitSet, 0x82)
        self.assertEqual(IOBluetooth.kOBEXOpCodeGet, 0x03)
        self.assertEqual(IOBluetooth.kOBEXOpCodeGetWithHighBitSet, 0x83)
        self.assertEqual(IOBluetooth.kOBEXOpCodeReservedWithHighBitSet, 0x84)
        self.assertEqual(IOBluetooth.kOBEXOpCodeSetPath, 0x85)
        self.assertEqual(IOBluetooth.kOBEXOpCodeAbort, 0xFF)
        self.assertEqual(IOBluetooth.kOBEXOpCodeReservedRangeStart, 0x06)
        self.assertEqual(IOBluetooth.kOBEXOpCodeReservedRangeEnd, 0x0F)
        self.assertEqual(IOBluetooth.kOBEXOpCodeUserDefinedStart, 0x10)
        self.assertEqual(IOBluetooth.kOBEXOpCodeUserDefinedEnd, 0x1F)

        self.assertIsEnumType(IOBluetooth.OBEXConnectFlagValues)
        self.assertEqual(IOBluetooth.kOBEXConnectFlagNone, 0 << 0)
        self.assertEqual(
            IOBluetooth.kOBEXConnectFlagSupportMultipleItLMPConnections, 1 << 0
        )
        self.assertEqual(IOBluetooth.kOBEXConnectFlag1Reserved, 1 << 1)
        self.assertEqual(IOBluetooth.kOBEXConnectFlag2Reserved, 1 << 2)
        self.assertEqual(IOBluetooth.kOBEXConnectFlag3Reserved, 1 << 3)
        self.assertEqual(IOBluetooth.kOBEXConnectFlag4Reserved, 1 << 4)
        self.assertEqual(IOBluetooth.kOBEXConnectFlag5Reserved, 1 << 5)
        self.assertEqual(IOBluetooth.kOBEXConnectFlag6Reserved, 1 << 6)
        self.assertEqual(IOBluetooth.kOBEXConnectFlag7Reserved, 1 << 7)

        self.assertIsEnumType(IOBluetooth.OBEXPutFlagValues)
        self.assertEqual(IOBluetooth.kOBEXPutFlagNone, 0 << 0)
        self.assertEqual(IOBluetooth.kOBEXPutFlagGoToParentDirFirst, 1 << 0)
        self.assertEqual(IOBluetooth.kOBEXPutFlagDontCreateDirectory, 1 << 1)
        self.assertEqual(IOBluetooth.kOBEXPutFlag2Reserved, 1 << 2)
        self.assertEqual(IOBluetooth.kOBEXPutFlag3Reserved, 1 << 3)
        self.assertEqual(IOBluetooth.kOBEXPutFlag4Reserved, 1 << 4)
        self.assertEqual(IOBluetooth.kOBEXPutFlag5Reserved, 1 << 5)
        self.assertEqual(IOBluetooth.kOBEXPutFlag6Reserved, 1 << 6)
        self.assertEqual(IOBluetooth.kOBEXPutFlag7Reserved, 1 << 7)

        self.assertIsEnumType(IOBluetooth.OBEXNonceFlagValues)
        self.assertEqual(IOBluetooth.kOBEXNonceFlagNone, 0 << 0)
        self.assertEqual(IOBluetooth.kOBEXNonceFlagSendUserIDInResponse, 1 << 0)
        self.assertEqual(IOBluetooth.kOBEXNonceFlagAccessModeReadOnly, 1 << 1)
        self.assertEqual(IOBluetooth.kOBEXNonceFlag2Reserved, 1 << 2)
        self.assertEqual(IOBluetooth.kOBEXNonceFlag3Reserved, 1 << 3)
        self.assertEqual(IOBluetooth.kOBEXNonceFlag4Reserved, 1 << 4)
        self.assertEqual(IOBluetooth.kOBEXNonceFlag5Reserved, 1 << 5)
        self.assertEqual(IOBluetooth.kOBEXNonceFlag6Reserved, 1 << 6)
        self.assertEqual(IOBluetooth.kOBEXNonceFlag7Reserved, 1 << 7)

        self.assertIsEnumType(IOBluetooth.OBEXRealmValues)
        self.assertEqual(IOBluetooth.kOBEXRealmASCII, 0x00)
        self.assertEqual(IOBluetooth.kOBEXRealmISO88591, 0x01)
        self.assertEqual(IOBluetooth.kOBEXRealmISO88592, 0x02)
        self.assertEqual(IOBluetooth.kOBEXRealmISO88593, 0x03)
        self.assertEqual(IOBluetooth.kOBEXRealmISO88594, 0x04)
        self.assertEqual(IOBluetooth.kOBEXRealmISO88595, 0x05)
        self.assertEqual(IOBluetooth.kOBEXRealmISO88596, 0x06)
        self.assertEqual(IOBluetooth.kOBEXRealmISO88597, 0x07)
        self.assertEqual(IOBluetooth.kOBEXRealmISO88598, 0x08)
        self.assertEqual(IOBluetooth.kOBEXRealmISO88599, 0x09)
        self.assertEqual(IOBluetooth.kOBEXRealmUNICODE, 0xFF)

        self.assertIsEnumType(IOBluetooth.OBEXOpCodeSessionValues)
        self.assertEqual(IOBluetooth.kOBEXOpCodeCreateSession, 0x00)
        self.assertEqual(IOBluetooth.kOBEXOpCodeCloseSession, 0x01)
        self.assertEqual(IOBluetooth.kOBEXOpCodeSuspendSession, 0x02)
        self.assertEqual(IOBluetooth.kOBEXOpCodeResumeSession, 0x03)
        self.assertEqual(IOBluetooth.kOBEXOpCodeSetTimeout, 0x04)

        self.assertIsEnumType(IOBluetooth.OBEXSessionParameterTags)
        self.assertEqual(IOBluetooth.kOBEXSessionParameterTagDeviceAddress, 0x00)
        self.assertEqual(IOBluetooth.kOBEXSessionParameterTagNonce, 0x01)
        self.assertEqual(IOBluetooth.kOBEXSessionParameterTagSessionID, 0x02)
        self.assertEqual(IOBluetooth.kOBEXSessionParameterTagNextSequenceNumber, 0x03)
        self.assertEqual(IOBluetooth.kOBEXSessionParameterTagTimeout, 0x04)
        self.assertEqual(IOBluetooth.kOBEXSessionParameterTagSessionOpcode, 0x05)

        self.assertIsEnumType(IOBluetooth.OBEXVersions)
        self.assertEqual(IOBluetooth.kOBEXVersion10, 0x10)

        self.assertIsEnumType(IOBluetooth.OBEXSessionEventTypes)
        self.assertEqual(
            IOBluetooth.kOBEXSessionEventTypeConnectCommandResponseReceived,
            fourcc(b"OCEC"),
        )
        self.assertEqual(
            IOBluetooth.kOBEXSessionEventTypeDisconnectCommandResponseReceived,
            fourcc(b"OCED"),
        )
        self.assertEqual(
            IOBluetooth.kOBEXSessionEventTypePutCommandResponseReceived, fourcc(b"OCEP")
        )
        self.assertEqual(
            IOBluetooth.kOBEXSessionEventTypeGetCommandResponseReceived, fourcc(b"OCEG")
        )
        self.assertEqual(
            IOBluetooth.kOBEXSessionEventTypeSetPathCommandResponseReceived,
            fourcc(b"OCES"),
        )
        self.assertEqual(
            IOBluetooth.kOBEXSessionEventTypeAbortCommandResponseReceived,
            fourcc(b"OCEA"),
        )
        self.assertEqual(
            IOBluetooth.kOBEXSessionEventTypeConnectCommandReceived, fourcc(b"OSEC")
        )
        self.assertEqual(
            IOBluetooth.kOBEXSessionEventTypeDisconnectCommandReceived, fourcc(b"OSED")
        )
        self.assertEqual(
            IOBluetooth.kOBEXSessionEventTypePutCommandReceived, fourcc(b"OSEP")
        )
        self.assertEqual(
            IOBluetooth.kOBEXSessionEventTypeGetCommandReceived, fourcc(b"OSEG")
        )
        self.assertEqual(
            IOBluetooth.kOBEXSessionEventTypeSetPathCommandReceived, fourcc(b"OSES")
        )
        self.assertEqual(
            IOBluetooth.kOBEXSessionEventTypeAbortCommandReceived, fourcc(b"OSEA")
        )
        self.assertEqual(IOBluetooth.kOBEXSessionEventTypeError, fourcc(b"OGEE"))

        self.assertEqual(IOBluetooth.kCharsetStringISO88591, b"CHARSET=ISO-8859-1")
        self.assertEqual(IOBluetooth.kCharsetStringUTF8, b"UTF-8")
        self.assertEqual(
            IOBluetooth.kEncodingStringQuotedPrintable, b"QUOTED-PRINTABLE"
        )
        self.assertEqual(IOBluetooth.kEncodingStringBase64, b"BASE-64")
        self.assertEqual(IOBluetooth.kEncodingString8Bit, b"8BIT")

        self.assertIsInstance(IOBluetooth.kOBEXHeaderIDKeyName, str)
        self.assertIsInstance(IOBluetooth.kOBEXHeaderIDKeyType, str)
        self.assertIsInstance(IOBluetooth.kOBEXHeaderIDKeyDescription, str)
        self.assertIsInstance(IOBluetooth.kOBEXHeaderIDKeyTimeISO, str)
        self.assertIsInstance(IOBluetooth.kOBEXHeaderIDKeyTime4Byte, str)
        self.assertIsInstance(IOBluetooth.kOBEXHeaderIDKeyTarget, str)
        self.assertIsInstance(IOBluetooth.kOBEXHeaderIDKeyHTTP, str)
        self.assertIsInstance(IOBluetooth.kOBEXHeaderIDKeyBody, str)
        self.assertIsInstance(IOBluetooth.kOBEXHeaderIDKeyEndOfBody, str)
        self.assertIsInstance(IOBluetooth.kOBEXHeaderIDKeyWho, str)
        self.assertIsInstance(IOBluetooth.kOBEXHeaderIDKeyAppParameters, str)
        self.assertIsInstance(IOBluetooth.kOBEXHeaderIDKeyAuthorizationChallenge, str)
        self.assertIsInstance(IOBluetooth.kOBEXHeaderIDKeyAuthorizationResponse, str)
        self.assertIsInstance(IOBluetooth.kOBEXHeaderIDKeyObjectClass, str)
        self.assertIsInstance(IOBluetooth.kOBEXHeaderIDKeyCount, str)
        self.assertIsInstance(IOBluetooth.kOBEXHeaderIDKeyLength, str)
        self.assertIsInstance(IOBluetooth.kOBEXHeaderIDKeyConnectionID, str)
        self.assertIsInstance(IOBluetooth.kOBEXHeaderIDKeyByteSequence, str)
        self.assertIsInstance(IOBluetooth.kOBEXHeaderIDKeyUnknownUnicodeText, str)
        self.assertIsInstance(IOBluetooth.kOBEXHeaderIDKeyUnknownByteSequence, str)
        self.assertIsInstance(IOBluetooth.kOBEXHeaderIDKeyUnknown1ByteQuantity, str)
        self.assertIsInstance(IOBluetooth.kOBEXHeaderIDKeyUnknown4ByteQuantity, str)
        self.assertIsInstance(IOBluetooth.kOBEXHeaderIDKeyUserDefined, str)

    def test_macro_functions(self):
        HEADER_ID = RESPONSE_CODE = 495

        self.assertEqual(
            IOBluetooth.GET_HEADER_ID_IS_NULL_TERMINATED_UNICODE_TEXT(HEADER_ID),
            (HEADER_ID & 0xC0) == 0x00,
        )
        self.assertEqual(
            IOBluetooth.GET_HEADER_ID_IS_BYTE_SEQUENCE(HEADER_ID),
            (HEADER_ID & 0xC0) == 0x40,
        )
        self.assertEqual(
            IOBluetooth.GET_HEADER_ID_IS_1_BYTE_QUANTITY(HEADER_ID),
            (HEADER_ID & 0xC0) == 0x80,
        )
        self.assertEqual(
            IOBluetooth.GET_HEADER_ID_IS_4_BYTE_QUANTITY(HEADER_ID),
            (HEADER_ID & 0xC0) == 0xC0,
        )
        self.assertEqual(
            IOBluetooth.SET_HEADER_ID_IS_NULL_TERMINATED_UNICODE_TEXT(HEADER_ID),
            (HEADER_ID & 0x3F),
        )
        self.assertEqual(
            IOBluetooth.SET_HEADER_ID_IS_BYTE_SEQUENCE(HEADER_ID),
            (HEADER_ID & 0x3F) | 0x40,
        )
        self.assertEqual(
            IOBluetooth.SET_HEADER_ID_IS_1_BYTE_QUANTITY(HEADER_ID),
            (HEADER_ID & 0x3F) | 0x80,
        )
        self.assertEqual(
            IOBluetooth.SET_HEADER_ID_IS_4_BYTE_QUANTITY(HEADER_ID),
            (HEADER_ID & 0x3F) | 0xC0,
        )
        self.assertEqual(
            IOBluetooth.IS_RESPONSE_CODE_FINAL_BIT_SET(RESPONSE_CODE),
            RESPONSE_CODE >> 7,
        )

        self.assertEqual(
            IOBluetooth.STRIP_RESPONSE_CODE_FINAL_BIT(RESPONSE_CODE),
            RESPONSE_CODE & 0x7F,
        )

    def test_types(self):
        self.assertIsOpaquePointer(IOBluetooth.OBEXSessionRef)

    def test_structs(self):
        # XXX: Need manual bindings
        v = IOBluetooth.OBEXConnectCommandResponseData()
        self.assertEqual(v.serverResponseOpCode, 0)
        self.assertEqual(v.headerDataPtr, None)
        self.assertEqual(v.headerDataLength, 0)
        self.assertEqual(v.maxPacketSize, 0)
        self.assertEqual(v.version, 0)
        self.assertEqual(v.flags, 0)

        # XXX: Need manual bindings
        v = IOBluetooth.OBEXDisconnectCommandResponseData()
        self.assertEqual(v.serverResponseOpCode, 0)
        self.assertEqual(v.headerDataPtr, None)
        self.assertEqual(v.headerDataLength, 0)

        # XXX: Need manual bindings
        v = IOBluetooth.OBEXPutCommandResponseData()
        self.assertEqual(v.serverResponseOpCode, 0)
        self.assertEqual(v.headerDataPtr, None)
        self.assertEqual(v.headerDataLength, 0)

        # XXX: Need manual bindings
        v = IOBluetooth.OBEXGetCommandResponseData()
        self.assertEqual(v.serverResponseOpCode, 0)
        self.assertEqual(v.headerDataPtr, None)
        self.assertEqual(v.headerDataLength, 0)

        # XXX: Need manual bindings
        v = IOBluetooth.OBEXSetPathCommandResponseData()
        self.assertEqual(v.serverResponseOpCode, 0)
        self.assertEqual(v.headerDataPtr, None)
        self.assertEqual(v.headerDataLength, 0)
        self.assertEqual(v.flags, 0)
        self.assertEqual(v.constants, 0)

        # XXX: Need manual bindings
        v = IOBluetooth.OBEXAbortCommandResponseData()
        self.assertEqual(v.serverResponseOpCode, 0)
        self.assertEqual(v.headerDataPtr, None)
        self.assertEqual(v.headerDataLength, 0)

        # XXX: Need manual bindings
        v = IOBluetooth.OBEXConnectCommandData()
        self.assertEqual(v.headerDataPtr, None)
        self.assertEqual(v.headerDataLength, 0)
        self.assertEqual(v.maxPacketSize, 0)
        self.assertEqual(v.version, 0)
        self.assertEqual(v.flags, 0)

        # XXX: Need manual bindings
        v = IOBluetooth.OBEXDisconnectCommandData()
        self.assertEqual(v.headerDataPtr, None)
        self.assertEqual(v.headerDataLength, 0)

        # XXX: Need manual bindings
        v = IOBluetooth.OBEXPutCommandData()
        self.assertEqual(v.headerDataPtr, None)
        self.assertEqual(v.headerDataLength, 0)
        self.assertEqual(v.bodyDataLeftToSend, 0)

        # XXX: Need manual bindings
        v = IOBluetooth.OBEXGetCommandData()
        self.assertEqual(v.headerDataPtr, None)
        self.assertEqual(v.headerDataLength, 0)

        # XXX: Need manual bindings
        v = IOBluetooth.OBEXSetPathCommandData()
        self.assertEqual(v.headerDataPtr, None)
        self.assertEqual(v.headerDataLength, 0)
        self.assertEqual(v.flags, 0)
        self.assertEqual(v.constants, 0)

        # XXX: Need manual bindings
        v = IOBluetooth.OBEXAbortCommandData()
        self.assertEqual(v.headerDataPtr, None)
        self.assertEqual(v.headerDataLength, 0)

        # XXX: Need manual bindings
        v = IOBluetooth.OBEXErrorData()
        self.assertEqual(v.error, 0)
        self.assertEqual(v.dataPtr, None)
        self.assertEqual(v.dataLength, 0)

        # XXX: Type contains a union
        self.assertNotHasAttr(IOBluetooth, "OBEXSessionEvent")
        # v = IOBluetooth.OBEXSessionEvent()
        # self.assertEqual(v.type, 0)
        # self.assertEqual(v.session, None)
        # self.assertEqual(v.refCon, 0)
        # self.assertEqual(v.isEndOfEventData, False)
        # self.assertEqual(v.reserved1, 0)
        # self.assertEqual(v.reserved2, 0)
        # self.assertEqual(v.u, None)

    def test_functions(self):
        IOBluetooth.OBEXSessionDelete
        self.assertArgIsOut(IOBluetooth.OBEXSessionHasOpenOBEXConnection, 1)
        self.assertArgIsOut(IOBluetooth.OBEXSessionGetMaxPacketLength, 1)
        self.assertArgIsOut(IOBluetooth.OBEXSessionGetAvailableCommandPayloadLength, 2)
        self.assertArgIsOut(
            IOBluetooth.OBEXSessionGetAvailableCommandResponsePayloadLength, 2
        )

        # A number of functions take an ``OBEXSessionEvent`` indirectly through
        # a callback function. Those are disabled for now because ``OBEXSessionEvent``
        # contains a union and hence needs manual bindings. Those are not written yet
        # due to these being deprecated APIs.
        if 1:
            self.assertNotHasAttr(IOBluetooth, "OBEXSessionConnect")
            self.assertNotHasAttr(IOBluetooth, "OBEXSessionDisconnec")
            self.assertNotHasAttr(IOBluetooth, "OBEXSessionPut")
            self.assertNotHasAttr(IOBluetooth, "OBEXSessionGet")
            self.assertNotHasAttr(IOBluetooth, "OBEXSessionAbort")
            self.assertNotHasAttr(IOBluetooth, "OBEXSessionSetPath")
            self.assertNotHasAttr(IOBluetooth, "OBEXSessionConnectResponse")
            self.assertNotHasAttr(IOBluetooth, "OBEXSessionDisconnectResponse")
            self.assertNotHasAttr(IOBluetooth, "OBEXSessionGetResponse")
            self.assertNotHasAttr(IOBluetooth, "OBEXSessionPutResponse")
            self.assertNotHasAttr(IOBluetooth, "OBEXSessionAbortResponse")
            self.assertNotHasAttr(IOBluetooth, "OBEXSessionSetPathResponse")
            self.assertNotHasAttr(IOBluetooth, "OBEXSessionSetServerCallback")

        else:
            self.assertArgIsFunction(
                IOBluetooth.OBEXSessionConnect, 5, OBEXSessionEventCallback, True
            )
            self.assertArgIsFunction(
                IOBluetooth.OBEXSessionDisconnect, 3, OBEXSessionEventCallback, True
            )

            self.assertArgIsIn(IOBluetooth.OBEXSessionPut, 2)
            self.assertArgSizeInArg(IOBluetooth.OBEXSessionPut, 2, 3)
            self.assertArgIsIn(IOBluetooth.OBEXSessionPut, 4)
            self.assertArgSizeInArg(IOBluetooth.OBEXSessionPut, 4, 5)
            self.assertArgIsFunction(
                IOBluetooth.OBEXSessionPut, 6, OBEXSessionEventCallback, True
            )

            self.assertArgIsIn(IOBluetooth.OBEXSessionGet, 2)
            self.assertArgSizeInArg(IOBluetooth.OBEXSessionGet, 2, 3)
            self.assertArgIsFunction(
                IOBluetooth.OBEXSessionGet, 4, OBEXSessionEventCallback, True
            )

            self.assertArgIsIn(IOBluetooth.OBEXSessionAbort, 2)
            self.assertArgSizeInArg(IOBluetooth.OBEXSessionAbort, 2, 3)
            self.assertArgIsFunction(
                IOBluetooth.OBEXSessionAbort, 4, OBEXSessionEventCallback, True
            )

            self.assertArgIsIn(IOBluetooth.OBEXSessionSetPath, 3)
            self.assertArgSizeInArg(IOBluetooth.OBEXSessionSetPath, 3, 4)
            self.assertArgIsFunction(
                IOBluetooth.OBEXSessionSetPath, 5, OBEXSessionEventCallback, True
            )

            self.assertArgIsIn(IOBluetooth.OBEXSessionConnectResponse, 4)
            self.assertArgSizeInArg(IOBluetooth.OBEXSessionConnectResponse, 4, 5)
            self.assertArgIsFunction(
                IOBluetooth.OBEXSessionConnectResponse,
                6,
                OBEXSessionEventCallback,
                True,
            )

            self.assertArgIsIn(IOBluetooth.OBEXSessionDisconnectResponse, 2)
            self.assertArgSizeInArg(IOBluetooth.OBEXSessionDisconnectResponse, 2, 3)
            self.assertArgIsFunction(
                IOBluetooth.OBEXSessionDisconnectResponse,
                4,
                OBEXSessionEventCallback,
                True,
            )

            self.assertArgIsIn(IOBluetooth.OBEXSessionGetResponse, 2)
            self.assertArgSizeInArg(IOBluetooth.OBEXSessionGetResponse, 2, 3)
            self.assertArgIsFunction(
                IOBluetooth.OBEXSessionGetResponse, 4, OBEXSessionEventCallback, True
            )

            self.assertArgIsIn(IOBluetooth.OBEXSessionPutResponse, 2)
            self.assertArgSizeInArg(IOBluetooth.OBEXSessionPutResponse, 2, 3)
            self.assertArgIsFunction(
                IOBluetooth.OBEXSessionPutResponse, 4, OBEXSessionEventCallback, True
            )

            self.assertArgIsIn(IOBluetooth.OBEXSessionAbortResponse, 2)
            self.assertArgSizeInArg(IOBluetooth.OBEXSessionAbortResponse, 2, 3)
            self.assertArgIsFunction(
                IOBluetooth.OBEXSessionAbortResponse, 4, OBEXSessionEventCallback, True
            )

            self.assertArgIsIn(IOBluetooth.OBEXSessionSetPathResponse, 2)
            self.assertArgSizeInArg(IOBluetooth.OBEXSessionSetPathResponse, 2, 3)
            self.assertArgIsFunction(
                IOBluetooth.OBEXSessionSetPathResponse,
                4,
                OBEXSessionEventCallback,
                True,
            )

            self.assertArgIsFunction(
                IOBluetooth.OBEXSessionSetServerCallback,
                1,
                OBEXSessionEventCallback,
                True,
            )

        self.assertArgIsIn(IOBluetooth.OBEXCreateVCard, 0)
        self.assertArgSizeInArg(IOBluetooth.OBEXCreateVCard, 0, 1)
        self.assertArgIsIn(IOBluetooth.OBEXCreateVCard, 2)
        self.assertArgSizeInArg(IOBluetooth.OBEXCreateVCard, 2, 3)
        self.assertArgIsIn(IOBluetooth.OBEXCreateVCard, 4)
        self.assertArgSizeInArg(IOBluetooth.OBEXCreateVCard, 4, 5)
        self.assertArgIsIn(IOBluetooth.OBEXCreateVCard, 6)
        self.assertArgSizeInArg(IOBluetooth.OBEXCreateVCard, 6, 7)
        self.assertArgIsIn(IOBluetooth.OBEXCreateVCard, 8)
        self.assertArgSizeInArg(IOBluetooth.OBEXCreateVCard, 8, 9)
        self.assertArgIsIn(IOBluetooth.OBEXCreateVCard, 10)
        self.assertArgSizeInArg(IOBluetooth.OBEXCreateVCard, 10, 11)
        self.assertArgIsIn(IOBluetooth.OBEXCreateVCard, 12)
        self.assertArgSizeInArg(IOBluetooth.OBEXCreateVCard, 12, 13)
        self.assertArgIsIn(IOBluetooth.OBEXCreateVCard, 14)
        self.assertArgSizeInArg(IOBluetooth.OBEXCreateVCard, 14, 15)
        self.assertArgIsIn(IOBluetooth.OBEXCreateVCard, 16)
        self.assertArgSizeInArg(IOBluetooth.OBEXCreateVCard, 16, 17)
        self.assertArgIsIn(IOBluetooth.OBEXCreateVCard, 18)
        self.assertArgSizeInArg(IOBluetooth.OBEXCreateVCard, 18, 19)
        self.assertArgIsIn(IOBluetooth.OBEXCreateVCard, 20)
        self.assertArgSizeInArg(IOBluetooth.OBEXCreateVCard, 20, 21)
        self.assertArgIsIn(IOBluetooth.OBEXCreateVCard, 22)
        self.assertArgSizeInArg(IOBluetooth.OBEXCreateVCard, 22, 23)
        self.assertArgIsIn(IOBluetooth.OBEXCreateVCard, 24)
        self.assertArgSizeInArg(IOBluetooth.OBEXCreateVCard, 24, 25)
        self.assertArgIsIn(IOBluetooth.OBEXCreateVCard, 26)
        self.assertArgSizeInArg(IOBluetooth.OBEXCreateVCard, 26, 27)

        self.assertArgIsIn(IOBluetooth.OBEXCreateVEvent, 0)
        self.assertArgSizeInArg(IOBluetooth.OBEXCreateVEvent, 0, 1)
        self.assertArgIsIn(IOBluetooth.OBEXCreateVEvent, 2)
        self.assertArgSizeInArg(IOBluetooth.OBEXCreateVEvent, 2, 3)
        self.assertArgIsIn(IOBluetooth.OBEXCreateVEvent, 4)
        self.assertArgSizeInArg(IOBluetooth.OBEXCreateVEvent, 4, 5)
        self.assertArgIsIn(IOBluetooth.OBEXCreateVEvent, 6)
        self.assertArgSizeInArg(IOBluetooth.OBEXCreateVEvent, 6, 7)
        self.assertArgIsIn(IOBluetooth.OBEXCreateVEvent, 8)
        self.assertArgSizeInArg(IOBluetooth.OBEXCreateVEvent, 8, 9)
        self.assertArgIsIn(IOBluetooth.OBEXCreateVEvent, 10)
        self.assertArgSizeInArg(IOBluetooth.OBEXCreateVEvent, 10, 11)
        self.assertArgIsIn(IOBluetooth.OBEXCreateVEvent, 12)
        self.assertArgSizeInArg(IOBluetooth.OBEXCreateVEvent, 12, 13)
        self.assertArgIsIn(IOBluetooth.OBEXCreateVEvent, 14)
        self.assertArgSizeInArg(IOBluetooth.OBEXCreateVEvent, 14, 15)
        self.assertArgIsIn(IOBluetooth.OBEXCreateVEvent, 16)
        self.assertArgSizeInArg(IOBluetooth.OBEXCreateVEvent, 16, 17)

        self.assertArgIsIn(IOBluetooth.OBEXGetHeaders, 0)
        self.assertArgSizeInArg(IOBluetooth.OBEXGetHeaders, 0, 1)

        IOBluetooth.OBEXHeadersToBytes
        IOBluetooth.OBEXAddNameHeader
        IOBluetooth.OBEXAddDescriptionHeader
        IOBluetooth.OBEXAddCountHeader
        IOBluetooth.OBEXAddTime4ByteHeader
        IOBluetooth.OBEXAddLengthHeader
        IOBluetooth.OBEXAddTypeHeader

        self.assertArgIsIn(IOBluetooth.OBEXAddTimeISOHeader, 0)
        self.assertArgSizeInArg(IOBluetooth.OBEXAddTimeISOHeader, 0, 1)

        self.assertArgIsIn(IOBluetooth.OBEXAddTargetHeader, 0)
        self.assertArgSizeInArg(IOBluetooth.OBEXAddTargetHeader, 0, 1)

        self.assertArgIsIn(IOBluetooth.OBEXAddHTTPHeader, 0)
        self.assertArgSizeInArg(IOBluetooth.OBEXAddHTTPHeader, 0, 1)

        self.assertArgIsIn(IOBluetooth.OBEXAddBodyHeader, 0)
        self.assertArgSizeInArg(IOBluetooth.OBEXAddBodyHeader, 0, 1)

        self.assertArgIsIn(IOBluetooth.OBEXAddWhoHeader, 0)
        self.assertArgSizeInArg(IOBluetooth.OBEXAddWhoHeader, 0, 1)

        self.assertArgIsIn(IOBluetooth.OBEXAddConnectionIDHeader, 0)
        self.assertArgSizeInArg(IOBluetooth.OBEXAddConnectionIDHeader, 0, 1)

        self.assertArgIsIn(IOBluetooth.OBEXAddApplicationParameterHeader, 0)
        self.assertArgSizeInArg(IOBluetooth.OBEXAddApplicationParameterHeader, 0, 1)

        self.assertArgIsIn(IOBluetooth.OBEXAddByteSequenceHeader, 0)
        self.assertArgSizeInArg(IOBluetooth.OBEXAddByteSequenceHeader, 0, 1)

        self.assertArgIsIn(IOBluetooth.OBEXAddObjectClassHeader, 0)
        self.assertArgSizeInArg(IOBluetooth.OBEXAddObjectClassHeader, 0, 1)

        self.assertArgIsIn(IOBluetooth.OBEXAddAuthorizationChallengeHeader, 0)
        self.assertArgSizeInArg(IOBluetooth.OBEXAddAuthorizationChallengeHeader, 0, 1)

        self.assertArgIsIn(IOBluetooth.OBEXAddAuthorizationResponseHeader, 0)
        self.assertArgSizeInArg(IOBluetooth.OBEXAddAuthorizationResponseHeader, 0, 1)

        self.assertArgIsIn(IOBluetooth.OBEXAddUserDefinedHeader, 0)
        self.assertArgSizeInArg(IOBluetooth.OBEXAddUserDefinedHeader, 0, 1)
