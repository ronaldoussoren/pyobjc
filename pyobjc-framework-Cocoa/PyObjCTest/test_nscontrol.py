import AppKit
from PyObjCTools.TestSupport import TestCase, min_os_level, min_sdk_level
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
    @min_os_level("10.10")
    def testMethods10_10(self):
        self.assertResultIsBOOL(AppKit.NSControl.usesSingleLineMode)
        self.assertArgIsBOOL(AppKit.NSControl.setUsesSingleLineMode_, 0)

        self.assertResultIsBOOL(AppKit.NSControl.isHighlighted)
        self.assertArgIsBOOL(AppKit.NSControl.setHighlighted_, 0)

    @min_os_level("10.8")
    def testMethods10_8(self):
        self.assertResultIsBOOL(AppKit.NSControl.allowsExpansionToolTips)
        self.assertArgIsBOOL(AppKit.NSControl.setAllowsExpansionToolTips_, 0)

    def testMethods(self):
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

    @min_sdk_level("10.6")
    def testProtocols(self):
        objc.protocolNamed("NSControlTextEditingDelegate")

    def testDelegate(self):
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

    def testConstants(self):
        self.assertIsInstance(AppKit.NSControlTextDidBeginEditingNotification, str)
        self.assertIsInstance(AppKit.NSControlTextDidEndEditingNotification, str)
        self.assertIsInstance(AppKit.NSControlTextDidChangeNotification, str)
