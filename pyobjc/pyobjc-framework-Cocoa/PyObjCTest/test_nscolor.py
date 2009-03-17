from PyObjCTools.TestSupport import *
from AppKit import *
import array

class TestRegressions (TestCase):
    def testQualifiersInSignature(self):
        NSColor.redColor().getRed_green_blue_alpha_(None, None, None, None)

    def testMethods(self):
        self.failUnlessResultIsBOOL(NSColor.ignoresAlpha)
        self.failUnlessArgIsBOOL(NSColor.setIgnoresAlpha_, 0)

        space = NSColorSpace.adobeRGB1998ColorSpace()
        color = NSColor.colorWithColorSpace_components_count_(space, (0.1, 0.2, 0.3, 0.4), 4)
        self.failUnlessIsInstance(color, NSColor)

        color = NSColor.colorWithCalibratedRed_green_blue_alpha_(0, 0, 0, 0)
        r, g, b, a = color.getRed_green_blue_alpha_(None, None, None, None)
        self.failUnlessIsInstance(r, float)
        self.failUnlessIsInstance(g, float)
        self.failUnlessIsInstance(b, float)
        self.failUnlessIsInstance(a, float)

        color = NSColor.colorWithCalibratedHue_saturation_brightness_alpha_(0.1, 0.2, 0.3, 0.4)
        h, s, b, a = color.getHue_saturation_brightness_alpha_(None, None, None, None)
        self.failUnlessIsInstance(h, float)
        self.failUnlessIsInstance(s, float)
        self.failUnlessIsInstance(b, float)
        self.failUnlessIsInstance(a, float)

        color = NSColor.colorWithCalibratedWhite_alpha_(0.1, 0.2)
        w, a = color.getWhite_alpha_(None, None)
        self.failUnlessIsInstance(w, float)
        self.failUnlessIsInstance(a, float)

        color = NSColor.colorWithDeviceCyan_magenta_yellow_black_alpha_(1, 1, 1, 1, 1)
        c, m, y, b, a  = color.getCyan_magenta_yellow_black_alpha_(None, None, None, None, None)
        self.failUnlessIsInstance(c, float)
        self.failUnlessIsInstance(m, float)
        self.failUnlessIsInstance(y, float)
        self.failUnlessIsInstance(b, float)
        self.failUnlessIsInstance(a, float)

        a = array.array('f', [0] * 6)
        v = color.getComponents_(a)
        self.failUnlessEqual(a[0], 1.0)

    def testConstants(self):
        self.failUnlessIsInstance(NSSystemColorsDidChangeNotification, unicode)

if __name__ == "__main__":
    main()
