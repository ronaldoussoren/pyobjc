import CoreServices
from PyObjCTools.TestSupport import TestCase, fourcc, cast_int
import objc


class TestIconsCore(TestCase):
    def testConstants(self):
        self.assertEqual(CoreServices.kGenericDocumentIconResource, -4000)
        self.assertEqual(CoreServices.kGenericStationeryIconResource, -3985)
        self.assertEqual(CoreServices.kGenericEditionFileIconResource, -3989)
        self.assertEqual(CoreServices.kGenericApplicationIconResource, -3996)
        self.assertEqual(CoreServices.kGenericDeskAccessoryIconResource, -3991)
        self.assertEqual(CoreServices.kGenericFolderIconResource, -3999)
        self.assertEqual(CoreServices.kPrivateFolderIconResource, -3994)
        self.assertEqual(CoreServices.kFloppyIconResource, -3998)
        self.assertEqual(CoreServices.kTrashIconResource, -3993)
        self.assertEqual(CoreServices.kGenericRAMDiskIconResource, -3988)
        self.assertEqual(CoreServices.kGenericCDROMIconResource, -3987)
        self.assertEqual(CoreServices.kDesktopIconResource, -3992)
        self.assertEqual(CoreServices.kOpenFolderIconResource, -3997)
        self.assertEqual(CoreServices.kGenericHardDiskIconResource, -3995)
        self.assertEqual(CoreServices.kGenericFileServerIconResource, -3972)
        self.assertEqual(CoreServices.kGenericSuitcaseIconResource, -3970)
        self.assertEqual(CoreServices.kGenericMoverObjectIconResource, -3969)

        self.assertEqual(CoreServices.kGenericPreferencesIconResource, -3971)
        self.assertEqual(CoreServices.kGenericQueryDocumentIconResource, -16506)
        self.assertEqual(CoreServices.kGenericExtensionIconResource, -16415)
        self.assertEqual(CoreServices.kSystemFolderIconResource, -3983)
        self.assertEqual(CoreServices.kHelpIconResource, -20271)
        self.assertEqual(CoreServices.kAppleMenuFolderIconResource, -3982)
        self.assertEqual(
            CoreServices.genericDocumentIconResource,
            CoreServices.kGenericDocumentIconResource,
        )
        self.assertEqual(
            CoreServices.genericStationeryIconResource,
            CoreServices.kGenericStationeryIconResource,
        )
        self.assertEqual(
            CoreServices.genericEditionFileIconResource,
            CoreServices.kGenericEditionFileIconResource,
        )
        self.assertEqual(
            CoreServices.genericApplicationIconResource,
            CoreServices.kGenericApplicationIconResource,
        )
        self.assertEqual(
            CoreServices.genericDeskAccessoryIconResource,
            CoreServices.kGenericDeskAccessoryIconResource,
        )
        self.assertEqual(
            CoreServices.genericFolderIconResource,
            CoreServices.kGenericFolderIconResource,
        )
        self.assertEqual(
            CoreServices.privateFolderIconResource,
            CoreServices.kPrivateFolderIconResource,
        )
        self.assertEqual(
            CoreServices.floppyIconResource, CoreServices.kFloppyIconResource
        )
        self.assertEqual(
            CoreServices.trashIconResource, CoreServices.kTrashIconResource
        )
        self.assertEqual(
            CoreServices.genericRAMDiskIconResource,
            CoreServices.kGenericRAMDiskIconResource,
        )
        self.assertEqual(
            CoreServices.genericCDROMIconResource,
            CoreServices.kGenericCDROMIconResource,
        )
        self.assertEqual(
            CoreServices.desktopIconResource, CoreServices.kDesktopIconResource
        )
        self.assertEqual(
            CoreServices.openFolderIconResource, CoreServices.kOpenFolderIconResource
        )
        self.assertEqual(
            CoreServices.genericHardDiskIconResource,
            CoreServices.kGenericHardDiskIconResource,
        )
        self.assertEqual(
            CoreServices.genericFileServerIconResource,
            CoreServices.kGenericFileServerIconResource,
        )
        self.assertEqual(
            CoreServices.genericSuitcaseIconResource,
            CoreServices.kGenericSuitcaseIconResource,
        )
        self.assertEqual(
            CoreServices.genericMoverObjectIconResource,
            CoreServices.kGenericMoverObjectIconResource,
        )
        self.assertEqual(
            CoreServices.genericPreferencesIconResource,
            CoreServices.kGenericPreferencesIconResource,
        )
        self.assertEqual(
            CoreServices.genericQueryDocumentIconResource,
            CoreServices.kGenericQueryDocumentIconResource,
        )
        self.assertEqual(
            CoreServices.genericExtensionIconResource,
            CoreServices.kGenericExtensionIconResource,
        )
        self.assertEqual(
            CoreServices.systemFolderIconResource,
            CoreServices.kSystemFolderIconResource,
        )
        self.assertEqual(
            CoreServices.appleMenuFolderIconResource,
            CoreServices.kAppleMenuFolderIconResource,
        )
        self.assertEqual(CoreServices.kStartupFolderIconResource, -3981)
        self.assertEqual(CoreServices.kOwnedFolderIconResource, -3980)
        self.assertEqual(CoreServices.kDropFolderIconResource, -3979)
        self.assertEqual(CoreServices.kSharedFolderIconResource, -3978)
        self.assertEqual(CoreServices.kMountedFolderIconResource, -3977)
        self.assertEqual(CoreServices.kControlPanelFolderIconResource, -3976)
        self.assertEqual(CoreServices.kPrintMonitorFolderIconResource, -3975)
        self.assertEqual(CoreServices.kPreferencesFolderIconResource, -3974)
        self.assertEqual(CoreServices.kExtensionsFolderIconResource, -3973)
        self.assertEqual(CoreServices.kFontsFolderIconResource, -3968)
        self.assertEqual(CoreServices.kFullTrashIconResource, -3984)
        self.assertEqual(
            CoreServices.startupFolderIconResource,
            CoreServices.kStartupFolderIconResource,
        )
        self.assertEqual(
            CoreServices.ownedFolderIconResource, CoreServices.kOwnedFolderIconResource
        )
        self.assertEqual(
            CoreServices.dropFolderIconResource, CoreServices.kDropFolderIconResource
        )
        self.assertEqual(
            CoreServices.sharedFolderIconResource,
            CoreServices.kSharedFolderIconResource,
        )
        self.assertEqual(
            CoreServices.mountedFolderIconResource,
            CoreServices.kMountedFolderIconResource,
        )
        self.assertEqual(
            CoreServices.controlPanelFolderIconResource,
            CoreServices.kControlPanelFolderIconResource,
        )
        self.assertEqual(
            CoreServices.printMonitorFolderIconResource,
            CoreServices.kPrintMonitorFolderIconResource,
        )
        self.assertEqual(
            CoreServices.preferencesFolderIconResource,
            CoreServices.kPreferencesFolderIconResource,
        )
        self.assertEqual(
            CoreServices.extensionsFolderIconResource,
            CoreServices.kExtensionsFolderIconResource,
        )
        self.assertEqual(
            CoreServices.fontsFolderIconResource, CoreServices.kFontsFolderIconResource
        )
        self.assertEqual(
            CoreServices.fullTrashIconResource, CoreServices.kFullTrashIconResource
        )
        self.assertEqual(CoreServices.kSystemIconsCreator, fourcc(b"macs"))

        self.assertEqual(CoreServices.kClipboardIcon, fourcc(b"CLIP"))
        self.assertEqual(CoreServices.kClippingUnknownTypeIcon, fourcc(b"clpu"))
        self.assertEqual(CoreServices.kClippingPictureTypeIcon, fourcc(b"clpp"))
        self.assertEqual(CoreServices.kClippingTextTypeIcon, fourcc(b"clpt"))
        self.assertEqual(CoreServices.kClippingSoundTypeIcon, fourcc(b"clps"))
        self.assertEqual(CoreServices.kDesktopIcon, fourcc(b"desk"))
        self.assertEqual(CoreServices.kFinderIcon, fourcc(b"FNDR"))
        self.assertEqual(CoreServices.kComputerIcon, fourcc(b"root"))
        self.assertEqual(CoreServices.kFontSuitcaseIcon, fourcc(b"FFIL"))
        self.assertEqual(CoreServices.kFullTrashIcon, fourcc(b"ftrh"))
        self.assertEqual(CoreServices.kGenericApplicationIcon, fourcc(b"APPL"))
        self.assertEqual(CoreServices.kGenericCDROMIcon, fourcc(b"cddr"))
        self.assertEqual(CoreServices.kGenericControlPanelIcon, fourcc(b"APPC"))
        self.assertEqual(CoreServices.kGenericControlStripModuleIcon, fourcc(b"sdev"))
        self.assertEqual(CoreServices.kGenericComponentIcon, fourcc(b"thng"))
        self.assertEqual(CoreServices.kGenericDeskAccessoryIcon, fourcc(b"APPD"))
        self.assertEqual(CoreServices.kGenericDocumentIcon, fourcc(b"docu"))
        self.assertEqual(CoreServices.kGenericEditionFileIcon, fourcc(b"edtf"))
        self.assertEqual(CoreServices.kGenericExtensionIcon, fourcc(b"INIT"))
        self.assertEqual(CoreServices.kGenericFileServerIcon, fourcc(b"srvr"))
        self.assertEqual(CoreServices.kGenericFontIcon, fourcc(b"ffil"))
        self.assertEqual(CoreServices.kGenericFontScalerIcon, fourcc(b"sclr"))
        self.assertEqual(CoreServices.kGenericFloppyIcon, fourcc(b"flpy"))
        self.assertEqual(CoreServices.kGenericHardDiskIcon, fourcc(b"hdsk"))
        self.assertEqual(CoreServices.kGenericIDiskIcon, fourcc(b"idsk"))
        self.assertEqual(CoreServices.kGenericRemovableMediaIcon, fourcc(b"rmov"))
        self.assertEqual(CoreServices.kGenericMoverObjectIcon, fourcc(b"movr"))
        self.assertEqual(CoreServices.kGenericPCCardIcon, fourcc(b"pcmc"))
        self.assertEqual(CoreServices.kGenericPreferencesIcon, fourcc(b"pref"))
        self.assertEqual(CoreServices.kGenericQueryDocumentIcon, fourcc(b"qery"))
        self.assertEqual(CoreServices.kGenericRAMDiskIcon, fourcc(b"ramd"))
        self.assertEqual(CoreServices.kGenericSharedLibaryIcon, fourcc(b"shlb"))
        self.assertEqual(CoreServices.kGenericStationeryIcon, fourcc(b"sdoc"))
        self.assertEqual(CoreServices.kGenericSuitcaseIcon, fourcc(b"suit"))
        self.assertEqual(CoreServices.kGenericURLIcon, fourcc(b"gurl"))
        self.assertEqual(CoreServices.kGenericWORMIcon, fourcc(b"worm"))
        self.assertEqual(CoreServices.kInternationalResourcesIcon, fourcc(b"ifil"))
        self.assertEqual(CoreServices.kKeyboardLayoutIcon, fourcc(b"kfil"))
        self.assertEqual(CoreServices.kSoundFileIcon, fourcc(b"sfil"))
        self.assertEqual(CoreServices.kSystemSuitcaseIcon, fourcc(b"zsys"))
        self.assertEqual(CoreServices.kTrashIcon, fourcc(b"trsh"))
        self.assertEqual(CoreServices.kTrueTypeFontIcon, fourcc(b"tfil"))
        self.assertEqual(CoreServices.kTrueTypeFlatFontIcon, fourcc(b"sfnt"))
        self.assertEqual(CoreServices.kTrueTypeMultiFlatFontIcon, fourcc(b"ttcf"))
        self.assertEqual(CoreServices.kUserIDiskIcon, fourcc(b"udsk"))
        self.assertEqual(CoreServices.kUnknownFSObjectIcon, fourcc(b"unfs"))
        self.assertEqual(
            CoreServices.kInternationResourcesIcon,
            CoreServices.kInternationalResourcesIcon,
        )
        self.assertEqual(CoreServices.kInternetLocationHTTPIcon, fourcc(b"ilht"))
        self.assertEqual(CoreServices.kInternetLocationFTPIcon, fourcc(b"ilft"))
        self.assertEqual(CoreServices.kInternetLocationAppleShareIcon, fourcc(b"ilaf"))
        self.assertEqual(
            CoreServices.kInternetLocationAppleTalkZoneIcon, fourcc(b"ilat")
        )
        self.assertEqual(CoreServices.kInternetLocationFileIcon, fourcc(b"ilfi"))
        self.assertEqual(CoreServices.kInternetLocationMailIcon, fourcc(b"ilma"))
        self.assertEqual(CoreServices.kInternetLocationNewsIcon, fourcc(b"ilnw"))
        self.assertEqual(
            CoreServices.kInternetLocationNSLNeighborhoodIcon, fourcc(b"ilns")
        )
        self.assertEqual(CoreServices.kInternetLocationGenericIcon, fourcc(b"ilge"))
        self.assertEqual(CoreServices.kGenericFolderIcon, fourcc(b"fldr"))
        self.assertEqual(CoreServices.kDropFolderIcon, fourcc(b"dbox"))
        self.assertEqual(CoreServices.kMountedFolderIcon, fourcc(b"mntd"))
        self.assertEqual(CoreServices.kOpenFolderIcon, fourcc(b"ofld"))
        self.assertEqual(CoreServices.kOwnedFolderIcon, fourcc(b"ownd"))
        self.assertEqual(CoreServices.kPrivateFolderIcon, fourcc(b"prvf"))
        self.assertEqual(CoreServices.kSharedFolderIcon, fourcc(b"shfl"))
        self.assertEqual(CoreServices.kSharingPrivsNotApplicableIcon, fourcc(b"shna"))
        self.assertEqual(CoreServices.kSharingPrivsReadOnlyIcon, fourcc(b"shro"))
        self.assertEqual(CoreServices.kSharingPrivsReadWriteIcon, fourcc(b"shrw"))
        self.assertEqual(CoreServices.kSharingPrivsUnknownIcon, fourcc(b"shuk"))
        self.assertEqual(CoreServices.kSharingPrivsWritableIcon, fourcc(b"writ"))
        self.assertEqual(CoreServices.kUserFolderIcon, fourcc(b"ufld"))
        self.assertEqual(CoreServices.kWorkgroupFolderIcon, fourcc(b"wfld"))
        self.assertEqual(CoreServices.kGuestUserIcon, fourcc(b"gusr"))
        self.assertEqual(CoreServices.kUserIcon, fourcc(b"user"))
        self.assertEqual(CoreServices.kOwnerIcon, fourcc(b"susr"))
        self.assertEqual(CoreServices.kGroupIcon, fourcc(b"grup"))
        self.assertEqual(CoreServices.kAppearanceFolderIcon, fourcc(b"appr"))
        self.assertEqual(CoreServices.kAppleExtrasFolderIcon, cast_int(0x616578C4))
        self.assertEqual(CoreServices.kAppleMenuFolderIcon, fourcc(b"amnu"))
        self.assertEqual(CoreServices.kApplicationsFolderIcon, fourcc(b"apps"))
        self.assertEqual(CoreServices.kApplicationSupportFolderIcon, fourcc(b"asup"))
        self.assertEqual(CoreServices.kAssistantsFolderIcon, cast_int(0x617374C4))
        self.assertEqual(CoreServices.kColorSyncFolderIcon, fourcc(b"prof"))
        self.assertEqual(CoreServices.kContextualMenuItemsFolderIcon, fourcc(b"cmnu"))
        self.assertEqual(CoreServices.kControlPanelDisabledFolderIcon, fourcc(b"ctrD"))
        self.assertEqual(CoreServices.kControlPanelFolderIcon, fourcc(b"ctrl"))
        self.assertEqual(
            CoreServices.kControlStripModulesFolderIcon, cast_int(0x736476C4)
        )
        self.assertEqual(CoreServices.kDocumentsFolderIcon, fourcc(b"docs"))
        self.assertEqual(CoreServices.kExtensionsDisabledFolderIcon, fourcc(b"extD"))
        self.assertEqual(CoreServices.kExtensionsFolderIcon, fourcc(b"extn"))
        self.assertEqual(CoreServices.kFavoritesFolderIcon, fourcc(b"favs"))
        self.assertEqual(CoreServices.kFontsFolderIcon, fourcc(b"font"))
        self.assertEqual(CoreServices.kHelpFolderIcon, cast_int(0xC4686C70))
        self.assertEqual(CoreServices.kInternetFolderIcon, cast_int(0x696E74C4))
        self.assertEqual(CoreServices.kInternetPlugInFolderIcon, cast_int(0xC46E6574))
        self.assertEqual(CoreServices.kInternetSearchSitesFolderIcon, fourcc(b"issf"))
        self.assertEqual(CoreServices.kLocalesFolderIcon, cast_int(0xC46C6F63))
        self.assertEqual(CoreServices.kMacOSReadMeFolderIcon, cast_int(0x6D6F72C4))
        self.assertEqual(CoreServices.kPublicFolderIcon, fourcc(b"pubf"))
        self.assertEqual(CoreServices.kPreferencesFolderIcon, cast_int(0x707266C4))
        self.assertEqual(CoreServices.kPrinterDescriptionFolderIcon, fourcc(b"ppdf"))
        self.assertEqual(CoreServices.kPrinterDriverFolderIcon, cast_int(0xC4707264))
        self.assertEqual(CoreServices.kPrintMonitorFolderIcon, fourcc(b"prnt"))
        self.assertEqual(CoreServices.kRecentApplicationsFolderIcon, fourcc(b"rapp"))
        self.assertEqual(CoreServices.kRecentDocumentsFolderIcon, fourcc(b"rdoc"))
        self.assertEqual(CoreServices.kRecentServersFolderIcon, fourcc(b"rsrv"))
        self.assertEqual(
            CoreServices.kScriptingAdditionsFolderIcon, cast_int(0xC4736372)
        )
        self.assertEqual(CoreServices.kSharedLibrariesFolderIcon, cast_int(0xC46C6962))
        self.assertEqual(CoreServices.kScriptsFolderIcon, cast_int(0x736372C4))
        self.assertEqual(CoreServices.kShutdownItemsDisabledFolderIcon, fourcc(b"shdD"))
        self.assertEqual(CoreServices.kShutdownItemsFolderIcon, fourcc(b"shdf"))
        self.assertEqual(CoreServices.kSpeakableItemsFolder, fourcc(b"spki"))
        self.assertEqual(CoreServices.kStartupItemsDisabledFolderIcon, fourcc(b"strD"))
        self.assertEqual(CoreServices.kStartupItemsFolderIcon, fourcc(b"strt"))
        self.assertEqual(
            CoreServices.kSystemExtensionDisabledFolderIcon, fourcc(b"macD")
        )
        self.assertEqual(CoreServices.kSystemFolderIcon, fourcc(b"macs"))
        self.assertEqual(CoreServices.kTextEncodingsFolderIcon, cast_int(0xC4746578))
        self.assertEqual(CoreServices.kUsersFolderIcon, cast_int(0x757372C4))
        self.assertEqual(CoreServices.kUtilitiesFolderIcon, cast_int(0x757469C4))
        self.assertEqual(CoreServices.kVoicesFolderIcon, fourcc(b"fvoc"))
        self.assertEqual(CoreServices.kAppleScriptBadgeIcon, fourcc(b"scrp"))
        self.assertEqual(CoreServices.kLockedBadgeIcon, fourcc(b"lbdg"))
        self.assertEqual(CoreServices.kMountedBadgeIcon, fourcc(b"mbdg"))
        self.assertEqual(CoreServices.kSharedBadgeIcon, fourcc(b"sbdg"))
        self.assertEqual(CoreServices.kAliasBadgeIcon, fourcc(b"abdg"))
        self.assertEqual(CoreServices.kAlertCautionBadgeIcon, fourcc(b"cbdg"))
        self.assertEqual(CoreServices.kAlertNoteIcon, fourcc(b"note"))
        self.assertEqual(CoreServices.kAlertCautionIcon, fourcc(b"caut"))
        self.assertEqual(CoreServices.kAlertStopIcon, fourcc(b"stop"))
        self.assertEqual(CoreServices.kAppleTalkIcon, fourcc(b"atlk"))
        self.assertEqual(CoreServices.kAppleTalkZoneIcon, fourcc(b"atzn"))
        self.assertEqual(CoreServices.kAFPServerIcon, fourcc(b"afps"))
        self.assertEqual(CoreServices.kFTPServerIcon, fourcc(b"ftps"))
        self.assertEqual(CoreServices.kHTTPServerIcon, fourcc(b"htps"))
        self.assertEqual(CoreServices.kGenericNetworkIcon, fourcc(b"gnet"))
        self.assertEqual(CoreServices.kIPFileServerIcon, fourcc(b"isrv"))
        self.assertEqual(CoreServices.kToolbarCustomizeIcon, fourcc(b"tcus"))
        self.assertEqual(CoreServices.kToolbarDeleteIcon, fourcc(b"tdel"))
        self.assertEqual(CoreServices.kToolbarFavoritesIcon, fourcc(b"tfav"))
        self.assertEqual(CoreServices.kToolbarHomeIcon, fourcc(b"thom"))
        self.assertEqual(CoreServices.kAppleLogoIcon, fourcc(b"capl"))
        self.assertEqual(CoreServices.kAppleMenuIcon, fourcc(b"sapl"))
        self.assertEqual(CoreServices.kBackwardArrowIcon, fourcc(b"baro"))
        self.assertEqual(CoreServices.kFavoriteItemsIcon, fourcc(b"favr"))
        self.assertEqual(CoreServices.kForwardArrowIcon, fourcc(b"faro"))
        self.assertEqual(CoreServices.kGridIcon, fourcc(b"grid"))
        self.assertEqual(CoreServices.kHelpIcon, fourcc(b"help"))
        self.assertEqual(CoreServices.kKeepArrangedIcon, fourcc(b"arng"))
        self.assertEqual(CoreServices.kLockedIcon, fourcc(b"lock"))
        self.assertEqual(CoreServices.kNoFilesIcon, fourcc(b"nfil"))
        self.assertEqual(CoreServices.kNoFolderIcon, fourcc(b"nfld"))
        self.assertEqual(CoreServices.kNoWriteIcon, fourcc(b"nwrt"))
        self.assertEqual(CoreServices.kProtectedApplicationFolderIcon, fourcc(b"papp"))
        self.assertEqual(CoreServices.kProtectedSystemFolderIcon, fourcc(b"psys"))
        self.assertEqual(CoreServices.kRecentItemsIcon, fourcc(b"rcnt"))
        self.assertEqual(CoreServices.kShortcutIcon, fourcc(b"shrt"))
        self.assertEqual(CoreServices.kSortAscendingIcon, fourcc(b"asnd"))
        self.assertEqual(CoreServices.kSortDescendingIcon, fourcc(b"dsnd"))
        self.assertEqual(CoreServices.kUnlockedIcon, fourcc(b"ulck"))
        self.assertEqual(CoreServices.kConnectToIcon, fourcc(b"cnct"))
        self.assertEqual(CoreServices.kGenericWindowIcon, fourcc(b"gwin"))
        self.assertEqual(CoreServices.kQuestionMarkIcon, fourcc(b"ques"))
        self.assertEqual(CoreServices.kDeleteAliasIcon, fourcc(b"dali"))
        self.assertEqual(CoreServices.kEjectMediaIcon, fourcc(b"ejec"))
        self.assertEqual(CoreServices.kBurningIcon, fourcc(b"burn"))
        self.assertEqual(CoreServices.kRightContainerArrowIcon, fourcc(b"rcar"))
        self.assertEqual(CoreServices.kIconServicesNormalUsageFlag, 0)
        self.assertEqual(CoreServices.kIconServicesNoBadgeFlag, 1)
        self.assertEqual(CoreServices.kIconServicesUpdateIfNeededFlag, 2)
        self.assertEqual(CoreServices.kIconServicesCatalogInfoMask, 531_550)

    def testFunctions(self):
        self.assertArgIsOut(CoreServices.GetIconRef, 3)
        err, icon = CoreServices.GetIconRef(
            0, CoreServices.kSystemIconsCreator, CoreServices.kShortcutIcon, None
        )
        self.assertIsInstance(err, int)
        self.assertIsInstance(icon, CoreServices.IconRef)

        try:
            self.assertArgIsOut(CoreServices.GetIconRefOwners, 1)
            err, cnt = CoreServices.GetIconRefOwners(icon, None)
            self.assertIsInstance(err, int)
            self.assertIsInstance(cnt, int)

            err = CoreServices.AcquireIconRef(icon)
            self.assertEqual(err, 0)

            err = CoreServices.ReleaseIconRef(icon)
            self.assertEqual(err, 0)

            self.assertArgIsOut(CoreServices.GetIconRefFromFolder, 5)

            self.assertArgHasType(
                CoreServices.GetIconRefFromFileInfo,
                2,
                objc._C_IN + objc._C_PTR + objc._C_UNICHAR,
            )
            self.assertArgIsOut(CoreServices.GetIconRefFromFileInfo, 6)
            self.assertArgIsOut(CoreServices.GetIconRefFromFileInfo, 7)

            self.assertArgIsOut(CoreServices.GetIconRefFromTypeInfo, 5)

            self.assertArgIsIn(CoreServices.GetIconRefFromIconFamilyPtr, 0)
            self.assertArgIsOut(CoreServices.GetIconRefFromIconFamilyPtr, 2)

            self.assertArgIsOut(CoreServices.GetIconRefFromComponent, 1)

            # XXX: Untested for now...
            CoreServices.RegisterIconRefFromIconFamily
            CoreServices.RegisterIconRefFromFSRef
            CoreServices.UnregisterIconRef
            CoreServices.UpdateIconRef
            CoreServices.OverrideIconRef
            CoreServices.RemoveIconRefOverride

            self.assertArgIsOut(CoreServices.CompositeIconRef, 2)

            self.assertArgIsOut(CoreServices.IsIconRefComposite, 1)
            self.assertArgIsOut(CoreServices.IsIconRefComposite, 2)

            self.assertResultIsBOOL(CoreServices.IsValidIconRef)
            self.assertResultIsBOOL(CoreServices.IsDataAvailableInIconRef)

            self.assertArgIsBOOL(CoreServices.SetCustomIconsEnabled, 1)
            self.assertArgIsOut(CoreServices.GetCustomIconsEnabled, 1)
            self.assertArgHasType(
                CoreServices.GetCustomIconsEnabled,
                1,
                objc._C_OUT + objc._C_PTR + objc._C_NSBOOL,
            )

            # Untested...
            CoreServices.ReadIconFromFSRef

        finally:
            err = CoreServices.ReleaseIconRef(icon)
            self.assertEqual(err, 0)

    def testOpaque(self):
        self.assertIsOpaquePointer(CoreServices.IconRef)
