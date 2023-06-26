import AppKit
from PyObjCTools.TestSupport import TestCase


class TestNSImage(TestCase):
    def test_constants(self):
        self.assertIsEnumType(AppKit.NSImageDynamicRange)
        self.assertEqual(AppKit.NSImageDynamicRangeUnspecified, -1)
        self.assertEqual(AppKit.NSImageDynamicRangeStandard, 0)
        self.assertEqual(AppKit.NSImageDynamicRangeConstrainedHigh, 1)
        self.assertEqual(AppKit.NSImageDynamicRangeHigh, 2)

    def testMethods(self):
        self.assertArgIsBOOL(AppKit.NSImageView.setEditable_, 0)
        self.assertResultIsBOOL(AppKit.NSImageView.isEditable)
        self.assertArgIsBOOL(AppKit.NSImageView.setAnimates_, 0)
        self.assertResultIsBOOL(AppKit.NSImageView.animates)
        self.assertArgIsBOOL(AppKit.NSImageView.setAllowsCutCopyPaste_, 0)
        self.assertResultIsBOOL(AppKit.NSImageView.allowsCutCopyPaste)
