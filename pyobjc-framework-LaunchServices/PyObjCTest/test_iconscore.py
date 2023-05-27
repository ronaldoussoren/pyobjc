import warnings

from PyObjCTools.TestSupport import TestCase, fourcc, cast_int
import objc

with warnings.catch_warnings():
    warnings.filterwarnings("ignore")
    import LaunchServices


class TestIconsCore(TestCase):
    def testConstants(self):
        self.assertEqual(LaunchServices.kGenericDocumentIconResource, -4000)
        self.assertEqual(LaunchServices.kGenericStationeryIconResource, -3985)
        self.assertEqual(LaunchServices.kGenericEditionFileIconResource, -3989)
        self.assertEqual(LaunchServices.kGenericApplicationIconResource, -3996)
        self.assertEqual(LaunchServices.kGenericDeskAccessoryIconResource, -3991)
        self.assertEqual(LaunchServices.kGenericFolderIconResource, -3999)
        self.assertEqual(LaunchServices.kPrivateFolderIconResource, -3994)
        self.assertEqual(LaunchServices.kFloppyIconResource, -3998)
        self.assertEqual(LaunchServices.kTrashIconResource, -3993)
        self.assertEqual(LaunchServices.kGenericRAMDiskIconResource, -3988)
        self.assertEqual(LaunchServices.kGenericCDROMIconResource, -3987)
        self.assertEqual(LaunchServices.kDesktopIconResource, -3992)
        self.assertEqual(LaunchServices.kOpenFolderIconResource, -3997)
        self.assertEqual(LaunchServices.kGenericHardDiskIconResource, -3995)
        self.assertEqual(LaunchServices.kGenericFileServerIconResource, -3972)
        self.assertEqual(LaunchServices.kGenericSuitcaseIconResource, -3970)
        self.assertEqual(LaunchServices.kGenericMoverObjectIconResource, -3969)

        self.assertEqual(LaunchServices.kGenericPreferencesIconResource, -3971)
        self.assertEqual(LaunchServices.kGenericQueryDocumentIconResource, -16506)
        self.assertEqual(LaunchServices.kGenericExtensionIconResource, -16415)
        self.assertEqual(LaunchServices.kSystemFolderIconResource, -3983)
        self.assertEqual(LaunchServices.kHelpIconResource, -20271)
        self.assertEqual(LaunchServices.kAppleMenuFolderIconResource, -3982)
        self.assertEqual(
            LaunchServices.genericDocumentIconResource,
            LaunchServices.kGenericDocumentIconResource,
        )
        self.assertEqual(
            LaunchServices.genericStationeryIconResource,
            LaunchServices.kGenericStationeryIconResource,
        )
        self.assertEqual(
            LaunchServices.genericEditionFileIconResource,
            LaunchServices.kGenericEditionFileIconResource,
        )
        self.assertEqual(
            LaunchServices.genericApplicationIconResource,
            LaunchServices.kGenericApplicationIconResource,
        )
        self.assertEqual(
            LaunchServices.genericDeskAccessoryIconResource,
            LaunchServices.kGenericDeskAccessoryIconResource,
        )
        self.assertEqual(
            LaunchServices.genericFolderIconResource,
            LaunchServices.kGenericFolderIconResource,
        )
        self.assertEqual(
            LaunchServices.privateFolderIconResource,
            LaunchServices.kPrivateFolderIconResource,
        )
        self.assertEqual(
            LaunchServices.floppyIconResource, LaunchServices.kFloppyIconResource
        )
        self.assertEqual(
            LaunchServices.trashIconResource, LaunchServices.kTrashIconResource
        )
        self.assertEqual(
            LaunchServices.genericRAMDiskIconResource,
            LaunchServices.kGenericRAMDiskIconResource,
        )
        self.assertEqual(
            LaunchServices.genericCDROMIconResource,
            LaunchServices.kGenericCDROMIconResource,
        )
        self.assertEqual(
            LaunchServices.desktopIconResource, LaunchServices.kDesktopIconResource
        )
        self.assertEqual(
            LaunchServices.openFolderIconResource,
            LaunchServices.kOpenFolderIconResource,
        )
        self.assertEqual(
            LaunchServices.genericHardDiskIconResource,
            LaunchServices.kGenericHardDiskIconResource,
        )
        self.assertEqual(
            LaunchServices.genericFileServerIconResource,
            LaunchServices.kGenericFileServerIconResource,
        )
        self.assertEqual(
            LaunchServices.genericSuitcaseIconResource,
            LaunchServices.kGenericSuitcaseIconResource,
        )
        self.assertEqual(
            LaunchServices.genericMoverObjectIconResource,
            LaunchServices.kGenericMoverObjectIconResource,
        )
        self.assertEqual(
            LaunchServices.genericPreferencesIconResource,
            LaunchServices.kGenericPreferencesIconResource,
        )
        self.assertEqual(
            LaunchServices.genericQueryDocumentIconResource,
            LaunchServices.kGenericQueryDocumentIconResource,
        )
        self.assertEqual(
            LaunchServices.genericExtensionIconResource,
            LaunchServices.kGenericExtensionIconResource,
        )
        self.assertEqual(
            LaunchServices.systemFolderIconResource,
            LaunchServices.kSystemFolderIconResource,
        )
        self.assertEqual(
            LaunchServices.appleMenuFolderIconResource,
            LaunchServices.kAppleMenuFolderIconResource,
        )
        self.assertEqual(LaunchServices.kStartupFolderIconResource, -3981)
        self.assertEqual(LaunchServices.kOwnedFolderIconResource, -3980)
        self.assertEqual(LaunchServices.kDropFolderIconResource, -3979)
        self.assertEqual(LaunchServices.kSharedFolderIconResource, -3978)
        self.assertEqual(LaunchServices.kMountedFolderIconResource, -3977)
        self.assertEqual(LaunchServices.kControlPanelFolderIconResource, -3976)
        self.assertEqual(LaunchServices.kPrintMonitorFolderIconResource, -3975)
        self.assertEqual(LaunchServices.kPreferencesFolderIconResource, -3974)
        self.assertEqual(LaunchServices.kExtensionsFolderIconResource, -3973)
        self.assertEqual(LaunchServices.kFontsFolderIconResource, -3968)
        self.assertEqual(LaunchServices.kFullTrashIconResource, -3984)
        self.assertEqual(
            LaunchServices.startupFolderIconResource,
            LaunchServices.kStartupFolderIconResource,
        )
        self.assertEqual(
            LaunchServices.ownedFolderIconResource,
            LaunchServices.kOwnedFolderIconResource,
        )
        self.assertEqual(
            LaunchServices.dropFolderIconResource,
            LaunchServices.kDropFolderIconResource,
        )
        self.assertEqual(
            LaunchServices.sharedFolderIconResource,
            LaunchServices.kSharedFolderIconResource,
        )
        self.assertEqual(
            LaunchServices.mountedFolderIconResource,
            LaunchServices.kMountedFolderIconResource,
        )
        self.assertEqual(
            LaunchServices.controlPanelFolderIconResource,
            LaunchServices.kControlPanelFolderIconResource,
        )
        self.assertEqual(
            LaunchServices.printMonitorFolderIconResource,
            LaunchServices.kPrintMonitorFolderIconResource,
        )
        self.assertEqual(
            LaunchServices.preferencesFolderIconResource,
            LaunchServices.kPreferencesFolderIconResource,
        )
        self.assertEqual(
            LaunchServices.extensionsFolderIconResource,
            LaunchServices.kExtensionsFolderIconResource,
        )
        self.assertEqual(
            LaunchServices.fontsFolderIconResource,
            LaunchServices.kFontsFolderIconResource,
        )
        self.assertEqual(
            LaunchServices.fullTrashIconResource, LaunchServices.kFullTrashIconResource
        )
        self.assertEqual(LaunchServices.kSystemIconsCreator, fourcc(b"macs"))

        self.assertEqual(LaunchServices.kClipboardIcon, fourcc(b"CLIP"))
        self.assertEqual(LaunchServices.kClippingUnknownTypeIcon, fourcc(b"clpu"))
        self.assertEqual(LaunchServices.kClippingPictureTypeIcon, fourcc(b"clpp"))
        self.assertEqual(LaunchServices.kClippingTextTypeIcon, fourcc(b"clpt"))
        self.assertEqual(LaunchServices.kClippingSoundTypeIcon, fourcc(b"clps"))
        self.assertEqual(LaunchServices.kDesktopIcon, fourcc(b"desk"))
        self.assertEqual(LaunchServices.kFinderIcon, fourcc(b"FNDR"))
        self.assertEqual(LaunchServices.kComputerIcon, fourcc(b"root"))
        self.assertEqual(LaunchServices.kFontSuitcaseIcon, fourcc(b"FFIL"))
        self.assertEqual(LaunchServices.kFullTrashIcon, fourcc(b"ftrh"))
        self.assertEqual(LaunchServices.kGenericApplicationIcon, fourcc(b"APPL"))
        self.assertEqual(LaunchServices.kGenericCDROMIcon, fourcc(b"cddr"))
        self.assertEqual(LaunchServices.kGenericControlPanelIcon, fourcc(b"APPC"))
        self.assertEqual(LaunchServices.kGenericControlStripModuleIcon, fourcc(b"sdev"))
        self.assertEqual(LaunchServices.kGenericComponentIcon, fourcc(b"thng"))
        self.assertEqual(LaunchServices.kGenericDeskAccessoryIcon, fourcc(b"APPD"))
        self.assertEqual(LaunchServices.kGenericDocumentIcon, fourcc(b"docu"))
        self.assertEqual(LaunchServices.kGenericEditionFileIcon, fourcc(b"edtf"))
        self.assertEqual(LaunchServices.kGenericExtensionIcon, fourcc(b"INIT"))
        self.assertEqual(LaunchServices.kGenericFileServerIcon, fourcc(b"srvr"))
        self.assertEqual(LaunchServices.kGenericFontIcon, fourcc(b"ffil"))
        self.assertEqual(LaunchServices.kGenericFontScalerIcon, fourcc(b"sclr"))
        self.assertEqual(LaunchServices.kGenericFloppyIcon, fourcc(b"flpy"))
        self.assertEqual(LaunchServices.kGenericHardDiskIcon, fourcc(b"hdsk"))
        self.assertEqual(LaunchServices.kGenericIDiskIcon, fourcc(b"idsk"))
        self.assertEqual(LaunchServices.kGenericRemovableMediaIcon, fourcc(b"rmov"))
        self.assertEqual(LaunchServices.kGenericMoverObjectIcon, fourcc(b"movr"))
        self.assertEqual(LaunchServices.kGenericPCCardIcon, fourcc(b"pcmc"))
        self.assertEqual(LaunchServices.kGenericPreferencesIcon, fourcc(b"pref"))
        self.assertEqual(LaunchServices.kGenericQueryDocumentIcon, fourcc(b"qery"))
        self.assertEqual(LaunchServices.kGenericRAMDiskIcon, fourcc(b"ramd"))
        self.assertEqual(LaunchServices.kGenericSharedLibaryIcon, fourcc(b"shlb"))
        self.assertEqual(LaunchServices.kGenericStationeryIcon, fourcc(b"sdoc"))
        self.assertEqual(LaunchServices.kGenericSuitcaseIcon, fourcc(b"suit"))
        self.assertEqual(LaunchServices.kGenericURLIcon, fourcc(b"gurl"))
        self.assertEqual(LaunchServices.kGenericWORMIcon, fourcc(b"worm"))
        self.assertEqual(LaunchServices.kInternationalResourcesIcon, fourcc(b"ifil"))
        self.assertEqual(LaunchServices.kKeyboardLayoutIcon, fourcc(b"kfil"))
        self.assertEqual(LaunchServices.kSoundFileIcon, fourcc(b"sfil"))
        self.assertEqual(LaunchServices.kSystemSuitcaseIcon, fourcc(b"zsys"))
        self.assertEqual(LaunchServices.kTrashIcon, fourcc(b"trsh"))
        self.assertEqual(LaunchServices.kTrueTypeFontIcon, fourcc(b"tfil"))
        self.assertEqual(LaunchServices.kTrueTypeFlatFontIcon, fourcc(b"sfnt"))
        self.assertEqual(LaunchServices.kTrueTypeMultiFlatFontIcon, fourcc(b"ttcf"))
        self.assertEqual(LaunchServices.kUserIDiskIcon, fourcc(b"udsk"))
        self.assertEqual(LaunchServices.kUnknownFSObjectIcon, fourcc(b"unfs"))
        self.assertEqual(
            LaunchServices.kInternationResourcesIcon,
            LaunchServices.kInternationalResourcesIcon,
        )
        self.assertEqual(LaunchServices.kInternetLocationHTTPIcon, fourcc(b"ilht"))
        self.assertEqual(LaunchServices.kInternetLocationFTPIcon, fourcc(b"ilft"))
        self.assertEqual(
            LaunchServices.kInternetLocationAppleShareIcon, fourcc(b"ilaf")
        )
        self.assertEqual(
            LaunchServices.kInternetLocationAppleTalkZoneIcon, fourcc(b"ilat")
        )
        self.assertEqual(LaunchServices.kInternetLocationFileIcon, fourcc(b"ilfi"))
        self.assertEqual(LaunchServices.kInternetLocationMailIcon, fourcc(b"ilma"))
        self.assertEqual(LaunchServices.kInternetLocationNewsIcon, fourcc(b"ilnw"))
        self.assertEqual(
            LaunchServices.kInternetLocationNSLNeighborhoodIcon, fourcc(b"ilns")
        )
        self.assertEqual(LaunchServices.kInternetLocationGenericIcon, fourcc(b"ilge"))
        self.assertEqual(LaunchServices.kGenericFolderIcon, fourcc(b"fldr"))
        self.assertEqual(LaunchServices.kDropFolderIcon, fourcc(b"dbox"))
        self.assertEqual(LaunchServices.kMountedFolderIcon, fourcc(b"mntd"))
        self.assertEqual(LaunchServices.kOpenFolderIcon, fourcc(b"ofld"))
        self.assertEqual(LaunchServices.kOwnedFolderIcon, fourcc(b"ownd"))
        self.assertEqual(LaunchServices.kPrivateFolderIcon, fourcc(b"prvf"))
        self.assertEqual(LaunchServices.kSharedFolderIcon, fourcc(b"shfl"))
        self.assertEqual(LaunchServices.kSharingPrivsNotApplicableIcon, fourcc(b"shna"))
        self.assertEqual(LaunchServices.kSharingPrivsReadOnlyIcon, fourcc(b"shro"))
        self.assertEqual(LaunchServices.kSharingPrivsReadWriteIcon, fourcc(b"shrw"))
        self.assertEqual(LaunchServices.kSharingPrivsUnknownIcon, fourcc(b"shuk"))
        self.assertEqual(LaunchServices.kSharingPrivsWritableIcon, fourcc(b"writ"))
        self.assertEqual(LaunchServices.kUserFolderIcon, fourcc(b"ufld"))
        self.assertEqual(LaunchServices.kWorkgroupFolderIcon, fourcc(b"wfld"))
        self.assertEqual(LaunchServices.kGuestUserIcon, fourcc(b"gusr"))
        self.assertEqual(LaunchServices.kUserIcon, fourcc(b"user"))
        self.assertEqual(LaunchServices.kOwnerIcon, fourcc(b"susr"))
        self.assertEqual(LaunchServices.kGroupIcon, fourcc(b"grup"))
        self.assertEqual(LaunchServices.kAppearanceFolderIcon, fourcc(b"appr"))
        self.assertEqual(LaunchServices.kAppleExtrasFolderIcon, cast_int(0x616578C4))
        self.assertEqual(LaunchServices.kAppleMenuFolderIcon, fourcc(b"amnu"))
        self.assertEqual(LaunchServices.kApplicationsFolderIcon, fourcc(b"apps"))
        self.assertEqual(LaunchServices.kApplicationSupportFolderIcon, fourcc(b"asup"))
        self.assertEqual(LaunchServices.kAssistantsFolderIcon, cast_int(0x617374C4))
        self.assertEqual(LaunchServices.kColorSyncFolderIcon, fourcc(b"prof"))
        self.assertEqual(LaunchServices.kContextualMenuItemsFolderIcon, fourcc(b"cmnu"))
        self.assertEqual(
            LaunchServices.kControlPanelDisabledFolderIcon, fourcc(b"ctrD")
        )
        self.assertEqual(LaunchServices.kControlPanelFolderIcon, fourcc(b"ctrl"))
        self.assertEqual(
            LaunchServices.kControlStripModulesFolderIcon, cast_int(0x736476C4)
        )
        self.assertEqual(LaunchServices.kDocumentsFolderIcon, fourcc(b"docs"))
        self.assertEqual(LaunchServices.kExtensionsDisabledFolderIcon, fourcc(b"extD"))
        self.assertEqual(LaunchServices.kExtensionsFolderIcon, fourcc(b"extn"))
        self.assertEqual(LaunchServices.kFavoritesFolderIcon, fourcc(b"favs"))
        self.assertEqual(LaunchServices.kFontsFolderIcon, fourcc(b"font"))
        self.assertEqual(LaunchServices.kHelpFolderIcon, cast_int(0xC4686C70))
        self.assertEqual(LaunchServices.kInternetFolderIcon, cast_int(0x696E74C4))
        self.assertEqual(LaunchServices.kInternetPlugInFolderIcon, cast_int(0xC46E6574))
        self.assertEqual(LaunchServices.kInternetSearchSitesFolderIcon, fourcc(b"issf"))
        self.assertEqual(LaunchServices.kLocalesFolderIcon, cast_int(0xC46C6F63))
        self.assertEqual(LaunchServices.kMacOSReadMeFolderIcon, cast_int(0x6D6F72C4))
        self.assertEqual(LaunchServices.kPublicFolderIcon, fourcc(b"pubf"))
        self.assertEqual(LaunchServices.kPreferencesFolderIcon, cast_int(0x707266C4))
        self.assertEqual(LaunchServices.kPrinterDescriptionFolderIcon, fourcc(b"ppdf"))
        self.assertEqual(LaunchServices.kPrinterDriverFolderIcon, cast_int(0xC4707264))
        self.assertEqual(LaunchServices.kPrintMonitorFolderIcon, fourcc(b"prnt"))
        self.assertEqual(LaunchServices.kRecentApplicationsFolderIcon, fourcc(b"rapp"))
        self.assertEqual(LaunchServices.kRecentDocumentsFolderIcon, fourcc(b"rdoc"))
        self.assertEqual(LaunchServices.kRecentServersFolderIcon, fourcc(b"rsrv"))
        self.assertEqual(
            LaunchServices.kScriptingAdditionsFolderIcon, cast_int(0xC4736372)
        )
        self.assertEqual(
            LaunchServices.kSharedLibrariesFolderIcon, cast_int(0xC46C6962)
        )
        self.assertEqual(LaunchServices.kScriptsFolderIcon, cast_int(0x736372C4))
        self.assertEqual(
            LaunchServices.kShutdownItemsDisabledFolderIcon, fourcc(b"shdD")
        )
        self.assertEqual(LaunchServices.kShutdownItemsFolderIcon, fourcc(b"shdf"))
        self.assertEqual(LaunchServices.kSpeakableItemsFolder, fourcc(b"spki"))
        self.assertEqual(
            LaunchServices.kStartupItemsDisabledFolderIcon, fourcc(b"strD")
        )
        self.assertEqual(LaunchServices.kStartupItemsFolderIcon, fourcc(b"strt"))
        self.assertEqual(
            LaunchServices.kSystemExtensionDisabledFolderIcon, fourcc(b"macD")
        )
        self.assertEqual(LaunchServices.kSystemFolderIcon, fourcc(b"macs"))
        self.assertEqual(LaunchServices.kTextEncodingsFolderIcon, cast_int(0xC4746578))
        self.assertEqual(LaunchServices.kUsersFolderIcon, cast_int(0x757372C4))
        self.assertEqual(LaunchServices.kUtilitiesFolderIcon, cast_int(0x757469C4))
        self.assertEqual(LaunchServices.kVoicesFolderIcon, fourcc(b"fvoc"))
        self.assertEqual(LaunchServices.kAppleScriptBadgeIcon, fourcc(b"scrp"))
        self.assertEqual(LaunchServices.kLockedBadgeIcon, fourcc(b"lbdg"))
        self.assertEqual(LaunchServices.kMountedBadgeIcon, fourcc(b"mbdg"))
        self.assertEqual(LaunchServices.kSharedBadgeIcon, fourcc(b"sbdg"))
        self.assertEqual(LaunchServices.kAliasBadgeIcon, fourcc(b"abdg"))
        self.assertEqual(LaunchServices.kAlertCautionBadgeIcon, fourcc(b"cbdg"))
        self.assertEqual(LaunchServices.kAlertNoteIcon, fourcc(b"note"))
        self.assertEqual(LaunchServices.kAlertCautionIcon, fourcc(b"caut"))
        self.assertEqual(LaunchServices.kAlertStopIcon, fourcc(b"stop"))
        self.assertEqual(LaunchServices.kAppleTalkIcon, fourcc(b"atlk"))
        self.assertEqual(LaunchServices.kAppleTalkZoneIcon, fourcc(b"atzn"))
        self.assertEqual(LaunchServices.kAFPServerIcon, fourcc(b"afps"))
        self.assertEqual(LaunchServices.kFTPServerIcon, fourcc(b"ftps"))
        self.assertEqual(LaunchServices.kHTTPServerIcon, fourcc(b"htps"))
        self.assertEqual(LaunchServices.kGenericNetworkIcon, fourcc(b"gnet"))
        self.assertEqual(LaunchServices.kIPFileServerIcon, fourcc(b"isrv"))
        self.assertEqual(LaunchServices.kToolbarCustomizeIcon, fourcc(b"tcus"))
        self.assertEqual(LaunchServices.kToolbarDeleteIcon, fourcc(b"tdel"))
        self.assertEqual(LaunchServices.kToolbarFavoritesIcon, fourcc(b"tfav"))
        self.assertEqual(LaunchServices.kToolbarHomeIcon, fourcc(b"thom"))
        self.assertEqual(LaunchServices.kAppleLogoIcon, fourcc(b"capl"))
        self.assertEqual(LaunchServices.kAppleMenuIcon, fourcc(b"sapl"))
        self.assertEqual(LaunchServices.kBackwardArrowIcon, fourcc(b"baro"))
        self.assertEqual(LaunchServices.kFavoriteItemsIcon, fourcc(b"favr"))
        self.assertEqual(LaunchServices.kForwardArrowIcon, fourcc(b"faro"))
        self.assertEqual(LaunchServices.kGridIcon, fourcc(b"grid"))
        self.assertEqual(LaunchServices.kHelpIcon, fourcc(b"help"))
        self.assertEqual(LaunchServices.kKeepArrangedIcon, fourcc(b"arng"))
        self.assertEqual(LaunchServices.kLockedIcon, fourcc(b"lock"))
        self.assertEqual(LaunchServices.kNoFilesIcon, fourcc(b"nfil"))
        self.assertEqual(LaunchServices.kNoFolderIcon, fourcc(b"nfld"))
        self.assertEqual(LaunchServices.kNoWriteIcon, fourcc(b"nwrt"))
        self.assertEqual(
            LaunchServices.kProtectedApplicationFolderIcon, fourcc(b"papp")
        )
        self.assertEqual(LaunchServices.kProtectedSystemFolderIcon, fourcc(b"psys"))
        self.assertEqual(LaunchServices.kRecentItemsIcon, fourcc(b"rcnt"))
        self.assertEqual(LaunchServices.kShortcutIcon, fourcc(b"shrt"))
        self.assertEqual(LaunchServices.kSortAscendingIcon, fourcc(b"asnd"))
        self.assertEqual(LaunchServices.kSortDescendingIcon, fourcc(b"dsnd"))
        self.assertEqual(LaunchServices.kUnlockedIcon, fourcc(b"ulck"))
        self.assertEqual(LaunchServices.kConnectToIcon, fourcc(b"cnct"))
        self.assertEqual(LaunchServices.kGenericWindowIcon, fourcc(b"gwin"))
        self.assertEqual(LaunchServices.kQuestionMarkIcon, fourcc(b"ques"))
        self.assertEqual(LaunchServices.kDeleteAliasIcon, fourcc(b"dali"))
        self.assertEqual(LaunchServices.kEjectMediaIcon, fourcc(b"ejec"))
        self.assertEqual(LaunchServices.kBurningIcon, fourcc(b"burn"))
        self.assertEqual(LaunchServices.kRightContainerArrowIcon, fourcc(b"rcar"))
        self.assertEqual(LaunchServices.kIconServicesNormalUsageFlag, 0)
        self.assertEqual(LaunchServices.kIconServicesNoBadgeFlag, 1)
        self.assertEqual(LaunchServices.kIconServicesUpdateIfNeededFlag, 2)
        self.assertEqual(LaunchServices.kIconServicesCatalogInfoMask, 531_550)

    def testFunctions(self):
        self.assertArgIsOut(LaunchServices.GetIconRef, 3)
        err, icon = LaunchServices.GetIconRef(
            0, LaunchServices.kSystemIconsCreator, LaunchServices.kShortcutIcon, None
        )
        self.assertIsInstance(err, int)
        self.assertIsInstance(icon, LaunchServices.IconRef)

        try:
            self.assertArgIsOut(LaunchServices.GetIconRefOwners, 1)
            err, cnt = LaunchServices.GetIconRefOwners(icon, None)
            self.assertIsInstance(err, int)
            self.assertIsInstance(cnt, int)

            err = LaunchServices.AcquireIconRef(icon)
            self.assertEqual(err, 0)

            err = LaunchServices.ReleaseIconRef(icon)
            self.assertEqual(err, 0)

            self.assertArgIsOut(LaunchServices.GetIconRefFromFolder, 5)

            self.assertArgHasType(
                LaunchServices.GetIconRefFromFileInfo,
                2,
                objc._C_IN + objc._C_PTR + objc._C_UNICHAR,
            )
            self.assertArgIsOut(LaunchServices.GetIconRefFromFileInfo, 6)
            self.assertArgIsOut(LaunchServices.GetIconRefFromFileInfo, 7)

            self.assertArgIsOut(LaunchServices.GetIconRefFromTypeInfo, 5)

            self.assertArgIsIn(LaunchServices.GetIconRefFromIconFamilyPtr, 0)
            self.assertArgIsOut(LaunchServices.GetIconRefFromIconFamilyPtr, 2)

            # self.assertArgIsOut(LaunchServices.GetIconRefFromComponent, 1)

            # XXX: Untested for now...
            # LaunchServices.RegisterIconRefFromIconFamily
            # LaunchServices.RegisterIconRefFromFSRef
            # LaunchServices.UnregisterIconRef
            # LaunchServices.UpdateIconRef
            # LaunchServices.OverrideIconRef
            # LaunchServices.RemoveIconRefOverride

            self.assertArgIsOut(LaunchServices.CompositeIconRef, 2)

            self.assertArgIsOut(LaunchServices.IsIconRefComposite, 1)
            self.assertArgIsOut(LaunchServices.IsIconRefComposite, 2)

            self.assertResultIsBOOL(LaunchServices.IsValidIconRef)
            self.assertResultIsBOOL(LaunchServices.IsDataAvailableInIconRef)

            self.assertArgIsBOOL(LaunchServices.SetCustomIconsEnabled, 1)
            self.assertArgIsOut(LaunchServices.GetCustomIconsEnabled, 1)
            self.assertArgHasType(
                LaunchServices.GetCustomIconsEnabled,
                1,
                objc._C_OUT + objc._C_PTR + objc._C_NSBOOL,
            )

            # Untested...
            # LaunchServices.ReadIconFromFSRef

        finally:
            err = LaunchServices.ReleaseIconRef(icon)
            self.assertEqual(err, 0)

    def testOpaque(self):
        self.assertIsOpaquePointer(LaunchServices.IconRef)
