
from PyObjCTools.TestSupport import *
from LaunchServices import *

class TestLSInfo (TestCase):
    def testConstants(self):
        self.assertEqual(kLSAppInTrashErr, -10660)
        self.assertEqual(kLSExecutableIncorrectFormat, -10661)
        self.assertEqual(kLSAttributeNotFoundErr, -10662)
        self.assertEqual(kLSAttributeNotSettableErr, -10663)
        self.assertEqual(kLSUnknownErr, -10810)
        self.assertEqual(kLSNotAnApplicationErr, -10811)
        self.assertEqual(kLSNotInitializedErr, -10812)
        self.assertEqual(kLSDataUnavailableErr, -10813)
        self.assertEqual(kLSApplicationNotFoundErr, -10814)
        self.assertEqual(kLSUnknownTypeErr, -10815)
        self.assertEqual(kLSDataTooOldErr, -10816)
        self.assertEqual(kLSDataErr, -10817)
        self.assertEqual(kLSLaunchInProgressErr, -10818)
        self.assertEqual(kLSNotRegisteredErr, -10819)
        self.assertEqual(kLSAppDoesNotClaimTypeErr, -10820)
        self.assertEqual(kLSAppDoesNotSupportSchemeWarning, -10821)
        self.assertEqual(kLSServerCommunicationErr, -10822)
        self.assertEqual(kLSCannotSetInfoErr, -10823)
        self.assertEqual(kLSNoRegistrationInfoErr, -10824)
        self.assertEqual(kLSIncompatibleSystemVersionErr, -10825)
        self.assertEqual(kLSNoLaunchPermissionErr, -10826)
        self.assertEqual(kLSNoExecutableErr, -10827)
        self.assertEqual(kLSNoClassicEnvironmentErr, -10828)
        self.assertEqual(kLSMultipleSessionsNotSupportedErr, -10829)
        self.assertEqual(kLSInitializeDefaults, 0x00000001)
        self.assertEqual(kLSMinCatInfoBitmap, 6154)
        self.assertEqual(kLSRequestExtension, 0x00000001)
        self.assertEqual(kLSRequestTypeCreator, 0x00000002)
        self.assertEqual(kLSRequestBasicFlagsOnly, 0x00000004)
        self.assertEqual(kLSRequestAppTypeFlags, 0x00000008)
        self.assertEqual(kLSRequestAllFlags, 0x00000010)
        self.assertEqual(kLSRequestIconAndKind, 0x00000020)
        self.assertEqual(kLSRequestExtensionFlagsOnly, 0x00000040)
        self.assertEqual(kLSRequestAllInfo, cast_int(0xFFFFFFFF))
        self.assertEqual(kLSItemInfoIsPlainFile, 0x00000001)
        self.assertEqual(kLSItemInfoIsPackage, 0x00000002)
        self.assertEqual(kLSItemInfoIsApplication, 0x00000004)
        self.assertEqual(kLSItemInfoIsContainer, 0x00000008)
        self.assertEqual(kLSItemInfoIsAliasFile, 0x00000010)
        self.assertEqual(kLSItemInfoIsSymlink, 0x00000020)
        self.assertEqual(kLSItemInfoIsInvisible, 0x00000040)
        self.assertEqual(kLSItemInfoIsNativeApp, 0x00000080)
        self.assertEqual(kLSItemInfoIsClassicApp, 0x00000100)
        self.assertEqual(kLSItemInfoAppPrefersNative, 0x00000200)
        self.assertEqual(kLSItemInfoAppPrefersClassic, 0x00000400)
        self.assertEqual(kLSItemInfoAppIsScriptable, 0x00000800)
        self.assertEqual(kLSItemInfoIsVolume, 0x00001000)
        self.assertEqual(kLSItemInfoExtensionIsHidden, 0x00100000)
        self.assertEqual(kLSRolesNone, 0x00000001)
        self.assertEqual(kLSRolesViewer, 0x00000002)
        self.assertEqual(kLSRolesEditor, 0x00000004)
        self.assertEqual(kLSRolesShell, 0x00000008)
        self.assertEqual(kLSRolesAll, cast_int(0xFFFFFFFF))
        self.assertEqual(kLSUnknownKindID, 0)
        self.assertEqual(kLSUnknownType, 0)
        self.assertEqual(kLSUnknownCreator, 0)
        self.assertEqual(kLSAcceptDefault, 0x00000001)
        self.assertEqual(kLSAcceptAllowLoginUI, 0x00000002)

    def testFunctions(self):
        LSInit(kLSInitializeDefaults)
        LSTerm()

        path = "/Library/Documents/Acknowledgements.rtf"
        url = CFURLCreateFromFileSystemRepresentation(None, path, len(path), True)
        self.assertIsInstance(url, CFURLRef)

        ok, info = LSCopyItemInfoForURL(url, kLSRequestExtension|kLSRequestTypeCreator, None)
        self.assertEqual(ok, 0)
        self.assertIsInstance(info, LSItemInfoRecord)

        self.fail("Start at LSGetExtensionInfo")



    def testFSRef(self):
        self.fail('LSCopyItemInfoForRef')
        


if __name__ == "__main__":
    main()
