from PyObjCTools.TestSupport import TestCase
import objc
import ColorSync


class TestColorSyncDevice(TestCase):
    def testConstants(self):
        self.assertIsInstance(ColorSync.kColorSyncDeviceID, str)
        self.assertIsInstance(ColorSync.kColorSyncDeviceClass, str)
        self.assertIsInstance(ColorSync.kColorSyncCameraDeviceClass, str)
        self.assertIsInstance(ColorSync.kColorSyncDisplayDeviceClass, str)
        self.assertIsInstance(ColorSync.kColorSyncPrinterDeviceClass, str)
        self.assertIsInstance(ColorSync.kColorSyncScannerDeviceClass, str)
        self.assertIsInstance(ColorSync.kColorSyncDeviceProfileURL, str)
        self.assertIsInstance(ColorSync.kColorSyncDeviceDescription, str)
        self.assertIsInstance(ColorSync.kColorSyncDeviceDescriptions, str)
        self.assertIsInstance(ColorSync.kColorSyncFactoryProfiles, str)
        self.assertIsInstance(ColorSync.kColorSyncCustomProfiles, str)
        self.assertIsInstance(ColorSync.kColorSyncDeviceModeDescription, str)
        self.assertIsInstance(ColorSync.kColorSyncDeviceModeDescriptions, str)
        self.assertIsInstance(ColorSync.kColorSyncDeviceDefaultProfileID, str)
        self.assertIsInstance(ColorSync.kColorSyncDeviceHostScope, str)
        self.assertIsInstance(ColorSync.kColorSyncDeviceUserScope, str)
        self.assertIsInstance(ColorSync.kColorSyncProfileHostScope, str)
        self.assertIsInstance(ColorSync.kColorSyncProfileUserScope, str)
        self.assertIsInstance(ColorSync.kColorSyncDeviceProfileIsFactory, str)
        self.assertIsInstance(ColorSync.kColorSyncDeviceProfileIsDefault, str)
        self.assertIsInstance(ColorSync.kColorSyncDeviceProfileIsCurrent, str)
        self.assertIsInstance(ColorSync.kColorSyncDeviceProfileID, str)
        self.assertIsInstance(ColorSync.kColorSyncDeviceRegisteredNotification, str)
        self.assertIsInstance(ColorSync.kColorSyncDeviceUnregisteredNotification, str)
        self.assertIsInstance(ColorSync.kColorSyncDeviceProfilesNotification, str)
        self.assertIsInstance(
            ColorSync.kColorSyncDisplayDeviceProfilesNotification, str
        )
        self.assertIsInstance(
            ColorSync.kColorSyncProfileRepositoryChangeNotification, str
        )
        self.assertIsInstance(ColorSync.kColorSyncRegistrationUpdateWindowServer, str)

    def testFunctions(self):
        ColorSync.ColorSyncRegisterDevice
        ColorSync.ColorSyncUnregisterDevice
        ColorSync.ColorSyncDeviceSetCustomProfiles
        self.assertResultIsCFRetained(ColorSync.ColorSyncDeviceCopyDeviceInfo)
        self.assertArgIsFunction(
            ColorSync.ColorSyncIterateDeviceProfiles,
            0,
            objc._C_BOOL + b"^{__CFDictionary=}^v",
            False,
        )
        self.assertResultIsCFRetained(ColorSync.CGDisplayCreateUUIDFromDisplayID)

        ColorSync.CGDisplayGetDisplayIDFromUUID
