
from PyObjCTools.TestSupport import *
from AppKit import *

class TestNSAlertHelper (NSObject):
    def alertShowHelp_(self, alert):
        return 1

class TestNSAlert (TestCase):
    def testConstants(self):
        self.failUnlessEqual(NSWarningAlertStyle, 0)
        self.failUnlessEqual(NSInformationalAlertStyle, 1)
        self.failUnlessEqual(NSCriticalAlertStyle, 2)
        self.failUnlessEqual(NSAlertFirstButtonReturn, 1000)
        self.failUnlessEqual(NSAlertSecondButtonReturn, 1001)
        self.failUnlessEqual(NSAlertThirdButtonReturn, 1002)



    def testMethods(self):
        self.failUnlessArgIsPrintf(NSAlert.alertWithMessageText_defaultButton_alternateButton_otherButton_informativeTextWithFormat_, 4)
        self.failUnlessArgIsSEL(NSAlert.beginSheetModalForWindow_modalDelegate_didEndSelector_contextInfo_, 2, 'v@:@' + objc._C_NSInteger + '^v')
        self.failUnlessArgHasType(NSAlert.beginSheetModalForWindow_modalDelegate_didEndSelector_contextInfo_, 3, '^v')

        self.failUnlessResultIsBOOL(NSAlert.showsHelp)
        self.failUnlessArgIsBOOL(NSAlert.setShowsHelp_, 0)

    @min_os_level('10.5')
    def testMethods10_5(self):
        self.failUnlessResultIsBOOL(NSAlert.showsSuppressionButton)
        self.failUnlessArgIsBOOL(NSAlert.setShowsSuppressionButton_, 0)

    def testProtocols(self):
        self.failUnlessResultIsBOOL(TestNSAlertHelper.alertShowHelp_)


if __name__ == "__main__":
    main()
