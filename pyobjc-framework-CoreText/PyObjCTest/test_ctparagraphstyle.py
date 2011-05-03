
from PyObjCTools.TestSupport import *
from CoreText import *
from Foundation import NSArray
import struct, sys

class TestCTParagraphStyle (TestCase):
    def testTypes(self):
        self.assertIsCFType(CTParagraphStyleRef)

    def testConstants(self):
        self.assertEqual(kCTLeftTextAlignment, 0)
        self.assertEqual(kCTRightTextAlignment, 1)
        self.assertEqual(kCTCenterTextAlignment, 2)
        self.assertEqual(kCTJustifiedTextAlignment, 3)
        self.assertEqual(kCTNaturalTextAlignment, 4)

        self.assertEqual(kCTLineBreakByWordWrapping, 0)
        self.assertEqual(kCTLineBreakByCharWrapping, 1)
        self.assertEqual(kCTLineBreakByClipping, 2)
        self.assertEqual(kCTLineBreakByTruncatingHead, 3)
        self.assertEqual(kCTLineBreakByTruncatingTail, 4)
        self.assertEqual(kCTLineBreakByTruncatingMiddle, 5)

        self.assertEqual(kCTWritingDirectionNatural, -1)
        self.assertEqual(kCTWritingDirectionLeftToRight, 0)
        self.assertEqual(kCTWritingDirectionRightToLeft, 1)
        self.assertEqual(kCTParagraphStyleSpecifierAlignment, 0)
        self.assertEqual(kCTParagraphStyleSpecifierFirstLineHeadIndent, 1)
        self.assertEqual(kCTParagraphStyleSpecifierHeadIndent, 2)
        self.assertEqual(kCTParagraphStyleSpecifierTailIndent, 3)
        self.assertEqual(kCTParagraphStyleSpecifierTabStops, 4)
        self.assertEqual(kCTParagraphStyleSpecifierDefaultTabInterval, 5)
        self.assertEqual(kCTParagraphStyleSpecifierLineBreakMode, 6)
        self.assertEqual(kCTParagraphStyleSpecifierLineHeightMultiple, 7)
        self.assertEqual(kCTParagraphStyleSpecifierMaximumLineHeight, 8)
        self.assertEqual(kCTParagraphStyleSpecifierMinimumLineHeight, 9)
        self.assertEqual(kCTParagraphStyleSpecifierLineSpacing, 10)
        self.assertEqual(kCTParagraphStyleSpecifierParagraphSpacing, 11)
        self.assertEqual(kCTParagraphStyleSpecifierParagraphSpacingBefore, 12)
        self.assertEqual(kCTParagraphStyleSpecifierBaseWritingDirection, 13)
        self.assertEqual(kCTParagraphStyleSpecifierCount, 14)

    def testStructs(self):
        v = CTParagraphStyleSetting()
        self.assertHasAttr(v, 'spec')
        self.assertHasAttr(v, 'valueSize')
        self.assertHasAttr(v, 'value')

    def testFunctions(self):
        v = CTParagraphStyleGetTypeID()
        self.assertIsInstance(v, (int, long))
        self.assertResultHasType(CTParagraphStyleGetValueForSpecifier, objc._C_BOOL)

        # Test below is not needed due to manaul wrapper:
        #self.assertResultIsCFRetained(CTParagraphStyleCreate)
        style = CTParagraphStyleCreate(None, 0)
        self.assertIsInstance(style, CTParagraphStyleRef);

        self.assertResultIsCFRetained(CTParagraphStyleCreateCopy)
        v = CTParagraphStyleCreateCopy(style)
        self.assertIsInstance(v, CTParagraphStyleRef);

        ok, v = CTParagraphStyleGetTabStops(style)
        self.assertTrue(ok)
        self.assertIsInstance(v, CFArrayRef)
        self.assertTrue(len(v))
        self.assertIsInstance(v[0], CTTextTabRef)

        ok, v = CTParagraphStyleGetValueForSpecifier(style,
                kCTParagraphStyleSpecifierAlignment, sizeof_CTTextAlignment, None)
        self.assertTrue(ok)
        self.assertIsInstance(v, bytes)
        self.assertEqual(len(v), sizeof_CTTextAlignment)

        ok, v = CTParagraphStyleGetValueForSpecifier(style,
                kCTParagraphStyleSpecifierFirstLineHeadIndent, sizeof_CGFloat, None)
        self.assertTrue(ok)
        self.assertIsInstance(v, bytes)
        self.assertEqual(len(v), sizeof_CGFloat)

        ok, v = CTParagraphStyleGetValueForSpecifier(style,
                kCTParagraphStyleSpecifierLineBreakMode, sizeof_CTLineBreakMode, None)
        self.assertTrue(ok)
        self.assertIsInstance(v, bytes)
        self.assertEqual(len(v), sizeof_CTLineBreakMode)

        ok, v = CTParagraphStyleGetValueForSpecifier(style,
                kCTParagraphStyleSpecifierBaseWritingDirection, sizeof_CTWritingDirection, None)
        self.assertTrue(ok)
        self.assertIsInstance(v, bytes)
        self.assertEqual(len(v), sizeof_CTWritingDirection)

        # And now the hard part: create a CTParagraphStyle with custom options
        if sys.maxint > 2**32:
            float_pack = "d"
        else:
            float_pack = "f"
        options = [
                CTParagraphStyleSetting(
                    spec=kCTParagraphStyleSpecifierBaseWritingDirection,
                    valueSize=sizeof_CTWritingDirection,
                    value=chr(kCTParagraphStyleSpecifierTailIndent).encode('latin1')),
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
        self.assertIsInstance(style, CTParagraphStyleRef);

        ok, v = CTParagraphStyleGetTabStops(style)
        self.assertTrue(ok)
        self.assertIsInstance(v, CFArrayRef)
        self.assertEqual(len(v), 2)

        ok, v = CTParagraphStyleGetValueForSpecifier(style,
                kCTParagraphStyleSpecifierBaseWritingDirection, sizeof_CTWritingDirection, None)
        self.assertTrue(ok)
        self.assertIsInstance(v, str)
        self.assertEqual(v, chr(kCTWritingDirectionRightToLeft))

        ok, v = CTParagraphStyleGetValueForSpecifier(style,
                kCTParagraphStyleSpecifierFirstLineHeadIndent, sizeof_CGFloat, None)
        self.assertTrue(ok)
        self.assertIsInstance(v, str)
        self.assertEqual(v, struct.pack(float_pack, 10.5))

if __name__ == "__main__":
    main()
