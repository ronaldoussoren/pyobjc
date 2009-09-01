from Foundation import *
from PyObjCTools.TestSupport import *


class TestNSURL (TestCase):
    def testMethods(self):
        self.failUnlessArgIsBOOL(NSURL.initFileURLWithPath_isDirectory_, 1)
        self.failUnlessArgIsBOOL(NSURL.fileURLWithPath_isDirectory_, 1)

        self.failUnlessArgIsBOOL(NSURL.resourceDataUsingCache_, 0)
        self.failUnlessArgIsBOOL(NSURL.loadResourceDataNotifyingClient_usingCache_, 1)
        self.failUnlessResultIsBOOL(NSURL.setResourceData_)
        self.failUnlessResultIsBOOL(NSURL.setProperty_forKey_)
        self.failUnlessArgIsBOOL(NSURL.URLHandleUsingCache_, 0)

    @min_os_level('10.6')
    def testConstants10_6(self):
        self.failUnlessEqual(NSURLBookmarkCreationPreferFileIDResolution, ( 1 << 8 ))
        self.failUnlessEqual(NSURLBookmarkCreationMinimalBookmark, ( 1 << 9 ))
        self.failUnlessEqual(NSURLBookmarkCreationSuitableForBookmarkFile, ( 1 << 10 ))
        self.failUnlessEqual(NSURLBookmarkResolutionWithoutUI, ( 1 << 8 ))
        self.failUnlessEqual(NSURLBookmarkResolutionWithoutMounting, ( 1 << 9 ))

        self.failUnlessIsInstance(NSURLNameKey, unicode)
        self.failUnlessIsInstance(NSURLLocalizedNameKey, unicode)
        self.failUnlessIsInstance(NSURLIsRegularFileKey, unicode)
        self.failUnlessIsInstance(NSURLIsDirectoryKey, unicode)
        self.failUnlessIsInstance(NSURLIsSymbolicLinkKey, unicode)
        self.failUnlessIsInstance(NSURLIsVolumeKey, unicode)
        self.failUnlessIsInstance(NSURLIsPackageKey, unicode)
        self.failUnlessIsInstance(NSURLIsSystemImmutableKey, unicode)
        self.failUnlessIsInstance(NSURLIsUserImmutableKey, unicode)
        self.failUnlessIsInstance(NSURLIsHiddenKey, unicode)
        self.failUnlessIsInstance(NSURLHasHiddenExtensionKey, unicode)
        self.failUnlessIsInstance(NSURLCreationDateKey, unicode)
        self.failUnlessIsInstance(NSURLContentAccessDateKey, unicode)
        self.failUnlessIsInstance(NSURLContentModificationDateKey, unicode)
        self.failUnlessIsInstance(NSURLAttributeModificationDateKey, unicode)
        self.failUnlessIsInstance(NSURLLinkCountKey, unicode)
        self.failUnlessIsInstance(NSURLParentDirectoryURLKey, unicode)
        self.failUnlessIsInstance(NSURLVolumeURLKey, unicode)
        self.failUnlessIsInstance(NSURLTypeIdentifierKey, unicode)
        self.failUnlessIsInstance(NSURLLocalizedTypeDescriptionKey, unicode)
        self.failUnlessIsInstance(NSURLLabelNumberKey, unicode)
        self.failUnlessIsInstance(NSURLLabelColorKey, unicode)
        self.failUnlessIsInstance(NSURLLocalizedLabelKey, unicode)
        self.failUnlessIsInstance(NSURLEffectiveIconKey, unicode)
        self.failUnlessIsInstance(NSURLCustomIconKey, unicode)
        self.failUnlessIsInstance(NSURLFileSizeKey, unicode)
        self.failUnlessIsInstance(NSURLFileAllocatedSizeKey, unicode)
        self.failUnlessIsInstance(NSURLIsAliasFileKey, unicode)
        self.failUnlessIsInstance(NSURLVolumeLocalizedFormatDescriptionKey, unicode)
        self.failUnlessIsInstance(NSURLVolumeTotalCapacityKey, unicode)
        self.failUnlessIsInstance(NSURLVolumeAvailableCapacityKey, unicode)
        self.failUnlessIsInstance(NSURLVolumeResourceCountKey, unicode)

    @min_os_level('10.6')
    @expectedFailure
    def testConstants10_6_notpresent(self):
        self.failUnlessIsInstance(NSURLVolumeSupportsPersistentIDsKey, unicode)
        self.failUnlessIsInstance(NSURLVolumeSupportsSymbolicLinksKey, unicode)
        self.failUnlessIsInstance(NSURLVolumeSupportsHardLinksKey, unicode)
        self.failUnlessIsInstance(NSURLVolumeSupportsJournalingKey, unicode)
        self.failUnlessIsInstance(NSURLVolumeIsJournalingKey, unicode)
        self.failUnlessIsInstance(NSURLVolumeSupportsSparseFilesKey, unicode)
        self.failUnlessIsInstance(NSURLVolumeSupportsZeroRunsKey, unicode)
        self.failUnlessIsInstance(NSURLVolumeSupportsCaseSensitiveNamesKey, unicode)
        self.failUnlessIsInstance(NSURLVolumeSupportsCasePreservedNamesKey, unicode)


    @min_os_level('10.6')
    def testMethods10_6(self):
        self.failUnlessResultIsBOOL(NSURL.getResourceValue_forKey_error_)
        self.failUnlessArgIsOut(NSURL.getResourceValue_forKey_error_, 0)
        self.failUnlessArgIsOut(NSURL.getResourceValue_forKey_error_, 2)
        self.failUnlessArgIsOut(NSURL.resourceValuesForKeys_error_, 1)
        self.failUnlessResultIsBOOL(NSURL.setResourceValue_forKey_error_)
        self.failUnlessArgIsOut(NSURL.setResourceValue_forKey_error_, 2)
        self.failUnlessResultIsBOOL(NSURL.setResourceValues_error_)
        self.failUnlessArgIsOut(NSURL.setResourceValues_error_, 1)
        self.failUnlessResultIsBOOL(NSURL.checkResourceIsReachableAndReturnError_)
        self.failUnlessArgIsOut(NSURL.checkResourceIsReachableAndReturnError_, 0)
        self.failUnlessResultIsBOOL(NSURL.isFileReferenceURL)

        self.failUnlessArgIsOut(NSURL.bookmarkDataWithOptions_includingResourceValuesForKeys_relativeToURL_error_, 3)
        self.failUnlessArgHasType(NSURL.initByResolvingBookmarkData_options_relativeToURL_bookmarkDataIsStale_error_, 3, 'o^' + objc._C_NSBOOL)
        self.failUnlessArgIsOut(NSURL.initByResolvingBookmarkData_options_relativeToURL_bookmarkDataIsStale_error_, 4)
        self.failUnlessArgHasType(NSURL.URLByResolvingBookmarkData_options_relativeToURL_bookmarkDataIsStale_error_, 3, 'o^' + objc._C_NSBOOL)
        self.failUnlessArgIsOut(NSURL.URLByResolvingBookmarkData_options_relativeToURL_bookmarkDataIsStale_error_, 4)
        self.failUnlessResultIsBOOL(NSURL.writeBookmarkData_toURL_options_error_)
        self.failUnlessArgIsOut(NSURL.writeBookmarkData_toURL_options_error_, 3)
        self.failUnlessArgIsOut(NSURL.bookmarkDataWithContentsOfURL_error_, 1)

if __name__ == "__main__":
    main()
