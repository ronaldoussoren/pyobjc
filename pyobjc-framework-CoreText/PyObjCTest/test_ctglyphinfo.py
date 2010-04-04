
from PyObjCTools.TestSupport import *
from CoreText import *

class TestCTGlyphInfo (TestCase):
    def testTypes(self):
        self.assertIsInstance(CTGlyphInfoRef, objc.objc_class)

    def testConstants(self):
        self.assertEqual(kCTIdentityMappingCharacterCollection, 0)
        self.assertEqual(kCTAdobeCNS1CharacterCollection, 1)
        self.assertEqual(kCTAdobeGB1CharacterCollection, 2)
        self.assertEqual(kCTAdobeJapan1CharacterCollection, 3)
        self.assertEqual(kCTAdobeJapan2CharacterCollection, 4)
        self.assertEqual(kCTAdobeKorea1CharacterCollection, 5)


    def testFunctions(self):
        v = CTGlyphInfoGetTypeID()
        self.assertIsInstance(v, (int, long))

        font = CTFontCreateWithName(u"Optima Bold", 14, None)
        self.assertIsInstance(font, CTFontRef)

        self.assertResultIsCFRetained(CTGlyphInfoCreateWithGlyphName)
        info = v = CTGlyphInfoCreateWithGlyphName(
                u"copyright",
                font,
                u"(c)")
        self.assertIsInstance(v, CTGlyphInfoRef)

        self.assertResultIsCFRetained(CTGlyphInfoCreateWithGlyph)
        v = CTGlyphInfoCreateWithGlyph(3254, font, "(c)")
        self.assertIsInstance(v, CTGlyphInfoRef)

        self.assertResultIsCFRetained(CTGlyphInfoCreateWithCharacterIdentifier)
        v = CTGlyphInfoCreateWithCharacterIdentifier(3254, kCTIdentityMappingCharacterCollection, "(c)")
        self.assertIsInstance(v, CTGlyphInfoRef)

        v = CTGlyphInfoGetGlyphName(info)
        self.assertIsInstance(v, unicode)

        v = CTGlyphInfoGetCharacterIdentifier(info)
        self.assertIsInstance(v, (int, long))

        self.failIfResultIsCFRetained(CTGlyphInfoGetCharacterCollection)
        v = CTGlyphInfoGetCharacterCollection(info)
        self.assertIsInstance(v, (int, long))


if __name__ == "__main__":
    main()
