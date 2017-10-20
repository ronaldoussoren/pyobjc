
from PyObjCTools.TestSupport import *
from AppKit import *

class TestNSTextList (TestCase):
    def testConstants(self):
        self.assertEqual(NSTextListPrependEnclosingMarker, 1)

    @min_os_level('10.13')
    def testConstants10_13(self):
        self.assertIsInstance(NSTextListMarkerBox, unicode)
        self.assertIsInstance(NSTextListMarkerCheck, unicode)
        self.assertIsInstance(NSTextListMarkerCircle, unicode)
        self.assertIsInstance(NSTextListMarkerDiamond, unicode)
        self.assertIsInstance(NSTextListMarkerDisc, unicode)
        self.assertIsInstance(NSTextListMarkerHyphen, unicode)
        self.assertIsInstance(NSTextListMarkerSquare, unicode)
        self.assertIsInstance(NSTextListMarkerLowercaseHexadecimal, unicode)
        self.assertIsInstance(NSTextListMarkerUppercaseHexadecimal, unicode)
        self.assertIsInstance(NSTextListMarkerOctal, unicode)
        self.assertIsInstance(NSTextListMarkerLowercaseAlpha, unicode)
        self.assertIsInstance(NSTextListMarkerUppercaseAlpha, unicode)
        self.assertIsInstance(NSTextListMarkerLowercaseLatin, unicode)
        self.assertIsInstance(NSTextListMarkerUppercaseLatin, unicode)
        self.assertIsInstance(NSTextListMarkerLowercaseRoman, unicode)
        self.assertIsInstance(NSTextListMarkerUppercaseRoman, unicode)
        self.assertIsInstance(NSTextListMarkerDecimal, unicode)

if __name__ == "__main__":
    main()
