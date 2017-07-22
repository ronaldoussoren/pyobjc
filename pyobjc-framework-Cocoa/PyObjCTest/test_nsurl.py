from Foundation import *
from PyObjCTools.TestSupport import *


class TestNSURL (TestCase):
    def testMethods(self):
        self.assertArgIsBOOL(NSURL.initFileURLWithPath_isDirectory_, 1)
        self.assertArgIsBOOL(NSURL.fileURLWithPath_isDirectory_, 1)
        self.assertResultIsBOOL(NSURL.isFileURL)

        self.assertArgIsBOOL(NSURL.resourceDataUsingCache_, 0)
        self.assertArgIsBOOL(NSURL.loadResourceDataNotifyingClient_usingCache_, 1)
        self.assertResultIsBOOL(NSURL.setResourceData_)
        self.assertResultIsBOOL(NSURL.setProperty_forKey_)
        self.assertArgIsBOOL(NSURL.URLHandleUsingCache_, 0)

    @min_os_level('10.7')
    def testMethods10_7(self):
        self.assertResultIsBOOL(NSURL.startAccessingSecurityScopedResource)

    @min_os_level('10.9')
    def testMethods10_9(self):
        self.assertArgIsIn(NSURL.initFileURLWithFileSystemRepresentation_isDirectory_relativeToURL_, 0)
        self.assertArgIsBOOL(NSURL.initFileURLWithFileSystemRepresentation_isDirectory_relativeToURL_, 1)

        self.assertArgIsIn(NSURL.fileURLWithFileSystemRepresentation_isDirectory_relativeToURL_, 0)
        self.assertArgIsBOOL(NSURL.fileURLWithFileSystemRepresentation_isDirectory_relativeToURL_, 1)

        self.assertResultIsBOOL(NSURL.getFileSystemRepresentation_maxLength_)
        self.assertArgIsOut(NSURL.getFileSystemRepresentation_maxLength_, 0)
        self.assertArgSizeInArg(NSURL.getFileSystemRepresentation_maxLength_, 0, 1)

        self.assertArgIsBOOL(NSURLComponents.initWithURL_resolvingAgainstBaseURL_, 1)
        self.assertArgIsBOOL(NSURLComponents.componentsWithURL_resolvingAgainstBaseURL_, 1)

    @min_os_level('10.10')
    def testMethods10_10(self):
        self.assertArgIsOut(NSURL.URLByResolvingAliasFileAtURL_options_error_, 2)

        self.assertResultIsBOOL(NSURL.getPromisedItemResourceValue_forKey_error_)
        self.assertArgIsOut(NSURL.getPromisedItemResourceValue_forKey_error_, 2)
        self.assertArgIsOut(NSURL.promisedItemResourceValuesForKeys_error_, 1)

        self.assertResultIsBOOL(NSURL.checkPromisedItemIsReachableAndReturnError_)
        self.assertArgIsOut(NSURL.checkPromisedItemIsReachableAndReturnError_, 0)

    @min_os_level('10.11')
    def testMethods10_11(self):
        self.assertArgIsBOOL(NSURL.initFileURLWithPath_isDirectory_relativeToURL_, 1)
        self.assertArgIsBOOL(NSURL.fileURLWithPath_isDirectory_relativeToURL_, 1)
        self.assertResultIsBOOL(NSURL.hasDirectoryPath)

    def testConstants(self):
        self.assertIsInstance(NSURLFileScheme, unicode)

    @min_os_level('10.6')
    def testConstants10_6(self):
        self.assertEqual(NSURLBookmarkCreationPreferFileIDResolution, ( 1 << 8 ))
        self.assertEqual(NSURLBookmarkCreationMinimalBookmark, ( 1 << 9 ))
        self.assertEqual(NSURLBookmarkCreationSuitableForBookmarkFile, ( 1 << 10 ))
        self.assertEqual(NSURLBookmarkResolutionWithoutUI, ( 1 << 8 ))
        self.assertEqual(NSURLBookmarkResolutionWithoutMounting, ( 1 << 9 ))

        self.assertIsInstance(NSURLNameKey, unicode)
        self.assertIsInstance(NSURLLocalizedNameKey, unicode)
        self.assertIsInstance(NSURLIsRegularFileKey, unicode)
        self.assertIsInstance(NSURLIsDirectoryKey, unicode)
        self.assertIsInstance(NSURLIsSymbolicLinkKey, unicode)
        self.assertIsInstance(NSURLIsVolumeKey, unicode)
        self.assertIsInstance(NSURLIsPackageKey, unicode)
        self.assertIsInstance(NSURLIsSystemImmutableKey, unicode)
        self.assertIsInstance(NSURLIsUserImmutableKey, unicode)
        self.assertIsInstance(NSURLIsHiddenKey, unicode)
        self.assertIsInstance(NSURLHasHiddenExtensionKey, unicode)
        self.assertIsInstance(NSURLCreationDateKey, unicode)
        self.assertIsInstance(NSURLContentAccessDateKey, unicode)
        self.assertIsInstance(NSURLContentModificationDateKey, unicode)
        self.assertIsInstance(NSURLAttributeModificationDateKey, unicode)
        self.assertIsInstance(NSURLLinkCountKey, unicode)
        self.assertIsInstance(NSURLParentDirectoryURLKey, unicode)
        self.assertIsInstance(NSURLVolumeURLKey, unicode)
        self.assertIsInstance(NSURLTypeIdentifierKey, unicode)
        self.assertIsInstance(NSURLLocalizedTypeDescriptionKey, unicode)
        self.assertIsInstance(NSURLLabelNumberKey, unicode)
        self.assertIsInstance(NSURLLabelColorKey, unicode)
        self.assertIsInstance(NSURLLocalizedLabelKey, unicode)
        self.assertIsInstance(NSURLEffectiveIconKey, unicode)
        self.assertIsInstance(NSURLCustomIconKey, unicode)
        self.assertIsInstance(NSURLFileSizeKey, unicode)
        self.assertIsInstance(NSURLFileAllocatedSizeKey, unicode)
        self.assertIsInstance(NSURLIsAliasFileKey, unicode)
        self.assertIsInstance(NSURLVolumeLocalizedFormatDescriptionKey, unicode)
        self.assertIsInstance(NSURLVolumeTotalCapacityKey, unicode)
        self.assertIsInstance(NSURLVolumeAvailableCapacityKey, unicode)
        self.assertIsInstance(NSURLVolumeResourceCountKey, unicode)

    @min_os_level('10.6')
    def testConstants10_6_2(self):
        self.assertIsInstance(NSURLVolumeSupportsPersistentIDsKey, unicode)
        self.assertIsInstance(NSURLVolumeSupportsSymbolicLinksKey, unicode)
        self.assertIsInstance(NSURLVolumeSupportsHardLinksKey, unicode)
        self.assertIsInstance(NSURLVolumeSupportsJournalingKey, unicode)
        self.assertIsInstance(NSURLVolumeIsJournalingKey, unicode)
        self.assertIsInstance(NSURLVolumeSupportsSparseFilesKey, unicode)
        self.assertIsInstance(NSURLVolumeSupportsZeroRunsKey, unicode)
        self.assertIsInstance(NSURLVolumeSupportsCaseSensitiveNamesKey, unicode)
        self.assertIsInstance(NSURLVolumeSupportsCasePreservedNamesKey, unicode)

    @min_os_level('10.7')
    def testConstants10_7(self):
        self.assertEqual(NSURLBookmarkCreationWithSecurityScope, ( 1 << 11 ))
        self.assertEqual(NSURLBookmarkCreationSecurityScopeAllowOnlyReadAccess, ( 1 << 12 ))
        self.assertEqual(NSURLBookmarkResolutionWithSecurityScope, ( 1 << 10 ))

        self.assertIsInstance(NSURLKeysOfUnsetValuesKey, unicode)

        self.assertIsInstance(NSURLFileResourceIdentifierKey, unicode)
        self.assertIsInstance(NSURLVolumeIdentifierKey, unicode)
        self.assertIsInstance(NSURLPreferredIOBlockSizeKey, unicode)
        self.assertIsInstance(NSURLIsReadableKey, unicode)
        self.assertIsInstance(NSURLIsWritableKey, unicode)
        self.assertIsInstance(NSURLIsExecutableKey, unicode)
        self.assertIsInstance(NSURLIsMountTriggerKey, unicode)
        self.assertIsInstance(NSURLFileSecurityKey, unicode)
        self.assertIsInstance(NSURLFileResourceTypeKey, unicode)
        self.assertIsInstance(NSURLFileResourceTypeNamedPipe, unicode)
        self.assertIsInstance(NSURLFileResourceTypeCharacterSpecial, unicode)
        self.assertIsInstance(NSURLFileResourceTypeDirectory, unicode)
        self.assertIsInstance(NSURLFileResourceTypeBlockSpecial, unicode)
        self.assertIsInstance(NSURLFileResourceTypeRegular, unicode)
        self.assertIsInstance(NSURLFileResourceTypeSymbolicLink, unicode)
        self.assertIsInstance(NSURLFileResourceTypeSocket, unicode)
        self.assertIsInstance(NSURLFileResourceTypeUnknown, unicode)
        self.assertIsInstance(NSURLTotalFileSizeKey, unicode)
        self.assertIsInstance(NSURLTotalFileAllocatedSizeKey, unicode)
        self.assertIsInstance(NSURLVolumeSupportsRootDirectoryDatesKey, unicode)
        self.assertIsInstance(NSURLVolumeSupportsVolumeSizesKey, unicode)
        self.assertIsInstance(NSURLVolumeSupportsRenamingKey, unicode)
        self.assertIsInstance(NSURLVolumeSupportsAdvisoryFileLockingKey, unicode)
        self.assertIsInstance(NSURLVolumeSupportsExtendedSecurityKey, unicode)
        self.assertIsInstance(NSURLVolumeIsBrowsableKey, unicode)
        self.assertIsInstance(NSURLVolumeMaximumFileSizeKey, unicode)
        self.assertIsInstance(NSURLVolumeIsEjectableKey, unicode)
        self.assertIsInstance(NSURLVolumeIsRemovableKey, unicode)
        self.assertIsInstance(NSURLVolumeIsInternalKey, unicode)
        self.assertIsInstance(NSURLVolumeIsAutomountedKey, unicode)
        self.assertIsInstance(NSURLVolumeIsLocalKey, unicode)
        self.assertIsInstance(NSURLVolumeIsReadOnlyKey, unicode)
        self.assertIsInstance(NSURLVolumeCreationDateKey, unicode)
        self.assertIsInstance(NSURLVolumeURLForRemountingKey, unicode)
        self.assertIsInstance(NSURLVolumeUUIDStringKey, unicode)
        self.assertIsInstance(NSURLVolumeNameKey, unicode)
        self.assertIsInstance(NSURLVolumeLocalizedNameKey, unicode)
        self.assertIsInstance(NSURLIsUbiquitousItemKey, unicode)
        self.assertIsInstance(NSURLUbiquitousItemHasUnresolvedConflictsKey, unicode)
        self.assertIsInstance(NSURLUbiquitousItemIsDownloadedKey, unicode)
        self.assertIsInstance(NSURLUbiquitousItemIsDownloadingKey, unicode)
        self.assertIsInstance(NSURLUbiquitousItemIsUploadedKey, unicode)
        self.assertIsInstance(NSURLUbiquitousItemIsUploadingKey, unicode)
        self.assertIsInstance(NSURLUbiquitousItemPercentDownloadedKey, unicode)
        self.assertIsInstance(NSURLUbiquitousItemPercentUploadedKey, unicode)

    @min_os_level('10.8')
    def testConstants10_8(self):
        self.assertIsInstance(NSURLIsExcludedFromBackupKey, unicode)
        self.assertIsInstance(NSURLPathKey, unicode)

    @min_os_level('10.9')
    def testConstants10_9(self):
        self.assertIsInstance(NSURLTagNamesKey, unicode)
        self.assertIsInstance(NSURLUbiquitousItemDownloadingStatusKey, unicode)
        self.assertIsInstance(NSURLUbiquitousItemDownloadingErrorKey, unicode)
        self.assertIsInstance(NSURLUbiquitousItemUploadingErrorKey, unicode)
        self.assertIsInstance(NSURLUbiquitousItemDownloadingStatusNotDownloaded, unicode)
        self.assertIsInstance(NSURLUbiquitousItemDownloadingStatusDownloaded, unicode)
        self.assertIsInstance(NSURLUbiquitousItemDownloadingStatusCurrent, unicode)

    @min_os_level('10.10')
    def testConstants10_10(self):
        self.assertIsInstance(NSURLGenerationIdentifierKey, unicode)
        self.assertIsInstance(NSURLDocumentIdentifierKey, unicode)
        self.assertIsInstance(NSURLAddedToDirectoryDateKey, unicode)
        self.assertIsInstance(NSURLQuarantinePropertiesKey, unicode)
        self.assertIsInstance(NSURLThumbnailDictionaryKey, unicode)
        self.assertIsInstance(NSURLThumbnailKey, unicode)
        self.assertIsInstance(NSThumbnail1024x1024SizeKey, unicode)
        self.assertIsInstance(NSURLUbiquitousItemDownloadRequestedKey, unicode)
        self.assertIsInstance(NSURLUbiquitousItemContainerDisplayNameKey, unicode)

    @min_os_level('10.11')
    def testConstants10_11(self):
        self.assertIsInstance(NSURLIsApplicationKey, unicode)
        self.assertIsInstance(NSURLApplicationIsScriptableKey, unicode)

    @min_os_level('10.12')
    def testConstants10_12(self):
        self.assertIsInstance(NSURLVolumeIsEncryptedKey, unicode)
        self.assertIsInstance(NSURLVolumeIsRootFileSystemKey, unicode)
        self.assertIsInstance(NSURLVolumeSupportsCompressionKey, unicode)
        self.assertIsInstance(NSURLVolumeSupportsFileCloningKey, unicode)
        self.assertIsInstance(NSURLVolumeSupportsSwapRenamingKey, unicode)
        self.assertIsInstance(NSURLVolumeSupportsExclusiveRenamingKey, unicode)
        self.assertIsInstance(NSURLCanonicalPathKey, unicode)
        self.assertIsInstance(NSURLUbiquitousItemIsSharedKey, unicode)
        self.assertIsInstance(NSURLUbiquitousSharedItemCurrentUserRoleKey, unicode)
        self.assertIsInstance(NSURLUbiquitousSharedItemCurrentUserPermissionsKey, unicode)
        self.assertIsInstance(NSURLUbiquitousSharedItemOwnerNameComponentsKey, unicode)
        self.assertIsInstance(NSURLUbiquitousSharedItemMostRecentEditorNameComponentsKey, unicode)
        self.assertIsInstance(NSURLUbiquitousSharedItemRoleOwner, unicode)
        self.assertIsInstance(NSURLUbiquitousSharedItemRoleParticipant, unicode)
        self.assertIsInstance(NSURLUbiquitousSharedItemPermissionsReadOnly, unicode)
        self.assertIsInstance(NSURLUbiquitousSharedItemPermissionsReadWrite, unicode)

    @min_os_level('10.13')
    def testConstants10_13(self):
        self.assertIsInstance(NSURLVolumeSupportsImmutableFilesKey, unicode)
        self.assertIsInstance(NSURLVolumeSupportsAccessPermissionsKey, unicode)
        self.assertIsInstance(NSURLVolumeAvailableCapacityForImportantUsageKey, unicode)
        self.assertIsInstance(NSURLVolumeAvailableCapacityForOpportunisticUsageKey, unicode)

    @min_os_level('10.6')
    def testMethods10_6(self):
        self.assertArgIsBOOL(NSURL.URLByAppendingPathComponent_isDirectory_, 1)

        self.assertResultIsBOOL(NSURL.getResourceValue_forKey_error_)
        self.assertArgIsOut(NSURL.getResourceValue_forKey_error_, 0)
        self.assertArgIsOut(NSURL.getResourceValue_forKey_error_, 2)
        self.assertArgIsOut(NSURL.resourceValuesForKeys_error_, 1)
        self.assertResultIsBOOL(NSURL.setResourceValue_forKey_error_)
        self.assertArgIsOut(NSURL.setResourceValue_forKey_error_, 2)
        self.assertResultIsBOOL(NSURL.setResourceValues_error_)
        self.assertArgIsOut(NSURL.setResourceValues_error_, 1)
        self.assertResultIsBOOL(NSURL.checkResourceIsReachableAndReturnError_)
        self.assertArgIsOut(NSURL.checkResourceIsReachableAndReturnError_, 0)
        self.assertResultIsBOOL(NSURL.isFileReferenceURL)

        self.assertArgIsOut(NSURL.bookmarkDataWithOptions_includingResourceValuesForKeys_relativeToURL_error_, 3)
        self.assertArgHasType(NSURL.initByResolvingBookmarkData_options_relativeToURL_bookmarkDataIsStale_error_, 3, b'o^' + objc._C_NSBOOL)
        self.assertArgIsOut(NSURL.initByResolvingBookmarkData_options_relativeToURL_bookmarkDataIsStale_error_, 4)
        self.assertArgHasType(NSURL.URLByResolvingBookmarkData_options_relativeToURL_bookmarkDataIsStale_error_, 3, b'o^' + objc._C_NSBOOL)
        self.assertArgIsOut(NSURL.URLByResolvingBookmarkData_options_relativeToURL_bookmarkDataIsStale_error_, 4)
        self.assertResultIsBOOL(NSURL.writeBookmarkData_toURL_options_error_)
        self.assertArgIsOut(NSURL.writeBookmarkData_toURL_options_error_, 3)
        self.assertArgIsOut(NSURL.bookmarkDataWithContentsOfURL_error_, 1)

if __name__ == "__main__":
    main()
