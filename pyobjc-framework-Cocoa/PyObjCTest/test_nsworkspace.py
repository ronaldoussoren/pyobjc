from PyObjCTools.TestSupport import *
import objc
import os

from AppKit import *


class TestNSWorkspace(TestCase):
    def testInfoForFile(self):
        ws = NSWorkspace.sharedWorkspace()

        # A method with 2 output parameters, this means the result
        # is a tuple with 3 elements (return value, param1, param2)
        res = ws.getInfoForFile_application_type_(u'/', None, None)
        self.assert_(isinstance(res, tuple))
        self.assert_(len(res) == 3)
        self.assert_(res[0] == 1)
        self.assert_(res[1] == u'/System/Library/CoreServices/Finder.app')
        self.assert_(res[2] == u'')

    def testConstants(self):
        self.assertEquals(NSWorkspaceLaunchAndPrint, 2)
        self.assertEquals(NSWorkspaceLaunchInhibitingBackgroundOnly, 0x00000080)
        self.assertEquals(NSWorkspaceLaunchWithoutAddingToRecents, 0x00000100)
        self.assertEquals(NSWorkspaceLaunchWithoutActivation, 0x00000200)
        self.assertEquals(NSWorkspaceLaunchAsync, 0x00010000)
        self.assertEquals(NSWorkspaceLaunchAllowingClassicStartup, 0x00020000)
        self.assertEquals(NSWorkspaceLaunchPreferringClassic, 0x00040000)
        self.assertEquals(NSWorkspaceLaunchNewInstance, 0x00080000)
        self.assertEquals(NSWorkspaceLaunchAndHide, 0x00100000)
        self.assertEquals(NSWorkspaceLaunchAndHideOthers, 0x00200000)
        self.assertEquals(NSWorkspaceLaunchDefault, (
                NSWorkspaceLaunchAsync | NSWorkspaceLaunchAllowingClassicStartup))

        self.assertEquals(NSExcludeQuickDrawElementsIconCreationOption, 1 << 1)
        self.assertEquals(NSExclude10_4ElementsIconCreationOption, 1 << 2)

        self.failUnless(isinstance(NSWorkspaceDidLaunchApplicationNotification, unicode))
        self.failUnless(isinstance(NSWorkspaceDidMountNotification, unicode))
        self.failUnless(isinstance(NSWorkspaceDidPerformFileOperationNotification, unicode))
        self.failUnless(isinstance(NSWorkspaceDidTerminateApplicationNotification, unicode))
        self.failUnless(isinstance(NSWorkspaceDidUnmountNotification, unicode))
        self.failUnless(isinstance(NSWorkspaceWillLaunchApplicationNotification, unicode))
        self.failUnless(isinstance(NSWorkspaceWillPowerOffNotification, unicode))
        self.failUnless(isinstance(NSWorkspaceWillUnmountNotification, unicode))
        self.failUnless(isinstance(NSWorkspaceWillSleepNotification, unicode))
        self.failUnless(isinstance(NSWorkspaceDidWakeNotification, unicode))
        self.failUnless(isinstance(NSWorkspaceSessionDidBecomeActiveNotification, unicode))
        self.failUnless(isinstance(NSWorkspaceSessionDidResignActiveNotification, unicode))
        self.failUnless(isinstance(NSPlainFileType, unicode))
        self.failUnless(isinstance(NSDirectoryFileType, unicode))
        self.failUnless(isinstance(NSApplicationFileType, unicode))
        self.failUnless(isinstance(NSFilesystemFileType, unicode))
        self.failUnless(isinstance(NSShellCommandFileType, unicode))
        self.failUnless(isinstance(NSWorkspaceMoveOperation, unicode))
        self.failUnless(isinstance(NSWorkspaceCopyOperation, unicode))
        self.failUnless(isinstance(NSWorkspaceLinkOperation, unicode))
        self.failUnless(isinstance(NSWorkspaceCompressOperation, unicode))
        self.failUnless(isinstance(NSWorkspaceDecompressOperation, unicode))
        self.failUnless(isinstance(NSWorkspaceEncryptOperation, unicode))
        self.failUnless(isinstance(NSWorkspaceDecryptOperation, unicode))
        self.failUnless(isinstance(NSWorkspaceDestroyOperation, unicode))
        self.failUnless(isinstance(NSWorkspaceRecycleOperation, unicode))
        self.failUnless(isinstance(NSWorkspaceDuplicateOperation, unicode))

    def testMethods(self):
        self.failUnlessResultIsBOOL(NSWorkspace.openFile_)
        self.failUnlessResultIsBOOL(NSWorkspace.openFile_withApplication_)
        self.failUnlessResultIsBOOL(NSWorkspace.openFile_withApplication_andDeactivate_)
        self.failUnlessArgIsBOOL(NSWorkspace.openFile_withApplication_andDeactivate_, 2)
        self.failUnlessResultIsBOOL(NSWorkspace.openTempFile_)
        self.failUnlessResultIsBOOL(NSWorkspace.openFile_fromImage_at_inView_)
        self.failUnlessResultIsBOOL(NSWorkspace.openURL_)
        self.failUnlessResultIsBOOL(NSWorkspace.launchApplication_)
        self.failUnlessResultIsBOOL(NSWorkspace.launchApplication_showIcon_autolaunch_)
        self.failUnlessArgIsBOOL(NSWorkspace.launchApplication_showIcon_autolaunch_, 1)
        self.failUnlessArgIsBOOL(NSWorkspace.launchApplication_showIcon_autolaunch_, 2)
        self.failUnlessResultIsBOOL(NSWorkspace.selectFile_inFileViewerRootedAtPath_)
        self.failUnlessResultIsBOOL(NSWorkspace.fileSystemChanged)
        self.failUnlessResultIsBOOL(NSWorkspace.userDefaultsChanged)
        self.failUnlessResultIsBOOL(NSWorkspace.getInfoForFile_application_type_)
        self.failUnlessArgIsOut(NSWorkspace.getInfoForFile_application_type_, 1)
        self.failUnlessArgIsOut(NSWorkspace.getInfoForFile_application_type_, 2)
        self.failUnlessResultIsBOOL(NSWorkspace.isFilePackageAtPath_)
        self.failUnlessResultIsBOOL(NSWorkspace.setIcon_forFile_options_)
        self.failUnlessResultIsBOOL(NSWorkspace.getFileSystemInfoForPath_isRemovable_isWritable_isUnmountable_description_type_)
        self.failUnlessArgHasType(NSWorkspace.getFileSystemInfoForPath_isRemovable_isWritable_isUnmountable_description_type_, 1, 'o^' + objc._C_NSBOOL)
        self.failUnlessArgHasType(NSWorkspace.getFileSystemInfoForPath_isRemovable_isWritable_isUnmountable_description_type_, 2, 'o^' + objc._C_NSBOOL)
        self.failUnlessArgHasType(NSWorkspace.getFileSystemInfoForPath_isRemovable_isWritable_isUnmountable_description_type_, 3, 'o^' + objc._C_NSBOOL)
        self.failUnlessArgIsOut(NSWorkspace.getFileSystemInfoForPath_isRemovable_isWritable_isUnmountable_description_type_, 4)
        self.failUnlessArgIsOut(NSWorkspace.getFileSystemInfoForPath_isRemovable_isWritable_isUnmountable_description_type_, 5)
        self.failUnlessResultIsBOOL(NSWorkspace.performFileOperation_source_destination_files_tag_)
        self.failUnlessArgIsOut(NSWorkspace.performFileOperation_source_destination_files_tag_, 4)
        self.failUnlessResultIsBOOL(NSWorkspace.unmountAndEjectDeviceAtPath_)
        self.failUnlessResultIsBOOL(NSWorkspace.launchAppWithBundleIdentifier_options_additionalEventParamDescriptor_launchIdentifier_)
        self.failUnlessArgIsOut(NSWorkspace.launchAppWithBundleIdentifier_options_additionalEventParamDescriptor_launchIdentifier_, 3)
        self.failUnlessResultIsBOOL(NSWorkspace.openURLs_withAppBundleIdentifier_options_additionalEventParamDescriptor_launchIdentifiers_)
        self.failUnlessArgIsOut(NSWorkspace.openURLs_withAppBundleIdentifier_options_additionalEventParamDescriptor_launchIdentifiers_, 4)
        self.failUnlessArgIsOut(NSWorkspace.typeOfFile_error_, 1)
        self.failUnlessResultIsBOOL(NSWorkspace.filenameExtension_isValidForType_)
        self.failUnlessResultIsBOOL(NSWorkspace.type_conformsToType_)


if __name__ == '__main__':
    main( )
