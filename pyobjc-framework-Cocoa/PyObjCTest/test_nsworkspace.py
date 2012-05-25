from PyObjCTools.TestSupport import *
import objc
import os

from AppKit import *

try:
    unicode
except NameError:
    unicode = str


class TestNSWorkspace(TestCase):
    def testInfoForFile(self):
        ws = NSWorkspace.sharedWorkspace()

        # A method with 2 output parameters, this means the result
        # is a tuple with 3 elements (return value, param1, param2)
        res = ws.getInfoForFile_application_type_(b'/'.decode('ascii'), None, None)
        self.assert_(isinstance(res, tuple))
        self.assert_(len(res) == 3)
        self.assert_(res[0] == 1)
        self.assert_(res[1] == b'/System/Library/CoreServices/Finder.app'.decode('ascii'))
        self.assert_(res[2] == b''.decode('ascii'))

    def testConstants(self):
        self.assertEqual(NSWorkspaceLaunchAndPrint, 2)
        self.assertEqual(NSWorkspaceLaunchInhibitingBackgroundOnly, 0x00000080)
        self.assertEqual(NSWorkspaceLaunchWithoutAddingToRecents, 0x00000100)
        self.assertEqual(NSWorkspaceLaunchWithoutActivation, 0x00000200)
        self.assertEqual(NSWorkspaceLaunchAsync, 0x00010000)
        self.assertEqual(NSWorkspaceLaunchAllowingClassicStartup, 0x00020000)
        self.assertEqual(NSWorkspaceLaunchPreferringClassic, 0x00040000)
        self.assertEqual(NSWorkspaceLaunchNewInstance, 0x00080000)
        self.assertEqual(NSWorkspaceLaunchAndHide, 0x00100000)
        self.assertEqual(NSWorkspaceLaunchAndHideOthers, 0x00200000)
        self.assertEqual(NSWorkspaceLaunchDefault, (
                NSWorkspaceLaunchAsync | NSWorkspaceLaunchAllowingClassicStartup))

        self.assertEqual(NSExcludeQuickDrawElementsIconCreationOption, 1 << 1)
        self.assertEqual(NSExclude10_4ElementsIconCreationOption, 1 << 2)

        self.assertIsInstance(NSWorkspaceDidLaunchApplicationNotification, unicode)
        self.assertIsInstance(NSWorkspaceDidMountNotification, unicode)
        self.assertIsInstance(NSWorkspaceDidPerformFileOperationNotification, unicode)
        self.assertIsInstance(NSWorkspaceDidTerminateApplicationNotification, unicode)
        self.assertIsInstance(NSWorkspaceDidUnmountNotification, unicode)
        self.assertIsInstance(NSWorkspaceWillLaunchApplicationNotification, unicode)
        self.assertIsInstance(NSWorkspaceWillPowerOffNotification, unicode)
        self.assertIsInstance(NSWorkspaceWillUnmountNotification, unicode)
        self.assertIsInstance(NSWorkspaceWillSleepNotification, unicode)
        self.assertIsInstance(NSWorkspaceDidWakeNotification, unicode)
        self.assertIsInstance(NSWorkspaceSessionDidBecomeActiveNotification, unicode)
        self.assertIsInstance(NSWorkspaceSessionDidResignActiveNotification, unicode)
        self.assertIsInstance(NSPlainFileType, unicode)
        self.assertIsInstance(NSDirectoryFileType, unicode)
        self.assertIsInstance(NSApplicationFileType, unicode)
        self.assertIsInstance(NSFilesystemFileType, unicode)
        self.assertIsInstance(NSShellCommandFileType, unicode)
        self.assertIsInstance(NSWorkspaceMoveOperation, unicode)
        self.assertIsInstance(NSWorkspaceCopyOperation, unicode)
        self.assertIsInstance(NSWorkspaceLinkOperation, unicode)
        self.assertIsInstance(NSWorkspaceCompressOperation, unicode)
        self.assertIsInstance(NSWorkspaceDecompressOperation, unicode)
        self.assertIsInstance(NSWorkspaceEncryptOperation, unicode)
        self.assertIsInstance(NSWorkspaceDecryptOperation, unicode)
        self.assertIsInstance(NSWorkspaceDestroyOperation, unicode)
        self.assertIsInstance(NSWorkspaceRecycleOperation, unicode)
        self.assertIsInstance(NSWorkspaceDuplicateOperation, unicode)
    @min_os_level('10.6')
    def testConstants10_6(self):
        self.assertIsInstance(NSWorkspaceDesktopImageScalingKey, unicode)
        self.assertIsInstance(NSWorkspaceDesktopImageAllowClippingKey, unicode)
        self.assertIsInstance(NSWorkspaceDesktopImageFillColorKey, unicode)
        self.assertIsInstance(NSWorkspaceApplicationKey, unicode)
        self.assertIsInstance(NSWorkspaceDidHideApplicationNotification, unicode)
        self.assertIsInstance(NSWorkspaceDidUnhideApplicationNotification, unicode)
        self.assertIsInstance(NSWorkspaceDidActivateApplicationNotification, unicode)
        self.assertIsInstance(NSWorkspaceDidDeactivateApplicationNotification, unicode)
        self.assertIsInstance(NSWorkspaceVolumeLocalizedNameKey, unicode)
        self.assertIsInstance(NSWorkspaceVolumeURLKey, unicode)
        self.assertIsInstance(NSWorkspaceVolumeOldLocalizedNameKey, unicode)
        self.assertIsInstance(NSWorkspaceVolumeOldURLKey, unicode)
        self.assertIsInstance(NSWorkspaceDidRenameVolumeNotification, unicode)
        self.assertIsInstance(NSWorkspaceScreensDidSleepNotification, unicode)
        self.assertIsInstance(NSWorkspaceScreensDidWakeNotification, unicode)
        self.assertIsInstance(NSWorkspaceDidChangeFileLabelsNotification, unicode)
        self.assertIsInstance(NSWorkspaceActiveSpaceDidChangeNotification, unicode)
        self.assertIsInstance(NSWorkspaceLaunchConfigurationAppleEvent, unicode)
        self.assertIsInstance(NSWorkspaceLaunchConfigurationArguments, unicode)
        self.assertIsInstance(NSWorkspaceLaunchConfigurationEnvironment, unicode)
        self.assertIsInstance(NSWorkspaceLaunchConfigurationArchitecture, unicode)


    def testMethods(self):
        self.assertResultIsBOOL(NSWorkspace.openFile_)
        self.assertResultIsBOOL(NSWorkspace.openFile_withApplication_)
        self.assertResultIsBOOL(NSWorkspace.openFile_withApplication_andDeactivate_)
        self.assertArgIsBOOL(NSWorkspace.openFile_withApplication_andDeactivate_, 2)
        self.assertResultIsBOOL(NSWorkspace.openTempFile_)
        self.assertResultIsBOOL(NSWorkspace.openFile_fromImage_at_inView_)
        self.assertResultIsBOOL(NSWorkspace.openURL_)
        self.assertResultIsBOOL(NSWorkspace.launchApplication_)
        self.assertResultIsBOOL(NSWorkspace.launchApplication_showIcon_autolaunch_)
        self.assertArgIsBOOL(NSWorkspace.launchApplication_showIcon_autolaunch_, 1)
        self.assertArgIsBOOL(NSWorkspace.launchApplication_showIcon_autolaunch_, 2)
        self.assertResultIsBOOL(NSWorkspace.selectFile_inFileViewerRootedAtPath_)
        self.assertResultIsBOOL(NSWorkspace.fileSystemChanged)
        self.assertResultIsBOOL(NSWorkspace.userDefaultsChanged)
        self.assertResultIsBOOL(NSWorkspace.getInfoForFile_application_type_)
        self.assertArgIsOut(NSWorkspace.getInfoForFile_application_type_, 1)
        self.assertArgIsOut(NSWorkspace.getInfoForFile_application_type_, 2)
        self.assertResultIsBOOL(NSWorkspace.isFilePackageAtPath_)
        self.assertResultIsBOOL(NSWorkspace.setIcon_forFile_options_)
        self.assertResultIsBOOL(NSWorkspace.getFileSystemInfoForPath_isRemovable_isWritable_isUnmountable_description_type_)
        self.assertArgHasType(NSWorkspace.getFileSystemInfoForPath_isRemovable_isWritable_isUnmountable_description_type_, 1, b'o^' + objc._C_NSBOOL)
        self.assertArgHasType(NSWorkspace.getFileSystemInfoForPath_isRemovable_isWritable_isUnmountable_description_type_, 2, b'o^' + objc._C_NSBOOL)
        self.assertArgHasType(NSWorkspace.getFileSystemInfoForPath_isRemovable_isWritable_isUnmountable_description_type_, 3, b'o^' + objc._C_NSBOOL)
        self.assertArgIsOut(NSWorkspace.getFileSystemInfoForPath_isRemovable_isWritable_isUnmountable_description_type_, 4)
        self.assertArgIsOut(NSWorkspace.getFileSystemInfoForPath_isRemovable_isWritable_isUnmountable_description_type_, 5)
        self.assertResultIsBOOL(NSWorkspace.performFileOperation_source_destination_files_tag_)
        self.assertArgIsOut(NSWorkspace.performFileOperation_source_destination_files_tag_, 4)
        self.assertResultIsBOOL(NSWorkspace.unmountAndEjectDeviceAtPath_)
        self.assertResultIsBOOL(NSWorkspace.launchAppWithBundleIdentifier_options_additionalEventParamDescriptor_launchIdentifier_)
        self.assertArgIsOut(NSWorkspace.launchAppWithBundleIdentifier_options_additionalEventParamDescriptor_launchIdentifier_, 3)
        self.assertResultIsBOOL(NSWorkspace.openURLs_withAppBundleIdentifier_options_additionalEventParamDescriptor_launchIdentifiers_)
        self.assertArgIsOut(NSWorkspace.openURLs_withAppBundleIdentifier_options_additionalEventParamDescriptor_launchIdentifiers_, 4)
        self.assertArgIsOut(NSWorkspace.typeOfFile_error_, 1)
        self.assertResultIsBOOL(NSWorkspace.filenameExtension_isValidForType_)
        self.assertResultIsBOOL(NSWorkspace.type_conformsToType_)

        self.assertResultIsBOOL(NSWorkspace.selectFile_inFileViewerRootedAtPath_)
        self.assertArgHasType(NSWorkspace.slideImage_from_to_, 1, NSPoint.__typestr__)
        self.assertArgHasType(NSWorkspace.slideImage_from_to_, 2, NSPoint.__typestr__)

    @min_os_level('10.6')
    def testMethods10_6(self):
        self.assertArgIsOut(NSWorkspace.launchApplicationAtURL_options_configuration_error_, 3)
        self.assertResultIsBOOL(NSWorkspace.showSearchResultsForQueryString_)

        self.assertArgIsBlock(NSWorkspace.recycleURLs_completionHandler_, 1, b'v@@')
        self.assertArgIsBlock(NSWorkspace.duplicateURLs_completionHandler_, 1, b'v@@')

        self.assertResultIsBOOL(NSWorkspace.unmountAndEjectDeviceAtURL_error_)
        self.assertArgIsOut(NSWorkspace.unmountAndEjectDeviceAtURL_error_, 1)

        self.assertResultIsBOOL(NSWorkspace.setDesktopImageURL_forScreen_options_error_)
        self.assertArgIsOut(NSWorkspace.setDesktopImageURL_forScreen_options_error_, 3)


if __name__ == '__main__':
    main( )
