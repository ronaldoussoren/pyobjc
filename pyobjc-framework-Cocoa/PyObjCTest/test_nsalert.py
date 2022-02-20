import AppKit
from PyObjCTools.TestSupport import TestCase, min_os_level, min_sdk_level
import objc


class TestNSAlertHelper(AppKit.NSObject):
    def alertShowHelp_(self, alert):
        return 1


class TestNSAlert(TestCase):
    def test_enum_types(self):
        self.assertIsEnumType(AppKit.NSAlertStyle)

    def testConstants(self):
        self.assertEqual(AppKit.NSWarningAlertStyle, 0)
        self.assertEqual(AppKit.NSInformationalAlertStyle, 1)
        self.assertEqual(AppKit.NSCriticalAlertStyle, 2)

        self.assertEqual(AppKit.NSAlertStyleWarning, 0)
        self.assertEqual(AppKit.NSAlertStyleInformational, 1)
        self.assertEqual(AppKit.NSAlertStyleCritical, 2)

        self.assertEqual(AppKit.NSAlertFirstButtonReturn, 1000)
        self.assertEqual(AppKit.NSAlertSecondButtonReturn, 1001)
        self.assertEqual(AppKit.NSAlertThirdButtonReturn, 1002)

    def testMethods(self):
        self.assertArgIsPrintf(
            AppKit.NSAlert.alertWithMessageText_defaultButton_alternateButton_otherButton_informativeTextWithFormat_,  # noqa: B950
            4,
        )
        self.assertArgIsSEL(
            AppKit.NSAlert.beginSheetModalForWindow_modalDelegate_didEndSelector_contextInfo_,
            2,
            b"v@:@" + objc._C_NSInteger + b"^v",
        )
        self.assertArgHasType(
            AppKit.NSAlert.beginSheetModalForWindow_modalDelegate_didEndSelector_contextInfo_,
            3,
            b"^v",
        )

        self.assertResultIsBOOL(AppKit.NSAlert.showsHelp)
        self.assertArgIsBOOL(AppKit.NSAlert.setShowsHelp_, 0)

    @min_os_level("10.5")
    def testMethods10_5(self):
        self.assertResultIsBOOL(AppKit.NSAlert.showsSuppressionButton)
        self.assertArgIsBOOL(AppKit.NSAlert.setShowsSuppressionButton_, 0)

    @min_os_level("10.9")
    def testMethods10_9(self):
        self.assertArgIsBlock(
            AppKit.NSAlert.beginSheetModalForWindow_completionHandler_,
            1,
            b"v" + objc._C_NSInteger,
        )

    def testProtocols(self):
        self.assertResultIsBOOL(TestNSAlertHelper.alertShowHelp_)

    @min_sdk_level("10.10")
    def testProtocolObjects(self):
        objc.protocolNamed("NSAlertDelegate")
