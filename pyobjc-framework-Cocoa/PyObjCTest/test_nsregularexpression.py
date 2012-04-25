from PyObjCTools.TestSupport import *
from Foundation import *

class TestNSRegularExpression (TestCase):

    @min_os_level('10.7')
    def testConstants10_7(self):
        self.assertEqual(NSRegularExpressionCaseInsensitive, 1 << 0)
        self.assertEqual(NSRegularExpressionAllowCommentsAndWhitespace, 1 << 1)
        self.assertEqual(NSRegularExpressionIgnoreMetacharacters, 1 << 2)
        self.assertEqual(NSRegularExpressionDotMatchesLineSeparators, 1 << 3)
        self.assertEqual(NSRegularExpressionAnchorsMatchLines, 1 << 4)
        self.assertEqual(NSRegularExpressionUseUnixLineSeparators, 1 << 5)
        self.assertEqual(NSRegularExpressionUseUnicodeWordBoundaries, 1 << 6)

        self.assertEqual(NSMatchingReportProgress, 1 << 0)
        self.assertEqual(NSMatchingReportCompletion, 1 << 1)
        self.assertEqual(NSMatchingAnchored, 1 << 2)
        self.assertEqual(NSMatchingWithTransparentBounds, 1 << 3)
        self.assertEqual(NSMatchingWithoutAnchoringBounds, 1 << 4)

        self.assertEqual(NSMatchingProgress, 1 << 0)
        self.assertEqual(NSMatchingCompleted, 1 << 1)
        self.assertEqual(NSMatchingHitEnd, 1 << 2)
        self.assertEqual(NSMatchingRequiredEnd, 1 << 3)
        self.assertEqual(NSMatchingInternalError, 1 << 4)


    @min_os_level('10.7')
    def testMethods10_7(self):
        self.assertArgIsOut(NSRegularExpression.regularExpressionWithPattern_options_error_, 2)
        self.assertArgIsOut(NSRegularExpression.initWithPattern_options_error_, 2)

        self.assertArgIsBlock(NSRegularExpression.enumerateMatchesInString_options_range_usingBlock_,
                3, b'v@' + objc._C_NSUInteger + b'o^' + objc._C_NSBOOL)

        self.assertArgIsOut(NSDataDetector.dataDetectorWithTypes_error_, 1)
        self.assertArgIsOut(NSDataDetector.initWithTypes_error_, 1)

if __name__ == "__main__":
    main()
