import struct

import CoreText
from Foundation import NSArray
from PyObjCTools.TestSupport import TestCase, NoObjCClass
import objc


class TestCTParagraphStyle(TestCase):
    def test_types(self):
        self.assertIsCFType(CoreText.CTParagraphStyleRef)

    def test_constants(self):
        self.assertEqual(CoreText.kCTLeftTextAlignment, 0)
        self.assertEqual(CoreText.kCTRightTextAlignment, 1)
        self.assertEqual(CoreText.kCTCenterTextAlignment, 2)
        self.assertEqual(CoreText.kCTJustifiedTextAlignment, 3)
        self.assertEqual(CoreText.kCTNaturalTextAlignment, 4)

        self.assertEqual(CoreText.kCTTextAlignmentLeft, 0)
        self.assertEqual(CoreText.kCTTextAlignmentRight, 1)
        self.assertEqual(CoreText.kCTTextAlignmentCenter, 2)
        self.assertEqual(CoreText.kCTTextAlignmentJustified, 3)
        self.assertEqual(CoreText.kCTTextAlignmentNatural, 4)

        self.assertEqual(CoreText.kCTLineBreakByWordWrapping, 0)
        self.assertEqual(CoreText.kCTLineBreakByCharWrapping, 1)
        self.assertEqual(CoreText.kCTLineBreakByClipping, 2)
        self.assertEqual(CoreText.kCTLineBreakByTruncatingHead, 3)
        self.assertEqual(CoreText.kCTLineBreakByTruncatingTail, 4)
        self.assertEqual(CoreText.kCTLineBreakByTruncatingMiddle, 5)

        self.assertEqual(CoreText.kCTWritingDirectionNatural, -1)
        self.assertEqual(CoreText.kCTWritingDirectionLeftToRight, 0)
        self.assertEqual(CoreText.kCTWritingDirectionRightToLeft, 1)

        self.assertEqual(CoreText.kCTParagraphStyleSpecifierAlignment, 0)
        self.assertEqual(CoreText.kCTParagraphStyleSpecifierFirstLineHeadIndent, 1)
        self.assertEqual(CoreText.kCTParagraphStyleSpecifierHeadIndent, 2)
        self.assertEqual(CoreText.kCTParagraphStyleSpecifierTailIndent, 3)
        self.assertEqual(CoreText.kCTParagraphStyleSpecifierTabStops, 4)
        self.assertEqual(CoreText.kCTParagraphStyleSpecifierDefaultTabInterval, 5)
        self.assertEqual(CoreText.kCTParagraphStyleSpecifierLineBreakMode, 6)
        self.assertEqual(CoreText.kCTParagraphStyleSpecifierLineHeightMultiple, 7)
        self.assertEqual(CoreText.kCTParagraphStyleSpecifierMaximumLineHeight, 8)
        self.assertEqual(CoreText.kCTParagraphStyleSpecifierMinimumLineHeight, 9)
        self.assertEqual(CoreText.kCTParagraphStyleSpecifierLineSpacing, 10)
        self.assertEqual(CoreText.kCTParagraphStyleSpecifierParagraphSpacing, 11)
        self.assertEqual(CoreText.kCTParagraphStyleSpecifierParagraphSpacingBefore, 12)
        self.assertEqual(CoreText.kCTParagraphStyleSpecifierBaseWritingDirection, 13)
        self.assertEqual(CoreText.kCTParagraphStyleSpecifierMaximumLineSpacing, 14)
        self.assertEqual(CoreText.kCTParagraphStyleSpecifierMinimumLineSpacing, 15)
        self.assertEqual(CoreText.kCTParagraphStyleSpecifierLineSpacingAdjustment, 16)
        self.assertEqual(CoreText.kCTParagraphStyleSpecifierLineBoundsOptions, 17)

    def test_structs(self):
        v = CoreText.CTParagraphStyleSetting()
        self.assertHasAttr(v, "spec")
        self.assertHasAttr(v, "valueSize")
        self.assertHasAttr(v, "value")
        self.assertPickleRoundTrips(v)

    def test_functions(self):
        v = CoreText.CTParagraphStyleGetTypeID()
        self.assertIsInstance(v, int)

        self.assertResultHasType(
            CoreText.CTParagraphStyleGetValueForSpecifier, objc._C_BOOL
        )

        # Test below is not needed due to manaul wrapper:
        # self.assertResultIsCFRetained(CTParagraphStyleCreate)
        with self.assertRaisesRegex(TypeError, "expected 2 arguments, got 0"):
            CoreText.CTParagraphStyleCreate()

        with self.assertRaisesRegex(TypeError, "'int' object is not iterable"):
            CoreText.CTParagraphStyleCreate(42, 0)

        with self.assertRaisesRegex(
            ValueError, "depythonifying 'long long', got 'str' of 5"
        ):
            CoreText.CTParagraphStyleCreate(None, "hello")

        with self.assertRaisesRegex(
            ValueError, "settings list is 'None', length is not 0"
        ):
            CoreText.CTParagraphStyleCreate(None, 10)

        style = CoreText.CTParagraphStyleCreate(None, 0)
        self.assertIsInstance(style, CoreText.CTParagraphStyleRef)

        self.assertResultIsCFRetained(CoreText.CTParagraphStyleCreateCopy)
        v = CoreText.CTParagraphStyleCreateCopy(style)
        self.assertIsInstance(v, CoreText.CTParagraphStyleRef)

        ok, v = CoreText.CTParagraphStyleGetTabStops(style)
        self.assertTrue(ok)
        self.assertIsInstance(v, NSArray)
        self.assertTrue(len(v))
        self.assertIsInstance(v[0], CoreText.CTTextTabRef)

        with self.assertRaisesRegex(TypeError, "expected 4 arguments, got 0"):
            CoreText.CTParagraphStyleGetValueForSpecifier()

        with self.assertRaisesRegex(TypeError, "Cannot proxy"):
            CoreText.CTParagraphStyleGetValueForSpecifier(
                NoObjCClass(),
                CoreText.kCTParagraphStyleSpecifierAlignment,
                CoreText.sizeof_CTTextAlignment,
                None,
            )

        with self.assertRaisesRegex(
            ValueError, "depythonifying 'unsigned int', got 'str'"
        ):
            CoreText.CTParagraphStyleGetValueForSpecifier(
                style,
                "hello",
                CoreText.sizeof_CTTextAlignment,
                None,
            )

        with self.assertRaisesRegex(
            ValueError, "depythonifying 'unsigned long long', got 'str'"
        ):
            CoreText.CTParagraphStyleGetValueForSpecifier(
                style,
                CoreText.kCTParagraphStyleSpecifierAlignment,
                "hello",
                None,
            )

        with self.assertRaisesRegex(ValueError, "'valueBuffer' must be None"):
            CoreText.CTParagraphStyleGetValueForSpecifier(
                style,
                CoreText.kCTParagraphStyleSpecifierAlignment,
                CoreText.sizeof_CTTextAlignment,
                42,
            )

        ok, v = CoreText.CTParagraphStyleGetValueForSpecifier(
            style,
            CoreText.kCTParagraphStyleSpecifierAlignment,
            CoreText.sizeof_CTTextAlignment,
            None,
        )
        self.assertTrue(ok)
        self.assertIsInstance(v, bytes)
        self.assertEqual(len(v), CoreText.sizeof_CTTextAlignment)

        ok, v = CoreText.CTParagraphStyleGetValueForSpecifier(
            style,
            CoreText.kCTParagraphStyleSpecifierAlignment,
            0,
            None,
        )
        self.assertTrue(ok)
        self.assertIsInstance(v, int)

        ok, v = CoreText.CTParagraphStyleGetValueForSpecifier(
            style,
            CoreText.kCTParagraphStyleSpecifierLineBoundsOptions,
            0,
            None,
        )
        self.assertTrue(ok)
        self.assertIsInstance(v, int)

        ok, v = CoreText.CTParagraphStyleGetValueForSpecifier(
            style,
            CoreText.kCTParagraphStyleSpecifierFirstLineHeadIndent,
            CoreText.sizeof_CGFloat,
            None,
        )
        self.assertTrue(ok)
        self.assertIsInstance(v, bytes)
        self.assertEqual(len(v), CoreText.sizeof_CGFloat)

        ok, v = CoreText.CTParagraphStyleGetValueForSpecifier(
            style,
            CoreText.kCTParagraphStyleSpecifierFirstLineHeadIndent,
            0,
            None,
        )
        self.assertTrue(ok)
        self.assertIsInstance(v, float)

        ok, v = CoreText.CTParagraphStyleGetValueForSpecifier(
            style,
            CoreText.kCTParagraphStyleSpecifierLineBreakMode,
            0,
            None,
        )
        self.assertTrue(ok)
        self.assertIsInstance(v, int)

        ok, v = CoreText.CTParagraphStyleGetValueForSpecifier(
            style,
            CoreText.kCTParagraphStyleSpecifierBaseWritingDirection,
            CoreText.sizeof_CTWritingDirection,
            None,
        )
        self.assertTrue(ok)
        self.assertIsInstance(v, bytes)
        self.assertEqual(len(v), CoreText.sizeof_CTWritingDirection)

        # And now the hard part: create a CoreText.CTParagraphStyle with custom options
        float_pack = "d"
        options = [
            CoreText.CTParagraphStyleSetting(
                spec=CoreText.kCTParagraphStyleSpecifierBaseWritingDirection,
                valueSize=CoreText.sizeof_CTWritingDirection,
                value=chr(CoreText.kCTParagraphStyleSpecifierTailIndent).encode(
                    "latin1"
                ),
            ),
            CoreText.CTParagraphStyleSetting(
                spec=CoreText.kCTParagraphStyleSpecifierFirstLineHeadIndent,
                valueSize=CoreText.sizeof_CGFloat,
                value=struct.pack(float_pack, 10.5),
            ),
            CoreText.CTParagraphStyleSetting(
                spec=CoreText.kCTParagraphStyleSpecifierTabStops,
                valueSize=CoreText.sizeof_id,
                value=NSArray.arrayWithArray_(
                    [
                        CoreText.CTTextTabCreate(
                            CoreText.kCTLeftTextAlignment, 40.0, None
                        ),
                        CoreText.CTTextTabCreate(
                            CoreText.kCTLeftTextAlignment, 80.0, None
                        ),
                    ]
                ),
            ),
        ]
        options.append(
            CoreText.CTParagraphStyleSetting(
                spec=CoreText.kCTParagraphStyleSpecifierBaseWritingDirection,
                valueSize=CoreText.sizeof_CTWritingDirection,
                value=chr(CoreText.kCTWritingDirectionRightToLeft).encode("latin1"),
            )
        )
        with self.assertRaisesRegex(
            ValueError, f"need sequence of at least {len(options) + 5} arguments"
        ):
            CoreText.CTParagraphStyleCreate(options, len(options) + 5)

        with self.assertRaisesRegex(TypeError, "'int' object is not iterable"):
            CoreText.CTParagraphStyleCreate(options + [42], len(options) + 1)
        with self.assertRaisesRegex(ValueError, "settings item has length 4, not 3"):
            CoreText.CTParagraphStyleCreate(options + [(1, 2, 3, 4)], len(options) + 1)
        with self.assertRaisesRegex(
            ValueError, "Multiple kCTParagraphStyleSpecifierTabStops settings"
        ):
            CoreText.CTParagraphStyleCreate(options + [options[-2]], len(options) + 1)
        with self.assertRaisesRegex(
            TypeError, "a bytes-like object is required, not 'int'"
        ):
            # XXX: With some effort the code code automaticly convert values.
            CoreText.CTParagraphStyleCreate(
                options
                + [
                    CoreText.CTParagraphStyleSetting(
                        spec=CoreText.kCTParagraphStyleSpecifierBaseWritingDirection,
                        valueSize=CoreText.sizeof_CTWritingDirection,
                        value=42,
                    )
                ],
                len(options) + 1,
            )
        with self.assertRaisesRegex(ValueError, "Got buffer of 40 bytes, need 1 bytes"):
            CoreText.CTParagraphStyleCreate(
                options
                + [
                    CoreText.CTParagraphStyleSetting(
                        spec=CoreText.kCTParagraphStyleSpecifierBaseWritingDirection,
                        valueSize=CoreText.sizeof_CTWritingDirection,
                        value=b"x" * 40,
                    )
                ],
                len(options) + 1,
            )

        with self.assertRaisesRegex(
            ValueError, "depythonifying 'unsigned int', got 'str'"
        ):
            CoreText.CTParagraphStyleCreate(
                options
                + [
                    CoreText.CTParagraphStyleSetting(
                        spec="hello",
                        valueSize=CoreText.sizeof_CTWritingDirection,
                        value=b"x" * 40,
                    )
                ],
                len(options) + 1,
            )

        with self.assertRaisesRegex(
            ValueError, "depythonifying 'unsigned long long', got 'str'"
        ):
            CoreText.CTParagraphStyleCreate(
                options
                + [
                    CoreText.CTParagraphStyleSetting(
                        spec=CoreText.kCTParagraphStyleSpecifierBaseWritingDirection,
                        valueSize="hello",
                        value=b"x" * 40,
                    )
                ],
                len(options) + 1,
            )

        style = CoreText.CTParagraphStyleCreate(options, len(options))
        self.assertIsInstance(style, CoreText.CTParagraphStyleRef)

        ok, v = CoreText.CTParagraphStyleGetTabStops(style)
        self.assertTrue(ok)
        self.assertIsInstance(v, NSArray)
        self.assertEqual(len(v), 2)

        ok, v = CoreText.CTParagraphStyleGetValueForSpecifier(
            style,
            CoreText.kCTParagraphStyleSpecifierBaseWritingDirection,
            CoreText.sizeof_CTWritingDirection,
            None,
        )
        self.assertTrue(ok)
        self.assertIsInstance(v, bytes)
        self.assertEqual(
            v, chr(CoreText.kCTWritingDirectionRightToLeft).encode("latin1")
        )
        ok, v = CoreText.CTParagraphStyleGetValueForSpecifier(
            style,
            CoreText.kCTParagraphStyleSpecifierBaseWritingDirection,
            0,
            None,
        )
        self.assertTrue(ok)
        self.assertEqual(v, CoreText.kCTWritingDirectionRightToLeft)

        ok, v = CoreText.CTParagraphStyleGetValueForSpecifier(
            style,
            CoreText.kCTParagraphStyleSpecifierFirstLineHeadIndent,
            CoreText.sizeof_CGFloat,
            None,
        )
        self.assertTrue(ok)
        self.assertIsInstance(v, bytes)
        self.assertEqual(v, struct.pack(float_pack, 10.5))

        ok, v = CoreText.CTParagraphStyleGetValueForSpecifier(
            style,
            CoreText.kCTParagraphStyleSpecifierFirstLineHeadIndent,
            0,
            None,
        )
        self.assertTrue(ok)
        self.assertEqual(v, 10.5)

        ok, v = CoreText.CTParagraphStyleGetValueForSpecifier(
            style,
            CoreText.kCTParagraphStyleSpecifierTabStops,
            0,
            None,
        )
        self.assertTrue(ok)
        self.assertIsInstance(v, CoreText.NSArray)
        self.assertNotEqual(len(v), 0)
        for entry in v:
            self.assertIsInstance(entry, CoreText.CTTextTabRef)

        ok, v = CoreText.CTParagraphStyleGetValueForSpecifier(
            style,
            99,
            8,
            None,
        )
        self.assertFalse(ok)

        with self.assertRaisesRegex(
            ValueError, "Cannot automatically determine 'size'"
        ):
            CoreText.CTParagraphStyleGetValueForSpecifier(
                style,
                99,
                0,
                None,
            )
        self.assertFalse(ok)
