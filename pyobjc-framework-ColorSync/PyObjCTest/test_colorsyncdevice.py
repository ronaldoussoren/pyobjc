import sys
from PyObjCTools.TestSupport import *

if sys.maxsize > 2 ** 32:
    import ColorSync

    class TestColorSyncDevice (TestCase):
        def testConstants(self):
            self.assertIsInstance(ColorSync.kColorSyncDeviceID, unicode)
            self.assertIsInstance(ColorSync.kColorSyncDeviceClass, unicode)
            self.assertIsInstance(ColorSync.kColorSyncCameraDeviceClass, unicode)
            self.assertIsInstance(ColorSync.kColorSyncDisplayDeviceClass, unicode)
            self.assertIsInstance(ColorSync.kColorSyncPrinterDeviceClass, unicode)
            self.assertIsInstance(ColorSync.kColorSyncScannerDeviceClass, unicode)
            self.assertIsInstance(ColorSync.kColorSyncDeviceProfileURL, unicode)
            self.assertIsInstance(ColorSync.kColorSyncDeviceDescription, unicode)
            self.assertIsInstance(ColorSync.kColorSyncDeviceDescriptions, unicode)
            self.assertIsInstance(ColorSync.kColorSyncFactoryProfiles, unicode)
            self.assertIsInstance(ColorSync.kColorSyncCustomProfiles, unicode)
            self.assertIsInstance(ColorSync.kColorSyncDeviceModeDescription, unicode)
            self.assertIsInstance(ColorSync.kColorSyncDeviceModeDescriptions, unicode)
            self.assertIsInstance(ColorSync.kColorSyncDeviceDefaultProfileID, unicode)
            self.assertIsInstance(ColorSync.kColorSyncDeviceHostScope, unicode)
            self.assertIsInstance(ColorSync.kColorSyncDeviceUserScope, unicode)
            self.assertIsInstance(ColorSync.kColorSyncProfileHostScope, unicode)
            self.assertIsInstance(ColorSync.kColorSyncProfileUserScope, unicode)
            self.assertIsInstance(ColorSync.kColorSyncDeviceProfileIsFactory, unicode)
            self.assertIsInstance(ColorSync.kColorSyncDeviceProfileIsDefault, unicode)
            self.assertIsInstance(ColorSync.kColorSyncDeviceProfileIsCurrent, unicode)
            self.assertIsInstance(ColorSync.kColorSyncDeviceProfileID, unicode)
            self.assertIsInstance(ColorSync.kColorSyncDeviceRegisteredNotification, unicode)
            self.assertIsInstance(ColorSync.kColorSyncDeviceUnregisteredNotification, unicode)
            self.assertIsInstance(ColorSync.kColorSyncDeviceProfilesNotification, unicode)
            self.assertIsInstance(ColorSync.kColorSyncDisplayDeviceProfilesNotification, unicode)
            self.assertIsInstance(ColorSync.kColorSyncProfileRepositoryChangeNotification, unicode)
            self.assertIsInstance(ColorSync.kColorSyncRegistrationUpdateWindowServer, unicode)

    def testFunctions(self):
        ColorSync.ColorSyncRegisterDevice
        ColorSync.ColorSyncUnregisterDevice
        ColorSync.ColorSyncDeviceSetCustomProfiles
        self.assertResultIsCFRetained(ColorSync.ColorSyncDeviceCopyDeviceInfo)
        self.assertArgIsFunction(ColorSync.ColorSyncIterateDeviceProfiles, 0, objc._C_BOOL + b'@^v', False)
        self.assertResultIsCFRetained(ColorSync.CGDisplayCreateUUIDFromDisplayID)

        ColorSync.CGDisplayGetDisplayIDFromUUID



if __name__ == "__main__":
    main()
