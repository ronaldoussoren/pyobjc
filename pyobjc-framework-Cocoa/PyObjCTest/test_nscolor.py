import array

import AppKit
from PyObjCTools.TestSupport import TestCase


class TestRegressions(TestCase):
    def testQualifiersInSignature(self):
        AppKit.NSColor.redColor().getRed_green_blue_alpha_(None, None, None, None)

    def testMethods(self):
        self.assertResultIsBOOL(AppKit.NSColor.ignoresAlpha)
        self.assertArgIsBOOL(AppKit.NSColor.setIgnoresAlpha_, 0)

        space = AppKit.NSColorSpace.adobeRGB1998ColorSpace()
        color = AppKit.NSColor.colorWithColorSpace_components_count_(
            space, (0.1, 0.2, 0.3, 0.4), 4
        )
        self.assertIsInstance(color, AppKit.NSColor)

        color = AppKit.NSColor.colorWithCalibratedRed_green_blue_alpha_(0, 0, 0, 0)
        r, g, b, a = color.getRed_green_blue_alpha_(None, None, None, None)
        self.assertIsInstance(r, float)
        self.assertIsInstance(g, float)
        self.assertIsInstance(b, float)
        self.assertIsInstance(a, float)

        color = AppKit.NSColor.colorWithCalibratedHue_saturation_brightness_alpha_(
            0.1, 0.2, 0.3, 0.4
        )
        h, s, b, a = color.getHue_saturation_brightness_alpha_(None, None, None, None)
        self.assertIsInstance(h, float)
        self.assertIsInstance(s, float)
        self.assertIsInstance(b, float)
        self.assertIsInstance(a, float)

        color = AppKit.NSColor.colorWithCalibratedWhite_alpha_(0.1, 0.2)
        w, a = color.getWhite_alpha_(None, None)
        self.assertIsInstance(w, float)
        self.assertIsInstance(a, float)

        color = AppKit.NSColor.colorWithDeviceCyan_magenta_yellow_black_alpha_(
            1, 1, 1, 1, 1
        )
        c, m, y, b, a = color.getCyan_magenta_yellow_black_alpha_(
            None, None, None, None, None
        )
        self.assertIsInstance(c, float)
        self.assertIsInstance(m, float)
        self.assertIsInstance(y, float)
        self.assertIsInstance(b, float)
        self.assertIsInstance(a, float)

        a = array.array("d", [0] * 6)
        v = color.getComponents_(a)
        self.assertIs(v, a)
        self.assertEqual(a[0], 1.0)

    def testConstants(self):
        self.assertIsInstance(AppKit.NSSystemColorsDidChangeNotification, str)

        self.assertEqual(AppKit.NSAppKitVersionNumberWithPatternColorLeakFix, 641.0)

        self.assertEqual(AppKit.NSColorTypeComponentBased, 0)
        self.assertEqual(AppKit.NSColorTypePattern, 1)
        self.assertEqual(AppKit.NSColorTypeCatalog, 2)

        self.assertEqual(AppKit.NSColorSystemEffectNone, 0)
        self.assertEqual(AppKit.NSColorSystemEffectPressed, 1)
        self.assertEqual(AppKit.NSColorSystemEffectDeepPressed, 2)
        self.assertEqual(AppKit.NSColorSystemEffectDisabled, 3)
        self.assertEqual(AppKit.NSColorSystemEffectRollover, 4)
