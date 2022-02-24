import objc
import AppKit
from PyObjCTools.TestSupport import TestCase, min_os_level


class TestNSWorkspace(TestCase):
    def test_typed_enum(self):
        self.assertIsTypedEnum(AppKit.NSWorkspaceDesktopImageOptionKey, str)

    def test_enum_types(self):
        self.assertIsEnumType(AppKit.NSWorkspaceAuthorizationType)
        self.assertIsEnumType(AppKit.NSWorkspaceIconCreationOptions)
        self.assertIsEnumType(AppKit.NSWorkspaceLaunchOptions)

    def testInfoForFile(self):
        ws = AppKit.NSWorkspace.sharedWorkspace()

        # A method with 2 output parameters, this means the result
        # is a tuple with 3 elements (return value, param1, param2)
        res = ws.getInfoForFile_application_type_("/", None, None)
        self.assertIsInstance(res, tuple)
        self.assertEqual(len(res), 3)
        self.assertEqual(res[0], 1)
        self.assertEqual(res[1], "/System/Library/CoreServices/Finder.app")
        self.assertEqual(res[2], "")

    def testConstants(self):
        self.assertEqual(AppKit.NSWorkspaceLaunchAndPrint, 0x00000002)
        self.assertEqual(AppKit.NSWorkspaceLaunchWithErrorPresentation, 0x00000040)
        self.assertEqual(AppKit.NSWorkspaceLaunchInhibitingBackgroundOnly, 0x00000080)
        self.assertEqual(AppKit.NSWorkspaceLaunchWithoutAddingToRecents, 0x00000100)
        self.assertEqual(AppKit.NSWorkspaceLaunchWithoutActivation, 0x00000200)
        self.assertEqual(AppKit.NSWorkspaceLaunchAsync, 0x00010000)
        self.assertEqual(AppKit.NSWorkspaceLaunchAllowingClassicStartup, 0x00020000)
        self.assertEqual(AppKit.NSWorkspaceLaunchPreferringClassic, 0x00040000)
        self.assertEqual(AppKit.NSWorkspaceLaunchNewInstance, 0x00080000)
        self.assertEqual(AppKit.NSWorkspaceLaunchAndHide, 0x00100000)
        self.assertEqual(AppKit.NSWorkspaceLaunchAndHideOthers, 0x00200000)
        self.assertEqual(AppKit.NSWorkspaceLaunchDefault, AppKit.NSWorkspaceLaunchAsync)

        self.assertEqual(AppKit.NSExcludeQuickDrawElementsIconCreationOption, 1 << 1)
        self.assertEqual(AppKit.NSExclude10_4ElementsIconCreationOption, 1 << 2)

        self.assertIsInstance(AppKit.NSWorkspaceDidLaunchApplicationNotification, str)
        self.assertIsInstance(AppKit.NSWorkspaceDidMountNotification, str)
        self.assertIsInstance(
            AppKit.NSWorkspaceDidPerformFileOperationNotification, str
        )
        self.assertIsInstance(
            AppKit.NSWorkspaceDidTerminateApplicationNotification, str
        )
        self.assertIsInstance(AppKit.NSWorkspaceDidUnmountNotification, str)
        self.assertIsInstance(AppKit.NSWorkspaceWillLaunchApplicationNotification, str)
        self.assertIsInstance(AppKit.NSWorkspaceWillPowerOffNotification, str)
        self.assertIsInstance(AppKit.NSWorkspaceWillUnmountNotification, str)
        self.assertIsInstance(AppKit.NSWorkspaceWillSleepNotification, str)
        self.assertIsInstance(AppKit.NSWorkspaceDidWakeNotification, str)
        self.assertIsInstance(AppKit.NSWorkspaceSessionDidBecomeActiveNotification, str)
        self.assertIsInstance(AppKit.NSWorkspaceSessionDidResignActiveNotification, str)
        self.assertIsInstance(AppKit.NSPlainFileType, str)
        self.assertIsInstance(AppKit.NSDirectoryFileType, str)
        self.assertIsInstance(AppKit.NSApplicationFileType, str)
        self.assertIsInstance(AppKit.NSFilesystemFileType, str)
        self.assertIsInstance(AppKit.NSShellCommandFileType, str)
        self.assertIsInstance(AppKit.NSWorkspaceMoveOperation, str)
        self.assertIsInstance(AppKit.NSWorkspaceCopyOperation, str)
        self.assertIsInstance(AppKit.NSWorkspaceLinkOperation, str)
        self.assertIsInstance(AppKit.NSWorkspaceCompressOperation, str)
        self.assertIsInstance(AppKit.NSWorkspaceDecompressOperation, str)
        self.assertIsInstance(AppKit.NSWorkspaceEncryptOperation, str)
        self.assertIsInstance(AppKit.NSWorkspaceDecryptOperation, str)
        self.assertIsInstance(AppKit.NSWorkspaceDestroyOperation, str)
        self.assertIsInstance(AppKit.NSWorkspaceRecycleOperation, str)
        self.assertIsInstance(AppKit.NSWorkspaceDuplicateOperation, str)

        self.assertEqual(AppKit.NSWorkspaceAuthorizationTypeCreateSymbolicLink, 0)
        self.assertEqual(AppKit.NSWorkspaceAuthorizationTypeSetAttributes, 1)
        self.assertEqual(AppKit.NSWorkspaceAuthorizationTypeReplaceFile, 2)

    @min_os_level("10.6")
    def testConstants10_6(self):
        self.assertIsInstance(AppKit.NSWorkspaceDesktopImageScalingKey, str)
        self.assertIsInstance(AppKit.NSWorkspaceDesktopImageAllowClippingKey, str)
        self.assertIsInstance(AppKit.NSWorkspaceDesktopImageFillColorKey, str)
        self.assertIsInstance(AppKit.NSWorkspaceApplicationKey, str)
        self.assertIsInstance(AppKit.NSWorkspaceDidHideApplicationNotification, str)
        self.assertIsInstance(AppKit.NSWorkspaceDidUnhideApplicationNotification, str)
        self.assertIsInstance(AppKit.NSWorkspaceDidActivateApplicationNotification, str)
        self.assertIsInstance(
            AppKit.NSWorkspaceDidDeactivateApplicationNotification, str
        )
        self.assertIsInstance(AppKit.NSWorkspaceVolumeLocalizedNameKey, str)
        self.assertIsInstance(AppKit.NSWorkspaceVolumeURLKey, str)
        self.assertIsInstance(AppKit.NSWorkspaceVolumeOldLocalizedNameKey, str)
        self.assertIsInstance(AppKit.NSWorkspaceVolumeOldURLKey, str)
        self.assertIsInstance(AppKit.NSWorkspaceDidRenameVolumeNotification, str)
        self.assertIsInstance(AppKit.NSWorkspaceScreensDidSleepNotification, str)
        self.assertIsInstance(AppKit.NSWorkspaceScreensDidWakeNotification, str)
        self.assertIsInstance(AppKit.NSWorkspaceDidChangeFileLabelsNotification, str)
        self.assertIsInstance(AppKit.NSWorkspaceActiveSpaceDidChangeNotification, str)
        self.assertIsInstance(AppKit.NSWorkspaceLaunchConfigurationAppleEvent, str)
        self.assertIsInstance(AppKit.NSWorkspaceLaunchConfigurationArguments, str)
        self.assertIsInstance(AppKit.NSWorkspaceLaunchConfigurationEnvironment, str)
        self.assertIsInstance(AppKit.NSWorkspaceLaunchConfigurationArchitecture, str)

    def testMethods(self):
        self.assertResultIsBOOL(AppKit.NSWorkspace.openFile_)
        self.assertResultIsBOOL(AppKit.NSWorkspace.openFile_withApplication_)
        self.assertResultIsBOOL(
            AppKit.NSWorkspace.openFile_withApplication_andDeactivate_
        )
        self.assertArgIsBOOL(
            AppKit.NSWorkspace.openFile_withApplication_andDeactivate_, 2
        )
        self.assertResultIsBOOL(AppKit.NSWorkspace.openTempFile_)
        self.assertResultIsBOOL(AppKit.NSWorkspace.openFile_fromImage_at_inView_)
        self.assertResultIsBOOL(AppKit.NSWorkspace.openURL_)
        self.assertResultIsBOOL(AppKit.NSWorkspace.launchApplication_)
        self.assertResultIsBOOL(
            AppKit.NSWorkspace.launchApplication_showIcon_autolaunch_
        )
        self.assertArgIsBOOL(
            AppKit.NSWorkspace.launchApplication_showIcon_autolaunch_, 1
        )
        self.assertArgIsBOOL(
            AppKit.NSWorkspace.launchApplication_showIcon_autolaunch_, 2
        )
        self.assertResultIsBOOL(AppKit.NSWorkspace.selectFile_inFileViewerRootedAtPath_)
        self.assertResultIsBOOL(AppKit.NSWorkspace.fileSystemChanged)
        self.assertResultIsBOOL(AppKit.NSWorkspace.userDefaultsChanged)
        self.assertResultIsBOOL(AppKit.NSWorkspace.getInfoForFile_application_type_)
        self.assertArgIsOut(AppKit.NSWorkspace.getInfoForFile_application_type_, 1)
        self.assertArgIsOut(AppKit.NSWorkspace.getInfoForFile_application_type_, 2)
        self.assertResultIsBOOL(AppKit.NSWorkspace.isFilePackageAtPath_)
        self.assertResultIsBOOL(AppKit.NSWorkspace.setIcon_forFile_options_)
        self.assertResultIsBOOL(
            AppKit.NSWorkspace.getFileSystemInfoForPath_isRemovable_isWritable_isUnmountable_description_type_  # noqa: B950
        )
        self.assertArgHasType(
            AppKit.NSWorkspace.getFileSystemInfoForPath_isRemovable_isWritable_isUnmountable_description_type_,  # noqa: B950
            1,
            b"o^" + objc._C_NSBOOL,
        )
        self.assertArgHasType(
            AppKit.NSWorkspace.getFileSystemInfoForPath_isRemovable_isWritable_isUnmountable_description_type_,  # noqa: B950
            2,
            b"o^" + objc._C_NSBOOL,
        )
        self.assertArgHasType(
            AppKit.NSWorkspace.getFileSystemInfoForPath_isRemovable_isWritable_isUnmountable_description_type_,  # noqa: B950
            3,
            b"o^" + objc._C_NSBOOL,
        )
        self.assertArgIsOut(
            AppKit.NSWorkspace.getFileSystemInfoForPath_isRemovable_isWritable_isUnmountable_description_type_,  # noqa: B950
            4,
        )
        self.assertArgIsOut(
            AppKit.NSWorkspace.getFileSystemInfoForPath_isRemovable_isWritable_isUnmountable_description_type_,  # noqa: B950
            5,
        )
        self.assertResultIsBOOL(
            AppKit.NSWorkspace.performFileOperation_source_destination_files_tag_
        )
        self.assertArgIsOut(
            AppKit.NSWorkspace.performFileOperation_source_destination_files_tag_, 4
        )
        self.assertResultIsBOOL(AppKit.NSWorkspace.unmountAndEjectDeviceAtPath_)
        self.assertResultIsBOOL(
            AppKit.NSWorkspace.launchAppWithBundleIdentifier_options_additionalEventParamDescriptor_launchIdentifier_  # noqa: B950
        )
        self.assertArgIsOut(
            AppKit.NSWorkspace.launchAppWithBundleIdentifier_options_additionalEventParamDescriptor_launchIdentifier_,  # noqa: B950
            3,
        )
        self.assertResultIsBOOL(
            AppKit.NSWorkspace.openURLs_withAppBundleIdentifier_options_additionalEventParamDescriptor_launchIdentifiers_  # noqa: B950
        )
        self.assertArgIsOut(
            AppKit.NSWorkspace.openURLs_withAppBundleIdentifier_options_additionalEventParamDescriptor_launchIdentifiers_,  # noqa: B950
            4,
        )
        self.assertArgIsOut(AppKit.NSWorkspace.typeOfFile_error_, 1)
        self.assertResultIsBOOL(AppKit.NSWorkspace.filenameExtension_isValidForType_)
        self.assertResultIsBOOL(AppKit.NSWorkspace.type_conformsToType_)

        self.assertResultIsBOOL(AppKit.NSWorkspace.selectFile_inFileViewerRootedAtPath_)
        self.assertArgHasType(
            AppKit.NSWorkspace.slideImage_from_to_, 1, AppKit.NSPoint.__typestr__
        )
        self.assertArgHasType(
            AppKit.NSWorkspace.slideImage_from_to_, 2, AppKit.NSPoint.__typestr__
        )

    @min_os_level("10.6")
    def testMethods10_6(self):
        self.assertArgIsOut(
            AppKit.NSWorkspace.launchApplicationAtURL_options_configuration_error_, 3
        )
        self.assertResultIsBOOL(AppKit.NSWorkspace.showSearchResultsForQueryString_)

        self.assertArgIsBlock(
            AppKit.NSWorkspace.recycleURLs_completionHandler_, 1, b"v@@"
        )
        self.assertArgIsBlock(
            AppKit.NSWorkspace.duplicateURLs_completionHandler_, 1, b"v@@"
        )

        self.assertResultIsBOOL(AppKit.NSWorkspace.unmountAndEjectDeviceAtURL_error_)
        self.assertArgIsOut(AppKit.NSWorkspace.unmountAndEjectDeviceAtURL_error_, 1)

        self.assertResultIsBOOL(
            AppKit.NSWorkspace.setDesktopImageURL_forScreen_options_error_
        )
        self.assertArgIsOut(
            AppKit.NSWorkspace.setDesktopImageURL_forScreen_options_error_, 3
        )

    @min_os_level("10.10")
    def testMethods10_10(self):
        self.assertArgIsOut(AppKit.NSWorkspace.openURL_options_configuration_error_, 3)
        self.assertArgIsOut(
            AppKit.NSWorkspace.openURLs_withApplicationAtURL_options_configuration_error_,
            4,
        )

    @min_os_level("10.13")
    def testMethods10_13(self):
        self.assertResultIsBOOL(AppKit.NSWorkspace.isVoiceOverEnabled)
        self.assertResultIsBOOL(AppKit.NSWorkspace.isSwitchControlEnabled)

    @min_os_level("10.14")
    def testMethods10_14(self):
        self.assertArgIsBlock(
            AppKit.NSWorkspace.requestAuthorizationOfType_completionHandler_, 1, b"v@@"
        )

    @min_os_level("10.15")
    def testMethods10_15(self):
        self.assertArgIsBlock(
            AppKit.NSWorkspace.openURL_configuration_completionHandler_, 2, b"v@@"
        )
        self.assertArgIsBlock(
            AppKit.NSWorkspace.openURLs_withApplicationAtURL_configuration_completionHandler_,
            3,
            b"v@@",
        )
        self.assertArgIsBlock(
            AppKit.NSWorkspace.openApplicationAtURL_configuration_completionHandler_,
            2,
            b"v@@",
        )

        self.assertResultIsBOOL(AppKit.NSWorkspaceOpenConfiguration.promptsUserIfNeeded)
        self.assertResultIsBOOL(AppKit.NSWorkspaceOpenConfiguration.addsToRecentItems)
        self.assertResultIsBOOL(AppKit.NSWorkspaceOpenConfiguration.activates)
        self.assertResultIsBOOL(AppKit.NSWorkspaceOpenConfiguration.hides)
        self.assertResultIsBOOL(AppKit.NSWorkspaceOpenConfiguration.hidesOthers)
        self.assertResultIsBOOL(AppKit.NSWorkspaceOpenConfiguration.isForPrinting)
        self.assertResultIsBOOL(
            AppKit.NSWorkspaceOpenConfiguration.createsNewApplicationInstance
        )
        self.assertResultIsBOOL(
            AppKit.NSWorkspaceOpenConfiguration.requiresUniversalLinks
        )

        self.assertArgIsBOOL(
            AppKit.NSWorkspaceOpenConfiguration.setPromptsUserIfNeeded_, 0
        )
        self.assertArgIsBOOL(
            AppKit.NSWorkspaceOpenConfiguration.setAddsToRecentItems_, 0
        )
        self.assertArgIsBOOL(AppKit.NSWorkspaceOpenConfiguration.setActivates_, 0)
        self.assertArgIsBOOL(AppKit.NSWorkspaceOpenConfiguration.setHides_, 0)
        self.assertArgIsBOOL(AppKit.NSWorkspaceOpenConfiguration.setHidesOthers_, 0)
        self.assertArgIsBOOL(AppKit.NSWorkspaceOpenConfiguration.setForPrinting_, 0)
        self.assertArgIsBOOL(
            AppKit.NSWorkspaceOpenConfiguration.setCreatesNewApplicationInstance_, 0
        )
        self.assertArgIsBOOL(
            AppKit.NSWorkspaceOpenConfiguration.setRequiresUniversalLinks_, 0
        )

    @min_os_level("12.0")
    def testMethods12_0(self):
        self.assertArgIsBlock(
            AppKit.NSWorkspace.setDefaultApplicationAtURL_toOpenContentTypeOfFileAtURL_completionHandler_,
            2,
            b"v@",
        )
        self.assertArgIsBlock(
            AppKit.NSWorkspace.setDefaultApplicationAtURL_toOpenURLsWithScheme_completionHandler_,
            2,
            b"v@",
        )
        self.assertArgIsBlock(
            AppKit.NSWorkspace.setDefaultApplicationAtURL_toOpenFileAtURL_completionHandler_,
            2,
            b"v@",
        )
        self.assertArgIsBlock(
            AppKit.NSWorkspace.setDefaultApplicationAtURL_toOpenContentType_completionHandler_,
            2,
            b"v@",
        )
