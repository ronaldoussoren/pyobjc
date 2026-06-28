import AppKit
from PyObjCTools.TestSupport import TestCase, min_os_level


class PopoverHelper(AppKit.NSObject):
    def popoverShouldClose_(self, a):
        return 1

    def popoverShouldDetach_(self, a):
        return 1


class TestNSPopover(TestCase):
    def test_typed_enums(self):
        self.assertIsTypedEnum(AppKit.NSPopoverCloseReasonValue, str)

    def test_enum_types(self):
        self.assertIsEnumType(AppKit.NSPopoverAppearance)
        self.assertIsEnumType(AppKit.NSPopoverBehavior)

    def test_constants(self):
        self.assertEqual(AppKit.NSPopoverAppearanceMinimal, 0)
        self.assertEqual(AppKit.NSPopoverAppearanceHUD, 1)

        self.assertEqual(AppKit.NSPopoverBehaviorApplicationDefined, 0)
        self.assertEqual(AppKit.NSPopoverBehaviorTransient, 1)
        self.assertEqual(AppKit.NSPopoverBehaviorSemitransient, 2)

        self.assertIsInstance(AppKit.NSPopoverCloseReasonKey, str)
        self.assertIsInstance(AppKit.NSPopoverCloseReasonStandard, str)
        self.assertIsInstance(AppKit.NSPopoverCloseReasonDetachToWindow, str)
        self.assertIsInstance(AppKit.NSPopoverWillShowNotification, str)
        self.assertIsInstance(AppKit.NSPopoverDidShowNotification, str)
        self.assertIsInstance(AppKit.NSPopoverWillCloseNotification, str)
        self.assertIsInstance(AppKit.NSPopoverDidCloseNotification, str)

    def test_methods(self):
        self.assertResultIsBOOL(AppKit.NSPopover.animates)
        self.assertArgIsBOOL(AppKit.NSPopover.setAnimates_, 0)

        self.assertResultIsBOOL(AppKit.NSPopover.isShown)
        self.assertArgIsBOOL(AppKit.NSPopover.setShown_, 0)

        self.assertArgHasType(
            AppKit.NSPopover.showRelativeToRect_ofView_preferredEdge_,
            0,
            AppKit.NSRect.__typestr__,
        )

    @min_os_level("10.10")
    def test_methods10_10(self):
        self.assertResultIsBOOL(AppKit.NSPopover.isDetached)
        # self.assertArgIsBOOL(AppKit.NSPopover.setDetached_, 0)

    @min_os_level("14.0")
    def test_methods14_0(self):
        self.assertResultIsBOOL(AppKit.NSPopover.hasFullSizeContent)
        self.assertArgIsBOOL(AppKit.NSPopover.setHasFullSizeContent_, 0)

    def test_protocols(self):
        self.assertResultIsBOOL(PopoverHelper.popoverShouldClose_)

    @min_os_level("10.10")
    def test_protocols10_10(self):
        self.assertProtocolExists("NSPopoverDelegate", AppKit)
        self.assertResultIsBOOL(PopoverHelper.popoverShouldDetach_)
