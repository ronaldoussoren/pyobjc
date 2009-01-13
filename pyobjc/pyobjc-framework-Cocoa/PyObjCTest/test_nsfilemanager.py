from PyObjCTools.TestSupport import *

from Foundation import *

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





if __name__ == '__main__':
    main()
