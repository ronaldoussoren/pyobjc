
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

        self.assertEqual(NSAlertStyleWarning, 0)
        self.assertEqual(NSAlertStyleInformational, 1)
        self.assertEqual(NSAlertStyleCritical, 2)

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

    @min_os_level('10.9')
    def testMethods10_9(self):
        self.assertArgIsBlock(NSAlert.beginSheetModalForWindow_completionHandler_, 1, b'v' + objc._C_NSInteger)

    def testProtocols(self):
        self.assertResultIsBOOL(TestNSAlertHelper.alertShowHelp_)

    @min_sdk_level('10.10')
    def testProtocolObjects(self):
        objc.protocolNamed('NSAlertDelegate')


if __name__ == "__main__":
    main()
