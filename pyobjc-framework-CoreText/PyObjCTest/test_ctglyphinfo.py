
from PyObjCTools.TestSupport import *
from CoreText import *

try:
    unicode
except NameError:
    unicode = str

try:
    long
except NameError:
    long = int

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

        font = CTFontCreateWithName(b"Optima Bold".decode('latin1'), 14, None)
        self.assertIsInstance(font, CTFontRef)

        self.assertResultIsCFRetained(CTGlyphInfoCreateWithGlyphName)
        info = v = CTGlyphInfoCreateWithGlyphName(
                b"copyright".decode('latin1'),
                font,
                b"(c)".decode('latin1'))
        self.assertIsInstance(v, CTGlyphInfoRef)

        self.assertResultIsCFRetained(CTGlyphInfoCreateWithGlyph)
        v = CTGlyphInfoCreateWithGlyph(3254, font, "(c)")
        self.assertIsInstance(v, CTGlyphInfoRef)

        self.assertResultIsCFRetained(CTGlyphInfoCreateWithCharacterIdentifier)

        for collection in (kCTIdentityMappingCharacterCollection, kCTAdobeCNS1CharacterCollection,
                kCTAdobeGB1CharacterCollection, kCTAdobeJapan1CharacterCollection,
                kCTAdobeJapan2CharacterCollection, kCTAdobeKorea1CharacterCollection):
            v = CTGlyphInfoCreateWithCharacterIdentifier(3254, collection, "(c)")
            if v is not None:
                break
        self.assertIsInstance(v, CTGlyphInfoRef)

        v = CTGlyphInfoGetGlyphName(info)
        self.assertIsInstance(v, unicode)

        v = CTGlyphInfoGetCharacterIdentifier(info)
        self.assertIsInstance(v, (int, long))

        self.assertResultIsNotCFRetained(CTGlyphInfoGetCharacterCollection)
        v = CTGlyphInfoGetCharacterCollection(info)
        self.assertIsInstance(v, (int, long))


if __name__ == "__main__":
    main()
