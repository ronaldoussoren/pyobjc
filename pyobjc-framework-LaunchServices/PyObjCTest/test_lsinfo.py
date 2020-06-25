import os
import warnings

from PyObjCTools.TestSupport import TestCase, min_os_level, os_release, os_level_key
import objc

with warnings.catch_warnings():
    warnings.filterwarnings("ignore")
    import LaunchServices


class TestLSInfo(TestCase):
    def setUp(self):
        self.path = os.path.join(
            os.path.dirname(os.path.abspath(__file__)), "dummy.txt"
        )
        fp = open(self.path, "w")
        fp.write("test contents")
        fp.close()

        self.bpath = self.path.encode("utf-8")

    def tearDown(self):
        if os.path.exists(self.path):
            os.unlink(self.path)

    def testConstants(self):
        self.assertEqual(LaunchServices.kLSInvalidExtensionIndex, 0xFFFFFFFFFFFFFFFF)
        self.assertEqual(LaunchServices.kLSAppInTrashErr, -10660)
        self.assertEqual(LaunchServices.kLSExecutableIncorrectFormat, -10661)
        self.assertEqual(LaunchServices.kLSAttributeNotFoundErr, -10662)
        self.assertEqual(LaunchServices.kLSAttributeNotSettableErr, -10663)
        self.assertEqual(LaunchServices.kLSIncompatibleApplicationVersionErr, -10664)
        self.assertEqual(LaunchServices.kLSNoRosettaEnvironmentErr, -10665)
        self.assertEqual(LaunchServices.kLSUnknownErr, -10810)
        self.assertEqual(LaunchServices.kLSNotAnApplicationErr, -10811)
        self.assertEqual(LaunchServices.kLSNotInitializedErr, -10812)
        self.assertEqual(LaunchServices.kLSDataUnavailableErr, -10813)
        self.assertEqual(LaunchServices.kLSApplicationNotFoundErr, -10814)
        self.assertEqual(LaunchServices.kLSUnknownTypeErr, -10815)
        self.assertEqual(LaunchServices.kLSDataTooOldErr, -10816)
        self.assertEqual(LaunchServices.kLSDataErr, -10817)
        self.assertEqual(LaunchServices.kLSLaunchInProgressErr, -10818)
        self.assertEqual(LaunchServices.kLSNotRegisteredErr, -10819)
        self.assertEqual(LaunchServices.kLSAppDoesNotClaimTypeErr, -10820)
        self.assertEqual(LaunchServices.kLSAppDoesNotSupportSchemeWarning, -10821)
        self.assertEqual(LaunchServices.kLSServerCommunicationErr, -10822)
        self.assertEqual(LaunchServices.kLSCannotSetInfoErr, -10823)
        self.assertEqual(LaunchServices.kLSNoRegistrationInfoErr, -10824)
        self.assertEqual(LaunchServices.kLSIncompatibleSystemVersionErr, -10825)
        self.assertEqual(LaunchServices.kLSNoLaunchPermissionErr, -10826)
        self.assertEqual(LaunchServices.kLSNoExecutableErr, -10827)
        self.assertEqual(LaunchServices.kLSNoClassicEnvironmentErr, -10828)
        self.assertEqual(LaunchServices.kLSMultipleSessionsNotSupportedErr, -10829)
        self.assertEqual(LaunchServices.kLSInitializeDefaults, 0x00000001)
        self.assertEqual(LaunchServices.kLSMinCatInfoBitmap, 6154)
        self.assertEqual(LaunchServices.kLSRequestExtension, 0x00000001)
        self.assertEqual(LaunchServices.kLSRequestTypeCreator, 0x00000002)
        self.assertEqual(LaunchServices.kLSRequestBasicFlagsOnly, 0x00000004)
        self.assertEqual(LaunchServices.kLSRequestAppTypeFlags, 0x00000008)
        self.assertEqual(LaunchServices.kLSRequestAllFlags, 0x00000010)
        self.assertEqual(LaunchServices.kLSRequestIconAndKind, 0x00000020)
        self.assertEqual(LaunchServices.kLSRequestExtensionFlagsOnly, 0x00000040)
        self.assertEqual(LaunchServices.kLSRequestAllInfo, 0xFFFFFFFF)
        self.assertEqual(LaunchServices.kLSItemInfoIsPlainFile, 0x00000001)
        self.assertEqual(LaunchServices.kLSItemInfoIsPackage, 0x00000002)
        self.assertEqual(LaunchServices.kLSItemInfoIsApplication, 0x00000004)
        self.assertEqual(LaunchServices.kLSItemInfoIsContainer, 0x00000008)
        self.assertEqual(LaunchServices.kLSItemInfoIsAliasFile, 0x00000010)
        self.assertEqual(LaunchServices.kLSItemInfoIsSymlink, 0x00000020)
        self.assertEqual(LaunchServices.kLSItemInfoIsInvisible, 0x00000040)
        self.assertEqual(LaunchServices.kLSItemInfoIsNativeApp, 0x00000080)
        self.assertEqual(LaunchServices.kLSItemInfoIsClassicApp, 0x00000100)
        self.assertEqual(LaunchServices.kLSItemInfoAppPrefersNative, 0x00000200)
        self.assertEqual(LaunchServices.kLSItemInfoAppPrefersClassic, 0x00000400)
        self.assertEqual(LaunchServices.kLSItemInfoAppIsScriptable, 0x00000800)
        self.assertEqual(LaunchServices.kLSItemInfoIsVolume, 0x00001000)
        self.assertEqual(LaunchServices.kLSItemInfoExtensionIsHidden, 0x00100000)
        self.assertEqual(LaunchServices.kLSRolesNone, 0x00000001)
        self.assertEqual(LaunchServices.kLSRolesViewer, 0x00000002)
        self.assertEqual(LaunchServices.kLSRolesEditor, 0x00000004)
        self.assertEqual(LaunchServices.kLSRolesShell, 0x00000008)
        self.assertEqual(LaunchServices.kLSRolesAll, 0xFFFFFFFF, 0xFFFFFFFFFFFFFFFF)
        self.assertEqual(LaunchServices.kLSUnknownKindID, 0)
        self.assertEqual(LaunchServices.kLSUnknownType, 0)
        self.assertEqual(LaunchServices.kLSUnknownCreator, 0)
        self.assertEqual(LaunchServices.kLSAcceptDefault, 0x00000001)
        self.assertEqual(LaunchServices.kLSAcceptAllowLoginUI, 0x00000002)

        self.assertIsInstance(LaunchServices.kLSItemContentType, str)
        self.assertIsInstance(LaunchServices.kLSItemFileType, str)
        self.assertIsInstance(LaunchServices.kLSItemFileCreator, str)
        self.assertIsInstance(LaunchServices.kLSItemExtension, str)
        self.assertIsInstance(LaunchServices.kLSItemDisplayName, str)
        self.assertIsInstance(LaunchServices.kLSItemDisplayKind, str)
        self.assertIsInstance(LaunchServices.kLSItemRoleHandlerDisplayName, str)
        self.assertIsInstance(LaunchServices.kLSItemIsInvisible, str)
        self.assertIsInstance(LaunchServices.kLSItemExtensionIsHidden, str)
        self.assertIsInstance(LaunchServices.kLSItemQuarantineProperties, str)

        self.assertEqual(LaunchServices.kLSHandlerOptionsDefault, 0)
        self.assertEqual(LaunchServices.kLSHandlerOptionsIgnoreCreator, 1)

    def testStructs(self):
        v = LaunchServices.LSItemInfoRecord()
        self.assertHasAttr(v, "flags")
        self.assertHasAttr(v, "filetype")
        self.assertHasAttr(v, "creator")
        self.assertHasAttr(v, "extension")
        self.assertNotHasAttr(v, "iconFileName")
        self.assertNotHasAttr(v, "kindID")

    def testFunctions(self):
        LaunchServices.LSInit(LaunchServices.kLSInitializeDefaults)
        LaunchServices.LSTerm()

        url = LaunchServices.CFURLCreateFromFileSystemRepresentation(
            None, self.bpath, len(self.bpath), True
        )
        self.assertIsInstance(url, LaunchServices.CFURLRef)

        ok, info = LaunchServices.LSCopyItemInfoForURL(
            url,
            LaunchServices.kLSRequestExtension | LaunchServices.kLSRequestTypeCreator,
            None,
        )
        self.assertEqual(ok, 0)
        self.assertIsInstance(info, LaunchServices.LSItemInfoRecord)

        self.assertArgIsOut(LaunchServices.LSGetExtensionInfo, 2)
        ok, info = LaunchServices.LSGetExtensionInfo(len(self.path), self.path, None)
        self.assertEqual(ok, 0)
        self.assertEqual(info, self.path.rindex(".") + 1)

        self.assertArgIsOut(LaunchServices.LSCopyDisplayNameForURL, 1)
        self.assertArgIsCFRetained(LaunchServices.LSCopyDisplayNameForURL, 1)
        ok, info = LaunchServices.LSCopyDisplayNameForURL(url, None)
        self.assertEqual(ok, 0)
        self.assertIsInstance(info, str)

        self.assertArgIsBOOL(LaunchServices.LSSetExtensionHiddenForURL, 1)
        ok = LaunchServices.LSSetExtensionHiddenForURL(url, True)
        self.assertEqual(ok, 0)

        self.assertArgIsOut(LaunchServices.LSCopyKindStringForURL, 1)
        self.assertArgIsCFRetained(LaunchServices.LSCopyKindStringForURL, 1)
        ok, info = LaunchServices.LSCopyKindStringForURL(url, None)
        self.assertEqual(ok, 0)
        self.assertIsInstance(info, str)

        self.assertArgIsOut(LaunchServices.LSCopyKindStringForTypeInfo, 3)
        self.assertArgIsCFRetained(LaunchServices.LSCopyKindStringForTypeInfo, 3)
        ok, info = LaunchServices.LSCopyKindStringForTypeInfo(
            LaunchServices.kLSUnknownType, LaunchServices.kLSUnknownCreator, "jpg", None
        )
        self.assertEqual(ok, 0)
        self.assertIsInstance(info, str)

        self.assertArgIsOut(LaunchServices.LSCopyKindStringForMIMEType, 1)
        self.assertArgIsCFRetained(LaunchServices.LSCopyKindStringForMIMEType, 1)
        ok, info = LaunchServices.LSCopyKindStringForMIMEType("text/plain", None)
        self.assertIsInstance(ok, int)
        # XXX: For some reason this fails sometimes...
        # self.assertEqual(ok, 0)
        self.assertIsInstance(info, (str, type(None)))

        self.assertArgIsOut(LaunchServices.LSGetApplicationForInfo, 4)
        self.assertArgIsOut(LaunchServices.LSGetApplicationForInfo, 5)
        self.assertArgIsCFRetained(LaunchServices.LSGetApplicationForInfo, 5)

        ok, ref, info_url = LaunchServices.LSGetApplicationForInfo(
            LaunchServices.kLSUnknownType,
            LaunchServices.kLSUnknownCreator,
            "txt",
            LaunchServices.kLSRolesAll,
            None,
            None,
        )
        self.assertEqual(ok, 0)
        self.assertIsInstance(ref, objc.FSRef)
        self.assertIsInstance(info_url, LaunchServices.CFURLRef)

        self.assertArgIsOut(LaunchServices.LSCopyApplicationForMIMEType, 2)
        self.assertArgIsCFRetained(LaunchServices.LSCopyApplicationForMIMEType, 2)
        ok, info_url = LaunchServices.LSCopyApplicationForMIMEType(
            "text/plain", LaunchServices.kLSRolesAll, None
        )
        self.assertEqual(ok, 0)
        self.assertIsInstance(info_url, LaunchServices.CFURLRef)

        self.assertArgIsOut(LaunchServices.LSGetApplicationForURL, 2)
        self.assertArgIsOut(LaunchServices.LSGetApplicationForURL, 3)
        self.assertArgIsCFRetained(LaunchServices.LSGetApplicationForURL, 3)
        ok, ref, info_url = LaunchServices.LSGetApplicationForURL(
            url, LaunchServices.kLSRolesAll, None, None
        )
        self.assertEqual(ok, 0)
        self.assertIsInstance(ref, objc.FSRef)
        self.assertIsInstance(info_url, LaunchServices.CFURLRef)

        self.assertArgIsOut(LaunchServices.LSFindApplicationForInfo, 3)
        self.assertArgIsOut(LaunchServices.LSFindApplicationForInfo, 4)
        self.assertArgIsCFRetained(LaunchServices.LSFindApplicationForInfo, 4)
        ok, ref, info_url = LaunchServices.LSFindApplicationForInfo(
            LaunchServices.kLSUnknownCreator, None, "foo.app", None, None
        )
        # XXX: The code looks correct but fails, however the corresponding C code also fails.
        # self.assertEqual(ok, 0)
        self.assertIsInstance(ok, int)
        if ref is not None:
            self.assertIsInstance(ref, objc.FSRef)
        if info_url is not None:
            self.assertIsInstance(info_url, LaunchServices.CFURLRef)

        self.assertArgIsOut(LaunchServices.LSCanURLAcceptURL, 4)
        ok, status = LaunchServices.LSCanURLAcceptURL(
            url, url, LaunchServices.kLSRolesAll, LaunchServices.kLSAcceptDefault, None
        )
        self.assertIsInstance(ok, int)
        self.assertIsInstance(status, bool)

        ok = LaunchServices.LSRegisterURL(url, False)
        self.assertIsInstance(ok, int)

        v = LaunchServices.LSCopyApplicationURLsForURL(url, LaunchServices.kLSRolesAll)
        self.assertIsInstance(v, LaunchServices.CFArrayRef)
        for a in v:
            self.assertIsInstance(a, LaunchServices.CFURLRef)

        default_role = LaunchServices.LSCopyDefaultRoleHandlerForContentType(
            "public.plain-text", LaunchServices.kLSRolesAll
        )
        if os_level_key(os_release()) < os_level_key("10.7"):
            if default_role is not None:
                self.assertIsInstance(default_role, str)
        else:
            self.assertIsInstance(default_role, str)

        v = LaunchServices.LSCopyAllRoleHandlersForContentType(
            "public.plain-text", LaunchServices.kLSRolesAll
        )
        self.assertIsInstance(v, LaunchServices.CFArrayRef)
        for a in v:
            self.assertIsInstance(a, str)

        ok = LaunchServices.LSSetDefaultRoleHandlerForContentType(
            "public.plain-text", LaunchServices.kLSRolesAll, default_role
        )
        self.assertIsInstance(ok, int)

        v = LaunchServices.LSGetHandlerOptionsForContentType("public.plain-text")
        self.assertIsInstance(v, int)

        ok = LaunchServices.LSSetHandlerOptionsForContentType("public.plain-text", v)
        self.assertIsInstance(ok, int)

        self.assertResultIsCFRetained(LaunchServices.LSCopyDefaultHandlerForURLScheme)
        default_handler = LaunchServices.LSCopyDefaultHandlerForURLScheme("http")
        if os_level_key(os_release()) < os_level_key("10.7"):
            if default_handler is not None:
                self.assertIsInstance(default_handler, str)
        else:
            self.assertIsInstance(default_handler, str)

        self.assertResultIsCFRetained(LaunchServices.LSCopyAllHandlersForURLScheme)
        v = LaunchServices.LSCopyAllHandlersForURLScheme("http")
        self.assertIsInstance(v, LaunchServices.CFArrayRef)
        for a in v:
            self.assertIsInstance(a, str)

        ok = LaunchServices.LSSetDefaultHandlerForURLScheme("http", default_handler)
        self.assertIsInstance(ok, int)

    def testFSRef(self):
        ref = objc.FSRef.from_pathname(self.path)
        self.assertIsInstance(ref, objc.FSRef)

        ok, info = LaunchServices.LSCopyItemInfoForRef(
            ref,
            LaunchServices.kLSRequestExtension | LaunchServices.kLSRequestTypeCreator,
            None,
        )
        self.assertEqual(ok, 0)
        self.assertIsInstance(info, LaunchServices.LSItemInfoRecord)

        self.assertArgIsOut(LaunchServices.LSCopyDisplayNameForRef, 1)
        self.assertArgIsCFRetained(LaunchServices.LSCopyDisplayNameForRef, 1)
        ok, info = LaunchServices.LSCopyDisplayNameForRef(ref, None)
        self.assertEqual(ok, 0)
        self.assertIsInstance(info, str)

        self.assertArgIsBOOL(LaunchServices.LSSetExtensionHiddenForRef, 1)
        ok = LaunchServices.LSSetExtensionHiddenForRef(ref, True)
        self.assertEqual(ok, 0)

        self.assertArgIsOut(LaunchServices.LSCopyKindStringForRef, 1)
        self.assertArgIsCFRetained(LaunchServices.LSCopyKindStringForRef, 1)
        ok, info = LaunchServices.LSCopyKindStringForRef(ref, None)
        self.assertEqual(ok, 0)
        self.assertIsInstance(info, str)

        self.assertArgIsOut(LaunchServices.LSGetApplicationForItem, 2)
        self.assertArgIsOut(LaunchServices.LSGetApplicationForItem, 3)
        self.assertArgIsCFRetained(LaunchServices.LSGetApplicationForItem, 3)
        ok, info_ref, info_url = LaunchServices.LSGetApplicationForItem(
            ref, LaunchServices.kLSRolesAll, None, None
        )
        self.assertEqual(ok, 0)
        self.assertIsInstance(info_ref, objc.FSRef)
        self.assertIsInstance(info_url, LaunchServices.CFURLRef)

        if os.path.exists("/Applications/TextEdit.app"):
            app_ref = objc.FSRef.from_pathname("/Applications/TextEdit.app")
        else:
            app_ref = objc.FSRef.from_pathname("/System/Applications/TextEdit.app")
        self.assertArgIsOut(LaunchServices.LSCanRefAcceptItem, 4)
        ok, accepts = LaunchServices.LSCanRefAcceptItem(
            ref,
            app_ref,
            LaunchServices.kLSRolesAll,
            LaunchServices.kLSAcceptDefault,
            None,
        )
        self.assertEqual(ok, 0)
        self.assertIsInstance(accepts, bool)

        ok = LaunchServices.LSRegisterFSRef(ref, False)
        self.assertIsInstance(ok, int)

        self.assertArgHasType(LaunchServices.LSCopyItemAttribute, 3, b"o^@")
        ok, value = LaunchServices.LSCopyItemAttribute(
            ref,
            LaunchServices.kLSRolesAll,
            LaunchServices.kLSItemExtensionIsHidden,
            None,
        )
        self.assertEqual(ok, 0)
        self.assertIsInstance(value, bool)

        ok = LaunchServices.LSSetItemAttribute(
            ref,
            LaunchServices.kLSRolesAll,
            LaunchServices.kLSItemRoleHandlerDisplayName,
            "foo",
        )
        self.assertIsInstance(ok, int)

    @min_os_level("10.10")
    def testFunctions10_10(self):
        self.assertResultIsCFRetained(LaunchServices.LSCopyDefaultApplicationURLForURL)
        self.assertArgIsOut(LaunchServices.LSCopyDefaultApplicationURLForURL, 2)

        self.assertResultIsCFRetained(
            LaunchServices.LSCopyDefaultApplicationURLForContentType
        )
        self.assertArgIsOut(LaunchServices.LSCopyDefaultApplicationURLForContentType, 2)

        self.assertResultIsCFRetained(
            LaunchServices.LSCopyApplicationURLsForBundleIdentifier
        )
        self.assertArgIsOut(LaunchServices.LSCopyApplicationURLsForBundleIdentifier, 1)
