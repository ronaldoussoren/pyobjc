from PyObjCTools.TestSupport import *
from CoreText import *

class TestCTFontManagerErrors (TestCase):
    @min_os_level("10.6")
    def testConstants10_6(self):
        self.assertIsInstance(kCTFontManagerErrorDomain, unicode)
        self.assertIsInstance(kCTFontManagerErrorFontURLsKey, unicode)

        self.assertEqual(kCTFontManagerErrorFileNotFound, 101)
        self.assertEqual(kCTFontManagerErrorInsufficientPermissions, 102)
        self.assertEqual(kCTFontManagerErrorUnrecognizedFormat, 103)
        self.assertEqual(kCTFontManagerErrorInvalidFontData, 104)
        self.assertEqual(kCTFontManagerErrorAlreadyRegistered, 105)

        self.assertEqual(kCTFontManagerErrorNotRegistered, 201)
        self.assertEqual(kCTFontManagerErrorInUse, 202)
        self.assertEqual(kCTFontManagerErrorSystemRequired, 203)


if __name__ == "__main__":
    main()
