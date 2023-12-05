import Foundation
from PyObjCTools.TestSupport import TestCase, min_os_level, min_sdk_level
import objc


class TestNSFileManagerHelper(Foundation.NSObject):
    def fileManager_shouldProceedAfterError_(self, a, b):
        return 1

    def fileManager_willProcessPath_(self, a, b):
        pass

    def fileManager_shouldCopyItemAtPath_toPath_(self, a, b, c):
        return 1

    def fileManager_shouldProceedAfterError_copyingItemAtPath_toPath_(self, a, b, c, d):
        return 1

    def fileManager_shouldMoveItemAtPath_toPath_(self, a, b, c):
        return 1

    def fileManager_shouldProceedAfterError_movingItemAtPath_toPath_(self, a, b, c, d):
        return 1

    def fileManager_shouldLinkItemAtPath_toPath_(self, a, b, c):
        return 1

    def fileManager_shouldProceedAfterError_linkingItemAtPath_toPath_(self, a, b, c, d):
        return 1

    def fileManager_shouldRemoveItemAtPath_(self, a, b):
        return 1

    def fileManager_shouldProceedAfterError_removingItemAtPath_(self, a, b, c):
        return 1

    def fileManager_shouldCopyItemAtURL_toURL_(self, a, b, c):
        return 1

    def fileManager_shouldProceedAfterError_copyingItemAtURL_toURL_(self, a, b, c, d):
        return 1

    def fileManager_shouldMoveItemAtURL_toURL_(self, a, b, c):
        return 1

    def fileManager_shouldProceedAfterError_movingItemAtURL_toURL_(self, a, b, c, d):
        return 1

    def fileManager_shouldLinkItemAtURL_toURL_(self, a, b, c):
        return 1

    def fileManager_shouldProceedAfterError_linkingItemAtURL_toURL_(self, a, b, c, d):
        return 1

    def fileManager_shouldRemoveItemAtURL_(self, a, b):
        return 1

    def fileManager_shouldProceedAfterError_removingItemAtURL_(self, a, b, c):
        return 1


