from Foundation import *
from PyObjCTools.TestSupport import *


class TestNSURL (TestCase):
    def testMethods(self):
        self.assertArgIsBOOL(NSURL.initFileURLWithPath_isDirectory_, 1)
        self.assertArgIsBOOL(NSURL.fileURLWithPath_isDirectory_, 1)

        self.assertArgIsBOOL(NSURL.resourceDataUsingCache_, 0)
        self.assertArgIsBOOL(NSURL.loadResourceDataNotifyingClient_usingCache_, 1)
        self.assertResultIsBOOL(NSURL.setResourceData_)
        self.assertResultIsBOOL(NSURL.setProperty_forKey_)
        self.assertArgIsBOOL(NSURL.URLHandleUsingCache_, 0)

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


    @min_os_level('10.6')
    def testMethods10_6(self):
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
