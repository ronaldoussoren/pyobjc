
from PyObjCTools.TestSupport import *
from AppKit import *

class TestNSGradient (TestCase):
    def testConstants(self):
        self.failUnlessEqual(NSGradientDrawsBeforeStartingLocation, (1 << 0))
        self.failUnlessEqual(NSGradientDrawsAfterEndingLocation, (1 << 1))

    def testMethods(self):
        self.fail("- (id)initWithColorsAndLocations:(NSColor *)firstColor, ...;")
        self.fail("- (id)initWithColors:(NSArray *)colorArray atLocations:(const CGFloat *)locations colorSpace:(NSColorSpace *)colorSpace;")
        self.fail("- (void)getColor:(NSColor **)color location:(CGFloat *)location atIndex:(NSInteger)index;")



if __name__ == "__main__":
    main()
