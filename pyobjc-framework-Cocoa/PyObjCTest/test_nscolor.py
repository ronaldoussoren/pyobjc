from PyObjCTools.TestSupport import *
from AppKit import *
import array
import sys

class TestRegressions (TestCase):
    def testQualifiersInSignature(self):
        NSColor.redColor().getRed_green_blue_alpha_(None, None, None, None)

    def testMethods(self):
        self.assertResultIsBOOL(NSColor.ignoresAlpha)
        self.assertArgIsBOOL(NSColor.setIgnoresAlpha_, 0)

        space = NSColorSpace.adobeRGB1998ColorSpace()
        color = NSColor.colorWithColorSpace_components_count_(space, (0.1, 0.2, 0.3, 0.4), 4)
        self.assertIsInstance(color, NSColor)

        color = NSColor.colorWithCalibratedRed_green_blue_alpha_(0, 0, 0, 0)
        r, g, b, a = color.getRed_green_blue_alpha_(None, None, None, None)
        self.assertIsInstance(r, float)
        self.assertIsInstance(g, float)
        self.assertIsInstance(b, float)
        self.assertIsInstance(a, float)

        color = NSColor.colorWithCalibratedHue_saturation_brightness_alpha_(0.1, 0.2, 0.3, 0.4)
        h, s, b, a = color.getHue_saturation_brightness_alpha_(None, None, None, None)
        self.assertIsInstance(h, float)
        self.assertIsInstance(s, float)
        self.assertIsInstance(b, float)
        self.assertIsInstance(a, float)

        color = NSColor.colorWithCalibratedWhite_alpha_(0.1, 0.2)
        w, a = color.getWhite_alpha_(None, None)
        self.assertIsInstance(w, float)
        self.assertIsInstance(a, float)

        color = NSColor.colorWithDeviceCyan_magenta_yellow_black_alpha_(1, 1, 1, 1, 1)
        c, m, y, b, a  = color.getCyan_magenta_yellow_black_alpha_(None, None, None, None, None)
        self.assertIsInstance(c, float)
        self.assertIsInstance(m, float)
        self.assertIsInstance(y, float)
        self.assertIsInstance(b, float)
        self.assertIsInstance(a, float)

        if sys.maxint > 2**32:
            a = array.array('d', [0] * 6)
        else:
            a = array.array('f', [0] * 6)
        v = color.getComponents_(a)
        self.assertEqual(a[0], 1.0)

    def testConstants(self):
        self.assertIsInstance(NSSystemColorsDidChangeNotification, unicode)

if __name__ == "__main__":
    main()
