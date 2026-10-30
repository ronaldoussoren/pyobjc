import AppKit
from PyObjCTools.TestSupport import TestCase, min_sdk_level
import objc


class TestNSAlertHelper(AppKit.NSObject):
    def alertShowHelp_(self, alert):
        return 1


class TestNSAlert(TestCase):
    def test_enums(self):
        # Legacy (NSAlertStyle)
        self.assertEqual(AppKit.NSWarningAlertStyle, 0)
        self.assertEqual(AppKit.NSInformationalAlertStyle, 1)
        self.assertEqual(AppKit.NSCriticalAlertStyle, 2)

        self.assertIsEnumType(AppKit.NSAlertStyle)
        self.assertEqual(AppKit.NSAlertStyleWarning, 0)
        self.assertEqual(AppKit.NSAlertStyleInformational, 1)
        self.assertEqual(AppKit.NSAlertStyleCritical, 2)

        self.assertIsEnumType(AppKit.NSModalResponse)
        self.assertEqual(AppKit.NSAlertFirstButtonReturn, 1000)
        self.assertEqual(AppKit.NSAlertSecondButtonReturn, 1001)
        self.assertEqual(AppKit.NSAlertThirdButtonReturn, 1002)

    def test_methods(self):
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

        self.assertResultIsBOOL(AppKit.NSAlert.showsSuppressionButton)
        self.assertArgIsBOOL(AppKit.NSAlert.setShowsSuppressionButton_, 0)

        self.assertArgIsBlock(
            AppKit.NSAlert.beginSheetModalForWindow_completionHandler_,
            1,
            b"v" + objc._C_NSInteger,
        )

    @min_sdk_level("10.10")
    def test_protocols10_10(self):
        self.assertProtocolExists("NSAlertDelegate", AppKit)

    def test_protocol_methods(self):
        self.assertResultIsBOOL(TestNSAlertHelper.alertShowHelp_)
