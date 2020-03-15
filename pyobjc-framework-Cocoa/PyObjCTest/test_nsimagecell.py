import AppKit
from PyObjCTools.TestSupport import TestCase


class TestNSImageCell(TestCase):
    def testConstants(self):
        self.assertEqual(AppKit.NSImageAlignCenter, 0)
        self.assertEqual(AppKit.NSImageAlignTop, 1)
        self.assertEqual(AppKit.NSImageAlignTopLeft, 2)
        self.assertEqual(AppKit.NSImageAlignTopRight, 3)
        self.assertEqual(AppKit.NSImageAlignLeft, 4)
        self.assertEqual(AppKit.NSImageAlignBottom, 5)
        self.assertEqual(AppKit.NSImageAlignBottomLeft, 6)
        self.assertEqual(AppKit.NSImageAlignBottomRight, 7)
        self.assertEqual(AppKit.NSImageAlignRight, 8)

        self.assertEqual(AppKit.NSImageFrameNone, 0)
        self.assertEqual(AppKit.NSImageFramePhoto, 1)
        self.assertEqual(AppKit.NSImageFrameGrayBezel, 2)
        self.assertEqual(AppKit.NSImageFrameGroove, 3)
        self.assertEqual(AppKit.NSImageFrameButton, 4)
