import AppKit
from PyObjCTools.TestSupport import TestCase, min_os_level, min_sdk_level


class TestNSStatusItemHelper(AppKit.NSObject):
    def statusItemDidEndExpandedInterfaceSession_animated_(self, a, b):
        pass


class TestNSStatusItem(TestCase):
    def test_enum_types(self):
        self.assertIsEnumType(AppKit.NSStatusItemBehavior)

    def test_constants(self):
        self.assertEqual(AppKit.NSStatusItemBehaviorRemovalAllowed, 1 << 1)
        self.assertEqual(AppKit.NSStatusItemBehaviorTerminationOnRemoval, 1 << 2)

    @min_sdk_level("27.0")
    def test_protocols(self):
        self.assertProtocolExists("NSStatusItemExpandedInterfaceDelegate", AppKit)

    def test_protocol_methods(self):
        self.assertArgIsBOOL(
            TestNSStatusItemHelper.statusItemDidEndExpandedInterfaceSession_animated_, 1
        )

    def test_methods(self):
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
    def test_methods10_12(self):
        self.assertResultIsBOOL(AppKit.NSStatusItem.isVisible)
        self.assertArgIsBOOL(AppKit.NSStatusItem.setVisible_, 0)
