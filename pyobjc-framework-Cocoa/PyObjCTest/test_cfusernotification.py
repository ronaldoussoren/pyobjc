from PyObjCTools.TestSupport import *
from CoreFoundation import *

try:
    unicode
except NameError:
    unicode = str


try:
    long
except NameError:
    long = int

class TestUserNotification (TestCase):
    def testTypes(self):
        self.assertIsCFType(CFUserNotificationRef)

    def testTypeID(self):
        id = CFUserNotificationGetTypeID()
        self.assertIsInstance(id, (int, long))

    def testCreation(self):
        runloop_mode = kCFRunLoopDefaultMode
        runloop_mode = b"pyobjctest.cfusernotificaton".decode('ascii')

        rl = CFRunLoopGetCurrent()

        infoDict = {
                kCFUserNotificationAlertHeaderKey: b"Alert Header".decode('ascii'),
                kCFUserNotificationProgressIndicatorValueKey: True,
                kCFUserNotificationDefaultButtonTitleKey: "Cancel"
        }

        self.assertArgIsOut(CFUserNotificationCreate, 3)
        ref, error = CFUserNotificationCreate(None,
                1.0, 0, None, infoDict)
        self.assertEqual(error , 0 )
        self.assertIsInstance(ref, CFUserNotificationRef)
        values = []
        @objc.callbackFor(CFUserNotificationCreateRunLoopSource)
        def callout(notification, flags):
            values.append((notification, flags))

        self.assertArgIsFunction(CFUserNotificationCreateRunLoopSource, 2, b'v^{__CFUserNotification=}' + objc._C_NSInteger, True)
        rls = CFUserNotificationCreateRunLoopSource(None, ref, callout, 1)
        self.assertIsInstance(rls, CFRunLoopSourceRef)
        CFRunLoopAddSource(rl, rls, runloop_mode)
        CFRunLoopRunInMode(runloop_mode, 2.0, True)

        CFUserNotificationCancel(ref)
        CFRunLoopRunInMode(runloop_mode, 5.0, True)
        CFRunLoopRemoveSource(rl, rls, runloop_mode)

        self.assertEqual(len(values), 1)
        self.assertIs(values[0][0], ref)
        self.assertIsInstance(values[0][1], (int, long))

        self.assertArgIsOut(CFUserNotificationReceiveResponse, 2)
        error, flags = CFUserNotificationReceiveResponse(ref, 1.0, None)
        self.assertIsInstance(error, (int, long))
        self.assertIsInstance(flags, (int, long))
        v = CFUserNotificationGetResponseDictionary(ref)
        if v is not None:
            self.assertIsInstance(v, CFDictionaryRef)
        error = CFUserNotificationUpdate(ref, 2.0, 0, infoDict)
        self.assertEqual(error , 0)
        error = CFUserNotificationCancel(ref)
        self.assertEqual(error, 0)

        v = CFUserNotificationGetResponseValue(ref, kCFUserNotificationTextFieldValuesKey, 0)
        if v is not None:
            self.assertIsInstance(v, unicode)

    def testAlert(self):
        err, flags = CFUserNotificationDisplayAlert(0.1, 0, None, None, None, "Header", "Message", "Cancel", None, None, None)
        self.assertEqual(err , 0)
        self.assertIsInstance(flags, (int, long))
        err, flags = CFUserNotificationDisplayAlert(0.1, 0, None, None, None, "Header", "Message", "Cancel", "OK", "Rest", None)
        self.assertEqual(err , 0)
        self.assertIsInstance(flags, (int, long))

    def testNotice(self):
        err = CFUserNotificationDisplayNotice(0.1, 0, None, None, None, "Header", "Message", "Cancel")
        self.assertEqual(err , 0)

    def testInlines(self):
        flag = CFUserNotificationCheckBoxChecked(2)
        self.assertEqual(flag , 1 << 10 )
        flag = CFUserNotificationSecureTextField(2)
        self.assertEqual(flag , 1 << 18 )
        flag = CFUserNotificationPopUpSelection(2)
        self.assertEqual(flag , 2 << 24 )

    def testConstants(self):
        self.assertEqual(kCFUserNotificationStopAlertLevel       , 0)
        self.assertEqual(kCFUserNotificationNoteAlertLevel       , 1)
        self.assertEqual(kCFUserNotificationCautionAlertLevel    , 2)
        self.assertEqual(kCFUserNotificationPlainAlertLevel      , 3)
        self.assertEqual(kCFUserNotificationDefaultResponse      , 0)
        self.assertEqual(kCFUserNotificationAlternateResponse    , 1)
        self.assertEqual(kCFUserNotificationOtherResponse        , 2)
        self.assertEqual(kCFUserNotificationCancelResponse       , 3)
        self.assertEqual(kCFUserNotificationNoDefaultButtonFlag  , (1 << 5))
        self.assertEqual(kCFUserNotificationUseRadioButtonsFlag  , (1 << 6))
        self.assertIsInstance(kCFUserNotificationIconURLKey, unicode)
        self.assertIsInstance(kCFUserNotificationSoundURLKey, unicode)
        self.assertIsInstance(kCFUserNotificationLocalizationURLKey, unicode)
        self.assertIsInstance(kCFUserNotificationAlertHeaderKey, unicode)
        self.assertIsInstance(kCFUserNotificationAlertMessageKey, unicode)
        self.assertIsInstance(kCFUserNotificationDefaultButtonTitleKey, unicode)
        self.assertIsInstance(kCFUserNotificationAlternateButtonTitleKey, unicode)
        self.assertIsInstance(kCFUserNotificationOtherButtonTitleKey, unicode)
        self.assertIsInstance(kCFUserNotificationProgressIndicatorValueKey, unicode)
        self.assertIsInstance(kCFUserNotificationPopUpTitlesKey, unicode)
        self.assertIsInstance(kCFUserNotificationTextFieldTitlesKey, unicode)
        self.assertIsInstance(kCFUserNotificationCheckBoxTitlesKey, unicode)
        self.assertIsInstance(kCFUserNotificationTextFieldValuesKey, unicode)
        self.assertIsInstance(kCFUserNotificationPopUpSelectionKey, unicode)


if __name__ == "__main__":
    main()
