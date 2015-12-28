
from PyObjCTools.TestSupport import *
from AppKit import *

class TestNSControlHelper (NSObject):
    def control_textShouldBeginEditing_(self, c, f): return 1
    def control_textShouldEndEditing_(self, c, f): return 1
    def control_didFailToFormatString_errorDescription_(self, c, s, e): return 1
    def control_isValidObject_(self, c, s): return 1
    def control_textView_doCommandBySelector_(self, c, t, com): return 1
    def control_textView_completions_forPartialWordRange_indexOfSelectedItem_(self, c, t, c1, r, i): return 1

class TestNSControl (TestCase):
    @min_os_level('10.10')
    def testMethods10_10(self):
        self.assertResultIsBOOL(NSControl.usesSingleLineMode)
        self.assertArgIsBOOL(NSControl.setUsesSingleLineMode_, 0)

        self.assertResultIsBOOL(NSControl.isHighlighted)
        self.assertArgIsBOOL(NSControl.setHighlighted_, 0)

    @min_os_level('10.8')
    def testMethods10_8(self):
        self.assertResultIsBOOL(NSControl.allowsExpansionToolTips)
        self.assertArgIsBOOL(NSControl.setAllowsExpansionToolTips_, 0)

    def testMethods(self):
        self.assertArgIsSEL(NSControl.setAction_, 0, b'v@:@')
        self.assertResultIsBOOL(NSControl.ignoresMultiClick)
        self.assertArgIsBOOL(NSControl.setIgnoresMultiClick_, 0)
        self.assertResultIsBOOL(NSControl.isContinuous)
        self.assertArgIsBOOL(NSControl.setContinuous_, 0)
        self.assertResultIsBOOL(NSControl.isEnabled)
        self.assertArgIsBOOL(NSControl.setEnabled_, 0)
        self.assertArgIsBOOL(NSControl.setFloatingPointFormat_left_right_, 0)
        self.assertResultIsBOOL(NSControl.sendAction_to_)
        self.assertArgIsSEL(NSControl.sendAction_to_, 0, b'v@:@')
        self.assertResultIsBOOL(NSControl.abortEditing)
        self.assertResultIsBOOL(NSControl.refusesFirstResponder)
        self.assertArgIsBOOL(NSControl.setRefusesFirstResponder_, 0)


    @min_sdk_level('10.6')
    def testProtocols(self):
        objc.protocolNamed('NSControlTextEditingDelegate')

    def testDelegate(self):
        self.assertResultIsBOOL(TestNSControlHelper.control_textShouldBeginEditing_)
        self.assertResultIsBOOL(TestNSControlHelper.control_textShouldEndEditing_)
        self.assertResultIsBOOL(TestNSControlHelper.control_didFailToFormatString_errorDescription_)
        self.assertResultIsBOOL(TestNSControlHelper.control_isValidObject_)
        self.assertResultIsBOOL(TestNSControlHelper.control_textView_doCommandBySelector_)

        self.assertArgHasType(TestNSControlHelper.control_textView_completions_forPartialWordRange_indexOfSelectedItem_, 3, NSRange.__typestr__)
        self.assertArgHasType(TestNSControlHelper.control_textView_completions_forPartialWordRange_indexOfSelectedItem_, 4, b'N^' + objc._C_NSInteger)

    def testConstants(self):
        self.assertIsInstance(NSControlTextDidBeginEditingNotification, unicode)
        self.assertIsInstance(NSControlTextDidEndEditingNotification, unicode)
        self.assertIsInstance(NSControlTextDidChangeNotification, unicode)

if __name__ == "__main__":
    main()
