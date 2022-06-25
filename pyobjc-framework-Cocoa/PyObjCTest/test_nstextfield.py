import AppKit
from PyObjCTools.TestSupport import TestCase, min_os_level, min_sdk_level
import objc


class TestNSTextFieldHelper(AppKit.NSObject):
    def textField_textView_candidatesForSelectedRange_(self, tf, tv, r):
        return 1

    def textField_textView_candidates_forSelectedRange_(self, tf, tv, c, r):
        return 1

    def textField_textView_shouldSelectCandidateAtIndex_(self, tf, tv, i):
        return 1


class TestNSTextField(TestCase):
    def testMethods(self):
        self.assertResultIsBOOL(AppKit.NSTextField.drawsBackground)
        self.assertArgIsBOOL(AppKit.NSTextField.setDrawsBackground_, 0)
        self.assertResultIsBOOL(AppKit.NSTextField.isBordered)
        self.assertArgIsBOOL(AppKit.NSTextField.setBordered_, 0)
        self.assertResultIsBOOL(AppKit.NSTextField.isBezeled)
        self.assertArgIsBOOL(AppKit.NSTextField.setBezeled_, 0)
        self.assertResultIsBOOL(AppKit.NSTextField.isEditable)
        self.assertArgIsBOOL(AppKit.NSTextField.setEditable_, 0)
        self.assertResultIsBOOL(AppKit.NSTextField.isSelectable)
        self.assertArgIsBOOL(AppKit.NSTextField.setSelectable_, 0)
        self.assertResultIsBOOL(AppKit.NSTextField.textShouldBeginEditing_)
        self.assertResultIsBOOL(AppKit.NSTextField.textShouldEndEditing_)
        self.assertResultIsBOOL(AppKit.NSTextField.acceptsFirstResponder)
        self.assertResultIsBOOL(AppKit.NSTextField.allowsEditingTextAttributes)
        self.assertArgIsBOOL(AppKit.NSTextField.setAllowsEditingTextAttributes_, 0)
        self.assertResultIsBOOL(AppKit.NSTextField.importsGraphics)
        self.assertArgIsBOOL(AppKit.NSTextField.setImportsGraphics_, 0)

    @min_os_level("10.11")
    def testMethods10_11(self):
        self.assertResultIsBOOL(AppKit.NSTextField.allowsDefaultTighteningForTruncation)
        self.assertArgIsBOOL(
            AppKit.NSTextField.setAllowsDefaultTighteningForTruncation_, 0
        )

    @min_os_level("10.12")
    def testMethods10_12(self):
        self.assertResultIsBOOL(AppKit.NSTextField.isAutomaticTextCompletionEnabled)
        self.assertArgIsBOOL(AppKit.NSTextField.setAutomaticTextCompletionEnabled_, 0)
        self.assertResultIsBOOL(AppKit.NSTextField.allowsCharacterPickerTouchBarItem)
        self.assertArgIsBOOL(
            AppKit.NSTextField.setAllowsCharacterPickerTouchBarItem_, 0
        )

        self.assertArgHasType(
            TestNSTextFieldHelper.textField_textView_candidatesForSelectedRange_,
            2,
            AppKit.NSRange.__typestr__,
        )
        self.assertArgHasType(
            TestNSTextFieldHelper.textField_textView_candidates_forSelectedRange_,
            3,
            AppKit.NSRange.__typestr__,
        )
        self.assertArgHasType(
            TestNSTextFieldHelper.textField_textView_shouldSelectCandidateAtIndex_,
            2,
            objc._C_NSUInteger,
        )
        self.assertResultIsBOOL(
            TestNSTextFieldHelper.textField_textView_shouldSelectCandidateAtIndex_
        )

    @min_sdk_level("10.6")
    def testProtocols(self):
        self.assertProtocolExists("NSTextFieldDelegate")
