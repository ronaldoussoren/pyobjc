
from PyObjCTools.TestSupport import *
from LaunchServices import *
import sys
import os

class TestLSInfo (TestCase):
    def setUp(self):
        self.path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'dummy.txt')
        fp = open(self.path, 'w')
        fp.write('test contents')
        fp.close()

    def tearDown(self):
        if os.path.exists(self.path):
            os.unlink(self.path)

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

        self.assertIsInstance(kLSItemContentType, unicode)
        self.assertIsInstance(kLSItemFileType, unicode)
        self.assertIsInstance(kLSItemFileCreator, unicode)
        self.assertIsInstance(kLSItemExtension, unicode)
        self.assertIsInstance(kLSItemDisplayName, unicode)
        self.assertIsInstance(kLSItemDisplayKind, unicode)
        self.assertIsInstance(kLSItemRoleHandlerDisplayName, unicode)
        self.assertIsInstance(kLSItemIsInvisible, unicode)
        self.assertIsInstance(kLSItemExtensionIsHidden, unicode)
        self.assertIsInstance(kLSItemQuarantineProperties, unicode)


        self.assertEqual(kLSHandlerOptionsDefault, 0)
        self.assertEqual(kLSHandlerOptionsIgnoreCreator, 1)


    def testStructs(self):
        v = LSItemInfoRecord()
        self.assertHasAttr(v, 'flags')
        self.assertHasAttr(v, 'filetype')
        self.assertHasAttr(v, 'creator')
        self.assertHasAttr(v, 'extension')
        if sys.maxint < 2 ** 32:
            self.assertHasAttr(v, 'iconFileName')
            self.assertHasAttr(v, 'kindID')
        else:
            self.assertNotHasAttr(v, 'iconFileName')
            self.assertNotHasAttr(v, 'kindID')

    def testFunctions(self):
        LSInit(kLSInitializeDefaults)
        LSTerm()

        url = CFURLCreateFromFileSystemRepresentation(None, self.path, len(self.path), True)
        self.assertIsInstance(url, CFURLRef)

        ok, info = LSCopyItemInfoForURL(url, kLSRequestExtension|kLSRequestTypeCreator, None)
        self.assertEqual(ok, 0)
        self.assertIsInstance(info, LSItemInfoRecord)

        self.assertArgIsOut(LSGetExtensionInfo, 2)
        ok, info = LSGetExtensionInfo(len(self.path), self.path, None)
        self.failUnlessEqual(ok, 0)
        self.failUnlessEqual(info, self.path.index('.')+1)

        self.assertArgIsOut(LSCopyDisplayNameForURL, 1)
        self.assertArgIsCFRetained(LSCopyDisplayNameForURL, 1)
        ok, info = LSCopyDisplayNameForURL(url, None)
        self.assertEquals(ok, 0)
        self.assertIsInstance(info, unicode)

        self.assertArgIsBOOL(LSSetExtensionHiddenForURL, 1)
        ok = LSSetExtensionHiddenForURL(url, True)
        self.assertEquals(ok, 0)

        self.assertArgIsOut(LSCopyKindStringForURL, 1)
        self.assertArgIsCFRetained(LSCopyKindStringForURL, 1)
        ok, info = LSCopyKindStringForURL(url, None)
        self.assertEquals(ok, 0)
        self.assertIsInstance(info, unicode)

        self.assertArgIsOut(LSCopyKindStringForTypeInfo, 3)
        self.assertArgIsCFRetained(LSCopyKindStringForTypeInfo, 3)
        ok, info = LSCopyKindStringForTypeInfo(kLSUnknownType, kLSUnknownCreator, "jpg", None)
        self.assertEquals(ok, 0)
        self.assertIsInstance(info, unicode)

        self.assertArgIsOut(LSCopyKindStringForMIMEType, 1)
        self.assertArgIsCFRetained(LSCopyKindStringForMIMEType, 1)
        ok, info = LSCopyKindStringForMIMEType("image/jpeg", None)
        self.assertEquals(ok, 0)
        self.assertIsInstance(info, unicode)

        self.assertArgIsOut(LSGetApplicationForInfo, 4)
        self.assertArgIsOut(LSGetApplicationForInfo, 5)
        self.assertArgIsCFRetained(LSGetApplicationForInfo, 5)
        ok, ref, url = LSGetApplicationForInfo(kLSUnknownType, kLSUnknownCreator, "txt", kLSRolesAll, None, None)
        self.assertEquals(ok, 0)
        self.assertIsInstance(ref, objc.FSRef)
        self.assertIsInstance(url, CFURLRef)
        
        self.assertArgIsOut(LSCopyApplicationForMIMEType, 2)
        self.assertArgIsCFRetained(LSGetApplicationForInfo, 2)
        ok, url = LSCopyApplicationForMIMEType("text/plain", kLSRolesAll, None)
        self.assertEquals(ok, 0)
        self.assertIsInstance(url, CFURLRef)

        self.assertArgIsOut(LSGetApplicationForURL, 2)
        self.assertArgIsOut(LSGetApplicationForURL, 3)
        self.assertArgIsCFRetained(LSGetApplicationForURL, 3)
        ok, ref, url = LSGetApplicationForURL(url, kLSRolesAll, None)
        self.assertEquals(ok, 0)
        self.assertIsInstance(ref, objc.FSRef)
        self.assertIsInstance(url, CFURLRef)

        self.assertArgIsOut(LSGetApplicationForURL, 3)
        self.assertArgIsOut(LSGetApplicationForURL, 4)
        self.assertArgIsCFRetained(LSGetApplicationForURL, 4)
        ok, ref, url = LSGetApplicationForURL(kLSUnknownCreator, None, self.path, None, None)
        self.assertEquals(ok, 0)
        self.assertIsInstance(ref, objc.FSRef)
        self.assertIsInstance(url, CFURLRef)

        self.assertArgIsOut(LSCanURLAcceptURL, 4)
        ok, status = LSCanURLAcceptURL(url, url, kLSRolesAll, kLSAcceptDefault, None)
        self.assertIsInstance(ok, (int, long))
        self.assertIsInstance(status, bool)

        ok = LSRegisterURL(url, False)
        self.assertIsInstance(ok, (int, long))


        v = LSCopyApplicationURLsForURL(url, kLSRolesAll)
        self.assertIsInstance(v, CFArrayRef)
        for a in v:
            self.assertIsInstance(a, CFURLRef)

        
        default_role = LSCopyDefaultRoleHandlerForContentType("text.plain", kLSRolesAll)
        self.assertIsInstance(default_role, unicode)

        v = LSCopyAllRoleHandlersForContentType("text.plain", kLSRolesAll)
        self.assertIsInstance(v, CFArrayRef)
        for a in v:
            self.assertIsInstance(a, unicode)


        ok = LSSetDefaultRoleHandlerForContentType("text.plain", kLSRolesAll, default_role)
        self.assertIsInstance(ok, (int, long))

        v = LSGetHandlerOptionsForContentType("text.plain")
        self.assertIsInstance(v, (int, long))

        ok = LSSetHandlerOptionsForContentType("text.plain", v)
        self.assertIsInstance(ok, (int, long))

        self.assertResultIsCFRetained(LSCopyDefaultHandlerForURLScheme)
        default_handler = LSCopyDefaultHandlerForURLScheme("http")
        self.assertIsInstance(default_handler, unicode)

        self.assertResultIsCFRetained(LSCopyAllHandlersForURLScheme)
        v = LSCopyAllHandlersForURLScheme("http")
        self.assertIsInstance(v, CFArrayRef)
        for a in v:
            self.assertIsInstance(a, unicode)

        ok = LSSetDefaultHandlerForURLScheme("http", default_handler)
        self.assertIsInstance(ok, (int, long))









    def testFSRef(self):
        self.fail('LSCopyItemInfoForRef')
        self.fail('LSCopyDisplayNameForRef')
        self.fail('LSSetExtensionHiddenForRef')
        self.fail('LSCopyKindStringForRef')
        self.fail('LSGetApplicationForItem')
        self.fail('LSCanRefAcceptItem')
        self.fail('LSRegisterFSRef')
        self.fail('LSCopyItemAttribute')
        self.fail('LSSetItemAttribute')

        


if __name__ == "__main__":
    main()
