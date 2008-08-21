import unittest
import objc
import os

from objc import YES, NO
from AppKit import NSWorkspace


class TestNSWorkspace(unittest.TestCase):
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

    def testGetFileSystemInfo(self):
        self.fail('- (BOOL)getFileSystemInfoForPath:(NSString *)fullPath isRemovable:(BOOL *)removableFlag isWritable:(BOOL *)writableFlag isUnmountable:(BOOL *)unmountableFlag description:(NSString **)description type:(NSString **)fileSystemType;')

    def testPerformOperation(self):
        self.fail('- (BOOL)performFileOperation:(NSString *)operation source:(NSString *)source destination:(NSString *)destination files:(NSArray *)files tag:(NSInteger *)tag;')

    def testLaunchApp(self):
        self.fail('- (BOOL)launchAppWithBundleIdentifier:(NSString *)bundleIdentifier options:(NSWorkspaceLaunchOptions)options additionalEventParamDescriptor:(NSAppleEventDescriptor *)descriptor launchIdentifier:(NSNumber **)identifier;')

    def testOpenURLs(self):
        self.fail('- (BOOL)openURLs:(NSArray *)urls withAppBundleIdentifier:(NSString *)bundleIdentifier options:(NSWorkspaceLaunchOptions)options additionalEventParamDescriptor:(NSAppleEventDescriptor *)descriptor launchIdentifiers:(NSArray **)identifiers;')

    def testTypeOfFile(self):
        self.fail('- (NSString *)typeOfFile:(NSString *)absoluteFilePath error:(NSError **)outError;')


    def testConstants(self):
        self.assertEquals(NSWorkspaceLaunchAndPrint, 0x00000002)
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




if __name__ == '__main__':
    unittest.main( )
