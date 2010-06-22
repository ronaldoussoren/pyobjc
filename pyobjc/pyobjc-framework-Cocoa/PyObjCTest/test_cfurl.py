from PyObjCTools.TestSupport import *
import array
from CoreFoundation import *
import os
from Foundation import NSURL


class TestURL (TestCase):
    def testTypes(self):
        self.assertIs(CFURLRef, NSURL)
    def testTypeID(self):
        val = CFURLGetTypeID()
        self.assertIsInstance(val, (int, long))

    def testCreateWithBytes(self):
        url = b"http://www.omroep.nl/"

        ref = CFURLCreateWithBytes(None, url, len(url), kCFStringEncodingUTF8, None)
        self.assertIsInstance(ref, CFURLRef)

        strval =  CFURLGetString(ref)
        self.assertEqual(strval, unicode(url, "utf-8"))

        ref2 = CFURLCreateWithBytes(None, url, len(url), kCFStringEncodingUTF8, ref)
        self.assertIsInstance(ref2, CFURLRef)

        a = array.array('b', b'http://www.nu.nl/')
        ref3 = CFURLCreateWithBytes(None, a, len(a), kCFStringEncodingUTF8, None)
        self.assertIsInstance(ref3, CFURLRef)

        # Explictely test for unicode's buffer madness.
        self.assertRaises((ValueError, TypeError), CFURLCreateWithBytes, None, unicode(url), len(url), kCFStringEncodingUTF8, None)

    def testCreateData(self):
        url = b"http://www.omroep.nl/ blank"

        ref = CFURLCreateWithBytes(None, url, len(url), kCFStringEncodingUTF8, None)
        self.assertIsInstance(ref, CFURLRef)

        data = CFURLCreateData(None, ref, kCFStringEncodingUTF8, False)
        self.assertIsInstance(data, CFDataRef)
        val = CFDataGetBytes(data, (0, CFDataGetLength(data)), None)
        self.assertEqual(val, url.replace(b' ', b'%20'))

        data = CFURLCreateData(None, ref, kCFStringEncodingUTF8, True)
        self.assertIsInstance(data, CFDataRef)
        val = CFDataGetBytes(data, (0, CFDataGetLength(data)), None)
        self.assertEqual(val, url.replace(b' ', b'%20'))

    def testCreateWithString(self):
        url = u"http://www.omroep.nl/"

        ref = CFURLCreateWithString(None, url, None)
        self.assertIsInstance(ref, CFURLRef)

        strval =  CFURLGetString(ref)
        self.assertEqual(strval, url)

        ref2 = CFURLCreateWithString(None, url, ref)
        self.assertIsInstance(ref2, CFURLRef)

    def testCreateAbsolute(self):
        url = u"http://www.omroep.nl/sport/"
        baseref = CFURLCreateWithString(None, url, None)

        self.assertArgHasType(CFURLCreateAbsoluteURLWithBytes, 1, b'n^v')
        self.assertArgSizeInArg(CFURLCreateAbsoluteURLWithBytes, 1, 2)
        ref = CFURLCreateAbsoluteURLWithBytes(None, b"socker", len(b"socker"), kCFStringEncodingUTF8, baseref, True)
        self.assertIsInstance(ref, CFURLRef)

        strval =  CFURLGetString(ref)
        self.assertEqual(strval, u"http://www.omroep.nl/sport/socker")

        relpath = b"../../../dummy"
        ref = CFURLCreateAbsoluteURLWithBytes(None, relpath, len(relpath), kCFStringEncodingUTF8, baseref, True)
        self.assertIsInstance(ref, CFURLRef)
        strval =  CFURLGetString(ref)
        self.assertEqual(strval, u"http://www.omroep.nl/dummy")

        relpath = b"../../../dummy"
        ref = CFURLCreateAbsoluteURLWithBytes(None, relpath, len(relpath), kCFStringEncodingUTF8, baseref, False)
        self.assertIsInstance(ref, CFURLRef)
        strval =  CFURLGetString(ref)
        self.assertEqual(strval, u"http://www.omroep.nl/../../dummy")


    def testCopyAbs(self):
        # CFURLCopyAbsoluteURL
        base = CFURLCreateWithString(None, u"http://www.omroep.nl/", None)
        self.assertIsInstance(base, CFURLRef)

        ref = CFURLCreateWithString(None, u"/sport", base)
        self.assertIsInstance(ref, CFURLRef)

        self.assertEqual(CFURLGetString(ref) , u"/sport" )
        abs = CFURLCopyAbsoluteURL(ref)
        self.assertIsInstance(abs, CFURLRef)
        self.assertEqual(CFURLGetString(abs) , u"http://www.omroep.nl/sport" )
    def testPaths(self):
        url = CFURLCreateWithFileSystemPath(None,
                u"/tmp/", kCFURLPOSIXPathStyle, True)
        self.assertIsInstance(url, CFURLRef)
        self.assertTrue(CFURLHasDirectoryPath(url))

        url = CFURLCreateWithFileSystemPath(None,
                u"/etc/hosts", kCFURLPOSIXPathStyle, False)
        self.assertIsInstance(url, CFURLRef)
        self.assertFalse(CFURLHasDirectoryPath(url))

        p = os.path.expanduser('~')
        p = p.encode('utf-8')
        self.assertArgHasType(CFURLCreateFromFileSystemRepresentation, 1, b'n^t')
        self.assertArgIsNullTerminated(CFURLCreateFromFileSystemRepresentation, 1)
        url = CFURLCreateFromFileSystemRepresentation(None,
                p, len(p), True)
        self.assertIsInstance(url, CFURLRef)
        self.assertRaises((ValueError, TypeError),
            CFURLCreateFromFileSystemRepresentation, None,
                u"/tmp/", 4, True)

        base = CFURLCreateWithFileSystemPath(None,
                u"/tmp", kCFURLPOSIXPathStyle, True)
        self.assertIsInstance(base, CFURLRef)

        self.assertArgIsBOOL(CFURLCreateWithFileSystemPathRelativeToBase, 3)
        url = CFURLCreateWithFileSystemPathRelativeToBase(None,
                u"filename", kCFURLPOSIXPathStyle, True, base)
        self.assertIsInstance(url, CFURLRef)

        strval =  CFURLGetString(url)
        self.assertEqual(strval, u"filename/")


        self.assertArgIsBOOL(CFURLCreateFromFileSystemRepresentationRelativeToBase, 3)
        url = CFURLCreateFromFileSystemRepresentationRelativeToBase(None,
                b"filename2", 9, False, base)
        self.assertIsInstance(url, CFURLRef)
        strval =  CFURLGetString(url)
        self.assertEqual(strval, u"filename2")

        ok, strval = CFURLGetFileSystemRepresentation(url, True, None, 100)
        self.assertTrue(ok)

        # Unfortunately metadata doesn't allow describing what we actually need
        if b'\0' in strval:
            strval = strval[:strval.index('\0')]
        self.assertEqual(strval, u"/tmp/filename2")

    def testParts(self):
        base = CFURLCreateWithString(None, u"http://www.omroep.nl/", None)
        self.assertIsInstance(base, CFURLRef)

        ref = CFURLCreateWithString(None, u"/sport", base)
        self.assertIsInstance(ref, CFURLRef)

        self.assertEqual(CFURLGetBaseURL(base), None)
        self.assertEqual(CFURLGetBaseURL(ref), base)
        self.assert_(CFURLCanBeDecomposed(ref) is True)

        self.assertEqual(CFURLCopyScheme(ref), u"http")
        self.assertEqual(CFURLCopyNetLocation(ref), u"www.omroep.nl")
        self.assertEqual(CFURLCopyPath(ref), u"/sport")

        path, isDir = CFURLCopyStrictPath(ref, None)
        self.assertEqual(path, u"sport")
        self.assertEqual(isDir, True)

        path = CFURLCopyFileSystemPath(ref, kCFURLPOSIXPathStyle)
        self.assertEqual(path, u"/sport")

        path = CFURLCopyFileSystemPath(ref, kCFURLPOSIXPathStyle)
        self.assertEqual(path, u"/sport")
        path = CFURLCopyFileSystemPath(ref, kCFURLWindowsPathStyle)
        self.assertEqual(path, u"\\sport")

        self.assertFalse(CFURLHasDirectoryPath(ref))

        v =  CFURLCopyResourceSpecifier(ref)
        self.assertEqual(v, None)

        v =  CFURLCopyHostName(ref)
        self.assertEqual(v, "www.omroep.nl")

        v =  CFURLGetPortNumber(ref)
        self.assertEqual(v, -1)

        ref = CFURLCreateWithString(None, u"https://ronald:test@www.nu.nl:42/sport/results.cgi?qs=1#anchor", None)
        v =  CFURLGetPortNumber(ref)
        self.assertEqual(v, 42)

        v = CFURLCopyResourceSpecifier(ref)
        self.assertEqual(v, u"?qs=1#anchor")

        v = CFURLCopyUserName(ref)
        self.assertEqual(v, "ronald")

        v = CFURLCopyPassword(ref)
        self.assertEqual(v, "test")

        v = CFURLCopyParameterString(ref, None)
        self.assertEqual(v, None)

        v = CFURLCopyQueryString(ref, None)
        self.assertEqual(v, "qs=1")

        v = CFURLCopyLastPathComponent(ref)
        self.assertEqual(v, "results.cgi")

        v = CFURLCopyPathExtension(ref)
        self.assertEqual(v, "cgi")

        cnt, bytes = CFURLGetBytes(ref, None, 100)
        self.assertEqual(cnt, 62)
        self.assertEqual(bytes, 
                b"https://ronald:test@www.nu.nl:42/sport/results.cgi?qs=1#anchor")

        cnt, bytes = CFURLGetBytes(ref, objc.NULL, 0)
        self.assertEqual(cnt, 62)
        self.assertEqual(bytes, objc.NULL)

        rng1, rng2 = CFURLGetByteRangeForComponent(ref, kCFURLComponentHost, None)
        self.assertIsInstance(rng1, CFRange)
        self.assertIsInstance(rng2, CFRange)
        

    def testUpdating(self):
        base = CFURLCreateWithString(None, u"http://www.omroep.nl/sport", None)
        self.assertIsInstance(base, CFURLRef)

        url = CFURLCreateCopyAppendingPathComponent(None, base, "soccer", True)
        self.assertIsInstance(url, CFURLRef)

        strval =  CFURLGetString(url)
        self.assertEqual(strval, "http://www.omroep.nl/sport/soccer/")

        url = CFURLCreateCopyDeletingLastPathComponent(None, base)
        self.assertIsInstance(url, CFURLRef)
        strval =  CFURLGetString(url)
        self.assertEqual(strval, "http://www.omroep.nl/")

        url = CFURLCreateCopyAppendingPathExtension(None, base, "cgi")
        self.assertIsInstance(url, CFURLRef)
        strval =  CFURLGetString(url)
        self.assertEqual(strval, "http://www.omroep.nl/sport.cgi")

        url2 = CFURLCreateCopyDeletingPathExtension(None, base)
        self.assertIsInstance(url2, CFURLRef)
        strval =  CFURLGetString(url2)
        self.assertEqual(strval, "http://www.omroep.nl/sport")

    def testStringEncoding(self):
        base = u"http://www.omroep.nl/sport%20en%20%73%70el"

        strval = CFURLCreateStringByReplacingPercentEscapes(None, base, objc.NULL)
        self.assertEqual(strval, "http://www.omroep.nl/sport%20en%20%73%70el")

        strval = CFURLCreateStringByReplacingPercentEscapes(None, base, "")
        self.assertEqual(strval, "http://www.omroep.nl/sport en spel")

        strval = CFURLCreateStringByReplacingPercentEscapes(None, base, " ")
        self.assertEqual(strval, "http://www.omroep.nl/sport%20en%20spel")

        strval = CFURLCreateStringByReplacingPercentEscapesUsingEncoding(None, base, "", kCFStringEncodingISOLatin1)
        self.assertEqual(strval, "http://www.omroep.nl/sport en spel")

        
        base = u"http://www.omroep.nl/sport en spel"
        strval = CFURLCreateStringByAddingPercentEscapes(None, base, "", "",
                kCFStringEncodingISOLatin1)
        self.assertEqual(strval, u"http://www.omroep.nl/sport%20en%20spel")
        strval = CFURLCreateStringByAddingPercentEscapes(None, base, " ", "s",
                kCFStringEncodingISOLatin1)
        self.assertEqual(strval, u"http://www.omroep.nl/%73port en %73pel")

    def testFSRef(self):
        ref = CFURLCreateWithFileSystemPath(None, os.getcwd(), kCFURLPOSIXPathStyle, True)
        self.assertIsInstance(ref, CFURLRef)

        ok, fsref = CFURLGetFSRef(ref, None)
        self.assertTrue(ok)
        self.assertIsInstance(fsref, objc.FSRef)
        self.assertEqual(fsref.as_pathname(), os.getcwd())

        ref2 = CFURLCreateFromFSRef(None, fsref)
        self.assertEqual(ref, ref2) 

    def testConstants(self):
        self.assertEqual(kCFURLPOSIXPathStyle, 0)
        self.assertEqual(kCFURLHFSPathStyle, 1)
        self.assertEqual(kCFURLWindowsPathStyle, 2)

        self.assertEqual(kCFURLComponentScheme, 1)
        self.assertEqual(kCFURLComponentNetLocation, 2)
        self.assertEqual(kCFURLComponentPath, 3)
        self.assertEqual(kCFURLComponentResourceSpecifier, 4)
        self.assertEqual(kCFURLComponentUser, 5)
        self.assertEqual(kCFURLComponentPassword, 6)
        self.assertEqual(kCFURLComponentUserInfo, 7)
        self.assertEqual(kCFURLComponentHost, 8)
        self.assertEqual(kCFURLComponentPort, 9)
        self.assertEqual(kCFURLComponentParameterString, 10)
        self.assertEqual(kCFURLComponentQuery, 11)
        self.assertEqual(kCFURLComponentFragment, 12)

    @min_os_level('10.6')
    def testFunctions10_6(self):
        fp = open("/tmp/pyobjc.test", "w")
        fp.close()
        try:
            baseURL = CFURLCreateWithFileSystemPath(None,
                u"/tmp/pyobjc.test", kCFURLPOSIXPathStyle, False)
            self.assertIsInstance(baseURL, CFURLRef)

            self.assertResultIsCFRetained(CFURLCreateFileReferenceURL)
            url, err = CFURLCreateFileReferenceURL(None, baseURL, None)
            self.assertIsInstance(url, CFURLRef)
            self.assertEqual(err, None)

            self.assertResultIsCFRetained(CFURLCreateFilePathURL)
            url, err = CFURLCreateFilePathURL(None, baseURL, None)
            self.assertIsInstance(url, CFURLRef)
            self.assertEqual(err, None)

            self.assertResultIsBOOL(CFURLCopyResourcePropertyForKey)
            self.assertArgIsCFRetained(CFURLCopyResourcePropertyForKey, 2)
            self.assertArgIsOut(CFURLCopyResourcePropertyForKey, 2)
            self.assertArgIsOut(CFURLCopyResourcePropertyForKey, 3)
            ok, value, error = CFURLCopyResourcePropertyForKey(url, kCFURLNameKey, None, None)
            self.assertTrue(ok)
            self.assertIsInstance(value, unicode)
            self.assertEqual(error, None)

            ok, value, error = CFURLCopyResourcePropertyForKey(url, kCFURLIsRegularFileKey, None, None)
            self.assertTrue(ok)
            self.assertIsInstance(value, bool)
            self.assertEqual(error, None)


            self.assertResultIsCFRetained(CFURLCreateFilePathURL)
            self.assertArgIsOut(CFURLCopyResourcePropertyForKey, 2)
            values, error = CFURLCopyResourcePropertiesForKeys(url, [kCFURLNameKey, kCFURLIsRegularFileKey], None)
            self.assertIsInstance(values, CFDictionaryRef)
            self.assertEqual(error, None)

            CFURLClearResourcePropertyCacheForKey(url, kCFURLIsRegularFileKey)
            CFURLClearResourcePropertyCache(url)
            self.assertResultIsBOOL(CFURLResourceIsReachable)
            v, err= CFURLResourceIsReachable(url, None)
            self.assertIsInstance(v, bool)
            self.assertEqual(err, None)

            CFURLSetTemporaryResourcePropertyForKey(url, "pyobjc.test", u"hello")
            ok, v, err = CFURLCopyResourcePropertyForKey(url, "pyobjc.test", None, None)
            self.assertTrue(ok)
            self.assertEqual(v, u"hello")

            ok, cur, err = CFURLCopyResourcePropertyForKey(url, kCFURLIsHiddenKey, None, None)
            self.assertTrue(ok)

            ok, err = CFURLSetResourcePropertyForKey(url, kCFURLIsHiddenKey, not cur, None)
            self.assertTrue(ok)

            ok, new, err = CFURLCopyResourcePropertyForKey(url, kCFURLIsHiddenKey, None, None)
            self.assertTrue(ok)
            self.assertEqual(new, not cur)
            self.assertEqual(err, None)

            ok, err = CFURLSetResourcePropertiesForKeys(url, {kCFURLIsHiddenKey:cur}, None)
            self.assertTrue(ok)
            self.assertEqual(err, None)

            ok, new, err = CFURLCopyResourcePropertyForKey(url, kCFURLIsHiddenKey, None, None)
            self.assertTrue(ok)
            self.assertEqual(new, cur)
            self.assertEqual(err, None)

            self.assertResultIsCFRetained(CFURLCreateBookmarkData)
            data, err = CFURLCreateBookmarkData(None, url, kCFURLBookmarkCreationSuitableForBookmarkFile, [kCFURLNameKey, kCFURLIsHiddenKey], None, None)
            self.assertIs(err, None)
            self.assertIsInstance(data, CFDataRef)

            self.assertResultIsCFRetained(CFURLCreateByResolvingBookmarkData)
            u, stale, err = CFURLCreateByResolvingBookmarkData(None, data, 0, None, None, None, None)
            self.assertEqual(u, url)
            self.assertIsInstance(stale, bool)
            self.assertFalse(stale)
            self.assertIs(err, None)
            self.assertResultIsCFRetained(CFURLCreateResourcePropertiesForKeysFromBookmarkData)
            v = CFURLCreateResourcePropertiesForKeysFromBookmarkData(None, [kCFURLNameKey], data)
            self.assertIsInstance(v, CFDictionaryRef)

            self.assertResultIsCFRetained(CFURLCreateResourcePropertyForKeyFromBookmarkData)
            v = CFURLCreateResourcePropertyForKeyFromBookmarkData(None, kCFURLNameKey, data)
            self.assertIsInstance(v, unicode)

            refURL = CFURLCreateWithFileSystemPath(None,
                u"/tmp/pyobjc.test.2", kCFURLPOSIXPathStyle, False)
            ok, err = CFURLWriteBookmarkDataToFile(data, refURL, 0, None)
            self.assertTrue(ok)
            self.assertIs(err, None)
            self.assertTrue(os.path.exists('/tmp/pyobjc.test.2'))

            self.assertResultIsCFRetained(CFURLCreateBookmarkDataFromFile)
            n, err = CFURLCreateBookmarkDataFromFile(None, refURL, None)
            self.assertIsInstance(n, CFDataRef)
            self.assertIs(err, None)
            self.assertResultIsCFRetained(CFURLCreateBookmarkDataFromAliasRecord)
            self.assertArgHasType(CFURLCreateBookmarkDataFromAliasRecord, 0, b'^{__CFAllocator=}')
            self.assertArgHasType(CFURLCreateBookmarkDataFromAliasRecord, 1, b'^{__CFData=}')

        finally:
            os.unlink('/tmp/pyobjc.test')
            if os.path.exists('/tmp/pyobjc.test.2'):
                os.unlink('/tmp/pyobjc.test.2')

    @min_os_level('10.6')
    def testConstants10_6(self):
        self.assertIsInstance(kCFURLNameKey, unicode)
        self.assertIsInstance(kCFURLLocalizedNameKey, unicode)
        self.assertIsInstance(kCFURLIsRegularFileKey, unicode)
        self.assertIsInstance(kCFURLIsDirectoryKey, unicode)
        self.assertIsInstance(kCFURLIsSymbolicLinkKey, unicode)
        self.assertIsInstance(kCFURLIsVolumeKey, unicode)
        self.assertIsInstance(kCFURLIsPackageKey, unicode)
        self.assertIsInstance(kCFURLIsSystemImmutableKey, unicode)
        self.assertIsInstance(kCFURLIsUserImmutableKey, unicode)
        self.assertIsInstance(kCFURLIsHiddenKey, unicode)
        self.assertIsInstance(kCFURLHasHiddenExtensionKey, unicode)
        self.assertIsInstance(kCFURLCreationDateKey, unicode)
        self.assertIsInstance(kCFURLContentAccessDateKey, unicode)
        self.assertIsInstance(kCFURLContentModificationDateKey, unicode)
        self.assertIsInstance(kCFURLAttributeModificationDateKey, unicode)
        self.assertIsInstance(kCFURLLinkCountKey, unicode)
        self.assertIsInstance(kCFURLParentDirectoryURLKey, unicode)
        self.assertIsInstance(kCFURLVolumeURLKey, unicode)
        self.assertIsInstance(kCFURLTypeIdentifierKey, unicode)
        self.assertIsInstance(kCFURLLocalizedTypeDescriptionKey, unicode)
        self.assertIsInstance(kCFURLLabelNumberKey, unicode)
        self.assertIsInstance(kCFURLLabelColorKey, unicode)
        self.assertIsInstance(kCFURLLocalizedLabelKey, unicode)
        self.assertIsInstance(kCFURLEffectiveIconKey, unicode)
        self.assertIsInstance(kCFURLCustomIconKey, unicode)
        self.assertIsInstance(kCFURLFileSizeKey, unicode)
        self.assertIsInstance(kCFURLFileAllocatedSizeKey, unicode)
        self.assertIsInstance(kCFURLIsAliasFileKey, unicode)
        self.assertIsInstance(kCFURLVolumeLocalizedFormatDescriptionKey, unicode)
        self.assertIsInstance(kCFURLVolumeTotalCapacityKey, unicode)
        self.assertIsInstance(kCFURLVolumeAvailableCapacityKey, unicode)
        self.assertIsInstance(kCFURLVolumeResourceCountKey, unicode)
        self.assertIsInstance(kCFURLVolumeSupportsPersistentIDsKey, unicode)
        self.assertIsInstance(kCFURLVolumeSupportsSymbolicLinksKey, unicode)
        self.assertIsInstance(kCFURLVolumeSupportsHardLinksKey, unicode)
        self.assertIsInstance(kCFURLVolumeSupportsJournalingKey, unicode)
        self.assertIsInstance(kCFURLVolumeIsJournalingKey, unicode)
        self.assertIsInstance(kCFURLVolumeSupportsSparseFilesKey, unicode)
        self.assertIsInstance(kCFURLVolumeSupportsZeroRunsKey, unicode)
        self.assertIsInstance(kCFURLVolumeSupportsCaseSensitiveNamesKey, unicode)
        self.assertIsInstance(kCFURLVolumeSupportsCasePreservedNamesKey, unicode)

        self.assertEqual(kCFURLBookmarkCreationPreferFileIDResolutionMask, 1<<8)
        self.assertEqual(kCFURLBookmarkCreationMinimalBookmarkMask, 1<<9)
        self.assertEqual(kCFURLBookmarkCreationSuitableForBookmarkFile, 1<<10)
        self.assertEqual(kCFBookmarkResolutionWithoutUIMask, 1<<8)
        self.assertEqual(kCFBookmarkResolutionWithoutMountingMask, 1<<9)



if __name__ == "__main__":
    main()
