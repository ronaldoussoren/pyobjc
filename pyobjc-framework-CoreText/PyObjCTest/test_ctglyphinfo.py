import CoreText
from PyObjCTools.TestSupport import TestCase, min_os_level
import objc


class TestCTGlyphInfo(TestCase):
    def testTypes(self):
        self.assertIsInstance(CoreText.CTGlyphInfoRef, objc.objc_class)

    def testConstants(self):
        self.assertEqual(CoreText.kCTIdentityMappingCharacterCollection, 0)
        self.assertEqual(CoreText.kCTAdobeCNS1CharacterCollection, 1)
        self.assertEqual(CoreText.kCTAdobeGB1CharacterCollection, 2)
        self.assertEqual(CoreText.kCTAdobeJapan1CharacterCollection, 3)
        self.assertEqual(CoreText.kCTAdobeJapan2CharacterCollection, 4)
        self.assertEqual(CoreText.kCTAdobeKorea1CharacterCollection, 5)

        self.assertEqual(CoreText.kCTCharacterCollectionIdentityMapping, 0)
        self.assertEqual(CoreText.kCTCharacterCollectionAdobeCNS1, 1)
        self.assertEqual(CoreText.kCTCharacterCollectionAdobeGB1, 2)
        self.assertEqual(CoreText.kCTCharacterCollectionAdobeJapan1, 3)
        self.assertEqual(CoreText.kCTCharacterCollectionAdobeJapan2, 4)
        self.assertEqual(CoreText.kCTCharacterCollectionAdobeKorea1, 5)

    def testFunctions(self):
        v = CoreText.CTGlyphInfoGetTypeID()
        self.assertIsInstance(v, int)

        font = CoreText.CTFontCreateWithName("Optima Bold", 14, None)
        self.assertIsInstance(font, CoreText.CTFontRef)

        self.assertResultIsCFRetained(CoreText.CTGlyphInfoCreateWithGlyphName)
        info = v = CoreText.CTGlyphInfoCreateWithGlyphName("copyright", font, "(c)")
        self.assertIsInstance(v, CoreText.CTGlyphInfoRef)

        self.assertResultIsCFRetained(CoreText.CTGlyphInfoCreateWithGlyph)
        # v = CTGlyphInfoCreateWithGlyph(3254, font, "(c)")
        # self.assertIsInstance(v, CTGlyphInfoRef)

        self.assertResultIsCFRetained(CoreText.CTGlyphInfoCreateWithCharacterIdentifier)

        for collection in (
            CoreText.kCTIdentityMappingCharacterCollection,
            CoreText.kCTAdobeCNS1CharacterCollection,
            CoreText.kCTAdobeGB1CharacterCollection,
            CoreText.kCTAdobeJapan1CharacterCollection,
            CoreText.kCTAdobeJapan2CharacterCollection,
            CoreText.kCTAdobeKorea1CharacterCollection,
        ):
            v = CoreText.CTGlyphInfoCreateWithCharacterIdentifier(
                3254, collection, "(c)"
            )
            if v is not None:
                break
        self.assertIsInstance(v, CoreText.CTGlyphInfoRef)

        v = CoreText.CTGlyphInfoGetGlyphName(info)
        self.assertIsInstance(v, str)

        v = CoreText.CTGlyphInfoGetCharacterIdentifier(info)
        self.assertIsInstance(v, int)

        self.assertResultIsNotCFRetained(CoreText.CTGlyphInfoGetCharacterCollection)
        v = CoreText.CTGlyphInfoGetCharacterCollection(info)
        self.assertIsInstance(v, int)

    @min_os_level("10.15")
    def testFunctions10_15(self):
        CoreText.CTGlyphInfoGetGlyph
