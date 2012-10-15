from PyObjCTools.TestSupport import *

from Foundation import *

try:
    unicode
except NameError:
    unicode = str

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

    def fileManager_shouldCopyItemAtURL_toURL_(self, a, b, c): return 1
    def fileManager_shouldProceedAfterError_copyingItemAtURL_toURL_(self, a, b, c, d): return 1
    def fileManager_shouldMoveItemAtURL_toURL_(self, a, b, c): return 1
    def fileManager_shouldProceedAfterError_movingItemAtURL_toURL_(self, a, b, c, d): return 1
    def fileManager_shouldLinkItemAtURL_toURL_(self, a, b, c): return 1
    def fileManager_shouldProceedAfterError_linkingItemAtURL_toURL_(self, a, b, c, d): return 1
    def fileManager_shouldRemoveItemAtURL_(self, a, b): return 1
    def fileManager_shouldProceedAfterError_removingItemAtURL_(self, a, b, c): return 1



class TestNSFileManager (TestCase):
    def testConstants(self):
        self.assertEqual(NSFoundationVersionWithFileManagerResourceForkSupport, 412)

        self.assertIsInstance(NSFileType, unicode)
        self.assertIsInstance(NSFileTypeDirectory, unicode)
        self.assertIsInstance(NSFileTypeRegular, unicode)
        self.assertIsInstance(NSFileTypeSymbolicLink, unicode)
        self.assertIsInstance(NSFileTypeSocket, unicode)
        self.assertIsInstance(NSFileTypeCharacterSpecial, unicode)
        self.assertIsInstance(NSFileTypeBlockSpecial, unicode)
        self.assertIsInstance(NSFileTypeUnknown, unicode)
        self.assertIsInstance(NSFileSize, unicode)
        self.assertIsInstance(NSFileModificationDate, unicode)
        self.assertIsInstance(NSFileReferenceCount, unicode)
        self.assertIsInstance(NSFileDeviceIdentifier, unicode)
        self.assertIsInstance(NSFileOwnerAccountName, unicode)
        self.assertIsInstance(NSFileGroupOwnerAccountName, unicode)
        self.assertIsInstance(NSFilePosixPermissions, unicode)
        self.assertIsInstance(NSFileSystemNumber, unicode)
        self.assertIsInstance(NSFileSystemFileNumber, unicode)
        self.assertIsInstance(NSFileExtensionHidden, unicode)
        self.assertIsInstance(NSFileHFSCreatorCode, unicode)
        self.assertIsInstance(NSFileHFSTypeCode, unicode)
        self.assertIsInstance(NSFileImmutable, unicode)
        self.assertIsInstance(NSFileAppendOnly, unicode)
        self.assertIsInstance(NSFileCreationDate, unicode)
        self.assertIsInstance(NSFileOwnerAccountID, unicode)
        self.assertIsInstance(NSFileGroupOwnerAccountID, unicode)
        self.assertIsInstance(NSFileBusy, unicode)
        self.assertIsInstance(NSFileSystemSize, unicode)
        self.assertIsInstance(NSFileSystemFreeSize, unicode)
        self.assertIsInstance(NSFileSystemNodes, unicode)
        self.assertIsInstance(NSFileSystemFreeNodes, unicode)

    @min_os_level('10.6')
    def testConstants10_6(self):
        self.assertEqual(NSVolumeEnumerationSkipHiddenVolumes, 1<<1)
        self.assertEqual(NSVolumeEnumerationProduceFileReferenceURLs, 1<<2)

        self.assertEqual(NSDirectoryEnumerationSkipsSubdirectoryDescendants, 1<<0)
        self.assertEqual(NSDirectoryEnumerationSkipsPackageDescendants, 1<<1)
        self.assertEqual(NSDirectoryEnumerationSkipsHiddenFiles, 1<<2)

        self.assertEqual(NSFileManagerItemReplacementUsingNewMetadataOnly, 1<<0)
        self.assertEqual(NSFileManagerItemReplacementWithoutDeletingBackupItem, 1<<1)

    @min_os_level('10.8')
    def testConstants10_8(self):
        self.assertIsInstance(NSUbiquityIdentityDidChangeNotification, unicode)

    @min_os_level('10.6')
    def testMethods10_6(self):
        self.assertArgIsOut(NSFileManager.contentsOfDirectoryAtURL_includingPropertiesForKeys_options_error_, 3)
        self.assertArgIsBOOL(NSFileManager.URLForDirectory_inDomain_appropriateForURL_create_error_, 3)
        self.assertArgIsOut(NSFileManager.URLForDirectory_inDomain_appropriateForURL_create_error_, 4)

        self.assertResultIsBOOL(NSFileManager.copyItemAtURL_toURL_error_)
        self.assertArgIsOut(NSFileManager.copyItemAtURL_toURL_error_, 2)
        self.assertResultIsBOOL(NSFileManager.moveItemAtURL_toURL_error_)
        self.assertArgIsOut(NSFileManager.moveItemAtURL_toURL_error_, 2)
        self.assertResultIsBOOL(NSFileManager.linkItemAtURL_toURL_error_)
        self.assertArgIsOut(NSFileManager.linkItemAtURL_toURL_error_, 2)
        self.assertResultIsBOOL(NSFileManager.removeItemAtURL_error_)
        self.assertArgIsOut(NSFileManager.removeItemAtURL_error_, 1)

        self.assertArgIsBlock(NSFileManager.enumeratorAtURL_includingPropertiesForKeys_options_errorHandler_, 3, objc._C_NSBOOL + b'@@')

        self.assertResultIsBOOL(NSFileManager.replaceItemAtURL_withItemAtURL_backupItemName_options_resultingItemURL_error_)
        self.assertArgIsOut(NSFileManager.replaceItemAtURL_withItemAtURL_backupItemName_options_resultingItemURL_error_, 4)
        self.assertArgIsOut(NSFileManager.replaceItemAtURL_withItemAtURL_backupItemName_options_resultingItemURL_error_, 5)


    @min_os_level('10.7')
    def testMethods10_7(self):
        self.assertResultIsBOOL(NSFileManager.createDirectoryAtURL_withIntermediateDirectories_attributes_error_)
        self.assertArgIsBOOL(NSFileManager.createDirectoryAtURL_withIntermediateDirectories_attributes_error_, 1)
        self.assertArgIsOut(NSFileManager.createDirectoryAtURL_withIntermediateDirectories_attributes_error_, 3)

        self.assertResultIsBOOL(NSFileManager.createSymbolicLinkAtURL_withDestinationURL_error_)
        self.assertArgIsOut(NSFileManager.createSymbolicLinkAtURL_withDestinationURL_error_, 2)

        self.assertResultIsBOOL(NSFileManager.setUbiquitous_itemAtURL_destinationURL_error_)
        self.assertArgIsBOOL(NSFileManager.setUbiquitous_itemAtURL_destinationURL_error_, 0)
        self.assertArgIsOut(NSFileManager.setUbiquitous_itemAtURL_destinationURL_error_, 3)
        self.assertResultIsBOOL(NSFileManager.isUbiquitousItemAtURL_)

        self.assertResultIsBOOL(NSFileManager.startDownloadingUbiquitousItemAtURL_error_)
        self.assertArgIsOut(NSFileManager.startDownloadingUbiquitousItemAtURL_error_, 1)

        self.assertResultIsBOOL(NSFileManager.evictUbiquitousItemAtURL_error_)
        self.assertArgIsOut(NSFileManager.evictUbiquitousItemAtURL_error_, 1)

        self.assertArgIsOut(NSFileManager.URLForPublishingUbiquitousItemAtURL_expirationDate_error_, 1)
        self.assertArgIsOut(NSFileManager.URLForPublishingUbiquitousItemAtURL_expirationDate_error_, 2)

    @min_os_level('10.8')
    def testMethods10_8(self):
        self.assertResultIsBOOL(NSFileManager.trashItemAtURL_resultingItemURL_error_)
        self.assertArgIsOut(NSFileManager.trashItemAtURL_resultingItemURL_error_, 1)
        self.assertArgIsOut(NSFileManager.trashItemAtURL_resultingItemURL_error_, 2)

    def testOutput(self):
        obj = NSFileManager.defaultManager()
        m = obj.setAttributes_ofItemAtPath_error_.__metadata__()
        self.assertTrue(m['arguments'][4]['type'].startswith(b'o^'))

        m = obj.createDirectoryAtPath_withIntermediateDirectories_attributes_error_.__metadata__()
        self.assertEqual(m['arguments'][3]['type'] , b'Z')
        self.assertTrue(m['arguments'][5]['type'].startswith(b'o^'))

        m = obj.contentsOfDirectoryAtPath_error_.__metadata__()
        self.assertTrue(m['arguments'][3]['type'].startswith(b'o^'))

        m = obj.subpathsOfDirectoryAtPath_error_.__metadata__()
        self.assertTrue(m['arguments'][3]['type'].startswith(b'o^'))

        m = obj.attributesOfItemAtPath_error_.__metadata__()
        self.assertTrue(m['arguments'][3]['type'].startswith(b'o^'))

        m = obj.attributesOfFileSystemForPath_error_.__metadata__()
        self.assertTrue(m['arguments'][3]['type'].startswith(b'o^'))

        m = obj.createSymbolicLinkAtPath_withDestinationPath_error_.__metadata__()
        self.assertTrue(m['arguments'][4]['type'].startswith(b'o^'))

        m = obj.destinationOfSymbolicLinkAtPath_error_.__metadata__()
        self.assertTrue(m['arguments'][3]['type'].startswith(b'o^'))

        m = obj.copyItemAtPath_toPath_error_.__metadata__()
        self.assertEqual(m['retval']['type'] , b'Z')
        self.assertTrue(m['arguments'][4]['type'].startswith(b'o^'))

        m = obj.moveItemAtPath_toPath_error_.__metadata__()
        self.assertEqual(m['retval']['type'] , b'Z')
        self.assertTrue(m['arguments'][4]['type'].startswith(b'o^'))

        m = obj.linkItemAtPath_toPath_error_.__metadata__()
        self.assertEqual(m['retval']['type'] , b'Z')
        self.assertTrue(m['arguments'][4]['type'].startswith(b'o^'))

        m = obj.removeItemAtPath_error_.__metadata__()
        self.assertEqual(m['retval']['type'] , b'Z')
        self.assertTrue(m['arguments'][3]['type'].startswith(b'o^'))

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
        self.assertEqual(m['retval']['type'] , 'Z')
        m = obj.fileManager_shouldProceedAfterError_copyingItemAtPath_toPath_.__metadata__()
        self.assertEqual(m['retval']['type'] , 'Z')
        m = obj.fileManager_shouldMoveItemAtPath_toPath_.__metadata__()
        self.assertEqual(m['retval']['type'] , 'Z')
        m = obj.fileManager_shouldProceedAfterError_movingItemAtPath_toPath_.__metadata__()
        self.assertEqual(m['retval']['type'] , 'Z')
        m = obj.fileManager_shouldLinkItemAtPath_toPath_.__metadata__()
        self.assertEqual(m['retval']['type'] , 'Z')
        m = obj.fileManager_shouldProceedAfterError_linkingItemAtPath_toPath_.__metadata__()
        self.assertEqual(m['retval']['type'] , 'Z')
        m = obj.fileManager_shouldRemoveItemAtPath_.__metadata__()
        self.assertEqual(m['retval']['type'] , 'Z')
        m = obj.fileManager_shouldProceedAfterError_removingItemAtPath_.__metadata__()
        self.assertEqual(m['retval']['type'] , 'Z')
    @min_os_level('10.5')
    def testMethods10_5(self):
        self.assertResultIsBOOL(NSFileManager.setAttributes_ofItemAtPath_error_)
        self.assertArgIsOut(NSFileManager.setAttributes_ofItemAtPath_error_, 2)

        self.assertResultIsBOOL(NSFileManager.createDirectoryAtPath_withIntermediateDirectories_attributes_error_)
        self.assertArgIsBOOL(NSFileManager.createDirectoryAtPath_withIntermediateDirectories_attributes_error_, 1)
        self.assertArgIsOut(NSFileManager.createDirectoryAtPath_withIntermediateDirectories_attributes_error_, 3)

        self.assertArgIsOut(NSFileManager.contentsOfDirectoryAtPath_error_, 1)
        self.assertArgIsOut(NSFileManager.subpathsOfDirectoryAtPath_error_, 1)
        self.assertArgIsOut(NSFileManager.attributesOfItemAtPath_error_, 1)
        self.assertArgIsOut(NSFileManager.attributesOfFileSystemForPath_error_, 1)

        self.assertResultIsBOOL(NSFileManager.createSymbolicLinkAtPath_withDestinationPath_error_)
        self.assertArgIsOut(NSFileManager.createSymbolicLinkAtPath_withDestinationPath_error_, 2)

        self.assertArgIsOut(NSFileManager.destinationOfSymbolicLinkAtPath_error_, 1)

        self.assertResultIsBOOL(NSFileManager.copyItemAtPath_toPath_error_)
        self.assertArgIsOut(NSFileManager.copyItemAtPath_toPath_error_, 2)
        self.assertResultIsBOOL(NSFileManager.moveItemAtPath_toPath_error_)
        self.assertArgIsOut(NSFileManager.moveItemAtPath_toPath_error_, 2)
        self.assertResultIsBOOL(NSFileManager.linkItemAtPath_toPath_error_)
        self.assertArgIsOut(NSFileManager.linkItemAtPath_toPath_error_, 2)
        self.assertResultIsBOOL(NSFileManager.removeItemAtPath_error_)
        self.assertArgIsOut(NSFileManager.removeItemAtPath_error_, 1)


    def testMethods(self):
        self.assertArgIsBOOL(NSFileManager.fileAttributesAtPath_traverseLink_, 1)
        self.assertResultIsBOOL(NSFileManager.changeFileAttributes_atPath_)
        self.assertResultIsBOOL(NSFileManager.createSymbolicLinkAtPath_pathContent_)
        self.assertResultIsBOOL(NSFileManager.createDirectoryAtPath_attributes_)
        self.assertResultIsBOOL(NSFileManager.linkPath_toPath_handler_)
        self.assertResultIsBOOL(NSFileManager.copyPath_toPath_handler_)
        self.assertResultIsBOOL(NSFileManager.movePath_toPath_handler_)
        self.assertResultIsBOOL(NSFileManager.removeFileAtPath_handler_)
        self.assertResultIsBOOL(NSFileManager.changeCurrentDirectoryPath_)
        self.assertResultIsBOOL(NSFileManager.fileExistsAtPath_)
        self.assertResultIsBOOL(NSFileManager.fileExistsAtPath_isDirectory_)
        self.assertArgHasType(NSFileManager.fileExistsAtPath_isDirectory_, 1, b'o^' + objc._C_NSBOOL)
        self.assertResultIsBOOL(NSFileManager.isReadableFileAtPath_)
        self.assertResultIsBOOL(NSFileManager.isWritableFileAtPath_)
        self.assertResultIsBOOL(NSFileManager.isExecutableFileAtPath_)
        self.assertResultIsBOOL(NSFileManager.isDeletableFileAtPath_)
        self.assertResultIsBOOL(NSFileManager.contentsEqualAtPath_andPath_)
        self.assertResultIsBOOL(NSFileManager.createFileAtPath_contents_attributes_)
        self.assertResultHasType(NSFileManager.fileSystemRepresentationWithPath_, b'^' + objc._C_CHAR_AS_TEXT)
        self.assertResultIsNullTerminated(NSFileManager.fileSystemRepresentationWithPath_)
        self.assertArgHasType(NSFileManager.stringWithFileSystemRepresentation_length_, 0, b'n^' + objc._C_CHAR_AS_TEXT)
        self.assertArgSizeInArg(NSFileManager.stringWithFileSystemRepresentation_length_, 0, 1)

        self.assertResultIsBOOL(NSDictionary.fileIsImmutable)
        self.assertResultIsBOOL(NSDictionary.fileIsAppendOnly)
        self.assertResultIsBOOL(NSDictionary.fileExtensionHidden)

    def testProtocols(self):
        self.assertResultIsBOOL(TestNSFileManagerHelper.fileManager_shouldProceedAfterError_)
        self.assertResultIsBOOL(TestNSFileManagerHelper.fileManager_shouldCopyItemAtPath_toPath_)
        self.assertResultIsBOOL(TestNSFileManagerHelper.fileManager_shouldProceedAfterError_copyingItemAtPath_toPath_)
        self.assertResultIsBOOL(TestNSFileManagerHelper.fileManager_shouldMoveItemAtPath_toPath_)
        self.assertResultIsBOOL(TestNSFileManagerHelper.fileManager_shouldProceedAfterError_movingItemAtPath_toPath_)
        self.assertResultIsBOOL(TestNSFileManagerHelper.fileManager_shouldLinkItemAtPath_toPath_)
        self.assertResultIsBOOL(TestNSFileManagerHelper.fileManager_shouldProceedAfterError_linkingItemAtPath_toPath_)
        self.assertResultIsBOOL(TestNSFileManagerHelper.fileManager_shouldRemoveItemAtPath_)
        self.assertResultIsBOOL(TestNSFileManagerHelper.fileManager_shouldProceedAfterError_removingItemAtPath_)

    @min_os_level('10.6')
    def testProtocols10_6(self):

        self.assertResultIsBOOL(TestNSFileManagerHelper.fileManager_shouldCopyItemAtURL_toURL_)
        self.assertResultIsBOOL(TestNSFileManagerHelper.fileManager_shouldProceedAfterError_copyingItemAtURL_toURL_)
        self.assertResultIsBOOL(TestNSFileManagerHelper.fileManager_shouldMoveItemAtURL_toURL_)
        self.assertResultIsBOOL(TestNSFileManagerHelper.fileManager_shouldProceedAfterError_movingItemAtURL_toURL_)
        self.assertResultIsBOOL(TestNSFileManagerHelper.fileManager_shouldLinkItemAtURL_toURL_)
        self.assertResultIsBOOL(TestNSFileManagerHelper.fileManager_shouldProceedAfterError_linkingItemAtURL_toURL_)
        self.assertResultIsBOOL(TestNSFileManagerHelper.fileManager_shouldRemoveItemAtURL_)
        self.assertResultIsBOOL(TestNSFileManagerHelper.fileManager_shouldProceedAfterError_removingItemAtURL_)

if __name__ == '__main__':
    main()
