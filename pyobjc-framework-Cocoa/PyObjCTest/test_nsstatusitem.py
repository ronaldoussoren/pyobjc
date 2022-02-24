import AppKit
from PyObjCTools.TestSupport import TestCase, min_os_level


class TestNSStatusItem(TestCase):
    def test_enum_types(self):
        self.assertIsEnumType(AppKit.NSStatusItemBehavior)

    def testConstants(self):
        self.assertEqual(AppKit.NSStatusItemBehaviorRemovalAllowed, 1 << 1)
        self.assertEqual(AppKit.NSStatusItemBehaviorTerminationOnRemoval, 1 << 2)

    def testMethods(self):
        m = AppKit.NSStatusItem.setAction_.__metadata__()
        self.assertEqual(m["arguments"][2]["sel_of_type"], b"v@:@")

        m = AppKit.NSStatusItem.setDoubleAction_.__metadata__()
        self.assertEqual(m["arguments"][2]["sel_of_type"], b"v@:@")

        self.assertResultIsBOOL(AppKit.NSStatusItem.isEnabled)
        self.assertArgIsBOOL(AppKit.NSStatusItem.setEnabled_, 0)
        self.assertResultIsBOOL(AppKit.NSStatusItem.highlightMode)
        self.assertArgIsBOOL(AppKit.NSStatusItem.setHighlightMode_, 0)
        self.assertArgIsBOOL(
            AppKit.NSStatusItem.drawStatusBarBackgroundInRect_withHighlight_, 1
        )

    @min_os_level("10.12")
    def testMethods10_12(self):
        self.assertResultIsBOOL(AppKit.NSStatusItem.isVisible)
        self.assertArgIsBOOL(AppKit.NSStatusItem.setVisible_, 0)
