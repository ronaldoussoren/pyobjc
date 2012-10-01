
from PyObjCTools.TestSupport import *
from AppKit import *

try:
    unicode
except NameError:
    unicode = str

class TestNSControlHelper (NSObject):
    def control_textShouldBeginEditing_(self, c, f): return 1
    def control_textShouldEndEditing_(self, c, f): return 1
    def control_didFailToFormatString_errorDescription_(self, c, s, e): return 1
    def control_isValidObject_(self, c, s): return 1
    def control_textView_doCommandBySelector_(self, c, t, com): return 1

class TestNSControl (TestCase):
    @min_os_level('10.8')
    def testMethods10_8(self):
        self.assertResultIsBOOL(NSControl.allowsExpansionToolTips)
        self.assertArgIsBOOL(NSControl.setAllowsExpansionToolTips_, 0)

    def testMethods(self):
        self.assertResultIsBOOL(NSControl.ignoresMultiClick)
        self.assertArgIsBOOL(NSControl.setIgnoresMultiClick_, 0)
        self.assertResultIsBOOL(NSControl.isContinuous)
        self.assertArgIsBOOL(NSControl.setContinuous_, 0)
        self.assertResultIsBOOL(NSControl.isEnabled)
        self.assertArgIsBOOL(NSControl.setEnabled_, 0)
        self.assertArgIsBOOL(NSControl.setFloatingPointFormat_left_right_, 0)
        self.assertResultIsBOOL(NSControl.sendAction_to_)
        self.assertResultIsBOOL(NSControl.abortEditing)
        self.assertResultIsBOOL(NSControl.refusesFirstResponder)
        self.assertArgIsBOOL(NSControl.setRefusesFirstResponder_, 0)

    def testDelegate(self):
        self.assertResultIsBOOL(TestNSControlHelper.control_textShouldBeginEditing_)
        self.assertResultIsBOOL(TestNSControlHelper.control_textShouldEndEditing_)
        self.assertResultIsBOOL(TestNSControlHelper.control_didFailToFormatString_errorDescription_)
        self.assertResultIsBOOL(TestNSControlHelper.control_isValidObject_)
        self.assertResultIsBOOL(TestNSControlHelper.control_textView_doCommandBySelector_)

    def testConstants(self):
        self.assertIsInstance(NSControlTextDidBeginEditingNotification, unicode)
        self.assertIsInstance(NSControlTextDidEndEditingNotification, unicode)
        self.assertIsInstance(NSControlTextDidChangeNotification, unicode)

if __name__ == "__main__":
    main()
