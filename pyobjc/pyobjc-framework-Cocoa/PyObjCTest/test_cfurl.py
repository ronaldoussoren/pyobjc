from PyObjCTools.TestSupport import *
import array
from CoreFoundation import *
import os
from Foundation import NSURL


class TestURL (TestCase):
    def testTypes(self):
        self.failUnless(CFURLRef is NSURL)

    def testTypeID(self):
        val = CFURLGetTypeID()
        self.failUnlessIsInstance(val, (int, long))

    def testCreateWithBytes(self):
        url = "http://www.omroep.nl/"

        ref = CFURLCreateWithBytes(None, url, len(url), kCFStringEncodingUTF8, None)
        self.failUnlessIsInstance(ref, CFURLRef)

        strval =  CFURLGetString(ref)
        self.failUnlessEqual(strval, unicode(url, "utf-8"))

        ref2 = CFURLCreateWithBytes(None, url, len(url), kCFStringEncodingUTF8, ref)
        self.failUnlessIsInstance(ref2, CFURLRef)

        a = array.array('c', 'http://www.nu.nl/')
        ref3 = CFURLCreateWithBytes(None, a, len(a), kCFStringEncodingUTF8, None)
        self.failUnlessIsInstance(ref3, CFURLRef)

        # Explictely test for unicode's buffer madness.
        self.failUnlessRaises((ValueError, TypeError), CFURLCreateWithBytes, None, unicode(url), len(url), kCFStringEncodingUTF8, None)

    def testCreateData(self):
        url = "http://www.omroep.nl/ blank"

        ref = CFURLCreateWithBytes(None, url, len(url), kCFStringEncodingUTF8, None)
        self.failUnlessIsInstance(ref, CFURLRef)

        data = CFURLCreateData(None, ref, kCFStringEncodingUTF8, False)
        self.failUnlessIsInstance(data, CFDataRef)
        val = CFDataGetBytes(data, (0, CFDataGetLength(data)), None)
        self.assertEquals(val, url.replace(' ', '%20'))

        data = CFURLCreateData(None, ref, kCFStringEncodingUTF8, True)
        self.failUnlessIsInstance(data, CFDataRef)
        val = CFDataGetBytes(data, (0, CFDataGetLength(data)), None)
        self.assertEquals(val, url.replace(' ', '%20'))

    def testCreateWithString(self):
        url = u"http://www.omroep.nl/"

        ref = CFURLCreateWithString(None, url, None)
        self.failUnlessIsInstance(ref, CFURLRef)

        strval =  CFURLGetString(ref)
        self.failUnlessEqual(strval, url)

        ref2 = CFURLCreateWithString(None, url, ref)
        self.failUnlessIsInstance(ref2, CFURLRef)

    def testCreateAbsolute(self):
        url = u"http://www.omroep.nl/sport/"
        baseref = CFURLCreateWithString(None, url, None)

        self.failUnlessArgHasType(CFURLCreateAbsoluteURLWithBytes, 1, 'n^v')
        self.failUnlessArgSizeInArg(CFURLCreateAbsoluteURLWithBytes, 1, 2)
        ref = CFURLCreateAbsoluteURLWithBytes(None, "socker", len("socker"), kCFStringEncodingUTF8, baseref, True)
        self.failUnlessIsInstance(ref, CFURLRef)

        strval =  CFURLGetString(ref)
        self.failUnlessEqual(strval, u"http://www.omroep.nl/sport/socker")

        relpath = "../../../dummy"
        ref = CFURLCreateAbsoluteURLWithBytes(None, relpath, len(relpath), kCFStringEncodingUTF8, baseref, True)
        self.failUnlessIsInstance(ref, CFURLRef)
        strval =  CFURLGetString(ref)
        self.failUnlessEqual(strval, u"http://www.omroep.nl/dummy")

        relpath = "../../../dummy"
        ref = CFURLCreateAbsoluteURLWithBytes(None, relpath, len(relpath), kCFStringEncodingUTF8, baseref, False)
        self.failUnlessIsInstance(ref, CFURLRef)
        strval =  CFURLGetString(ref)
        self.failUnlessEqual(strval, u"http://www.omroep.nl/../../dummy")


    def testCopyAbs(self):
        # CFURLCopyAbsoluteURL
        base = CFURLCreateWithString(None, u"http://www.omroep.nl/", None)
        self.failUnlessIsInstance(base, CFURLRef)

        ref = CFURLCreateWithString(None, u"/sport", base)
        self.failUnlessIsInstance(ref, CFURLRef)

        self.failUnless( CFURLGetString(ref) == u"/sport" )

        abs = CFURLCopyAbsoluteURL(ref)
        self.failUnlessIsInstance(abs, CFURLRef)
        self.failUnless( CFURLGetString(abs) == u"http://www.omroep.nl/sport" )

    def testPaths(self):
        url = CFURLCreateWithFileSystemPath(None,
                u"/tmp/", kCFURLPOSIXPathStyle, True)
        self.failUnlessIsInstance(url, CFURLRef)
        self.failUnless(CFURLHasDirectoryPath(url))

        url = CFURLCreateWithFileSystemPath(None,
                u"/etc/hosts", kCFURLPOSIXPathStyle, False)
        self.failUnlessIsInstance(url, CFURLRef)
        self.failIf(CFURLHasDirectoryPath(url))

        p = os.path.expanduser('~')
        self.failUnlessArgHasType(CFURLCreateFromFileSystemRepresentation, 1, 'n^t')
        self.failUnlessArgIsNullTerminated(CFURLCreateFromFileSystemRepresentation, 1)
        url = CFURLCreateFromFileSystemRepresentation(None,
                p, len(p), True)
        self.failUnlessIsInstance(url, CFURLRef)
        self.assertRaises((ValueError, TypeError),
            CFURLCreateFromFileSystemRepresentation, None,
                u"/tmp/", 4, True)

        base = CFURLCreateWithFileSystemPath(None,
                u"/tmp", kCFURLPOSIXPathStyle, True)
        self.failUnlessIsInstance(base, CFURLRef)

        self.failUnlessArgIsBOOL(CFURLCreateWithFileSystemPathRelativeToBase, 3)
        url = CFURLCreateWithFileSystemPathRelativeToBase(None,
                u"filename", kCFURLPOSIXPathStyle, True, base)
        self.failUnlessIsInstance(url, CFURLRef)

        strval =  CFURLGetString(url)
        self.assertEquals(strval, u"filename/")


        self.failUnlessArgIsBOOL(CFURLCreateFromFileSystemRepresentationRelativeToBase, 3)
        url = CFURLCreateFromFileSystemRepresentationRelativeToBase(None,
                "filename2", 9, False, base)
        self.failUnlessIsInstance(url, CFURLRef)
        strval =  CFURLGetString(url)
        self.assertEquals(strval, u"filename2")

        ok, strval = CFURLGetFileSystemRepresentation(url, True, None, 100)
        self.failUnless(ok)

        # Unfortunately metadata doesn't allow describing what we actually need
        if '\0' in strval:
            strval = strval[:strval.index('\0')]
        self.assertEquals(strval, u"/tmp/filename2")

    def testParts(self):
        base = CFURLCreateWithString(None, u"http://www.omroep.nl/", None)
        self.failUnlessIsInstance(base, CFURLRef)

        ref = CFURLCreateWithString(None, u"/sport", base)
        self.failUnlessIsInstance(ref, CFURLRef)

        self.assertEquals(CFURLGetBaseURL(base), None)
        self.assertEquals(CFURLGetBaseURL(ref), base)
        self.assert_(CFURLCanBeDecomposed(ref) is True)

        self.assertEquals(CFURLCopyScheme(ref), u"http")
        self.assertEquals(CFURLCopyNetLocation(ref), u"www.omroep.nl")
        self.assertEquals(CFURLCopyPath(ref), u"/sport")

        path, isDir = CFURLCopyStrictPath(ref, None)
        self.assertEquals(path, u"sport")
        self.assertEquals(isDir, True)

        path = CFURLCopyFileSystemPath(ref, kCFURLPOSIXPathStyle)
        self.assertEquals(path, u"/sport")

        path = CFURLCopyFileSystemPath(ref, kCFURLPOSIXPathStyle)
        self.assertEquals(path, u"/sport")
        path = CFURLCopyFileSystemPath(ref, kCFURLWindowsPathStyle)
        self.assertEquals(path, u"\\sport")

        self.failIf(CFURLHasDirectoryPath(ref))

        v =  CFURLCopyResourceSpecifier(ref)
        self.assertEquals(v, None)

        v =  CFURLCopyHostName(ref)
        self.assertEquals(v, "www.omroep.nl")

        v =  CFURLGetPortNumber(ref)
        self.assertEquals(v, -1)

        ref = CFURLCreateWithString(None, u"https://ronald:test@www.nu.nl:42/sport/results.cgi?qs=1#anchor", None)
        v =  CFURLGetPortNumber(ref)
        self.assertEquals(v, 42)

        v = CFURLCopyResourceSpecifier(ref)
        self.assertEquals(v, u"?qs=1#anchor")

        v = CFURLCopyUserName(ref)
        self.assertEquals(v, "ronald")

        v = CFURLCopyPassword(ref)
        self.assertEquals(v, "test")

        v = CFURLCopyParameterString(ref, None)
        self.assertEquals(v, None)

        v = CFURLCopyQueryString(ref, None)
        self.assertEquals(v, "qs=1")

        v = CFURLCopyLastPathComponent(ref)
        self.assertEquals(v, "results.cgi")

        v = CFURLCopyPathExtension(ref)
        self.assertEquals(v, "cgi")

        cnt, bytes = CFURLGetBytes(ref, None, 100)
        self.assertEquals(cnt, 62)
        self.assertEquals(bytes, 
                "https://ronald:test@www.nu.nl:42/sport/results.cgi?qs=1#anchor")

        cnt, bytes = CFURLGetBytes(ref, objc.NULL, 0)
        self.assertEquals(cnt, 62)
        self.assertEquals(bytes, objc.NULL)

        rng1, rng2 = CFURLGetByteRangeForComponent(ref, kCFURLComponentHost, None)
        self.failUnlessIsInstance(rng1, CFRange)
        self.failUnlessIsInstance(rng2, CFRange)
        

    def testUpdating(self):
        base = CFURLCreateWithString(None, u"http://www.omroep.nl/sport", None)
        self.failUnlessIsInstance(base, CFURLRef)

        url = CFURLCreateCopyAppendingPathComponent(None, base, "soccer", True)
        self.failUnlessIsInstance(url, CFURLRef)

        strval =  CFURLGetString(url)
        self.assertEquals(strval, "http://www.omroep.nl/sport/soccer/")

        url = CFURLCreateCopyDeletingLastPathComponent(None, base)
        self.failUnlessIsInstance(url, CFURLRef)
        strval =  CFURLGetString(url)
        self.assertEquals(strval, "http://www.omroep.nl/")

        url = CFURLCreateCopyAppendingPathExtension(None, base, "cgi")
        self.failUnlessIsInstance(url, CFURLRef)
        strval =  CFURLGetString(url)
        self.assertEquals(strval, "http://www.omroep.nl/sport.cgi")

        url2 = CFURLCreateCopyDeletingPathExtension(None, base)
        self.failUnlessIsInstance(url2, CFURLRef)
        strval =  CFURLGetString(url2)
        self.assertEquals(strval, "http://www.omroep.nl/sport")

    def testStringEncoding(self):
        base = u"http://www.omroep.nl/sport%20en%20%73%70el"

        strval = CFURLCreateStringByReplacingPercentEscapes(None, base, objc.NULL)
        self.assertEquals(strval, "http://www.omroep.nl/sport%20en%20%73%70el")

        strval = CFURLCreateStringByReplacingPercentEscapes(None, base, "")
        self.assertEquals(strval, "http://www.omroep.nl/sport en spel")

        strval = CFURLCreateStringByReplacingPercentEscapes(None, base, " ")
        self.assertEquals(strval, "http://www.omroep.nl/sport%20en%20spel")

        strval = CFURLCreateStringByReplacingPercentEscapesUsingEncoding(None, base, "", kCFStringEncodingISOLatin1)
        self.assertEquals(strval, "http://www.omroep.nl/sport en spel")

        
        base = u"http://www.omroep.nl/sport en spel"
        strval = CFURLCreateStringByAddingPercentEscapes(None, base, "", "",
                kCFStringEncodingISOLatin1)
        self.assertEquals(strval, u"http://www.omroep.nl/sport%20en%20spel")
        strval = CFURLCreateStringByAddingPercentEscapes(None, base, " ", "s",
                kCFStringEncodingISOLatin1)
        self.assertEquals(strval, u"http://www.omroep.nl/%73port en %73pel")

    def testFSRef(self):
        ref = CFURLCreateWithFileSystemPath(None, os.getcwd(), kCFURLPOSIXPathStyle, True)
        self.failUnlessIsInstance(ref, CFURLRef)

        ok, fsref = CFURLGetFSRef(ref, None)
        self.failUnless(ok)
        self.failUnlessIsInstance(fsref, objc.FSRef)
        self.failUnlessEqual(fsref.as_pathname(), os.getcwd())

        ref2 = CFURLCreateFromFSRef(None, fsref)
        self.failUnlessEqual(ref, ref2) 

    def testConstants(self):
        self.failUnlessEqual(kCFURLPOSIXPathStyle, 0)
        self.failUnlessEqual(kCFURLHFSPathStyle, 1)
        self.failUnlessEqual(kCFURLWindowsPathStyle, 2)

        self.failUnlessEqual(kCFURLComponentScheme, 1)
        self.failUnlessEqual(kCFURLComponentNetLocation, 2)
        self.failUnlessEqual(kCFURLComponentPath, 3)
        self.failUnlessEqual(kCFURLComponentResourceSpecifier, 4)
        self.failUnlessEqual(kCFURLComponentUser, 5)
        self.failUnlessEqual(kCFURLComponentPassword, 6)
        self.failUnlessEqual(kCFURLComponentUserInfo, 7)
        self.failUnlessEqual(kCFURLComponentHost, 8)
        self.failUnlessEqual(kCFURLComponentPort, 9)
        self.failUnlessEqual(kCFURLComponentParameterString, 10)
        self.failUnlessEqual(kCFURLComponentQuery, 11)
        self.failUnlessEqual(kCFURLComponentFragment, 12)

    @min_os_level('10.6')
    def testFunctions10_6(self):
        fp = open("/tmp/pyobjc.test", "w")
        fp.close()
        try:
            baseURL = CFURLCreateWithFileSystemPath(None,
                u"/tmp/pyobjc.test", kCFURLPOSIXPathStyle, False)
            self.failUnlessIsInstance(baseURL, CFURLRef)

            self.failUnlessResultIsCFRetained(CFURLCreateFileReferenceURL)
            url, err = CFURLCreateFileReferenceURL(None, baseURL, None)
            self.failUnlessIsInstance(url, CFURLRef)
            self.failUnlessEqual(err, None)

            self.failUnlessResultIsCFRetained(CFURLCreateFilePathURL)
            url, err = CFURLCreateFilePathURL(None, baseURL, None)
            self.failUnlessIsInstance(url, CFURLRef)
            self.failUnlessEqual(err, None)

            self.failUnlessResultIsBOOL(CFURLCopyResourcePropertyForKey)
            self.failUnlessArgIsCFRetained(CFURLCopyResourcePropertyForKey, 2)
            self.failUnlessArgIsOut(CFURLCopyResourcePropertyForKey, 2)
            self.failUnlessArgIsOut(CFURLCopyResourcePropertyForKey, 3)
            ok, value, error = CFURLCopyResourcePropertyForKey(url, kCFURLNameKey, None, None)
            self.failUnless(ok)
            self.failUnlessIsInstance(value, unicode)
            self.failUnlessEqual(error, None)

            ok, value, error = CFURLCopyResourcePropertyForKey(url, kCFURLIsRegularFileKey, None, None)
            self.failUnless(ok)
            self.failUnlessIsInstance(value, bool)
            self.failUnlessEqual(error, None)


            self.failUnlessResultIsCFRetained(CFURLCreateFilePathURL)
            self.failUnlessArgIsOut(CFURLCopyResourcePropertyForKey, 2)
            values, error = CFURLCopyResourcePropertiesForKeys(url, [kCFURLNameKey, kCFURLIsRegularFileKey], None)
            self.failUnlessIsInstance(values, CFDictionaryRef)
            self.failUnlessEqual(error, None)

            CFURLClearResourcePropertyCacheForKey(url, kCFURLIsRegularFileKey)
            CFURLClearResourcePropertyCache(url)
            self.failUnlessResultIsBOOL(CFURLResourceIsReachable)
            v, err= CFURLResourceIsReachable(url, None)
            self.failUnlessIsInstance(v, bool)
            self.failUnlessEqual(err, None)

            CFURLSetTemporaryResourcePropertyForKey(url, "pyobjc.test", u"hello")
            ok, v, err = CFURLCopyResourcePropertyForKey(url, "pyobjc.test", None, None)
            self.failUnless(ok)
            self.failUnlessEqual(v, u"hello")

            ok, cur, err = CFURLCopyResourcePropertyForKey(url, kCFURLIsHiddenKey, None, None)
            self.failUnless(ok)

            ok, err = CFURLSetResourcePropertyForKey(url, kCFURLIsHiddenKey, not cur, None)
            self.failUnless(ok)

            ok, new, err = CFURLCopyResourcePropertyForKey(url, kCFURLIsHiddenKey, None, None)
            self.failUnless(ok)
            self.failUnlessEqual(new, not cur)
            self.failUnlessEqual(err, None)

            ok, err = CFURLSetResourcePropertiesForKeys(url, {kCFURLIsHiddenKey:cur}, None)
            self.failUnless(ok)
            self.failUnlessEqual(err, None)

            ok, new, err = CFURLCopyResourcePropertyForKey(url, kCFURLIsHiddenKey, None, None)
            self.failUnless(ok)
            self.failUnlessEqual(new, cur)
            self.failUnlessEqual(err, None)

            self.failUnlessResultIsCFRetained(CFURLCreateBookmarkData)
            data, err = CFURLCreateBookmarkData(None, url, kCFURLBookmarkCreationSuitableForBookmarkFile, [kCFURLNameKey, kCFURLIsHiddenKey], None, None)
            self.failUnless(err is None)
            self.failUnlessIsInstance(data, CFDataRef)

            self.failUnlessResultIsCFRetained(CFURLCreateByResolvingBookmarkData)
            u, stale, err = CFURLCreateByResolvingBookmarkData(None, data, 0, None, None, None, None)
            self.failUnlessEqual(u, url)
            self.failUnlessIsInstance(stale, bool)
            self.failIf(stale)
            self.failUnless(err is None)

            self.failUnlessResultIsCFRetained(CFURLCreateResourcePropertiesForKeysFromBookmarkData)
            v = CFURLCreateResourcePropertiesForKeysFromBookmarkData(None, [kCFURLNameKey], data)
            self.failUnlessIsInstance(v, CFDictionaryRef)

            self.failUnlessResultIsCFRetained(CFURLCreateResourcePropertyForKeyFromBookmarkData)
            v = CFURLCreateResourcePropertyForKeyFromBookmarkData(None, kCFURLNameKey, data)
            self.failUnlessIsInstance(v, unicode)

            refURL = CFURLCreateWithFileSystemPath(None,
                u"/tmp/pyobjc.test.2", kCFURLPOSIXPathStyle, False)
            ok, err = CFURLWriteBookmarkDataToFile(data, refURL, 0, None)
            self.failUnless(ok)
            self.failUnless(err is None)
            self.failUnless(os.path.exists('/tmp/pyobjc.test.2'))

            self.failUnlessResultIsCFRetained(CFURLCreateBookmarkDataFromFile)
            n, err = CFURLCreateBookmarkDataFromFile(None, refURL, None)
            self.failUnlessIsInstance(n, CFDataRef)
            self.failUnless(err is None)

            self.failUnlessResultIsCFRetained(CFURLCreateBookmarkDataFromAliasRecord)
            self.failUnlessArgHasType(CFURLCreateBookmarkDataFromAliasRecord, 0, '^{__CFAllocator=}')
            self.failUnlessArgHasType(CFURLCreateBookmarkDataFromAliasRecord, 1, '^{__CFData=}')

        finally:
            os.unlink('/tmp/pyobjc.test')
            if os.path.exists('/tmp/pyobjc.test.2'):
                os.unlink('/tmp/pyobjc.test.2')

    @min_os_level('10.6')
    def testConstants10_6(self):
        self.failUnlessIsInstance(kCFURLNameKey, unicode)
        self.failUnlessIsInstance(kCFURLLocalizedNameKey, unicode)
        self.failUnlessIsInstance(kCFURLIsRegularFileKey, unicode)
        self.failUnlessIsInstance(kCFURLIsDirectoryKey, unicode)
        self.failUnlessIsInstance(kCFURLIsSymbolicLinkKey, unicode)
        self.failUnlessIsInstance(kCFURLIsVolumeKey, unicode)
        self.failUnlessIsInstance(kCFURLIsPackageKey, unicode)
        self.failUnlessIsInstance(kCFURLIsSystemImmutableKey, unicode)
        self.failUnlessIsInstance(kCFURLIsUserImmutableKey, unicode)
        self.failUnlessIsInstance(kCFURLIsHiddenKey, unicode)
        self.failUnlessIsInstance(kCFURLHasHiddenExtensionKey, unicode)
        self.failUnlessIsInstance(kCFURLCreationDateKey, unicode)
        self.failUnlessIsInstance(kCFURLContentAccessDateKey, unicode)
        self.failUnlessIsInstance(kCFURLContentModificationDateKey, unicode)
        self.failUnlessIsInstance(kCFURLAttributeModificationDateKey, unicode)
        self.failUnlessIsInstance(kCFURLLinkCountKey, unicode)
        self.failUnlessIsInstance(kCFURLParentDirectoryURLKey, unicode)
        self.failUnlessIsInstance(kCFURLVolumeURLKey, unicode)
        self.failUnlessIsInstance(kCFURLTypeIdentifierKey, unicode)
        self.failUnlessIsInstance(kCFURLLocalizedTypeDescriptionKey, unicode)
        self.failUnlessIsInstance(kCFURLLabelNumberKey, unicode)
        self.failUnlessIsInstance(kCFURLLabelColorKey, unicode)
        self.failUnlessIsInstance(kCFURLLocalizedLabelKey, unicode)
        self.failUnlessIsInstance(kCFURLEffectiveIconKey, unicode)
        self.failUnlessIsInstance(kCFURLCustomIconKey, unicode)
        self.failUnlessIsInstance(kCFURLFileSizeKey, unicode)
        self.failUnlessIsInstance(kCFURLFileAllocatedSizeKey, unicode)
        self.failUnlessIsInstance(kCFURLIsAliasFileKey, unicode)
        self.failUnlessIsInstance(kCFURLVolumeLocalizedFormatDescriptionKey, unicode)
        self.failUnlessIsInstance(kCFURLVolumeTotalCapacityKey, unicode)
        self.failUnlessIsInstance(kCFURLVolumeAvailableCapacityKey, unicode)
        self.failUnlessIsInstance(kCFURLVolumeResourceCountKey, unicode)
        self.failUnlessIsInstance(kCFURLVolumeSupportsPersistentIDsKey, unicode)
        self.failUnlessIsInstance(kCFURLVolumeSupportsSymbolicLinksKey, unicode)
        self.failUnlessIsInstance(kCFURLVolumeSupportsHardLinksKey, unicode)
        self.failUnlessIsInstance(kCFURLVolumeSupportsJournalingKey, unicode)
        self.failUnlessIsInstance(kCFURLVolumeIsJournalingKey, unicode)
        self.failUnlessIsInstance(kCFURLVolumeSupportsSparseFilesKey, unicode)
        self.failUnlessIsInstance(kCFURLVolumeSupportsZeroRunsKey, unicode)
        self.failUnlessIsInstance(kCFURLVolumeSupportsCaseSensitiveNamesKey, unicode)
        self.failUnlessIsInstance(kCFURLVolumeSupportsCasePreservedNamesKey, unicode)

        self.failUnlessEqual(kCFURLBookmarkCreationPreferFileIDResolutionMask, 1<<8)
        self.failUnlessEqual(kCFURLBookmarkCreationMinimalBookmarkMask, 1<<9)
        self.failUnlessEqual(kCFURLBookmarkCreationSuitableForBookmarkFile, 1<<10)
        self.failUnlessEqual(kCFBookmarkResolutionWithoutUIMask, 1<<8)
        self.failUnlessEqual(kCFBookmarkResolutionWithoutMountingMask, 1<<9)



if __name__ == "__main__":
    main()
