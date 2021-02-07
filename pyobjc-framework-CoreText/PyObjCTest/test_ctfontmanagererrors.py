import CoreText
from PyObjCTools.TestSupport import TestCase, min_os_level


class TestCTFontManagerErrors(TestCase):
    @min_os_level("10.6")
    def testConstants10_6(self):
        self.assertIsInstance(CoreText.kCTFontManagerErrorDomain, str)
        self.assertIsInstance(CoreText.kCTFontManagerErrorFontURLsKey, str)

    def testConstants(self):
        self.assertEqual(CoreText.kCTFontManagerErrorFileNotFound, 101)
        self.assertEqual(CoreText.kCTFontManagerErrorInsufficientPermissions, 102)
        self.assertEqual(CoreText.kCTFontManagerErrorUnrecognizedFormat, 103)
        self.assertEqual(CoreText.kCTFontManagerErrorInvalidFontData, 104)
        self.assertEqual(CoreText.kCTFontManagerErrorAlreadyRegistered, 105)
        self.assertEqual(CoreText.kCTFontManagerErrorExceededResourceLimit, 106)
        self.assertEqual(CoreText.kCTFontManagerErrorAssetNotFound, 107)

        self.assertEqual(CoreText.kCTFontManagerErrorNotRegistered, 201)
        self.assertEqual(CoreText.kCTFontManagerErrorInUse, 202)
        self.assertEqual(CoreText.kCTFontManagerErrorSystemRequired, 203)
        self.assertEqual(CoreText.kCTFontManagerErrorRegistrationFailed, 301)
        self.assertEqual(CoreText.kCTFontManagerErrorMissingEntitlement, 302)
        self.assertEqual(CoreText.kCTFontManagerErrorInsufficientInfo, 303)
        self.assertEqual(CoreText.kCTFontManagerErrorCancelledByUser, 304)
        self.assertEqual(CoreText.kCTFontManagerErrorDuplicatedName, 305)
        self.assertEqual(CoreText.kCTFontManagerErrorInvalidFilePath, 306)
        self.assertEqual(CoreText.kCTFontManagerErrorUnsupportedScope, 307)
