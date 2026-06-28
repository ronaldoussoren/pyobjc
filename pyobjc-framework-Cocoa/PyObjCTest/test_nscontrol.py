import AppKit
from PyObjCTools.TestSupport import TestCase, min_os_level
import objc


class TestNSControlHelper(AppKit.NSObject):
    def control_textShouldBeginEditing_(self, c, f):
        return 1

    def control_textShouldEndEditing_(self, c, f):
        return 1

    def control_didFailToFormatString_errorDescription_(self, c, s, e):
        return 1

    def control_isValidObject_(self, c, s):
        return 1

    def control_textView_doCommandBySelector_(self, c, t, com):
        return 1

    def control_textView_completions_forPartialWordRange_indexOfSelectedItem_(
        self, c, t, c1, r, i
    ):
        return 1


class TestNSControl(TestCase):
    def test_enums(self):
        self.assertIsEnumType(AppKit.NSControlBorderShape)
        self.assertEqual(AppKit.NSControlBorderShapeAutomatic, 0)
        self.assertEqual(AppKit.NSControlBorderShapeCapsule, 1)
        self.assertEqual(AppKit.NSControlBorderShapeRoundedRectangle, 2)
        self.assertEqual(AppKit.NSControlBorderShapeCircle, 3)

        self.assertIsEnumType(AppKit.NSControlEvents)
        self.assertEqual(AppKit.NSControlEventTrackingBegan, 1 << 0)
        self.assertEqual(AppKit.NSControlEventTrackingRepeated, 1 << 1)
        self.assertEqual(AppKit.NSControlEventTrackingInside, 1 << 2)
        self.assertEqual(AppKit.NSControlEventTrackingOutside, 1 << 3)
        self.assertEqual(AppKit.NSControlEventTrackingEntered, 1 << 4)
        self.assertEqual(AppKit.NSControlEventTrackingExited, 1 << 5)
        self.assertEqual(AppKit.NSControlEventTrackingEndedInside, 1 << 6)
        self.assertEqual(AppKit.NSControlEventTrackingEndedOutside, 1 << 7)
        self.assertEqual(AppKit.NSControlEventTrackingCancelled, 1 << 8)
        self.assertEqual(AppKit.NSControlEventValueChanged, 1 << 12)
        self.assertEqual(AppKit.NSControlEventPrimaryActionTriggered, 1 << 13)
        self.assertEqual(AppKit.NSControlEventMenuActionTriggered, 1 << 14)
        self.assertEqual(AppKit.NSControlEventAllTrackingEvents, 0x00000FFF)
        self.assertEqual(AppKit.NSControlEventApplicationReserved, 0x0F000000)
        self.assertEqual(AppKit.NSControlEventSystemReserved, 0xF0000000)
        self.assertEqual(AppKit.NSControlEventAllEvents, 0xFFFFFFFF)

    def test_constants(self):
        self.assertIsInstance(AppKit.NSControlTextDidBeginEditingNotification, str)
        self.assertIsInstance(AppKit.NSControlTextDidEndEditingNotification, str)
        self.assertIsInstance(AppKit.NSControlTextDidChangeNotification, str)

    def test_methods(self):
        self.assertArgIsSEL(AppKit.NSControl.setAction_, 0, b"v@:@")
        self.assertResultIsBOOL(AppKit.NSControl.ignoresMultiClick)
        self.assertArgIsBOOL(AppKit.NSControl.setIgnoresMultiClick_, 0)
        self.assertResultIsBOOL(AppKit.NSControl.isContinuous)
        self.assertArgIsBOOL(AppKit.NSControl.setContinuous_, 0)
        self.assertResultIsBOOL(AppKit.NSControl.isEnabled)
        self.assertArgIsBOOL(AppKit.NSControl.setEnabled_, 0)
        self.assertArgIsBOOL(AppKit.NSControl.setFloatingPointFormat_left_right_, 0)
        self.assertResultIsBOOL(AppKit.NSControl.sendAction_to_)
        self.assertArgIsSEL(AppKit.NSControl.sendAction_to_, 0, b"v@:@")
        self.assertResultIsBOOL(AppKit.NSControl.abortEditing)
        self.assertResultIsBOOL(AppKit.NSControl.refusesFirstResponder)
        self.assertArgIsBOOL(AppKit.NSControl.setRefusesFirstResponder_, 0)

        self.assertResultIsBOOL(AppKit.NSControl.allowsExpansionToolTips)
        self.assertArgIsBOOL(AppKit.NSControl.setAllowsExpansionToolTips_, 0)

    @min_os_level("10.10")
    def test_methods10_10(self):
        self.assertResultIsBOOL(AppKit.NSControl.usesSingleLineMode)
        self.assertArgIsBOOL(AppKit.NSControl.setUsesSingleLineMode_, 0)

        self.assertResultIsBOOL(AppKit.NSControl.isHighlighted)
        self.assertArgIsBOOL(AppKit.NSControl.setHighlighted_, 0)

    @min_os_level("27.0")
    def test_methods27_0(self):
        # XXX: "The selector may include the sender, the event, or both as parameters, in that order."
        #      The SEL can have either 1 or 2 arguments, that's not something we can represent ATM
        self.assertArgIsSEL(
            AppKit.NSControl.addTarget_action_forControlEvents_, 1, b"v@:@@"
        )
        self.assertArgIsSEL(
            AppKit.NSControl.removeTarget_action_forControlEvents_, 1, b"v@:@@"
        )

    def test_protocols(self):
        self.assertProtocolExists("NSControlTextEditingDelegate", AppKit)

    def test_protocol_methods(self):
        self.assertResultIsBOOL(TestNSControlHelper.control_textShouldBeginEditing_)
        self.assertResultIsBOOL(TestNSControlHelper.control_textShouldEndEditing_)
        self.assertResultIsBOOL(
            TestNSControlHelper.control_didFailToFormatString_errorDescription_
        )
        self.assertResultIsBOOL(TestNSControlHelper.control_isValidObject_)
        self.assertResultIsBOOL(
            TestNSControlHelper.control_textView_doCommandBySelector_
        )

        self.assertArgHasType(
            TestNSControlHelper.control_textView_completions_forPartialWordRange_indexOfSelectedItem_,  # noqa: B950
            3,
            AppKit.NSRange.__typestr__,
        )
        self.assertArgHasType(
            TestNSControlHelper.control_textView_completions_forPartialWordRange_indexOfSelectedItem_,  # noqa: B950
            4,
            b"N^" + objc._C_NSInteger,
        )
