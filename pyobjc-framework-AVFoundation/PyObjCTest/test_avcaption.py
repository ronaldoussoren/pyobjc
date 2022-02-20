import AVFoundation
from PyObjCTools.TestSupport import TestCase, min_os_level


class TestAVCaption(TestCase):
    def test_enum_types(self):
        self.assertIsEnumType(AVFoundation.AVCaptionAnimation)
        self.assertIsEnumType(AVFoundation.AVCaptionDecoration)
        self.assertIsEnumType(AVFoundation.AVCaptionFontStyle)
        self.assertIsEnumType(AVFoundation.AVCaptionFontWeight)
        self.assertIsEnumType(AVFoundation.AVCaptionRegionDisplayAlignment)
        self.assertIsEnumType(AVFoundation.AVCaptionRegionScroll)
        self.assertIsEnumType(AVFoundation.AVCaptionRegionWritingMode)
        self.assertIsEnumType(AVFoundation.AVCaptionRubyAlignment)
        self.assertIsEnumType(AVFoundation.AVCaptionRubyPosition)
        self.assertIsEnumType(AVFoundation.AVCaptionTextAlignment)
        self.assertIsEnumType(AVFoundation.AVCaptionTextCombine)
        self.assertIsEnumType(AVFoundation.AVCaptionUnitsType)

    def test_structs(self):
        v = AVFoundation.AVCaptionDimension()
        self.assertIsInstance(v.value, float)
        self.assertIsInstance(v.units, int)
        self.assertPickleRoundTrips(v)

        v = AVFoundation.AVCaptionPoint()
        self.assertIsInstance(v.x, AVFoundation.AVCaptionDimension)
        self.assertIsInstance(v.y, AVFoundation.AVCaptionDimension)
        self.assertPickleRoundTrips(v)

        v = AVFoundation.AVCaptionSize()
        self.assertIsInstance(v.width, AVFoundation.AVCaptionDimension)
        self.assertIsInstance(v.height, AVFoundation.AVCaptionDimension)
        self.assertPickleRoundTrips(v)

    def test_constants(self):
        self.assertEqual(AVFoundation.AVCaptionUnitsTypeUnspecified, 0)
        self.assertEqual(AVFoundation.AVCaptionUnitsTypeCells, 1)
        self.assertEqual(AVFoundation.AVCaptionUnitsTypePercent, 2)

        self.assertEqual(AVFoundation.AVCaptionRegionDisplayAlignmentBefore, 0)
        self.assertEqual(AVFoundation.AVCaptionRegionDisplayAlignmentCenter, 1)
        self.assertEqual(AVFoundation.AVCaptionRegionDisplayAlignmentAfter, 2)

        self.assertEqual(
            AVFoundation.AVCaptionRegionWritingModeLeftToRightAndTopToBottom, 0
        )
        self.assertEqual(
            AVFoundation.AVCaptionRegionWritingModeTopToBottomAndRightToLeft, 2
        )

        self.assertEqual(AVFoundation.AVCaptionRegionScrollNone, 0)
        self.assertEqual(AVFoundation.AVCaptionRegionScrollRollUp, 1)

        self.assertEqual(AVFoundation.AVCaptionAnimationNone, 0)
        self.assertEqual(AVFoundation.AVCaptionAnimationCharacterReveal, 1)

        self.assertEqual(AVFoundation.AVCaptionFontWeightUnknown, 0)
        self.assertEqual(AVFoundation.AVCaptionFontWeightNormal, 1)
        self.assertEqual(AVFoundation.AVCaptionFontWeightBold, 2)

        self.assertEqual(AVFoundation.AVCaptionFontStyleUnknown, 0)
        self.assertEqual(AVFoundation.AVCaptionFontStyleNormal, 1)
        self.assertEqual(AVFoundation.AVCaptionFontStyleItalic, 2)

        self.assertEqual(AVFoundation.AVCaptionDecorationNone, 0)
        self.assertEqual(AVFoundation.AVCaptionDecorationUnderline, 1 << 0)
        self.assertEqual(AVFoundation.AVCaptionDecorationLineThrough, 1 << 1)
        self.assertEqual(AVFoundation.AVCaptionDecorationOverline, 1 << 2)

        self.assertEqual(AVFoundation.AVCaptionTextCombineAll, -1)
        self.assertEqual(AVFoundation.AVCaptionTextCombineNone, 0)
        self.assertEqual(AVFoundation.AVCaptionTextCombineOneDigit, 1)
        self.assertEqual(AVFoundation.AVCaptionTextCombineTwoDigits, 2)
        self.assertEqual(AVFoundation.AVCaptionTextCombineThreeDigits, 3)
        self.assertEqual(AVFoundation.AVCaptionTextCombineFourDigits, 4)

        self.assertEqual(AVFoundation.AVCaptionTextAlignmentStart, 0)
        self.assertEqual(AVFoundation.AVCaptionTextAlignmentEnd, 1)
        self.assertEqual(AVFoundation.AVCaptionTextAlignmentCenter, 2)
        self.assertEqual(AVFoundation.AVCaptionTextAlignmentLeft, 3)
        self.assertEqual(AVFoundation.AVCaptionTextAlignmentRight, 4)

        self.assertEqual(AVFoundation.AVCaptionRubyPositionBefore, 0)
        self.assertEqual(AVFoundation.AVCaptionRubyPositionAfter, 1)

        self.assertEqual(AVFoundation.AVCaptionRubyAlignmentStart, 0)
        self.assertEqual(AVFoundation.AVCaptionRubyAlignmentCenter, 1)
        self.assertEqual(AVFoundation.AVCaptionRubyAlignmentDistributeSpaceBetween, 2)
        self.assertEqual(AVFoundation.AVCaptionRubyAlignmentDistributeSpaceAround, 3)

    @min_os_level("12.0")
    def test_methods(self):
        self.assertArgIsOut(AVFoundation.AVCaption.textColorAtIndex_range_, 1)
        self.assertArgIsOut(AVFoundation.AVCaption.backgroundColorAtIndex_range_, 1)
        self.assertArgIsOut(AVFoundation.AVCaption.fontWeightAtIndex_range_, 1)
        self.assertArgIsOut(AVFoundation.AVCaption.fontStyleAtIndex_range_, 1)
        self.assertArgIsOut(AVFoundation.AVCaption.decorationAtIndex_range_, 1)
        self.assertArgIsOut(AVFoundation.AVCaption.textCombineAtIndex_range_, 1)
        self.assertArgIsOut(AVFoundation.AVCaption.rubyAtIndex_range_, 1)

    @min_os_level("12.0")
    def test_functions(self):
        AVFoundation.AVCaptionDimensionMake
        AVFoundation.AVCaptionPointMake
        AVFoundation.AVCaptionSize
