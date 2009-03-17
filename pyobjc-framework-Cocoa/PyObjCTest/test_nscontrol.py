
from PyObjCTools.TestSupport import *
from AppKit import *

class TestNSControlHelper (NSObject):
    def control_textShouldBeginEditing_(self, c, f): return 1
    def control_textShouldEndEditing_(self, c, f): return 1
    def control_didFailToFormatString_errorDescription_(self, c, s, e): return 1
    def control_isValidObject_(self, c, s): return 1
    def control_textView_doCommandBySelector_(self, c, t, com): return 1

class TestNSControl (TestCase):
    def testMethods(self):
        self.failUnlessResultIsBOOL(NSControl.ignoresMultiClick)
        self.failUnlessArgIsBOOL(NSControl.setIgnoresMultiClick_, 0)
        self.failUnlessResultIsBOOL(NSControl.isContinuous)
        self.failUnlessArgIsBOOL(NSControl.setContinuous_, 0)
        self.failUnlessResultIsBOOL(NSControl.isEnabled)
        self.failUnlessArgIsBOOL(NSControl.setEnabled_, 0)
        self.failUnlessArgIsBOOL(NSControl.setFloatingPointFormat_left_right_, 0)
        self.failUnlessResultIsBOOL(NSControl.sendAction_to_)
        self.failUnlessResultIsBOOL(NSControl.abortEditing)
        self.failUnlessResultIsBOOL(NSControl.refusesFirstResponder)
        self.failUnlessArgIsBOOL(NSControl.setRefusesFirstResponder_, 0)

    def testDelegate(self):
        self.failUnlessResultIsBOOL(TestNSControlHelper.control_textShouldBeginEditing_)
        self.failUnlessResultIsBOOL(TestNSControlHelper.control_textShouldEndEditing_)
        self.failUnlessResultIsBOOL(TestNSControlHelper.control_didFailToFormatString_errorDescription_)
        self.failUnlessResultIsBOOL(TestNSControlHelper.control_isValidObject_)
        self.failUnlessResultIsBOOL(TestNSControlHelper.control_textView_doCommandBySelector_)

    def testConstants(self):
        self.failUnlessIsInstance(NSControlTextDidBeginEditingNotification, unicode)
        self.failUnlessIsInstance(NSControlTextDidEndEditingNotification, unicode)
        self.failUnlessIsInstance(NSControlTextDidChangeNotification, unicode)

if __name__ == "__main__":
    main()
