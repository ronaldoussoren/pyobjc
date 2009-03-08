from PyObjCTools.TestSupport import *
from AppKit import *

class TestRegressions (TestCase):
    def testQualifiersInSignature(self):
        NSColor.redColor().getRed_green_blue_alpha_(None, None, None, None)

    def testMethods(self):
        self.fail("+ (NSColor *)colorWithColorSpace:(NSColorSpace *)space components:(const CGFloat *)components count:(NSInteger)numberOfComponents;")
        self.fail("- (void)getRed:(CGFloat *)red green:(CGFloat *)green blue:(CGFloat *)blue alpha:(CGFloat *)alpha;")
        self.fail("- (void)getHue:(CGFloat *)hue saturation:(CGFloat *)saturation brightness:(CGFloat *)brightness alpha:(CGFloat *)alpha;")
        self.fail("- (void)getWhite:(CGFloat *)white alpha:(CGFloat *)alpha;")
        self.fail("- (void)getCyan:(CGFloat *)cyan magenta:(CGFloat *)magenta yellow:(CGFloat *)yellow black:(CGFloat *)black alpha:(CGFloat *)alpha;")
        self.fail("- (void)getComponents:(CGFloat *)components;")

    def testConstants(self):
        self.failUnlessIsInstance(NSSystemColorsDidChangeNotification, unicode)

if __name__ == "__main__":
    main()
