
from PyObjCTools.TestSupport import *
from CoreText import *

class TestCTGlyphInfo (TestCase):
    def testTypes(self):
        self.failUnlessIsInstance(CTGlyphInfoRef, objc.objc_class)

    def testConstants(self):
        self.failUnlessEqual(kCTIdentityMappingCharacterCollection, 0)
        self.failUnlessEqual(kCTAdobeCNS1CharacterCollection, 1)
        self.failUnlessEqual(kCTAdobeGB1CharacterCollection, 2)
        self.failUnlessEqual(kCTAdobeJapan1CharacterCollection, 3)
        self.failUnlessEqual(kCTAdobeJapan2CharacterCollection, 4)
        self.failUnlessEqual(kCTAdobeKorea1CharacterCollection, 5)


    def testFunctions(self):
        v = CTGlyphInfoGetTypeID()
        self.failUnlessIsInstance(v, (int, long))

        font = CTFontCreateWithName(u"Optima Bold", 14, None)
        self.failUnless(isinstance(font, CTFontRef))

        self.failUnlessResultIsCFRetained(CTGlyphInfoCreateWithGlyphName)
        info = v = CTGlyphInfoCreateWithGlyphName(
                u"copyright", 
                font, 
                u"(c)")
        self.failUnlessIsInstance(v, CTGlyphInfoRef)

        self.failUnlessResultIsCFRetained(CTGlyphInfoCreateWithGlyph)
        v = CTGlyphInfoCreateWithGlyph(3254, font, "(c)")
        self.failUnlessIsInstance(v, CTGlyphInfoRef)

        self.failUnlessResultIsCFRetained(CTGlyphInfoCreateWithCharacterIdentifier)
        v = CTGlyphInfoCreateWithCharacterIdentifier(3254, kCTIdentityMappingCharacterCollection, "(c)")
        self.failUnlessIsInstance(v, CTGlyphInfoRef)

        v = CTGlyphInfoGetGlyphName(info)
        self.failUnlessIsInstance(v, unicode)

        v = CTGlyphInfoGetCharacterIdentifier(info)
        self.failUnlessIsInstance(v, (int, long))

        self.failIfResultIsCFRetained(CTGlyphInfoGetCharacterCollection)
        v = CTGlyphInfoGetCharacterCollection(info)
        self.failUnlessIsInstance(v, (int, long))


if __name__ == "__main__":
    main()
