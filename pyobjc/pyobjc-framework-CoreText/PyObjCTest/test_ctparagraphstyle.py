
from PyObjCTools.TestSupport import *
from CoreText import *
from Foundation import NSArray
import struct, sys

class TestCTParagraphStyle (TestCase):
    def testTypes(self):
        self.failUnlessIsCFType(CTParagraphStyleRef)

    def testConstants(self):
        self.failUnlessEqual(kCTLeftTextAlignment, 0)
        self.failUnlessEqual(kCTRightTextAlignment, 1)
        self.failUnlessEqual(kCTCenterTextAlignment, 2)
        self.failUnlessEqual(kCTJustifiedTextAlignment, 3)
        self.failUnlessEqual(kCTNaturalTextAlignment, 4)

        self.failUnlessEqual(kCTLineBreakByWordWrapping, 0)
        self.failUnlessEqual(kCTLineBreakByCharWrapping, 1)
        self.failUnlessEqual(kCTLineBreakByClipping, 2)
        self.failUnlessEqual(kCTLineBreakByTruncatingHead, 3)
        self.failUnlessEqual(kCTLineBreakByTruncatingTail, 4)
        self.failUnlessEqual(kCTLineBreakByTruncatingMiddle, 5)

        self.failUnlessEqual(kCTWritingDirectionNatural, -1)
        self.failUnlessEqual(kCTWritingDirectionLeftToRight, 0)
        self.failUnlessEqual(kCTWritingDirectionRightToLeft, 1)
        self.failUnlessEqual(kCTParagraphStyleSpecifierAlignment, 0)
        self.failUnlessEqual(kCTParagraphStyleSpecifierFirstLineHeadIndent, 1)
        self.failUnlessEqual(kCTParagraphStyleSpecifierHeadIndent, 2)
        self.failUnlessEqual(kCTParagraphStyleSpecifierTailIndent, 3)
        self.failUnlessEqual(kCTParagraphStyleSpecifierTabStops, 4)
        self.failUnlessEqual(kCTParagraphStyleSpecifierDefaultTabInterval, 5)
        self.failUnlessEqual(kCTParagraphStyleSpecifierLineBreakMode, 6)
        self.failUnlessEqual(kCTParagraphStyleSpecifierLineHeightMultiple, 7)
        self.failUnlessEqual(kCTParagraphStyleSpecifierMaximumLineHeight, 8)
        self.failUnlessEqual(kCTParagraphStyleSpecifierMinimumLineHeight, 9)
        self.failUnlessEqual(kCTParagraphStyleSpecifierLineSpacing, 10)
        self.failUnlessEqual(kCTParagraphStyleSpecifierParagraphSpacing, 11)
        self.failUnlessEqual(kCTParagraphStyleSpecifierParagraphSpacingBefore, 12)
        self.failUnlessEqual(kCTParagraphStyleSpecifierBaseWritingDirection, 13)
        self.failUnlessEqual(kCTParagraphStyleSpecifierCount, 14)

    def testStructs(self):
        v = CTParagraphStyleSetting()
        self.failUnless(hasattr(v, 'spec'))
        self.failUnless(hasattr(v, 'valueSize'))
        self.failUnless(hasattr(v, 'value'))

    def testFunctions(self):
        v = CTParagraphStyleGetTypeID()
        self.failUnlessIsInstance(v, (int, long))
        self.failUnlessResultHasType(CTParagraphStyleGetValueForSpecifier, objc._C_BOOL)

        # Test below is not needed due to manaul wrapper:
        #self.failUnlessResultIsCFRetained(CTParagraphStyleCreate)
        style = CTParagraphStyleCreate(None, 0)
        self.failUnlessIsInstance(style, CTParagraphStyleRef);

        self.failUnlessResultIsCFRetained(CTParagraphStyleCreateCopy)
        v = CTParagraphStyleCreateCopy(style)
        self.failUnlessIsInstance(v, CTParagraphStyleRef);

        ok, v = CTParagraphStyleGetTabStops(style)
        self.failUnless(ok)
        self.failUnlessIsInstance(v, CFArrayRef)
        self.failUnless(len(v))
        self.failUnlessIsInstance(v[0], CTTextTabRef)

        ok, v = CTParagraphStyleGetValueForSpecifier(style,
                kCTParagraphStyleSpecifierAlignment, sizeof_CTTextAlignment, None)
        self.failUnless(ok)
        self.failUnlessIsInstance(v, str)
        self.failUnlessEqual(len(v), sizeof_CTTextAlignment)

        ok, v = CTParagraphStyleGetValueForSpecifier(style,
                kCTParagraphStyleSpecifierFirstLineHeadIndent, sizeof_CGFloat, None)
        self.failUnless(ok)
        self.failUnlessIsInstance(v, str)
        self.failUnlessEqual(len(v), sizeof_CGFloat)

        ok, v = CTParagraphStyleGetValueForSpecifier(style,
                kCTParagraphStyleSpecifierLineBreakMode, sizeof_CTLineBreakMode, None)
        self.failUnless(ok)
        self.failUnlessIsInstance(v, str)
        self.failUnlessEqual(len(v), sizeof_CTLineBreakMode)

        ok, v = CTParagraphStyleGetValueForSpecifier(style,
                kCTParagraphStyleSpecifierBaseWritingDirection, sizeof_CTWritingDirection, None)
        self.failUnless(ok)
        self.failUnlessIsInstance(v, str)
        self.failUnlessEqual(len(v), sizeof_CTWritingDirection)

        # And now the hard part: create a CTParagraphStyle with custom options
        if sys.maxint > 2**32:
            float_pack = "d"
        else:
            float_pack = "f"
        options = [
                CTParagraphStyleSetting(
                    spec=kCTParagraphStyleSpecifierBaseWritingDirection,
                    valueSize=sizeof_CTWritingDirection,
                    value=chr(kCTParagraphStyleSpecifierTailIndent)),
                CTParagraphStyleSetting(
                    spec=kCTParagraphStyleSpecifierFirstLineHeadIndent,
                    valueSize=sizeof_CGFloat,
                    value=struct.pack(float_pack, 10.5)),
                CTParagraphStyleSetting(
                    spec=kCTParagraphStyleSpecifierTabStops,
                    valueSize=sizeof_id,
                    value=NSArray.arrayWithArray_([
                        CTTextTabCreate(kCTLeftTextAlignment, 40.0, None),
                        CTTextTabCreate(kCTLeftTextAlignment, 80.0, None),
                    ])),
        ]
        options.append(
                CTParagraphStyleSetting(
                    spec=kCTParagraphStyleSpecifierBaseWritingDirection,
                    valueSize=sizeof_CTWritingDirection,
                    value=chr(kCTWritingDirectionRightToLeft)),
        )
        style = CTParagraphStyleCreate(options, len(options))
        self.failUnlessIsInstance(style, CTParagraphStyleRef);

        ok, v = CTParagraphStyleGetTabStops(style)
        self.failUnless(ok)
        self.failUnlessIsInstance(v, CFArrayRef)
        self.failUnlessEqual(len(v), 2)

        ok, v = CTParagraphStyleGetValueForSpecifier(style,
                kCTParagraphStyleSpecifierBaseWritingDirection, sizeof_CTWritingDirection, None)
        self.failUnless(ok)
        self.failUnlessIsInstance(v, str)
        self.failUnlessEqual(v, chr(kCTWritingDirectionRightToLeft))

        ok, v = CTParagraphStyleGetValueForSpecifier(style,
                kCTParagraphStyleSpecifierFirstLineHeadIndent, sizeof_CGFloat, None)
        self.failUnless(ok)
        self.failUnlessIsInstance(v, str)
        self.failUnlessEqual(v, struct.pack(float_pack, 10.5))

if __name__ == "__main__":
    main()

