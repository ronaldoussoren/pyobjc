import Foundation
from PyObjCTools.TestSupport import TestCase, min_os_level
import objc


class TestNSURL(TestCase):
    def testMethods(self):
        self.assertArgIsBOOL(Foundation.NSURL.initFileURLWithPath_isDirectory_, 1)
        self.assertArgIsBOOL(Foundation.NSURL.fileURLWithPath_isDirectory_, 1)
        self.assertResultIsBOOL(Foundation.NSURL.isFileURL)

        self.assertArgIsBOOL(Foundation.NSURL.resourceDataUsingCache_, 0)
        self.assertArgIsBOOL(
            Foundation.NSURL.loadResourceDataNotifyingClient_usingCache_, 1
        )
        self.assertResultIsBOOL(Foundation.NSURL.setResourceData_)
        self.assertResultIsBOOL(Foundation.NSURL.setProperty_forKey_)
        self.assertArgIsBOOL(Foundation.NSURL.URLHandleUsingCache_, 0)

    @min_os_level("10.7")
    def testMethods10_7(self):
        self.assertResultIsBOOL(Foundation.NSURL.startAccessingSecurityScopedResource)

    @min_os_level("10.9")
    def testMethods10_9(self):
        self.assertArgIsIn(
            Foundation.NSURL.initFileURLWithFileSystemRepresentation_isDirectory_relativeToURL_,
            0,
        )
        self.assertArgIsBOOL(
            Foundation.NSURL.initFileURLWithFileSystemRepresentation_isDirectory_relativeToURL_,
            1,
        )

        self.assertArgIsIn(
            Foundation.NSURL.fileURLWithFileSystemRepresentation_isDirectory_relativeToURL_,
            0,
        )
        self.assertArgIsBOOL(
            Foundation.NSURL.fileURLWithFileSystemRepresentation_isDirectory_relativeToURL_,
            1,
        )

        self.assertResultIsBOOL(Foundation.NSURL.getFileSystemRepresentation_maxLength_)
        self.assertArgIsOut(Foundation.NSURL.getFileSystemRepresentation_maxLength_, 0)
        self.assertArgSizeInArg(
            Foundation.NSURL.getFileSystemRepresentation_maxLength_, 0, 1
        )

        self.assertArgIsBOOL(
            Foundation.NSURLComponents.initWithURL_resolvingAgainstBaseURL_, 1
        )
        self.assertArgIsBOOL(
            Foundation.NSURLComponents.componentsWithURL_resolvingAgainstBaseURL_, 1
        )

    @min_os_level("10.10")
    def testMethods10_10(self):
        self.assertArgIsOut(
            Foundation.NSURL.URLByResolvingAliasFileAtURL_options_error_, 2
        )

        self.assertResultIsBOOL(
            Foundation.NSURL.getPromisedItemResourceValue_forKey_error_
        )
        self.assertArgIsOut(
            Foundation.NSURL.getPromisedItemResourceValue_forKey_error_, 2
        )
        self.assertArgIsOut(
            Foundation.NSURL.promisedItemResourceValuesForKeys_error_, 1
        )

        self.assertResultIsBOOL(
            Foundation.NSURL.checkPromisedItemIsReachableAndReturnError_
        )
        self.assertArgIsOut(
            Foundation.NSURL.checkPromisedItemIsReachableAndReturnError_, 0
        )

    @min_os_level("10.11")
    def testMethods10_11(self):
        self.assertArgIsBOOL(
            Foundation.NSURL.initFileURLWithPath_isDirectory_relativeToURL_, 1
        )
        self.assertArgIsBOOL(
            Foundation.NSURL.fileURLWithPath_isDirectory_relativeToURL_, 1
        )
        self.assertResultIsBOOL(Foundation.NSURL.hasDirectoryPath)

    def testConstants(self):
        self.assertIsInstance(Foundation.NSURLFileScheme, str)

    @min_os_level("10.6")
    def testConstants10_6(self):
        self.assertEqual(
            Foundation.NSURLBookmarkCreationPreferFileIDResolution, (1 << 8)
        )
        self.assertEqual(Foundation.NSURLBookmarkCreationMinimalBookmark, (1 << 9))
        self.assertEqual(
            Foundation.NSURLBookmarkCreationSuitableForBookmarkFile, (1 << 10)
        )
        self.assertEqual(Foundation.NSURLBookmarkResolutionWithoutUI, (1 << 8))
        self.assertEqual(Foundation.NSURLBookmarkResolutionWithoutMounting, (1 << 9))

        self.assertIsInstance(Foundation.NSURLNameKey, str)
        self.assertIsInstance(Foundation.NSURLLocalizedNameKey, str)
        self.assertIsInstance(Foundation.NSURLIsRegularFileKey, str)
        self.assertIsInstance(Foundation.NSURLIsDirectoryKey, str)
        self.assertIsInstance(Foundation.NSURLIsSymbolicLinkKey, str)
        self.assertIsInstance(Foundation.NSURLIsVolumeKey, str)
        self.assertIsInstance(Foundation.NSURLIsPackageKey, str)
        self.assertIsInstance(Foundation.NSURLIsSystemImmutableKey, str)
        self.assertIsInstance(Foundation.NSURLIsUserImmutableKey, str)
        self.assertIsInstance(Foundation.NSURLIsHiddenKey, str)
        self.assertIsInstance(Foundation.NSURLHasHiddenExtensionKey, str)
        self.assertIsInstance(Foundation.NSURLCreationDateKey, str)
        self.assertIsInstance(Foundation.NSURLContentAccessDateKey, str)
        self.assertIsInstance(Foundation.NSURLContentModificationDateKey, str)
        self.assertIsInstance(Foundation.NSURLAttributeModificationDateKey, str)
        self.assertIsInstance(Foundation.NSURLLinkCountKey, str)
        self.assertIsInstance(Foundation.NSURLParentDirectoryURLKey, str)
        self.assertIsInstance(Foundation.NSURLVolumeURLKey, str)
        self.assertIsInstance(Foundation.NSURLTypeIdentifierKey, str)
        self.assertIsInstance(Foundation.NSURLLocalizedTypeDescriptionKey, str)
        self.assertIsInstance(Foundation.NSURLLabelNumberKey, str)
        self.assertIsInstance(Foundation.NSURLLabelColorKey, str)
        self.assertIsInstance(Foundation.NSURLLocalizedLabelKey, str)
        self.assertIsInstance(Foundation.NSURLEffectiveIconKey, str)
        self.assertIsInstance(Foundation.NSURLCustomIconKey, str)
        self.assertIsInstance(Foundation.NSURLFileSizeKey, str)
        self.assertIsInstance(Foundation.NSURLFileAllocatedSizeKey, str)
        self.assertIsInstance(Foundation.NSURLIsAliasFileKey, str)
        self.assertIsInstance(Foundation.NSURLVolumeLocalizedFormatDescriptionKey, str)
        self.assertIsInstance(Foundation.NSURLVolumeTotalCapacityKey, str)
        self.assertIsInstance(Foundation.NSURLVolumeAvailableCapacityKey, str)
        self.assertIsInstance(Foundation.NSURLVolumeResourceCountKey, str)

    @min_os_level("10.6")
    def testConstants10_6_2(self):
        self.assertIsInstance(Foundation.NSURLVolumeSupportsPersistentIDsKey, str)
        self.assertIsInstance(Foundation.NSURLVolumeSupportsSymbolicLinksKey, str)
        self.assertIsInstance(Foundation.NSURLVolumeSupportsHardLinksKey, str)
        self.assertIsInstance(Foundation.NSURLVolumeSupportsJournalingKey, str)
        self.assertIsInstance(Foundation.NSURLVolumeIsJournalingKey, str)
        self.assertIsInstance(Foundation.NSURLVolumeSupportsSparseFilesKey, str)
        self.assertIsInstance(Foundation.NSURLVolumeSupportsZeroRunsKey, str)
        self.assertIsInstance(Foundation.NSURLVolumeSupportsCaseSensitiveNamesKey, str)
        self.assertIsInstance(Foundation.NSURLVolumeSupportsCasePreservedNamesKey, str)

    @min_os_level("10.7")
    def testConstants10_7(self):
        self.assertEqual(Foundation.NSURLBookmarkCreationWithSecurityScope, (1 << 11))
        self.assertEqual(
            Foundation.NSURLBookmarkCreationSecurityScopeAllowOnlyReadAccess, (1 << 12)
        )
        self.assertEqual(Foundation.NSURLBookmarkResolutionWithSecurityScope, (1 << 10))

        self.assertIsInstance(Foundation.NSURLKeysOfUnsetValuesKey, str)

        self.assertIsInstance(Foundation.NSURLFileResourceIdentifierKey, str)
        self.assertIsInstance(Foundation.NSURLVolumeIdentifierKey, str)
        self.assertIsInstance(Foundation.NSURLPreferredIOBlockSizeKey, str)
        self.assertIsInstance(Foundation.NSURLIsReadableKey, str)
        self.assertIsInstance(Foundation.NSURLIsWritableKey, str)
        self.assertIsInstance(Foundation.NSURLIsExecutableKey, str)
        self.assertIsInstance(Foundation.NSURLIsMountTriggerKey, str)
        self.assertIsInstance(Foundation.NSURLFileSecurityKey, str)
        self.assertIsInstance(Foundation.NSURLFileResourceTypeKey, str)
        self.assertIsInstance(Foundation.NSURLFileResourceTypeNamedPipe, str)
        self.assertIsInstance(Foundation.NSURLFileResourceTypeCharacterSpecial, str)
        self.assertIsInstance(Foundation.NSURLFileResourceTypeDirectory, str)
        self.assertIsInstance(Foundation.NSURLFileResourceTypeBlockSpecial, str)
        self.assertIsInstance(Foundation.NSURLFileResourceTypeRegular, str)
        self.assertIsInstance(Foundation.NSURLFileResourceTypeSymbolicLink, str)
        self.assertIsInstance(Foundation.NSURLFileResourceTypeSocket, str)
        self.assertIsInstance(Foundation.NSURLFileResourceTypeUnknown, str)
        self.assertIsInstance(Foundation.NSURLTotalFileSizeKey, str)
        self.assertIsInstance(Foundation.NSURLTotalFileAllocatedSizeKey, str)
        self.assertIsInstance(Foundation.NSURLVolumeSupportsRootDirectoryDatesKey, str)
        self.assertIsInstance(Foundation.NSURLVolumeSupportsVolumeSizesKey, str)
        self.assertIsInstance(Foundation.NSURLVolumeSupportsRenamingKey, str)
        self.assertIsInstance(Foundation.NSURLVolumeSupportsAdvisoryFileLockingKey, str)
        self.assertIsInstance(Foundation.NSURLVolumeSupportsExtendedSecurityKey, str)
        self.assertIsInstance(Foundation.NSURLVolumeIsBrowsableKey, str)
        self.assertIsInstance(Foundation.NSURLVolumeMaximumFileSizeKey, str)
        self.assertIsInstance(Foundation.NSURLVolumeIsEjectableKey, str)
        self.assertIsInstance(Foundation.NSURLVolumeIsRemovableKey, str)
        self.assertIsInstance(Foundation.NSURLVolumeIsInternalKey, str)
        self.assertIsInstance(Foundation.NSURLVolumeIsAutomountedKey, str)
        self.assertIsInstance(Foundation.NSURLVolumeIsLocalKey, str)
        self.assertIsInstance(Foundation.NSURLVolumeIsReadOnlyKey, str)
        self.assertIsInstance(Foundation.NSURLVolumeCreationDateKey, str)
        self.assertIsInstance(Foundation.NSURLVolumeURLForRemountingKey, str)
        self.assertIsInstance(Foundation.NSURLVolumeUUIDStringKey, str)
        self.assertIsInstance(Foundation.NSURLVolumeNameKey, str)
        self.assertIsInstance(Foundation.NSURLVolumeLocalizedNameKey, str)
        self.assertIsInstance(Foundation.NSURLIsUbiquitousItemKey, str)
        self.assertIsInstance(
            Foundation.NSURLUbiquitousItemHasUnresolvedConflictsKey, str
        )
        self.assertIsInstance(Foundation.NSURLUbiquitousItemIsDownloadedKey, str)
        self.assertIsInstance(Foundation.NSURLUbiquitousItemIsDownloadingKey, str)
        self.assertIsInstance(Foundation.NSURLUbiquitousItemIsUploadedKey, str)
        self.assertIsInstance(Foundation.NSURLUbiquitousItemIsUploadingKey, str)
        self.assertIsInstance(Foundation.NSURLUbiquitousItemPercentDownloadedKey, str)
        self.assertIsInstance(Foundation.NSURLUbiquitousItemPercentUploadedKey, str)

    @min_os_level("10.8")
    def testConstants10_8(self):
        self.assertIsInstance(Foundation.NSURLIsExcludedFromBackupKey, str)
        self.assertIsInstance(Foundation.NSURLPathKey, str)

    @min_os_level("10.9")
    def testConstants10_9(self):
        self.assertIsInstance(Foundation.NSURLTagNamesKey, str)
        self.assertIsInstance(Foundation.NSURLUbiquitousItemDownloadingStatusKey, str)
        self.assertIsInstance(Foundation.NSURLUbiquitousItemDownloadingErrorKey, str)
        self.assertIsInstance(Foundation.NSURLUbiquitousItemUploadingErrorKey, str)
        self.assertIsInstance(
            Foundation.NSURLUbiquitousItemDownloadingStatusNotDownloaded, str
        )
        self.assertIsInstance(
            Foundation.NSURLUbiquitousItemDownloadingStatusDownloaded, str
        )
        self.assertIsInstance(
            Foundation.NSURLUbiquitousItemDownloadingStatusCurrent, str
        )

    @min_os_level("10.10")
    def testConstants10_10(self):
        self.assertIsInstance(Foundation.NSURLGenerationIdentifierKey, str)
        self.assertIsInstance(Foundation.NSURLDocumentIdentifierKey, str)
        self.assertIsInstance(Foundation.NSURLAddedToDirectoryDateKey, str)
        self.assertIsInstance(Foundation.NSURLQuarantinePropertiesKey, str)
        self.assertIsInstance(Foundation.NSURLThumbnailDictionaryKey, str)
        self.assertIsInstance(Foundation.NSURLThumbnailKey, str)
        self.assertIsInstance(Foundation.NSThumbnail1024x1024SizeKey, str)
        self.assertIsInstance(Foundation.NSURLUbiquitousItemDownloadRequestedKey, str)
        self.assertIsInstance(
            Foundation.NSURLUbiquitousItemContainerDisplayNameKey, str
        )

    @min_os_level("10.11")
    def testConstants10_11(self):
        self.assertIsInstance(Foundation.NSURLIsApplicationKey, str)
        self.assertIsInstance(Foundation.NSURLApplicationIsScriptableKey, str)

    @min_os_level("10.12")
    def testConstants10_12(self):
        self.assertIsInstance(Foundation.NSURLVolumeIsEncryptedKey, str)
        self.assertIsInstance(Foundation.NSURLVolumeIsRootFileSystemKey, str)
        self.assertIsInstance(Foundation.NSURLVolumeSupportsCompressionKey, str)
        self.assertIsInstance(Foundation.NSURLVolumeSupportsFileCloningKey, str)
        self.assertIsInstance(Foundation.NSURLVolumeSupportsSwapRenamingKey, str)
        self.assertIsInstance(Foundation.NSURLVolumeSupportsExclusiveRenamingKey, str)
        self.assertIsInstance(Foundation.NSURLCanonicalPathKey, str)
        self.assertIsInstance(Foundation.NSURLUbiquitousItemIsSharedKey, str)
        self.assertIsInstance(
            Foundation.NSURLUbiquitousSharedItemCurrentUserRoleKey, str
        )
        self.assertIsInstance(
            Foundation.NSURLUbiquitousSharedItemCurrentUserPermissionsKey, str
        )
        self.assertIsInstance(
            Foundation.NSURLUbiquitousSharedItemOwnerNameComponentsKey, str
        )
        self.assertIsInstance(
            Foundation.NSURLUbiquitousSharedItemMostRecentEditorNameComponentsKey, str
        )
        self.assertIsInstance(Foundation.NSURLUbiquitousSharedItemRoleOwner, str)
        self.assertIsInstance(Foundation.NSURLUbiquitousSharedItemRoleParticipant, str)
        self.assertIsInstance(
            Foundation.NSURLUbiquitousSharedItemPermissionsReadOnly, str
        )
        self.assertIsInstance(
            Foundation.NSURLUbiquitousSharedItemPermissionsReadWrite, str
        )

    @min_os_level("10.13")
    def testConstants10_13(self):
        self.assertIsInstance(Foundation.NSURLVolumeSupportsImmutableFilesKey, str)
        self.assertIsInstance(Foundation.NSURLVolumeSupportsAccessPermissionsKey, str)
        self.assertIsInstance(
            Foundation.NSURLVolumeAvailableCapacityForImportantUsageKey, str
        )
        self.assertIsInstance(
            Foundation.NSURLVolumeAvailableCapacityForOpportunisticUsageKey, str
        )

    @min_os_level("10.16")
    def testConstants10_16(self):
        self.assertIsInstance(Foundation.NSURLContentTypeKey, str)

        self.assertIsInstance(Foundation.NSURLFileContentIdentifierKey, str)
        self.assertIsInstance(Foundation.NSURLMayShareFileContentKey, str)
        self.assertIsInstance(Foundation.NSURLMayHaveExtendedAttributesKey, str)
        self.assertIsInstance(Foundation.NSURLIsPurgeableKey, str)
        self.assertIsInstance(Foundation.NSURLIsSparseKey, str)
        self.assertIsInstance(Foundation.NSURLVolumeSupportsFileProtectionKey, str)

        self.assertIsInstance(Foundation.NSURLFileProtectionKey, str)

    @min_os_level("10.6")
    def testMethods10_6(self):
        self.assertArgIsBOOL(
            Foundation.NSURL.URLByAppendingPathComponent_isDirectory_, 1
        )

        self.assertResultIsBOOL(Foundation.NSURL.getResourceValue_forKey_error_)
        self.assertArgIsOut(Foundation.NSURL.getResourceValue_forKey_error_, 0)
        self.assertArgIsOut(Foundation.NSURL.getResourceValue_forKey_error_, 2)
        self.assertArgIsOut(Foundation.NSURL.resourceValuesForKeys_error_, 1)
        self.assertResultIsBOOL(Foundation.NSURL.setResourceValue_forKey_error_)
        self.assertArgIsOut(Foundation.NSURL.setResourceValue_forKey_error_, 2)
        self.assertResultIsBOOL(Foundation.NSURL.setResourceValues_error_)
        self.assertArgIsOut(Foundation.NSURL.setResourceValues_error_, 1)
        self.assertResultIsBOOL(
            Foundation.NSURL.checkResourceIsReachableAndReturnError_
        )
        self.assertArgIsOut(Foundation.NSURL.checkResourceIsReachableAndReturnError_, 0)
        self.assertResultIsBOOL(Foundation.NSURL.isFileReferenceURL)

        self.assertArgIsOut(
            Foundation.NSURL.bookmarkDataWithOptions_includingResourceValuesForKeys_relativeToURL_error_,  # noqa: B950
            3,
        )
        self.assertArgHasType(
            Foundation.NSURL.initByResolvingBookmarkData_options_relativeToURL_bookmarkDataIsStale_error_,  # noqa: B950
            3,
            b"o^" + objc._C_NSBOOL,
        )
        self.assertArgIsOut(
            Foundation.NSURL.initByResolvingBookmarkData_options_relativeToURL_bookmarkDataIsStale_error_,  # noqa: B950
            4,
        )
        self.assertArgHasType(
            Foundation.NSURL.URLByResolvingBookmarkData_options_relativeToURL_bookmarkDataIsStale_error_,  # noqa: B950
            3,
            b"o^" + objc._C_NSBOOL,
        )
        self.assertArgIsOut(
            Foundation.NSURL.URLByResolvingBookmarkData_options_relativeToURL_bookmarkDataIsStale_error_,  # noqa: B950
            4,
        )
        self.assertResultIsBOOL(Foundation.NSURL.writeBookmarkData_toURL_options_error_)
        self.assertArgIsOut(Foundation.NSURL.writeBookmarkData_toURL_options_error_, 3)
        self.assertArgIsOut(Foundation.NSURL.bookmarkDataWithContentsOfURL_error_, 1)
