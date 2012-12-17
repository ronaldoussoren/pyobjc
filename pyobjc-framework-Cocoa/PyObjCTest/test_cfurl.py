from PyObjCTools.TestSupport import *
import array
from CoreFoundation import *
import os
from Foundation import NSURL

try:
    unicode
except NameError:
    unicode = str


try:
    long
except NameError:
    long = int


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
        url = b"http://www.omroep.nl/".decode('ascii')

        ref = CFURLCreateWithString(None, url, None)
        self.assertIsInstance(ref, CFURLRef)

        strval =  CFURLGetString(ref)
        self.assertEqual(strval, url)

        ref2 = CFURLCreateWithString(None, url, ref)
        self.assertIsInstance(ref2, CFURLRef)

    def testCreateAbsolute(self):
        url = b"http://www.omroep.nl/sport/".decode('ascii')
        baseref = CFURLCreateWithString(None, url, None)

        self.assertArgHasType(CFURLCreateAbsoluteURLWithBytes, 1, b'n^v')
        self.assertArgSizeInArg(CFURLCreateAbsoluteURLWithBytes, 1, 2)
        ref = CFURLCreateAbsoluteURLWithBytes(None, b"socker", len(b"socker"), kCFStringEncodingUTF8, baseref, True)
        self.assertIsInstance(ref, CFURLRef)

        strval =  CFURLGetString(ref)
        self.assertEqual(strval, b"http://www.omroep.nl/sport/socker".decode('ascii'))

        relpath = b"../../../dummy"
        ref = CFURLCreateAbsoluteURLWithBytes(None, relpath, len(relpath), kCFStringEncodingUTF8, baseref, True)
        self.assertIsInstance(ref, CFURLRef)
        strval =  CFURLGetString(ref)
        self.assertEqual(strval, b"http://www.omroep.nl/dummy".decode('ascii'))

        relpath = b"../../../dummy"
        ref = CFURLCreateAbsoluteURLWithBytes(None, relpath, len(relpath), kCFStringEncodingUTF8, baseref, False)
        self.assertIsInstance(ref, CFURLRef)
        strval =  CFURLGetString(ref)
        self.assertEqual(strval, b"http://www.omroep.nl/../../dummy".decode('ascii'))


    def testCopyAbs(self):
        # CFURLCopyAbsoluteURL
        base = CFURLCreateWithString(None, b"http://www.omroep.nl/".decode('ascii'), None)
        self.assertIsInstance(base, CFURLRef)

        ref = CFURLCreateWithString(None, b"/sport".decode('ascii'), base)
        self.assertIsInstance(ref, CFURLRef)

        self.assertEqual(CFURLGetString(ref) , b"/sport".decode('ascii') )
        abs = CFURLCopyAbsoluteURL(ref)
        self.assertIsInstance(abs, CFURLRef)
        self.assertEqual(CFURLGetString(abs) , b"http://www.omroep.nl/sport".decode('ascii') )

    def testPaths(self):
        url = CFURLCreateWithFileSystemPath(None,
                b"/tmp/".decode('ascii'), kCFURLPOSIXPathStyle, True)
        self.assertIsInstance(url, CFURLRef)
        self.assertTrue(CFURLHasDirectoryPath(url))

        url = CFURLCreateWithFileSystemPath(None,
                b"/etc/hosts".decode('ascii'), kCFURLPOSIXPathStyle, False)
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
                b"/tmp/".decode('ascii'), 4, True)

        base = CFURLCreateWithFileSystemPath(None,
                b"/tmp".decode('ascii'), kCFURLPOSIXPathStyle, True)
        self.assertIsInstance(base, CFURLRef)

        self.assertArgIsBOOL(CFURLCreateWithFileSystemPathRelativeToBase, 3)
        url = CFURLCreateWithFileSystemPathRelativeToBase(None,
                b"filename".decode('ascii'), kCFURLPOSIXPathStyle, True, base)
        self.assertIsInstance(url, CFURLRef)

        strval =  CFURLGetString(url)
        self.assertEqual(strval, b"filename/".decode('ascii'))


        self.assertArgIsBOOL(CFURLCreateFromFileSystemRepresentationRelativeToBase, 3)
        url = CFURLCreateFromFileSystemRepresentationRelativeToBase(None,
                b"filename2", 9, False, base)
        self.assertIsInstance(url, CFURLRef)
        strval =  CFURLGetString(url)
        self.assertEqual(strval, b"filename2".decode('ascii'))

        ok, strval = CFURLGetFileSystemRepresentation(url, True, None, 100)
        self.assertTrue(ok)

        # Unfortunately metadata doesn't allow describing what we actually need
        if b'\0' in strval:
            strval = strval[:strval.index(b'\0')]
        self.assertEqual(strval, b"/tmp/filename2")

    def testParts(self):
        base = CFURLCreateWithString(None, b"http://www.omroep.nl/".decode('ascii'), None)
        self.assertIsInstance(base, CFURLRef)

        ref = CFURLCreateWithString(None, b"/sport".decode('ascii'), base)
        self.assertIsInstance(ref, CFURLRef)

        self.assertEqual(CFURLGetBaseURL(base), None)
        self.assertEqual(CFURLGetBaseURL(ref), base)
        self.assertTrue(CFURLCanBeDecomposed(ref) is True)

        self.assertEqual(CFURLCopyScheme(ref), b"http".decode('ascii'))
        self.assertEqual(CFURLCopyNetLocation(ref), b"www.omroep.nl".decode('ascii'))
        self.assertEqual(CFURLCopyPath(ref), b"/sport".decode('ascii'))

        path, isDir = CFURLCopyStrictPath(ref, None)
        self.assertEqual(path, b"sport".decode('ascii'))
        self.assertEqual(isDir, True)

        path = CFURLCopyFileSystemPath(ref, kCFURLPOSIXPathStyle)
        self.assertEqual(path, b"/sport".decode('ascii'))

        path = CFURLCopyFileSystemPath(ref, kCFURLPOSIXPathStyle)
        self.assertEqual(path, b"/sport".decode('ascii'))
        path = CFURLCopyFileSystemPath(ref, kCFURLWindowsPathStyle)
        self.assertEqual(path, b"\\sport".decode('ascii'))

        self.assertFalse(CFURLHasDirectoryPath(ref))

        v =  CFURLCopyResourceSpecifier(ref)
        self.assertEqual(v, None)

        v =  CFURLCopyHostName(ref)
        self.assertEqual(v, "www.omroep.nl")

        v =  CFURLGetPortNumber(ref)
        self.assertEqual(v, -1)

        ref = CFURLCreateWithString(None, b"https://ronald:test@www.nu.nl:42/sport/results.cgi?qs=1#anchor".decode('ascii'), None)
        v =  CFURLGetPortNumber(ref)
        self.assertEqual(v, 42)

        v = CFURLCopyResourceSpecifier(ref)
        self.assertEqual(v, b"?qs=1#anchor".decode('ascii'))

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
        base = CFURLCreateWithString(None, b"http://www.omroep.nl/sport".decode('ascii'), None)
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
        base = b"http://www.omroep.nl/sport%20en%20%73%70el".decode('ascii')

        strval = CFURLCreateStringByReplacingPercentEscapes(None, base, objc.NULL)
        self.assertEqual(strval, "http://www.omroep.nl/sport%20en%20%73%70el")

        strval = CFURLCreateStringByReplacingPercentEscapes(None, base, "")
        self.assertEqual(strval, "http://www.omroep.nl/sport en spel")

        strval = CFURLCreateStringByReplacingPercentEscapes(None, base, " ")
        self.assertEqual(strval, "http://www.omroep.nl/sport%20en%20spel")

        strval = CFURLCreateStringByReplacingPercentEscapesUsingEncoding(None, base, "", kCFStringEncodingISOLatin1)
        self.assertEqual(strval, "http://www.omroep.nl/sport en spel")


        base = b"http://www.omroep.nl/sport en spel".decode('ascii')
        strval = CFURLCreateStringByAddingPercentEscapes(None, base, "", "",
                kCFStringEncodingISOLatin1)
        self.assertEqual(strval, b"http://www.omroep.nl/sport%20en%20spel".decode('ascii'))
        strval = CFURLCreateStringByAddingPercentEscapes(None, base, " ", "s",
                kCFStringEncodingISOLatin1)
        self.assertEqual(strval, b"http://www.omroep.nl/%73port en %73pel".decode('ascii'))

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
                os.path.realpath(b"/tmp/pyobjc.test".decode('ascii')),
                kCFURLPOSIXPathStyle, False)
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

            CFURLSetTemporaryResourcePropertyForKey(url, "pyobjc.test", b"hello".decode('ascii'))
            ok, v, err = CFURLCopyResourcePropertyForKey(url, "pyobjc.test", None, None)
            self.assertTrue(ok)
            self.assertEqual(v, b"hello".decode('ascii'))

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
                b"/tmp/pyobjc.test.2".decode('ascii'), kCFURLPOSIXPathStyle, False)
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

    @min_os_level('10.8')
    def testFunctions10_8(self):
        self.assertResultIsBOOL(CFURLStartAccessingSecurityScopedResource)

    @min_os_level('10.8')
    def testConstants10_8(self):
        self.assertIsInstance(kCFURLIsExcludedFromBackupKey, unicode)

        self.assertIsInstance(kCFURLPathKey, unicode)

        self.assertEqual(kCFBookmarkResolutionWithoutUIMask, 1 << 8)
        self.assertEqual(kCFBookmarkResolutionWithoutMountingMask, 1 << 9)
        self.assertEqual(kCFURLBookmarkResolutionWithSecurityScope, 1 << 10)


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

    @min_os_level('10.7')
    def testConstants10_7(self):
        self.assertIsInstance(kCFURLKeysOfUnsetValuesKey, unicode)
        self.assertIsInstance(kCFURLFileResourceIdentifierKey, unicode)
        self.assertIsInstance(kCFURLVolumeIdentifierKey, unicode)
        self.assertIsInstance(kCFURLPreferredIOBlockSizeKey, unicode)
        self.assertIsInstance(kCFURLIsReadableKey, unicode)
        self.assertIsInstance(kCFURLIsWritableKey, unicode)
        self.assertIsInstance(kCFURLIsExecutableKey, unicode)
        self.assertIsInstance(kCFURLFileSecurityKey, unicode)
        self.assertIsInstance(kCFURLFileResourceTypeKey, unicode)
        self.assertIsInstance(kCFURLFileResourceTypeNamedPipe, unicode)
        self.assertIsInstance(kCFURLFileResourceTypeCharacterSpecial, unicode)
        self.assertIsInstance(kCFURLFileResourceTypeDirectory, unicode)
        self.assertIsInstance(kCFURLFileResourceTypeBlockSpecial, unicode)
        self.assertIsInstance(kCFURLFileResourceTypeRegular, unicode)
        self.assertIsInstance(kCFURLFileResourceTypeSymbolicLink, unicode)
        self.assertIsInstance(kCFURLFileResourceTypeSocket, unicode)
        self.assertIsInstance(kCFURLFileResourceTypeUnknown, unicode)
        self.assertIsInstance(kCFURLTotalFileSizeKey, unicode)
        self.assertIsInstance(kCFURLTotalFileAllocatedSizeKey, unicode)
        self.assertIsInstance(kCFURLIsMountTriggerKey, unicode)
        self.assertIsInstance(kCFURLVolumeSupportsRootDirectoryDatesKey, unicode)
        self.assertIsInstance(kCFURLVolumeSupportsVolumeSizesKey, unicode)
        self.assertIsInstance(kCFURLVolumeSupportsRenamingKey, unicode)
        self.assertIsInstance(kCFURLVolumeSupportsAdvisoryFileLockingKey, unicode)
        self.assertIsInstance(kCFURLVolumeSupportsExtendedSecurityKey, unicode)
        self.assertIsInstance(kCFURLVolumeIsBrowsableKey, unicode)
        self.assertIsInstance(kCFURLVolumeMaximumFileSizeKey, unicode)
        self.assertIsInstance(kCFURLVolumeIsEjectableKey, unicode)
        self.assertIsInstance(kCFURLVolumeIsRemovableKey, unicode)
        self.assertIsInstance(kCFURLVolumeIsInternalKey, unicode)
        self.assertIsInstance(kCFURLVolumeIsAutomountedKey, unicode)
        self.assertIsInstance(kCFURLVolumeIsLocalKey, unicode)
        self.assertIsInstance(kCFURLVolumeIsReadOnlyKey, unicode)
        self.assertIsInstance(kCFURLVolumeCreationDateKey, unicode)
        self.assertIsInstance(kCFURLVolumeURLForRemountingKey, unicode)
        self.assertIsInstance(kCFURLVolumeUUIDStringKey, unicode)
        self.assertIsInstance(kCFURLVolumeNameKey, unicode)
        self.assertIsInstance(kCFURLVolumeLocalizedNameKey, unicode)
        self.assertIsInstance(kCFURLIsUbiquitousItemKey, unicode)
        self.assertIsInstance(kCFURLUbiquitousItemHasUnresolvedConflictsKey, unicode)
        self.assertIsInstance(kCFURLUbiquitousItemIsDownloadedKey, unicode)
        self.assertIsInstance(kCFURLUbiquitousItemIsDownloadingKey, unicode)
        self.assertIsInstance(kCFURLUbiquitousItemIsUploadedKey, unicode)
        self.assertIsInstance(kCFURLUbiquitousItemIsUploadingKey, unicode)
        self.assertIsInstance(kCFURLUbiquitousItemPercentDownloadedKey, unicode)
        self.assertIsInstance(kCFURLUbiquitousItemPercentUploadedKey, unicode)

if __name__ == "__main__":
    main()
