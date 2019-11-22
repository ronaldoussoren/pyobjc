from PyObjCTools.TestSupport import *
from CoreText import *


class TestCTFontManagerErrors(TestCase):
    @min_os_level("10.6")
    def testConstants10_6(self):
        self.assertIsInstance(kCTFontManagerErrorDomain, unicode)
        self.assertIsInstance(kCTFontManagerErrorFontURLsKey, unicode)

    def testConstants(self):
        self.assertEqual(kCTFontManagerErrorFileNotFound, 101)
        self.assertEqual(kCTFontManagerErrorInsufficientPermissions, 102)
        self.assertEqual(kCTFontManagerErrorUnrecognizedFormat, 103)
        self.assertEqual(kCTFontManagerErrorInvalidFontData, 104)
        self.assertEqual(kCTFontManagerErrorAlreadyRegistered, 105)
        self.assertEqual(kCTFontManagerErrorExceededResourceLimit, 106)

        self.assertEqual(kCTFontManagerErrorNotRegistered, 201)
        self.assertEqual(kCTFontManagerErrorInUse, 202)
        self.assertEqual(kCTFontManagerErrorSystemRequired, 203)
        self.assertEqual(kCTFontManagerErrorRegistrationFailed, 301)
        self.assertEqual(kCTFontManagerErrorMissingEntitlement, 302)
        self.assertEqual(kCTFontManagerErrorInsufficientInfo, 303)
        self.assertEqual(kCTFontManagerErrorCancelledByUser, 304)
        self.assertEqual(kCTFontManagerErrorDuplicatedName, 305)
        self.assertEqual(kCTFontManagerErrorInvalidFilePath, 306)


if __name__ == "__main__":
    main()
