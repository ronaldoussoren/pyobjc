import AppKit
from PyObjCTools.TestSupport import TestCase, min_os_level, min_sdk_level


class TestNSTextContent(TestCase):
    def test_typed_enum(self):
        self.assertIsTypedEnum(AppKit.NSTextContentType, str)

    @min_os_level("11.0")
    def test_constants11_0(self):
        self.assertIsInstance(AppKit.NSTextContentTypeUsername, str)
        self.assertIsInstance(AppKit.NSTextContentTypePassword, str)
        self.assertIsInstance(AppKit.NSTextContentTypeOneTimeCode, str)

    @min_os_level("14.0")
    def test_constants14_0(self):
        self.assertIsInstance(AppKit.NSTextContentTypeNewPassword, str)
        self.assertIsInstance(AppKit.NSTextContentTypeName, str)
        self.assertIsInstance(AppKit.NSTextContentTypeNamePrefix, str)
        self.assertIsInstance(AppKit.NSTextContentTypeGivenName, str)
        self.assertIsInstance(AppKit.NSTextContentTypeMiddleName, str)
        self.assertIsInstance(AppKit.NSTextContentTypeFamilyName, str)
        self.assertIsInstance(AppKit.NSTextContentTypeNameSuffix, str)
        self.assertIsInstance(AppKit.NSTextContentTypeNickname, str)
        self.assertIsInstance(AppKit.NSTextContentTypeJobTitle, str)
        self.assertIsInstance(AppKit.NSTextContentTypeOrganizationName, str)
        self.assertIsInstance(AppKit.NSTextContentTypeLocation, str)
        self.assertIsInstance(AppKit.NSTextContentTypeFullStreetAddress, str)
        self.assertIsInstance(AppKit.NSTextContentTypeStreetAddressLine1, str)
        self.assertIsInstance(AppKit.NSTextContentTypeStreetAddressLine2, str)
        self.assertIsInstance(AppKit.NSTextContentTypeAddressCity, str)
        self.assertIsInstance(AppKit.NSTextContentTypeAddressState, str)
        self.assertIsInstance(AppKit.NSTextContentTypeAddressCityAndState, str)
        self.assertIsInstance(AppKit.NSTextContentTypeSublocality, str)
        self.assertIsInstance(AppKit.NSTextContentTypeCountryName, str)
        self.assertIsInstance(AppKit.NSTextContentTypePostalCode, str)
        self.assertIsInstance(AppKit.NSTextContentTypeTelephoneNumber, str)
        self.assertIsInstance(AppKit.NSTextContentTypeEmailAddress, str)
        self.assertIsInstance(AppKit.NSTextContentTypeURL, str)
        self.assertIsInstance(AppKit.NSTextContentTypeCreditCardNumber, str)
        self.assertIsInstance(AppKit.NSTextContentTypeCreditCardName, str)
        self.assertIsInstance(AppKit.NSTextContentTypeCreditCardGivenName, str)
        self.assertIsInstance(AppKit.NSTextContentTypeCreditCardMiddleName, str)
        self.assertIsInstance(AppKit.NSTextContentTypeCreditCardFamilyName, str)
        self.assertIsInstance(AppKit.NSTextContentTypeCreditCardSecurityCode, str)
        self.assertIsInstance(AppKit.NSTextContentTypeCreditCardExpiration, str)
        self.assertIsInstance(AppKit.NSTextContentTypeCreditCardExpirationMonth, str)
        self.assertIsInstance(AppKit.NSTextContentTypeCreditCardExpirationYear, str)
        self.assertIsInstance(AppKit.NSTextContentTypeCreditCardType, str)
        self.assertIsInstance(AppKit.NSTextContentTypeShipmentTrackingNumber, str)
        self.assertIsInstance(AppKit.NSTextContentTypeFlightNumber, str)
        self.assertIsInstance(AppKit.NSTextContentTypeDateTime, str)
        self.assertIsInstance(AppKit.NSTextContentTypeBirthdate, str)
        self.assertIsInstance(AppKit.NSTextContentTypeBirthdateDay, str)
        self.assertIsInstance(AppKit.NSTextContentTypeBirthdateMonth, str)
        self.assertIsInstance(AppKit.NSTextContentTypeBirthdateYear, str)

    @min_sdk_level("11.0")
    def test_protocols(self):
        self.assertProtocolExists("NSTextContent")
