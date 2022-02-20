import Foundation
import objc
from PyObjCTools.TestSupport import TestCase, min_os_level


class TestNSRegularExpression(TestCase):
    def test_enum_types(self):
        self.assertIsEnumType(Foundation.NSMatchingFlags)
        self.assertIsEnumType(Foundation.NSMatchingOptions)
        self.assertIsEnumType(Foundation.NSRegularExpressionOptions)

    @min_os_level("10.7")
    def testConstants10_7(self):
        self.assertEqual(Foundation.NSRegularExpressionCaseInsensitive, 1 << 0)
        self.assertEqual(
            Foundation.NSRegularExpressionAllowCommentsAndWhitespace, 1 << 1
        )
        self.assertEqual(Foundation.NSRegularExpressionIgnoreMetacharacters, 1 << 2)
        self.assertEqual(Foundation.NSRegularExpressionDotMatchesLineSeparators, 1 << 3)
        self.assertEqual(Foundation.NSRegularExpressionAnchorsMatchLines, 1 << 4)
        self.assertEqual(Foundation.NSRegularExpressionUseUnixLineSeparators, 1 << 5)
        self.assertEqual(Foundation.NSRegularExpressionUseUnicodeWordBoundaries, 1 << 6)

        self.assertEqual(Foundation.NSMatchingReportProgress, 1 << 0)
        self.assertEqual(Foundation.NSMatchingReportCompletion, 1 << 1)
        self.assertEqual(Foundation.NSMatchingAnchored, 1 << 2)
        self.assertEqual(Foundation.NSMatchingWithTransparentBounds, 1 << 3)
        self.assertEqual(Foundation.NSMatchingWithoutAnchoringBounds, 1 << 4)

        self.assertEqual(Foundation.NSMatchingProgress, 1 << 0)
        self.assertEqual(Foundation.NSMatchingCompleted, 1 << 1)
        self.assertEqual(Foundation.NSMatchingHitEnd, 1 << 2)
        self.assertEqual(Foundation.NSMatchingRequiredEnd, 1 << 3)
        self.assertEqual(Foundation.NSMatchingInternalError, 1 << 4)

    @min_os_level("10.7")
    def testMethods10_7(self):
        self.assertArgIsOut(
            Foundation.NSRegularExpression.regularExpressionWithPattern_options_error_,
            2,
        )
        self.assertArgIsOut(
            Foundation.NSRegularExpression.initWithPattern_options_error_, 2
        )

        self.assertArgIsBlock(
            Foundation.NSRegularExpression.enumerateMatchesInString_options_range_usingBlock_,
            3,
            b"v@" + objc._C_NSUInteger + b"o^" + objc._C_NSBOOL,
        )

        self.assertArgIsOut(Foundation.NSDataDetector.dataDetectorWithTypes_error_, 1)
        self.assertArgIsOut(Foundation.NSDataDetector.initWithTypes_error_, 1)