class TestNSFileManager(TestCase):
    def test_typed_enum(self):
        self.assertIsTypedEnum(Foundation.NSFileAttributeKey, str)
        self.assertIsTypedEnum(Foundation.NSFileAttributeType, str)
        self.assertIsTypedEnum(Foundation.NSFileProtectionType, str)
        self.assertIsTypedEnum(Foundation.NSFileProviderServiceName, str)

    def test_enum_types(self):
        self.assertIsEnumType(Foundation.NSDirectoryEnumerationOptions)
        self.assertIsEnumType(Foundation.NSFileManagerItemReplacementOptions)
        self.assertIsEnumType(Foundation.NSFileManagerUnmountOptions)
        self.assertIsEnumType(Foundation.NSURLRelationship)
        self.assertIsEnumType(Foundation.NSVolumeEnumerationOptions)

    def testConstants(self):
        self.assertEqual(
            Foundation.NSFoundationVersionWithFileManagerResourceForkSupport, 412
        )

        self.assertIsInstance(Foundation.NSFileType, str)
        self.assertIsInstance(Foundation.NSFileTypeDirectory, str)
        self.assertIsInstance(Foundation.NSFileTypeRegular, str)
        self.assertIsInstance(Foundation.NSFileTypeSymbolicLink, str)
        self.assertIsInstance(Foundation.NSFileTypeSocket, str)
        self.assertIsInstance(Foundation.NSFileTypeCharacterSpecial, str)
        self.assertIsInstance(Foundation.NSFileTypeBlockSpecial, str)
        self.assertIsInstance(Foundation.NSFileTypeUnknown, str)
        self.assertIsInstance(Foundation.NSFileSize, str)
        self.assertIsInstance(Foundation.NSFileModificationDate, str)
        self.assertIsInstance(Foundation.NSFileReferenceCount, str)
        self.assertIsInstance(Foundation.NSFileDeviceIdentifier, str)
        self.assertIsInstance(Foundation.NSFileOwnerAccountName, str)
        self.assertIsInstance(Foundation.NSFileGroupOwnerAccountName, str)
        self.assertIsInstance(Foundation.NSFilePosixPermissions, str)
        self.assertIsInstance(Foundation.NSFileSystemNumber, str)
        self.assertIsInstance(Foundation.NSFileSystemFileNumber, str)
        self.assertIsInstance(Foundation.NSFileExtensionHidden, str)
        self.assertIsInstance(Foundation.NSFileHFSCreatorCode, str)
        self.assertIsInstance(Foundation.NSFileHFSTypeCode, str)
        self.assertIsInstance(Foundation.NSFileImmutable, str)
        self.assertIsInstance(Foundation.NSFileAppendOnly, str)
        self.assertIsInstance(Foundation.NSFileCreationDate, str)
        self.assertIsInstance(Foundation.NSFileOwnerAccountID, str)
        self.assertIsInstance(Foundation.NSFileGroupOwnerAccountID, str)
        self.assertIsInstance(Foundation.NSFileBusy, str)
        self.assertIsInstance(Foundation.NSFileSystemSize, str)
        self.assertIsInstance(Foundation.NSFileSystemFreeSize, str)
        self.assertIsInstance(Foundation.NSFileSystemNodes, str)
        self.assertIsInstance(Foundation.NSFileSystemFreeNodes, str)

    @min_os_level("10.14")
    def testConstantsMissingOn10_9(self):
        self.assertIsInstance(Foundation.NSFileProtectionKey, str)
        self.assertIsInstance(Foundation.NSFileProtectionNone, str)
        self.assertIsInstance(Foundation.NSFileProtectionComplete, str)
        self.assertIsInstance(Foundation.NSFileProtectionCompleteUnlessOpen, str)
        self.assertIsInstance(
            Foundation.NSFileProtectionCompleteUntilFirstUserAuthentication, str
        )

    @min_os_level("10.6")
    def testConstants10_6(self):
        self.assertEqual(Foundation.NSVolumeEnumerationSkipHiddenVolumes, 1 << 1)
        self.assertEqual(Foundation.NSVolumeEnumerationProduceFileReferenceURLs, 1 << 2)

        self.assertEqual(
            Foundation.NSDirectoryEnumerationSkipsSubdirectoryDescendants, 1 << 0
        )
        self.assertEqual(
            Foundation.NSDirectoryEnumerationSkipsPackageDescendants, 1 << 1
        )
        self.assertEqual(Foundation.NSDirectoryEnumerationSkipsHiddenFiles, 1 << 2)

        self.assertEqual(
            Foundation.NSFileManagerItemReplacementUsingNewMetadataOnly, 1 << 0
        )
        self.assertEqual(
            Foundation.NSFileManagerItemReplacementWithoutDeletingBackupItem, 1 << 1
        )

    @min_os_level("10.8")
    def testConstants10_8(self):
        self.assertIsInstance(Foundation.NSUbiquityIdentityDidChangeNotification, str)

    @min_os_level("10.10")
    def testConstants10_10(self):
        self.assertEqual(Foundation.NSURLRelationshipContains, 0)
        self.assertEqual(Foundation.NSURLRelationshipSame, 1)
        self.assertEqual(Foundation.NSURLRelationshipOther, 2)

    @min_os_level("10.11")
    def testConstants10_11(self):
        self.assertEqual(
            Foundation.NSFileManagerUnmountAllPartitionsAndEjectDisk, 1 << 0
        )
        self.assertEqual(Foundation.NSFileManagerUnmountWithoutUI, 1 << 1)

        self.assertIsInstance(
            Foundation.NSFileManagerUnmountDissentingProcessIdentifierErrorKey, str
        )

    @min_os_level("10.15")
    def testConstants10_15(self):
        self.assertEqual(
            Foundation.NSDirectoryEnumerationIncludesDirectoriesPostOrder, 1 << 3
        )
        self.assertEqual(
            Foundation.NSDirectoryEnumerationProducesRelativePathURLs, 1 << 4
        )

    @min_os_level("11.0")
    def testConstants11_0(self):
        self.assertIsInstance(Foundation.NSURLFileProtectionComplete, str)
        self.assertIsInstance(Foundation.NSURLFileProtectionCompleteUnlessOpen, str)
        self.assertIsInstance(
            Foundation.NSURLFileProtectionCompleteUntilFirstUserAuthentication, str
        )

    @min_os_level("14.0")
    def testConstants14_0(self):
        self.assertIsInstance(Foundation.NSFileProtectionCompleteWhenUserInactive, str)

    @min_os_level("10.6")
    def testMethods10_6(self):
        self.assertArgIsOut(
            Foundation.NSFileManager.contentsOfDirectoryAtURL_includingPropertiesForKeys_options_error_,  # noqa: B950
            3,
        )
        self.assertArgIsBOOL(
            Foundation.NSFileManager.URLForDirectory_inDomain_appropriateForURL_create_error_,
            3,
        )
        self.assertArgIsOut(
            Foundation.NSFileManager.URLForDirectory_inDomain_appropriateForURL_create_error_,
            4,
        )

        self.assertResultIsBOOL(Foundation.NSFileManager.copyItemAtURL_toURL_error_)
        self.assertArgIsOut(Foundation.NSFileManager.copyItemAtURL_toURL_error_, 2)
        self.assertResultIsBOOL(Foundation.NSFileManager.moveItemAtURL_toURL_error_)
        self.assertArgIsOut(Foundation.NSFileManager.moveItemAtURL_toURL_error_, 2)
        self.assertResultIsBOOL(Foundation.NSFileManager.linkItemAtURL_toURL_error_)
        self.assertArgIsOut(Foundation.NSFileManager.linkItemAtURL_toURL_error_, 2)
        self.assertResultIsBOOL(Foundation.NSFileManager.removeItemAtURL_error_)
        self.assertArgIsOut(Foundation.NSFileManager.removeItemAtURL_error_, 1)

        self.assertArgIsBlock(
            Foundation.NSFileManager.enumeratorAtURL_includingPropertiesForKeys_options_errorHandler_,  # noqa: B950
            3,
            objc._C_NSBOOL + b"@@",
        )

        self.assertResultIsBOOL(
            Foundation.NSFileManager.replaceItemAtURL_withItemAtURL_backupItemName_options_resultingItemURL_error_  # noqa: B950
        )
        self.assertArgIsOut(
            Foundation.NSFileManager.replaceItemAtURL_withItemAtURL_backupItemName_options_resultingItemURL_error_,  # noqa: B950
            4,
        )
        self.assertArgIsOut(
            Foundation.NSFileManager.replaceItemAtURL_withItemAtURL_backupItemName_options_resultingItemURL_error_,  # noqa: B950
            5,
        )

    @min_os_level("10.7")
    def testMethods10_7(self):
        self.assertResultIsBOOL(
            Foundation.NSFileManager.createDirectoryAtURL_withIntermediateDirectories_attributes_error_  # noqa: B950
        )
        self.assertArgIsBOOL(
            Foundation.NSFileManager.createDirectoryAtURL_withIntermediateDirectories_attributes_error_,  # noqa: B950
            1,
        )
        self.assertArgIsOut(
            Foundation.NSFileManager.createDirectoryAtURL_withIntermediateDirectories_attributes_error_,  # noqa: B950
            3,
        )

        self.assertResultIsBOOL(
            Foundation.NSFileManager.createSymbolicLinkAtURL_withDestinationURL_error_
        )
        self.assertArgIsOut(
            Foundation.NSFileManager.createSymbolicLinkAtURL_withDestinationURL_error_,
            2,
        )

        self.assertResultIsBOOL(
            Foundation.NSFileManager.setUbiquitous_itemAtURL_destinationURL_error_
        )
        self.assertArgIsBOOL(
            Foundation.NSFileManager.setUbiquitous_itemAtURL_destinationURL_error_, 0
        )
        self.assertArgIsOut(
            Foundation.NSFileManager.setUbiquitous_itemAtURL_destinationURL_error_, 3
        )
        self.assertResultIsBOOL(Foundation.NSFileManager.isUbiquitousItemAtURL_)

        self.assertResultIsBOOL(
            Foundation.NSFileManager.startDownloadingUbiquitousItemAtURL_error_
        )
        self.assertArgIsOut(
            Foundation.NSFileManager.startDownloadingUbiquitousItemAtURL_error_, 1
        )

        self.assertResultIsBOOL(
            Foundation.NSFileManager.evictUbiquitousItemAtURL_error_
        )
        self.assertArgIsOut(Foundation.NSFileManager.evictUbiquitousItemAtURL_error_, 1)

        self.assertArgIsOut(
            Foundation.NSFileManager.URLForPublishingUbiquitousItemAtURL_expirationDate_error_,
            1,
        )
        self.assertArgIsOut(
            Foundation.NSFileManager.URLForPublishingUbiquitousItemAtURL_expirationDate_error_,
            2,
        )

    @min_os_level("10.8")
    def testMethods10_8(self):
        self.assertResultIsBOOL(
            Foundation.NSFileManager.trashItemAtURL_resultingItemURL_error_
        )
        self.assertArgIsOut(
            Foundation.NSFileManager.trashItemAtURL_resultingItemURL_error_, 1
        )
        self.assertArgIsOut(
            Foundation.NSFileManager.trashItemAtURL_resultingItemURL_error_, 2
        )

    @min_os_level("10.10")
    def testMethods10_10(self):
        self.assertResultIsBOOL(
            Foundation.NSFileManager.getRelationship_ofDirectoryAtURL_toItemAtURL_error_
        )
        self.assertArgIsOut(
            Foundation.NSFileManager.getRelationship_ofDirectoryAtURL_toItemAtURL_error_,
            0,
        )
        self.assertArgIsOut(
            Foundation.NSFileManager.getRelationship_ofDirectoryAtURL_toItemAtURL_error_,
            3,
        )

        self.assertResultIsBOOL(
            Foundation.NSFileManager.getRelationship_ofDirectory_inDomain_toItemAtURL_error_
        )
        self.assertArgIsOut(
            Foundation.NSFileManager.getRelationship_ofDirectory_inDomain_toItemAtURL_error_,
            0,
        )
        self.assertArgIsOut(
            Foundation.NSFileManager.getRelationship_ofDirectory_inDomain_toItemAtURL_error_,
            4,
        )

    def testOutput(self):
        obj = Foundation.NSFileManager.defaultManager()
        m = obj.setAttributes_ofItemAtPath_error_.__metadata__()
        self.assertTrue(m["arguments"][4]["type"].startswith(b"o^"))

        m = (
            obj.createDirectoryAtPath_withIntermediateDirectories_attributes_error_.__metadata__()  # noqa: B950
        )
        self.assertEqual(m["arguments"][3]["type"], b"Z")
        self.assertTrue(m["arguments"][5]["type"].startswith(b"o^"))

        m = obj.contentsOfDirectoryAtPath_error_.__metadata__()
        self.assertTrue(m["arguments"][3]["type"].startswith(b"o^"))

        m = obj.subpathsOfDirectoryAtPath_error_.__metadata__()
        self.assertTrue(m["arguments"][3]["type"].startswith(b"o^"))

        m = obj.attributesOfItemAtPath_error_.__metadata__()
        self.assertTrue(m["arguments"][3]["type"].startswith(b"o^"))

        m = obj.attributesOfFileSystemForPath_error_.__metadata__()
        self.assertTrue(m["arguments"][3]["type"].startswith(b"o^"))

        m = obj.createSymbolicLinkAtPath_withDestinationPath_error_.__metadata__()
        self.assertTrue(m["arguments"][4]["type"].startswith(b"o^"))

        m = obj.destinationOfSymbolicLinkAtPath_error_.__metadata__()
        self.assertTrue(m["arguments"][3]["type"].startswith(b"o^"))

        m = obj.copyItemAtPath_toPath_error_.__metadata__()
        self.assertEqual(m["retval"]["type"], b"Z")
        self.assertTrue(m["arguments"][4]["type"].startswith(b"o^"))

        m = obj.moveItemAtPath_toPath_error_.__metadata__()
        self.assertEqual(m["retval"]["type"], b"Z")
        self.assertTrue(m["arguments"][4]["type"].startswith(b"o^"))

        m = obj.linkItemAtPath_toPath_error_.__metadata__()
        self.assertEqual(m["retval"]["type"], b"Z")
        self.assertTrue(m["arguments"][4]["type"].startswith(b"o^"))

        m = obj.removeItemAtPath_error_.__metadata__()
        self.assertEqual(m["retval"]["type"], b"Z")
        self.assertTrue(m["arguments"][3]["type"].startswith(b"o^"))

    def testProtocols(self):
        class FileManagerTest1(Foundation.NSObject):
            def fileManager_shouldCopyItemAtPath_toPath_(self, fm, src, dst):
                return True

            def fileManager_shouldProceedAfterError_copyingItemAtPath_toPath_(
                self, fm, error, src, dst
            ):
                return True

            def fileManager_shouldMoveItemAtPath_toPath_(self, fm, src, dst):
                return True

            def fileManager_shouldProceedAfterError_movingItemAtPath_toPath_(
                self, fm, error, src, dst
            ):
                return True

            def fileManager_shouldLinkItemAtPath_toPath_(self, fm, src, dst):
                return True

            def fileManager_shouldProceedAfterError_linkingItemAtPath_toPath_(
                self, fm, error, src, dst
            ):
                return True

            def fileManager_shouldRemoveItemAtPath_(self, fm, src):
                return True

            def fileManager_shouldProceedAfterError_removingItemAtPath_(
                self, fm, error, src
            ):
                return True

        obj = FileManagerTest1.alloc().init()
        m = obj.fileManager_shouldCopyItemAtPath_toPath_.__metadata__()
        self.assertEqual(m["retval"]["type"], b"Z")
        m = (
            obj.fileManager_shouldProceedAfterError_copyingItemAtPath_toPath_.__metadata__()
        )
        self.assertEqual(m["retval"]["type"], b"Z")
        m = obj.fileManager_shouldMoveItemAtPath_toPath_.__metadata__()
        self.assertEqual(m["retval"]["type"], b"Z")
        m = (
            obj.fileManager_shouldProceedAfterError_movingItemAtPath_toPath_.__metadata__()
        )
        self.assertEqual(m["retval"]["type"], b"Z")
        m = obj.fileManager_shouldLinkItemAtPath_toPath_.__metadata__()
        self.assertEqual(m["retval"]["type"], b"Z")
        m = (
            obj.fileManager_shouldProceedAfterError_linkingItemAtPath_toPath_.__metadata__()
        )
        self.assertEqual(m["retval"]["type"], b"Z")
        m = obj.fileManager_shouldRemoveItemAtPath_.__metadata__()
        self.assertEqual(m["retval"]["type"], b"Z")
        m = obj.fileManager_shouldProceedAfterError_removingItemAtPath_.__metadata__()
        self.assertEqual(m["retval"]["type"], b"Z")

    @min_os_level("10.5")
    def testMethods10_5(self):
        self.assertResultIsBOOL(
            Foundation.NSFileManager.setAttributes_ofItemAtPath_error_
        )
        self.assertArgIsOut(
            Foundation.NSFileManager.setAttributes_ofItemAtPath_error_, 2
        )

        self.assertResultIsBOOL(
            Foundation.NSFileManager.createDirectoryAtPath_withIntermediateDirectories_attributes_error_  # noqa: B950
        )
        self.assertArgIsBOOL(
            Foundation.NSFileManager.createDirectoryAtPath_withIntermediateDirectories_attributes_error_,  # noqa: B950
            1,
        )
        self.assertArgIsOut(
            Foundation.NSFileManager.createDirectoryAtPath_withIntermediateDirectories_attributes_error_,  # noqa: B950
            3,
        )

        self.assertArgIsOut(
            Foundation.NSFileManager.contentsOfDirectoryAtPath_error_, 1
        )
        self.assertArgIsOut(
            Foundation.NSFileManager.subpathsOfDirectoryAtPath_error_, 1
        )
        self.assertArgIsOut(Foundation.NSFileManager.attributesOfItemAtPath_error_, 1)
        self.assertArgIsOut(
            Foundation.NSFileManager.attributesOfFileSystemForPath_error_, 1
        )

        self.assertResultIsBOOL(
            Foundation.NSFileManager.createSymbolicLinkAtPath_withDestinationPath_error_
        )
        self.assertArgIsOut(
            Foundation.NSFileManager.createSymbolicLinkAtPath_withDestinationPath_error_,
            2,
        )

        self.assertArgIsOut(
            Foundation.NSFileManager.destinationOfSymbolicLinkAtPath_error_, 1
        )

        self.assertResultIsBOOL(Foundation.NSFileManager.copyItemAtPath_toPath_error_)
        self.assertArgIsOut(Foundation.NSFileManager.copyItemAtPath_toPath_error_, 2)
        self.assertResultIsBOOL(Foundation.NSFileManager.moveItemAtPath_toPath_error_)
        self.assertArgIsOut(Foundation.NSFileManager.moveItemAtPath_toPath_error_, 2)
        self.assertResultIsBOOL(Foundation.NSFileManager.linkItemAtPath_toPath_error_)
        self.assertArgIsOut(Foundation.NSFileManager.linkItemAtPath_toPath_error_, 2)
        self.assertResultIsBOOL(Foundation.NSFileManager.removeItemAtPath_error_)
        self.assertArgIsOut(Foundation.NSFileManager.removeItemAtPath_error_, 1)

    def testMethods(self):
        self.assertArgIsBOOL(
            Foundation.NSFileManager.fileAttributesAtPath_traverseLink_, 1
        )
        self.assertResultIsBOOL(Foundation.NSFileManager.changeFileAttributes_atPath_)
        self.assertResultIsBOOL(
            Foundation.NSFileManager.createSymbolicLinkAtPath_pathContent_
        )
        self.assertResultIsBOOL(
            Foundation.NSFileManager.createDirectoryAtPath_attributes_
        )
        self.assertResultIsBOOL(Foundation.NSFileManager.linkPath_toPath_handler_)
        self.assertResultIsBOOL(Foundation.NSFileManager.copyPath_toPath_handler_)
        self.assertResultIsBOOL(Foundation.NSFileManager.movePath_toPath_handler_)
        self.assertResultIsBOOL(Foundation.NSFileManager.removeFileAtPath_handler_)
        self.assertResultIsBOOL(Foundation.NSFileManager.changeCurrentDirectoryPath_)
        self.assertResultIsBOOL(Foundation.NSFileManager.fileExistsAtPath_)
        self.assertResultIsBOOL(Foundation.NSFileManager.fileExistsAtPath_isDirectory_)
        self.assertArgHasType(
            Foundation.NSFileManager.fileExistsAtPath_isDirectory_,
            1,
            b"o^" + objc._C_NSBOOL,
        )
        self.assertResultIsBOOL(Foundation.NSFileManager.isReadableFileAtPath_)
        self.assertResultIsBOOL(Foundation.NSFileManager.isWritableFileAtPath_)
        self.assertResultIsBOOL(Foundation.NSFileManager.isExecutableFileAtPath_)
        self.assertResultIsBOOL(Foundation.NSFileManager.isDeletableFileAtPath_)
        self.assertResultIsBOOL(Foundation.NSFileManager.contentsEqualAtPath_andPath_)
        self.assertResultIsBOOL(
            Foundation.NSFileManager.createFileAtPath_contents_attributes_
        )
        self.assertResultHasType(
            Foundation.NSFileManager.fileSystemRepresentationWithPath_,
            b"^" + objc._C_CHAR_AS_TEXT,
        )
        self.assertResultIsNullTerminated(
            Foundation.NSFileManager.fileSystemRepresentationWithPath_
        )
        self.assertArgHasType(
            Foundation.NSFileManager.stringWithFileSystemRepresentation_length_,
            0,
            b"n^" + objc._C_CHAR_AS_TEXT,
        )
        self.assertArgSizeInArg(
            Foundation.NSFileManager.stringWithFileSystemRepresentation_length_, 0, 1
        )

        self.assertResultIsBOOL(Foundation.NSDictionary.fileIsImmutable)
        self.assertResultIsBOOL(Foundation.NSDictionary.fileIsAppendOnly)
        self.assertResultIsBOOL(Foundation.NSDictionary.fileExtensionHidden)

    @min_os_level("10.11")
    def testMethods10_11(self):
        self.assertArgIsBlock(
            Foundation.NSFileManager.unmountVolumeAtURL_options_completionHandler_,
            2,
            b"v@",
        )

    @min_os_level("10.13")
    def testMethods10_13(self):
        self.assertArgIsBlock(
            Foundation.NSFileManager.getFileProviderMessageInterfacesForItemAtURL_completionHandler_,  # noqa: B950
            1,
            b"v@@",
        )

    @min_os_level("10.15")
    def testMethods10_15(self):
        self.assertResultIsBOOL(
            Foundation.NSDirectoryEnumerator.isEnumeratingDirectoryPostOrder
        )

    def testProtocolsMethods(self):
        self.assertResultIsBOOL(
            TestNSFileManagerHelper.fileManager_shouldProceedAfterError_
        )
        self.assertResultIsBOOL(
            TestNSFileManagerHelper.fileManager_shouldCopyItemAtPath_toPath_
        )
        self.assertResultIsBOOL(
            TestNSFileManagerHelper.fileManager_shouldProceedAfterError_copyingItemAtPath_toPath_  # noqa: B950
        )
        self.assertResultIsBOOL(
            TestNSFileManagerHelper.fileManager_shouldMoveItemAtPath_toPath_
        )
        self.assertResultIsBOOL(
            TestNSFileManagerHelper.fileManager_shouldProceedAfterError_movingItemAtPath_toPath_
        )
        self.assertResultIsBOOL(
            TestNSFileManagerHelper.fileManager_shouldLinkItemAtPath_toPath_
        )
        self.assertResultIsBOOL(
            TestNSFileManagerHelper.fileManager_shouldProceedAfterError_linkingItemAtPath_toPath_  # noqa: B950
        )
        self.assertResultIsBOOL(
            TestNSFileManagerHelper.fileManager_shouldRemoveItemAtPath_
        )
        self.assertResultIsBOOL(
            TestNSFileManagerHelper.fileManager_shouldProceedAfterError_removingItemAtPath_
        )

    @min_os_level("10.6")
    def testProtocols10_6(self):
        self.assertResultIsBOOL(
            TestNSFileManagerHelper.fileManager_shouldCopyItemAtURL_toURL_
        )
        self.assertResultIsBOOL(
            TestNSFileManagerHelper.fileManager_shouldProceedAfterError_copyingItemAtURL_toURL_
        )
        self.assertResultIsBOOL(
            TestNSFileManagerHelper.fileManager_shouldMoveItemAtURL_toURL_
        )
        self.assertResultIsBOOL(
            TestNSFileManagerHelper.fileManager_shouldProceedAfterError_movingItemAtURL_toURL_
        )
        self.assertResultIsBOOL(
            TestNSFileManagerHelper.fileManager_shouldLinkItemAtURL_toURL_
        )
        self.assertResultIsBOOL(
            TestNSFileManagerHelper.fileManager_shouldProceedAfterError_linkingItemAtURL_toURL_
        )
        self.assertResultIsBOOL(
            TestNSFileManagerHelper.fileManager_shouldRemoveItemAtURL_
        )
        self.assertResultIsBOOL(
            TestNSFileManagerHelper.fileManager_shouldProceedAfterError_removingItemAtURL_
        )

    @min_sdk_level("10.10")
    def testProtocols10_10(self):
        self.assertProtocolExists("NSFileManagerDelegate")
