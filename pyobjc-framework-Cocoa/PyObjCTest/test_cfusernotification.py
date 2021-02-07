import CoreFoundation
from PyObjCTools.TestSupport import TestCase
import objc


class TestUserNotification(TestCase):
    def testTypes(self):
        self.assertIsCFType(CoreFoundation.CFUserNotificationRef)

    def testTypeID(self):
        value = CoreFoundation.CFUserNotificationGetTypeID()
        self.assertIsInstance(value, int)

    def testCreation(self):
        runloop_mode = CoreFoundation.kCFRunLoopDefaultMode
        runloop_mode = "pyobjctest.cfusernotificaton"

        rl = CoreFoundation.CFRunLoopGetCurrent()

        infoDict = {
            CoreFoundation.kCFUserNotificationAlertHeaderKey: b"Alert Header".decode(
                "ascii"
            ),
            CoreFoundation.kCFUserNotificationProgressIndicatorValueKey: True,
            CoreFoundation.kCFUserNotificationDefaultButtonTitleKey: "Cancel",
        }

        self.assertArgIsOut(CoreFoundation.CFUserNotificationCreate, 3)
        ref, error = CoreFoundation.CFUserNotificationCreate(
            None, 3.0, 0, None, infoDict
        )
        self.assertEqual(error, 0)
        self.assertIsInstance(ref, CoreFoundation.CFUserNotificationRef)
        values = []

        @objc.callbackFor(CoreFoundation.CFUserNotificationCreateRunLoopSource)
        def callout(notification, flags):
            values.append((notification, flags))
            CoreFoundation.CFRunLoopStop(rl)

        self.assertArgIsFunction(
            CoreFoundation.CFUserNotificationCreateRunLoopSource,
            2,
            b"v^{__CFUserNotification=}" + objc._C_NSInteger,
            True,
        )
        rls = CoreFoundation.CFUserNotificationCreateRunLoopSource(
            None, ref, callout, 1
        )
        self.assertIsInstance(rls, CoreFoundation.CFRunLoopSourceRef)
        CoreFoundation.CFRunLoopAddSource(rl, rls, runloop_mode)
        CoreFoundation.CFRunLoopRunInMode(runloop_mode, 5.0, True)

        CoreFoundation.CFUserNotificationCancel(ref)
        CoreFoundation.CFRunLoopRunInMode(runloop_mode, 5.0, True)
        CoreFoundation.CFRunLoopRemoveSource(rl, rls, runloop_mode)

        self.assertEqual(len(values), 1)
        self.assertIs(values[0][0], ref)
        self.assertIsInstance(values[0][1], int)

        self.assertArgIsOut(CoreFoundation.CFUserNotificationReceiveResponse, 2)
        error, flags = CoreFoundation.CFUserNotificationReceiveResponse(ref, 1.0, None)
        self.assertIsInstance(error, int)
        self.assertIsInstance(flags, int)
        v = CoreFoundation.CFUserNotificationGetResponseDictionary(ref)
        if v is not None:
            self.assertIsInstance(v, CoreFoundation.CFDictionaryRef)
        error = CoreFoundation.CFUserNotificationUpdate(ref, 2.0, 0, infoDict)
        self.assertEqual(error, 0)
        error = CoreFoundation.CFUserNotificationCancel(ref)
        self.assertEqual(error, 0)

        v = CoreFoundation.CFUserNotificationGetResponseValue(
            ref, CoreFoundation.kCFUserNotificationTextFieldValuesKey, 0
        )
        if v is not None:
            self.assertIsInstance(v, str)

    def testAlert(self):
        err, flags = CoreFoundation.CFUserNotificationDisplayAlert(
            0.1, 0, None, None, None, "Header", "Message", "Cancel", None, None, None
        )
        self.assertEqual(err, 0)
        self.assertIsInstance(flags, int)
        err, flags = CoreFoundation.CFUserNotificationDisplayAlert(
            0.1, 0, None, None, None, "Header", "Message", "Cancel", "OK", "Rest", None
        )
        self.assertEqual(err, 0)
        self.assertIsInstance(flags, int)

    def testNotice(self):
        err = CoreFoundation.CFUserNotificationDisplayNotice(
            0.1, 0, None, None, None, "Header", "Message", "Cancel"
        )
        self.assertEqual(err, 0)

    def testInlines(self):
        flag = CoreFoundation.CFUserNotificationCheckBoxChecked(2)
        self.assertEqual(flag, 1 << 10)
        flag = CoreFoundation.CFUserNotificationSecureTextField(2)
        self.assertEqual(flag, 1 << 18)
        flag = CoreFoundation.CFUserNotificationPopUpSelection(2)
        self.assertEqual(flag, 2 << 24)

    def testConstants(self):
        self.assertEqual(CoreFoundation.kCFUserNotificationStopAlertLevel, 0)
        self.assertEqual(CoreFoundation.kCFUserNotificationNoteAlertLevel, 1)
        self.assertEqual(CoreFoundation.kCFUserNotificationCautionAlertLevel, 2)
        self.assertEqual(CoreFoundation.kCFUserNotificationPlainAlertLevel, 3)
        self.assertEqual(CoreFoundation.kCFUserNotificationDefaultResponse, 0)
        self.assertEqual(CoreFoundation.kCFUserNotificationAlternateResponse, 1)
        self.assertEqual(CoreFoundation.kCFUserNotificationOtherResponse, 2)
        self.assertEqual(CoreFoundation.kCFUserNotificationCancelResponse, 3)
        self.assertEqual(
            CoreFoundation.kCFUserNotificationNoDefaultButtonFlag, (1 << 5)
        )
        self.assertEqual(
            CoreFoundation.kCFUserNotificationUseRadioButtonsFlag, (1 << 6)
        )
        self.assertIsInstance(CoreFoundation.kCFUserNotificationIconURLKey, str)
        self.assertIsInstance(CoreFoundation.kCFUserNotificationSoundURLKey, str)
        self.assertIsInstance(CoreFoundation.kCFUserNotificationLocalizationURLKey, str)
        self.assertIsInstance(CoreFoundation.kCFUserNotificationAlertHeaderKey, str)
        self.assertIsInstance(CoreFoundation.kCFUserNotificationAlertMessageKey, str)
        self.assertIsInstance(
            CoreFoundation.kCFUserNotificationDefaultButtonTitleKey, str
        )
        self.assertIsInstance(
            CoreFoundation.kCFUserNotificationAlternateButtonTitleKey, str
        )
        self.assertIsInstance(
            CoreFoundation.kCFUserNotificationOtherButtonTitleKey, str
        )
        self.assertIsInstance(
            CoreFoundation.kCFUserNotificationProgressIndicatorValueKey, str
        )
        self.assertIsInstance(CoreFoundation.kCFUserNotificationPopUpTitlesKey, str)
        self.assertIsInstance(CoreFoundation.kCFUserNotificationTextFieldTitlesKey, str)
        self.assertIsInstance(CoreFoundation.kCFUserNotificationCheckBoxTitlesKey, str)
        self.assertIsInstance(CoreFoundation.kCFUserNotificationTextFieldValuesKey, str)
        self.assertIsInstance(CoreFoundation.kCFUserNotificationPopUpSelectionKey, str)
