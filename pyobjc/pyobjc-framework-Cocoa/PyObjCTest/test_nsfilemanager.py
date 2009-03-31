from PyObjCTools.TestSupport import *

from Foundation import *

class TestNSFileManagerHelper (NSObject):
    def fileManager_shouldProceedAfterError_(self, a, b): return 1
    def fileManager_willProcessPath_(self, a, b): pass
    def fileManager_shouldCopyItemAtPath_toPath_(self, a, b, c): return 1
    def fileManager_shouldProceedAfterError_copyingItemAtPath_toPath_(self, a, b, c, d): return 1
    def fileManager_shouldMoveItemAtPath_toPath_(self, a, b, c): return 1
    def fileManager_shouldProceedAfterError_movingItemAtPath_toPath_(self, a, b, c, d): return 1
    def fileManager_shouldLinkItemAtPath_toPath_(self, a, b, c): return 1
    def fileManager_shouldProceedAfterError_linkingItemAtPath_toPath_(self, a, b, c, d): return 1
    def fileManager_shouldRemoveItemAtPath_(self, a, b): return 1
    def fileManager_shouldProceedAfterError_removingItemAtPath_(self, a, b, c): return 1



class TestNSFileManager (TestCase):
    def testConstants(self):
        self.assertEquals(NSFoundationVersionWithFileManagerResourceForkSupport, 412)

        self.failUnless( isinstance(NSFileType, unicode) )
        self.failUnless( isinstance(NSFileTypeDirectory, unicode) )
        self.failUnless( isinstance(NSFileTypeRegular, unicode) )
        self.failUnless( isinstance(NSFileTypeSymbolicLink, unicode) )
        self.failUnless( isinstance(NSFileTypeSocket, unicode) )
        self.failUnless( isinstance(NSFileTypeCharacterSpecial, unicode) )
        self.failUnless( isinstance(NSFileTypeBlockSpecial, unicode) )
        self.failUnless( isinstance(NSFileTypeUnknown, unicode) )
        self.failUnless( isinstance(NSFileSize, unicode) )
        self.failUnless( isinstance(NSFileModificationDate, unicode) )
        self.failUnless( isinstance(NSFileReferenceCount, unicode) )
        self.failUnless( isinstance(NSFileDeviceIdentifier, unicode) )
        self.failUnless( isinstance(NSFileOwnerAccountName, unicode) )
        self.failUnless( isinstance(NSFileGroupOwnerAccountName, unicode) )
        self.failUnless( isinstance(NSFilePosixPermissions, unicode) )
        self.failUnless( isinstance(NSFileSystemNumber, unicode) )
        self.failUnless( isinstance(NSFileSystemFileNumber, unicode) )
        self.failUnless( isinstance(NSFileExtensionHidden, unicode) )
        self.failUnless( isinstance(NSFileHFSCreatorCode, unicode) )
        self.failUnless( isinstance(NSFileHFSTypeCode, unicode) )
        self.failUnless( isinstance(NSFileImmutable, unicode) )
        self.failUnless( isinstance(NSFileAppendOnly, unicode) )
        self.failUnless( isinstance(NSFileCreationDate, unicode) )
        self.failUnless( isinstance(NSFileOwnerAccountID, unicode) )
        self.failUnless( isinstance(NSFileGroupOwnerAccountID, unicode) )
        self.failUnless( isinstance(NSFileBusy, unicode) )
        self.failUnless( isinstance(NSFileSystemSize, unicode) )
        self.failUnless( isinstance(NSFileSystemFreeSize, unicode) )
        self.failUnless( isinstance(NSFileSystemNodes, unicode) )
        self.failUnless( isinstance(NSFileSystemFreeNodes, unicode) )

    def testOutput(self):
        obj = NSFileManager.defaultManager()
        m = obj.setAttributes_ofItemAtPath_error_.__metadata__()
        self.failUnless(m['arguments'][4]['type'].startswith('o^'))

        m = obj.createDirectoryAtPath_withIntermediateDirectories_attributes_error_.__metadata__()
        self.failUnless(m['arguments'][3]['type'] == 'Z')
        self.failUnless(m['arguments'][5]['type'].startswith('o^'))

        m = obj.contentsOfDirectoryAtPath_error_.__metadata__()
        self.failUnless(m['arguments'][3]['type'].startswith('o^'))

        m = obj.subpathsOfDirectoryAtPath_error_.__metadata__()
        self.failUnless(m['arguments'][3]['type'].startswith('o^'))

        m = obj.attributesOfItemAtPath_error_.__metadata__()
        self.failUnless(m['arguments'][3]['type'].startswith('o^'))

        m = obj.attributesOfFileSystemForPath_error_.__metadata__()
        self.failUnless(m['arguments'][3]['type'].startswith('o^'))

        m = obj.createSymbolicLinkAtPath_withDestinationPath_error_.__metadata__()
        self.failUnless(m['arguments'][4]['type'].startswith('o^'))

        m = obj.destinationOfSymbolicLinkAtPath_error_.__metadata__()
        self.failUnless(m['arguments'][3]['type'].startswith('o^'))

        m = obj.copyItemAtPath_toPath_error_.__metadata__()
        self.failUnless(m['retval']['type'] == 'Z')
        self.failUnless(m['arguments'][4]['type'].startswith('o^'))

        m = obj.moveItemAtPath_toPath_error_.__metadata__()
        self.failUnless(m['retval']['type'] == 'Z')
        self.failUnless(m['arguments'][4]['type'].startswith('o^'))

        m = obj.linkItemAtPath_toPath_error_.__metadata__()
        self.failUnless(m['retval']['type'] == 'Z')
        self.failUnless(m['arguments'][4]['type'].startswith('o^'))

        m = obj.removeItemAtPath_error_.__metadata__()
        self.failUnless(m['retval']['type'] == 'Z')
        self.failUnless(m['arguments'][3]['type'].startswith('o^'))

    def testProtocols(self):
        class FileManagerTest1 (NSObject):
            def fileManager_shouldCopyItemAtPath_toPath_(self, fm, src, dst):
                return True

            def fileManager_shouldProceedAfterError_copyingItemAtPath_toPath_(self, fm, error, src, dst):
                return True

            def fileManager_shouldMoveItemAtPath_toPath_(self, fm,  src, dst):
                return True

            def fileManager_shouldProceedAfterError_movingItemAtPath_toPath_(self, fm,  error, src, dst):
                return True

            def fileManager_shouldLinkItemAtPath_toPath_(self, fm, src, dst):
                return True

            def fileManager_shouldProceedAfterError_linkingItemAtPath_toPath_(self, fm,  error, src, dst):
                return True

            def fileManager_shouldRemoveItemAtPath_(self, fm, src):
                return True

            def fileManager_shouldProceedAfterError_removingItemAtPath_(self, fm,  error, src):
                return True

        obj = FileManagerTest1.alloc().init()
        m = obj.fileManager_shouldCopyItemAtPath_toPath_.__metadata__()
        self.failUnless(m['retval']['type'] == 'Z')

        m = obj.fileManager_shouldProceedAfterError_copyingItemAtPath_toPath_.__metadata__()
        self.failUnless(m['retval']['type'] == 'Z')

        m = obj.fileManager_shouldMoveItemAtPath_toPath_.__metadata__()
        self.failUnless(m['retval']['type'] == 'Z')

        m = obj.fileManager_shouldProceedAfterError_movingItemAtPath_toPath_.__metadata__()
        self.failUnless(m['retval']['type'] == 'Z')

        m = obj.fileManager_shouldLinkItemAtPath_toPath_.__metadata__()
        self.failUnless(m['retval']['type'] == 'Z')

        m = obj.fileManager_shouldProceedAfterError_linkingItemAtPath_toPath_.__metadata__()
        self.failUnless(m['retval']['type'] == 'Z')

        m = obj.fileManager_shouldRemoveItemAtPath_.__metadata__()
        self.failUnless(m['retval']['type'] == 'Z')

        m = obj.fileManager_shouldProceedAfterError_removingItemAtPath_.__metadata__()
        self.failUnless(m['retval']['type'] == 'Z')


    @min_os_level('10.5')
    def testMethods10_5(self):
        self.failUnlessResultIsBOOL(NSFileManager.setAttributes_ofItemAtPath_error_)
        self.failUnlessArgIsOut(NSFileManager.setAttributes_ofItemAtPath_error_, 2)

        self.failUnlessResultIsBOOL(NSFileManager.createDirectoryAtPath_withIntermediateDirectories_attributes_error_)
        self.failUnlessArgIsBOOL(NSFileManager.createDirectoryAtPath_withIntermediateDirectories_attributes_error_, 1)
        self.failUnlessArgIsOut(NSFileManager.createDirectoryAtPath_withIntermediateDirectories_attributes_error_, 3)

        self.failUnlessArgIsOut(NSFileManager.contentsOfDirectoryAtPath_error_, 1)
        self.failUnlessArgIsOut(NSFileManager.subpathsOfDirectoryAtPath_error_, 1)
        self.failUnlessArgIsOut(NSFileManager.attributesOfItemAtPath_error_, 1)
        self.failUnlessArgIsOut(NSFileManager.attributesOfFileSystemForPath_error_, 1)

        self.failUnlessResultIsBOOL(NSFileManager.createSymbolicLinkAtPath_withDestinationPath_error_)
        self.failUnlessArgIsOut(NSFileManager.createSymbolicLinkAtPath_withDestinationPath_error_, 2)

        self.failUnlessArgIsOut(NSFileManager.destinationOfSymbolicLinkAtPath_error_, 1)

        self.failUnlessResultIsBOOL(NSFileManager.copyItemAtPath_toPath_error_)
        self.failUnlessArgIsOut(NSFileManager.copyItemAtPath_toPath_error_, 2)
        self.failUnlessResultIsBOOL(NSFileManager.moveItemAtPath_toPath_error_)
        self.failUnlessArgIsOut(NSFileManager.moveItemAtPath_toPath_error_, 2)
        self.failUnlessResultIsBOOL(NSFileManager.linkItemAtPath_toPath_error_)
        self.failUnlessArgIsOut(NSFileManager.linkItemAtPath_toPath_error_, 2)
        self.failUnlessResultIsBOOL(NSFileManager.removeItemAtPath_error_)
        self.failUnlessArgIsOut(NSFileManager.removeItemAtPath_error_, 1)

    def testMethods(self):
        self.failUnlessArgIsBOOL(NSFileManager.fileAttributesAtPath_traverseLink_, 1)
        self.failUnlessResultIsBOOL(NSFileManager.changeFileAttributes_atPath_)
        self.failUnlessResultIsBOOL(NSFileManager.createSymbolicLinkAtPath_pathContent_)
        self.failUnlessResultIsBOOL(NSFileManager.createDirectoryAtPath_attributes_)
        self.failUnlessResultIsBOOL(NSFileManager.linkPath_toPath_handler_)
        self.failUnlessResultIsBOOL(NSFileManager.copyPath_toPath_handler_)
        self.failUnlessResultIsBOOL(NSFileManager.movePath_toPath_handler_)
        self.failUnlessResultIsBOOL(NSFileManager.removeFileAtPath_handler_)
        self.failUnlessResultIsBOOL(NSFileManager.changeCurrentDirectoryPath_)
        self.failUnlessResultIsBOOL(NSFileManager.fileExistsAtPath_)
        self.failUnlessResultIsBOOL(NSFileManager.fileExistsAtPath_isDirectory_)
        self.failUnlessArgHasType(NSFileManager.fileExistsAtPath_isDirectory_, 1, 'o^' + objc._C_NSBOOL)
        self.failUnlessResultIsBOOL(NSFileManager.isReadableFileAtPath_)
        self.failUnlessResultIsBOOL(NSFileManager.isWritableFileAtPath_)
        self.failUnlessResultIsBOOL(NSFileManager.isExecutableFileAtPath_)
        self.failUnlessResultIsBOOL(NSFileManager.isDeletableFileAtPath_)
        self.failUnlessResultIsBOOL(NSFileManager.contentsEqualAtPath_andPath_)
        self.failUnlessResultIsBOOL(NSFileManager.createFileAtPath_contents_attributes_)
        self.failUnlessResultHasType(NSFileManager.fileSystemRepresentationWithPath_, '^' + objc._C_CHAR_AS_TEXT)
        self.failUnlessResultIsNullTerminated(NSFileManager.fileSystemRepresentationWithPath_)
        self.failUnlessArgHasType(NSFileManager.stringWithFileSystemRepresentation_length_, 0, 'n^' + objc._C_CHAR_AS_TEXT)
        self.failUnlessArgSizeInArg(NSFileManager.stringWithFileSystemRepresentation_length_, 0, 1)

        self.failUnlessResultIsBOOL(NSDictionary.fileIsImmutable)
        self.failUnlessResultIsBOOL(NSDictionary.fileIsAppendOnly)
        self.failUnlessResultIsBOOL(NSDictionary.fileExtensionHidden)

    def testProtocols(self):
        self.failUnlessResultIsBOOL(TestNSFileManagerHelper.fileManager_shouldProceedAfterError_)
        self.failUnlessResultIsBOOL(TestNSFileManagerHelper.fileManager_shouldCopyItemAtPath_toPath_)
        self.failUnlessResultIsBOOL(TestNSFileManagerHelper.fileManager_shouldProceedAfterError_copyingItemAtPath_toPath_)
        self.failUnlessResultIsBOOL(TestNSFileManagerHelper.fileManager_shouldMoveItemAtPath_toPath_)
        self.failUnlessResultIsBOOL(TestNSFileManagerHelper.fileManager_shouldProceedAfterError_movingItemAtPath_toPath_)
        self.failUnlessResultIsBOOL(TestNSFileManagerHelper.fileManager_shouldLinkItemAtPath_toPath_)
        self.failUnlessResultIsBOOL(TestNSFileManagerHelper.fileManager_shouldProceedAfterError_linkingItemAtPath_toPath_)
        self.failUnlessResultIsBOOL(TestNSFileManagerHelper.fileManager_shouldRemoveItemAtPath_)
        self.failUnlessResultIsBOOL(TestNSFileManagerHelper.fileManager_shouldProceedAfterError_removingItemAtPath_)

if __name__ == '__main__':
    main()
