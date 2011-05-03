
from PyObjCTools.TestSupport import *
from AppKit import *

class TestNSAlertHelper (NSObject):
    def alertShowHelp_(self, alert):
        return 1

class TestNSAlert (TestCase):
    def testConstants(self):
        self.assertEqual(NSWarningAlertStyle, 0)
        self.assertEqual(NSInformationalAlertStyle, 1)
        self.assertEqual(NSCriticalAlertStyle, 2)
        self.assertEqual(NSAlertFirstButtonReturn, 1000)
        self.assertEqual(NSAlertSecondButtonReturn, 1001)
        self.assertEqual(NSAlertThirdButtonReturn, 1002)



    def testMethods(self):
        self.assertArgIsPrintf(NSAlert.alertWithMessageText_defaultButton_alternateButton_otherButton_informativeTextWithFormat_, 4)
        self.assertArgIsSEL(NSAlert.beginSheetModalForWindow_modalDelegate_didEndSelector_contextInfo_, 2, b'v@:@' + objc._C_NSInteger + b'^v')
        self.assertArgHasType(NSAlert.beginSheetModalForWindow_modalDelegate_didEndSelector_contextInfo_, 3, b'^v')

        self.assertResultIsBOOL(NSAlert.showsHelp)
        self.assertArgIsBOOL(NSAlert.setShowsHelp_, 0)

    @min_os_level('10.5')
    def testMethods10_5(self):
        self.assertResultIsBOOL(NSAlert.showsSuppressionButton)
        self.assertArgIsBOOL(NSAlert.setShowsSuppressionButton_, 0)

    def testProtocols(self):
        self.assertResultIsBOOL(TestNSAlertHelper.alertShowHelp_)


if __name__ == "__main__":
    main()
