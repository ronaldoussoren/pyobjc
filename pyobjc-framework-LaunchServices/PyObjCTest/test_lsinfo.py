
from PyObjCTools.TestSupport import *
from LaunchServices import *

class TestLSInfo (TestCase):
    def testConstants(self):
        self.failUnlessEqual(kLSAppInTrashErr, -10660)
        self.failUnlessEqual(kLSExecutableIncorrectFormat, -10661)
        self.failUnlessEqual(kLSAttributeNotFoundErr, -10662)
        self.failUnlessEqual(kLSAttributeNotSettableErr, -10663)
        self.failUnlessEqual(kLSUnknownErr, -10810)
        self.failUnlessEqual(kLSNotAnApplicationErr, -10811)
        self.failUnlessEqual(kLSNotInitializedErr, -10812)
        self.failUnlessEqual(kLSDataUnavailableErr, -10813)
        self.failUnlessEqual(kLSApplicationNotFoundErr, -10814)
        self.failUnlessEqual(kLSUnknownTypeErr, -10815)
        self.failUnlessEqual(kLSDataTooOldErr, -10816)
        self.failUnlessEqual(kLSDataErr, -10817)
        self.failUnlessEqual(kLSLaunchInProgressErr, -10818)
        self.failUnlessEqual(kLSNotRegisteredErr, -10819)
        self.failUnlessEqual(kLSAppDoesNotClaimTypeErr, -10820)
        self.failUnlessEqual(kLSAppDoesNotSupportSchemeWarning, -10821)
        self.failUnlessEqual(kLSServerCommunicationErr, -10822)
        self.failUnlessEqual(kLSCannotSetInfoErr, -10823)
        self.failUnlessEqual(kLSNoRegistrationInfoErr, -10824)
        self.failUnlessEqual(kLSIncompatibleSystemVersionErr, -10825)
        self.failUnlessEqual(kLSNoLaunchPermissionErr, -10826)
        self.failUnlessEqual(kLSNoExecutableErr, -10827)
        self.failUnlessEqual(kLSNoClassicEnvironmentErr, -10828)
        self.failUnlessEqual(kLSMultipleSessionsNotSupportedErr, -10829)
        self.failUnlessEqual(kLSInitializeDefaults, 0x00000001)
        self.failUnlessEqual(kLSMinCatInfoBitmap, 6154)
        self.failUnlessEqual(kLSRequestExtension, 0x00000001)
        self.failUnlessEqual(kLSRequestTypeCreator, 0x00000002)
        self.failUnlessEqual(kLSRequestBasicFlagsOnly, 0x00000004)
        self.failUnlessEqual(kLSRequestAppTypeFlags, 0x00000008)
        self.failUnlessEqual(kLSRequestAllFlags, 0x00000010)
        self.failUnlessEqual(kLSRequestIconAndKind, 0x00000020)
        self.failUnlessEqual(kLSRequestExtensionFlagsOnly, 0x00000040)
        self.failUnlessEqual(kLSRequestAllInfo, cast_int(0xFFFFFFFF))
        self.failUnlessEqual(kLSItemInfoIsPlainFile, 0x00000001)
        self.failUnlessEqual(kLSItemInfoIsPackage, 0x00000002)
        self.failUnlessEqual(kLSItemInfoIsApplication, 0x00000004)
        self.failUnlessEqual(kLSItemInfoIsContainer, 0x00000008)
        self.failUnlessEqual(kLSItemInfoIsAliasFile, 0x00000010)
        self.failUnlessEqual(kLSItemInfoIsSymlink, 0x00000020)
        self.failUnlessEqual(kLSItemInfoIsInvisible, 0x00000040)
        self.failUnlessEqual(kLSItemInfoIsNativeApp, 0x00000080)
        self.failUnlessEqual(kLSItemInfoIsClassicApp, 0x00000100)
        self.failUnlessEqual(kLSItemInfoAppPrefersNative, 0x00000200)
        self.failUnlessEqual(kLSItemInfoAppPrefersClassic, 0x00000400)
        self.failUnlessEqual(kLSItemInfoAppIsScriptable, 0x00000800)
        self.failUnlessEqual(kLSItemInfoIsVolume, 0x00001000)
        self.failUnlessEqual(kLSItemInfoExtensionIsHidden, 0x00100000)
        self.failUnlessEqual(kLSRolesNone, 0x00000001)
        self.failUnlessEqual(kLSRolesViewer, 0x00000002)
        self.failUnlessEqual(kLSRolesEditor, 0x00000004)
        self.failUnlessEqual(kLSRolesShell, 0x00000008)
        self.failUnlessEqual(kLSRolesAll, cast_int(0xFFFFFFFF))
        self.failUnlessEqual(kLSUnknownKindID, 0)
        self.failUnlessEqual(kLSUnknownType, 0)
        self.failUnlessEqual(kLSUnknownCreator, 0)
        self.failUnlessEqual(kLSAcceptDefault, 0x00000001)
        self.failUnlessEqual(kLSAcceptAllowLoginUI, 0x00000002)

    def testFunctions(self):
        LSInit(kLSInitializeDefaults)
        LSTerm()

        path = "/Library/Documents/Acknowledgements.rtf"
        url = CFURLCreateFromFileSystemRepresentation(None, path, len(path), True)
        self.failUnlessIsInstance(url, CFURLRef)

        ok, info = LSCopyItemInfoForURL(url, kLSRequestExtension|kLSRequestTypeCreator, None)
        self.failUnlessEqual(ok, 0)
        self.failUnlessIsInstance(info, LSItemInfoRecord)

        self.fail("Start at LSGetExtensionInfo")



    def testFSRef(self):
        self.fail('LSCopyItemInfoForRef')
        


if __name__ == "__main__":
    main()
