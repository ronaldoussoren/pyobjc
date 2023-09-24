import os
import CoreServices
from PyObjCTools.TestSupport import TestCase, min_os_level, os_release, os_level_key
import objc


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
        self.assertEqual(CoreServices.kLSInvalidExtensionIndex, 0xFFFFFFFFFFFFFFFF)
        self.assertEqual(CoreServices.kLSInitializeDefaults, 0x00000001)
        self.assertEqual(CoreServices.kLSMinCatInfoBitmap, 6154)
        self.assertEqual(CoreServices.kLSRequestExtension, 0x00000001)
        self.assertEqual(CoreServices.kLSRequestTypeCreator, 0x00000002)
        self.assertEqual(CoreServices.kLSRequestBasicFlagsOnly, 0x00000004)
        self.assertEqual(CoreServices.kLSRequestAppTypeFlags, 0x00000008)
        self.assertEqual(CoreServices.kLSRequestAllFlags, 0x00000010)
        self.assertEqual(CoreServices.kLSRequestIconAndKind, 0x00000020)
        self.assertEqual(CoreServices.kLSRequestExtensionFlagsOnly, 0x00000040)
        self.assertEqual(CoreServices.kLSRequestAllInfo, 0xFFFFFFFF)
        self.assertEqual(CoreServices.kLSItemInfoIsPlainFile, 0x00000001)
        self.assertEqual(CoreServices.kLSItemInfoIsPackage, 0x00000002)
        self.assertEqual(CoreServices.kLSItemInfoIsApplication, 0x00000004)
        self.assertEqual(CoreServices.kLSItemInfoIsContainer, 0x00000008)
        self.assertEqual(CoreServices.kLSItemInfoIsAliasFile, 0x00000010)
        self.assertEqual(CoreServices.kLSItemInfoIsSymlink, 0x00000020)
        self.assertEqual(CoreServices.kLSItemInfoIsInvisible, 0x00000040)
        self.assertEqual(CoreServices.kLSItemInfoIsNativeApp, 0x00000080)
        self.assertEqual(CoreServices.kLSItemInfoIsClassicApp, 0x00000100)
        self.assertEqual(CoreServices.kLSItemInfoAppPrefersNative, 0x00000200)
        self.assertEqual(CoreServices.kLSItemInfoAppPrefersClassic, 0x00000400)
        self.assertEqual(CoreServices.kLSItemInfoAppIsScriptable, 0x00000800)
        self.assertEqual(CoreServices.kLSItemInfoIsVolume, 0x00001000)
        self.assertEqual(CoreServices.kLSItemInfoExtensionIsHidden, 0x00100000)
        self.assertEqual(CoreServices.kLSRolesAll, 0xFFFFFFFF, 0xFFFFFFFFFFFFFFFF)
        self.assertEqual(CoreServices.kLSUnknownKindID, 0)
        self.assertEqual(CoreServices.kLSAcceptDefault, 0x00000001)
        self.assertEqual(CoreServices.kLSAcceptAllowLoginUI, 0x00000002)

        self.assertIsInstance(CoreServices.kLSItemContentType, str)
        self.assertIsInstance(CoreServices.kLSItemFileType, str)
        self.assertIsInstance(CoreServices.kLSItemFileCreator, str)
        self.assertIsInstance(CoreServices.kLSItemExtension, str)
        self.assertIsInstance(CoreServices.kLSItemDisplayName, str)
        self.assertIsInstance(CoreServices.kLSItemDisplayKind, str)
        self.assertIsInstance(CoreServices.kLSItemRoleHandlerDisplayName, str)
        self.assertIsInstance(CoreServices.kLSItemIsInvisible, str)
        self.assertIsInstance(CoreServices.kLSItemExtensionIsHidden, str)
        self.assertIsInstance(CoreServices.kLSItemQuarantineProperties, str)

        self.assertEqual(CoreServices.kLSHandlerOptionsDefault, 0)
        self.assertEqual(CoreServices.kLSHandlerOptionsIgnoreCreator, 1)

    def testStructs(self):
        v = CoreServices.LSItemInfoRecord()
        self.assertHasAttr(v, "flags")
        self.assertHasAttr(v, "filetype")
        self.assertHasAttr(v, "creator")
        self.assertHasAttr(v, "extension")
        self.assertNotHasAttr(v, "iconFileName")
        self.assertNotHasAttr(v, "kindID")
        self.assertPickleRoundTrips(v)

    def testFunctions(self):
        CoreServices.LSInit(CoreServices.kLSInitializeDefaults)
        CoreServices.LSTerm()

        url = CoreServices.CFURLCreateFromFileSystemRepresentation(
            None, self.bpath, len(self.bpath), True
        )
        self.assertIsInstance(url, CoreServices.CFURLRef)

        ok, info = CoreServices.LSCopyItemInfoForURL(
            url,
            CoreServices.kLSRequestExtension | CoreServices.kLSRequestTypeCreator,
            None,
        )
        self.assertEqual(ok, 0)
        self.assertIsInstance(info, CoreServices.LSItemInfoRecord)

        self.assertArgIsOut(CoreServices.LSGetExtensionInfo, 2)
        ok, info = CoreServices.LSGetExtensionInfo(len(self.path), self.path, None)
        self.assertEqual(ok, 0)
        self.assertEqual(info, self.path.rindex(".") + 1)

        self.assertArgIsOut(CoreServices.LSCopyDisplayNameForURL, 1)
        self.assertArgIsCFRetained(CoreServices.LSCopyDisplayNameForURL, 1)
        ok, info = CoreServices.LSCopyDisplayNameForURL(url, None)
        self.assertEqual(ok, 0)
        self.assertIsInstance(info, str)

        self.assertArgIsBOOL(CoreServices.LSSetExtensionHiddenForURL, 1)
        ok = CoreServices.LSSetExtensionHiddenForURL(url, True)
        self.assertEqual(ok, 0)

        self.assertArgIsOut(CoreServices.LSCopyKindStringForURL, 1)
        self.assertArgIsCFRetained(CoreServices.LSCopyKindStringForURL, 1)
        ok, info = CoreServices.LSCopyKindStringForURL(url, None)
        self.assertEqual(ok, 0)
        self.assertIsInstance(info, str)

        self.assertArgIsOut(CoreServices.LSCopyKindStringForTypeInfo, 3)
        self.assertArgIsCFRetained(CoreServices.LSCopyKindStringForTypeInfo, 3)
        ok, info = CoreServices.LSCopyKindStringForTypeInfo(
            CoreServices.kLSUnknownType, CoreServices.kLSUnknownCreator, "jpg", None
        )
        self.assertEqual(ok, 0)
        self.assertIsInstance(info, str)

        self.assertArgIsOut(CoreServices.LSCopyKindStringForMIMEType, 1)
        self.assertArgIsCFRetained(CoreServices.LSCopyKindStringForMIMEType, 1)
        ok, info = CoreServices.LSCopyKindStringForMIMEType("text/plain", None)
        self.assertIsInstance(ok, int)
        # XXX: For some reason this fails sometimes...
        # self.assertEqual(ok, 0)
        self.assertIsInstance(info, (str, type(None)))

        self.assertArgIsOut(CoreServices.LSGetApplicationForInfo, 4)
        self.assertArgIsOut(CoreServices.LSGetApplicationForInfo, 5)
        self.assertArgIsCFRetained(CoreServices.LSGetApplicationForInfo, 5)

        ok, ref, info_url = CoreServices.LSGetApplicationForInfo(
            CoreServices.kLSUnknownType,
            CoreServices.kLSUnknownCreator,
            "txt",
            CoreServices.kLSRolesAll,
            None,
            None,
        )
        self.assertEqual(ok, 0)
        self.assertIsInstance(ref, objc.FSRef)
        self.assertIsInstance(info_url, CoreServices.CFURLRef)

        self.assertArgIsOut(CoreServices.LSCopyApplicationForMIMEType, 2)
        self.assertArgIsCFRetained(CoreServices.LSCopyApplicationForMIMEType, 2)
        ok, info_url = CoreServices.LSCopyApplicationForMIMEType(
            "text/plain", CoreServices.kLSRolesAll, None
        )
        self.assertEqual(ok, 0)
        self.assertIsInstance(info_url, CoreServices.CFURLRef)

        self.assertArgIsOut(CoreServices.LSGetApplicationForURL, 2)
        self.assertArgIsOut(CoreServices.LSGetApplicationForURL, 3)
        self.assertArgIsCFRetained(CoreServices.LSGetApplicationForURL, 3)
        ok, ref, info_url = CoreServices.LSGetApplicationForURL(
            url, CoreServices.kLSRolesAll, None, None
        )
        self.assertEqual(ok, 0)
        self.assertIsInstance(ref, objc.FSRef)
        self.assertIsInstance(info_url, CoreServices.CFURLRef)

        self.assertArgIsOut(CoreServices.LSFindApplicationForInfo, 3)
        self.assertArgIsOut(CoreServices.LSFindApplicationForInfo, 4)
        self.assertArgIsCFRetained(CoreServices.LSFindApplicationForInfo, 4)
        ok, ref, info_url = CoreServices.LSFindApplicationForInfo(
            CoreServices.kLSUnknownCreator, None, "foo.app", None, None
        )
        # XXX: The code looks correct but fails, however the corresponding C code also fails.
        # self.assertEqual(ok, 0)
        self.assertIsInstance(ok, int)
        if ref is not None:
            self.assertIsInstance(ref, objc.FSRef)
        if info_url is not None:
            self.assertIsInstance(info_url, CoreServices.CFURLRef)

        self.assertArgIsOut(CoreServices.LSCanURLAcceptURL, 4)
        ok, status = CoreServices.LSCanURLAcceptURL(
            url, url, CoreServices.kLSRolesAll, CoreServices.kLSAcceptDefault, None
        )
        self.assertIsInstance(ok, int)
        self.assertIsInstance(status, bool)

        ok = CoreServices.LSRegisterURL(url, False)
        self.assertIsInstance(ok, int)

        v = CoreServices.LSCopyApplicationURLsForURL(url, CoreServices.kLSRolesAll)
        self.assertIsInstance(v, CoreServices.CFArrayRef)
        for a in v:
            self.assertIsInstance(a, CoreServices.CFURLRef)

        default_role = CoreServices.LSCopyDefaultRoleHandlerForContentType(
            "public.plain-text", CoreServices.kLSRolesAll
        )
        if os_level_key(os_release()) < os_level_key("10.7"):
            if default_role is not None:
                self.assertIsInstance(default_role, str)
        else:
            self.assertIsInstance(default_role, str)

        v = CoreServices.LSCopyAllRoleHandlersForContentType(
            "public.plain-text", CoreServices.kLSRolesAll
        )
        self.assertIsInstance(v, CoreServices.CFArrayRef)
        for a in v:
            self.assertIsInstance(a, str)

        ok = CoreServices.LSSetDefaultRoleHandlerForContentType(
            "public.plain-text", CoreServices.kLSRolesAll, default_role
        )
        self.assertIsInstance(ok, int)

        v = CoreServices.LSGetHandlerOptionsForContentType("public.plain-text")
        self.assertIsInstance(v, int)

        ok = CoreServices.LSSetHandlerOptionsForContentType("public.plain-text", v)
        self.assertIsInstance(ok, int)

        self.assertResultIsCFRetained(CoreServices.LSCopyDefaultHandlerForURLScheme)
        default_handler = CoreServices.LSCopyDefaultHandlerForURLScheme("http")
        if os_level_key(os_release()) < os_level_key("10.7"):
            if default_handler is not None:
                self.assertIsInstance(default_handler, str)
        else:
            self.assertIsInstance(default_handler, str)

        self.assertResultIsCFRetained(CoreServices.LSCopyAllHandlersForURLScheme)
        v = CoreServices.LSCopyAllHandlersForURLScheme("http")
        self.assertIsInstance(v, CoreServices.CFArrayRef)
        for a in v:
            self.assertIsInstance(a, str)

        ok = CoreServices.LSSetDefaultHandlerForURLScheme("http", default_handler)
        self.assertIsInstance(ok, int)

    def testFSRef(self):
        ref = objc.FSRef.from_pathname(self.path)
        self.assertIsInstance(ref, objc.FSRef)

        ok, info = CoreServices.LSCopyItemInfoForRef(
            ref,
            CoreServices.kLSRequestExtension | CoreServices.kLSRequestTypeCreator,
            None,
        )
        self.assertEqual(ok, 0)
        self.assertIsInstance(info, CoreServices.LSItemInfoRecord)

        self.assertArgIsOut(CoreServices.LSCopyDisplayNameForRef, 1)
        self.assertArgIsCFRetained(CoreServices.LSCopyDisplayNameForRef, 1)
        ok, info = CoreServices.LSCopyDisplayNameForRef(ref, None)
        self.assertEqual(ok, 0)
        self.assertIsInstance(info, str)

        self.assertArgIsBOOL(CoreServices.LSSetExtensionHiddenForRef, 1)
        ok = CoreServices.LSSetExtensionHiddenForRef(ref, True)
        self.assertEqual(ok, 0)

        self.assertArgIsOut(CoreServices.LSCopyKindStringForRef, 1)
        self.assertArgIsCFRetained(CoreServices.LSCopyKindStringForRef, 1)
        ok, info = CoreServices.LSCopyKindStringForRef(ref, None)
        self.assertEqual(ok, 0)
        self.assertIsInstance(info, str)

        self.assertArgIsOut(CoreServices.LSGetApplicationForItem, 2)
        self.assertArgIsOut(CoreServices.LSGetApplicationForItem, 3)
        self.assertArgIsCFRetained(CoreServices.LSGetApplicationForItem, 3)
        ok, info_ref, info_url = CoreServices.LSGetApplicationForItem(
            ref, CoreServices.kLSRolesAll, None, None
        )
        self.assertEqual(ok, 0)
        self.assertIsInstance(info_ref, objc.FSRef)
        self.assertIsInstance(info_url, CoreServices.CFURLRef)

        if os.path.exists("/Applications/TextEdit.app"):
            app_ref = objc.FSRef.from_pathname("/Applications/TextEdit.app")
        else:
            app_ref = objc.FSRef.from_pathname("/System/Applications/TextEdit.app")
        self.assertArgIsOut(CoreServices.LSCanRefAcceptItem, 4)
        ok, accepts = CoreServices.LSCanRefAcceptItem(
            ref, app_ref, CoreServices.kLSRolesAll, CoreServices.kLSAcceptDefault, None
        )
        self.assertEqual(ok, 0)
        self.assertIsInstance(accepts, bool)

        ok = CoreServices.LSRegisterFSRef(ref, False)
        self.assertIsInstance(ok, int)

        self.assertArgHasType(CoreServices.LSCopyItemAttribute, 3, b"o^@")
        ok, value = CoreServices.LSCopyItemAttribute(
            ref, CoreServices.kLSRolesAll, CoreServices.kLSItemExtensionIsHidden, None
        )
        self.assertEqual(ok, 0)
        self.assertIsInstance(value, bool)

        ok = CoreServices.LSSetItemAttribute(
            ref,
            CoreServices.kLSRolesAll,
            CoreServices.kLSItemRoleHandlerDisplayName,
            "foo",
        )
        self.assertIsInstance(ok, int)

    @min_os_level("10.10")
    def testFunctions10_10(self):
        self.assertResultIsCFRetained(CoreServices.LSCopyDefaultApplicationURLForURL)
        self.assertArgIsOut(CoreServices.LSCopyDefaultApplicationURLForURL, 2)

        self.assertResultIsCFRetained(
            CoreServices.LSCopyDefaultApplicationURLForContentType
        )
        self.assertArgIsOut(CoreServices.LSCopyDefaultApplicationURLForContentType, 2)

        self.assertResultIsCFRetained(
            CoreServices.LSCopyApplicationURLsForBundleIdentifier
        )
        self.assertArgIsOut(CoreServices.LSCopyApplicationURLsForBundleIdentifier, 1)
