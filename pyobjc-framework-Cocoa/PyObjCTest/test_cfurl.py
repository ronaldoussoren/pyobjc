import array
import os

import CoreFoundation
from Foundation import NSURL
from PyObjCTools.TestSupport import TestCase, min_os_level
import objc


class TestURL(TestCase):
    def testTypes(self):
        self.assertIs(CoreFoundation.CFURLRef, NSURL)

    def testTypeID(self):
        val = CoreFoundation.CFURLGetTypeID()
        self.assertIsInstance(val, int)

    def testCreateWithBytes(self):
        url = b"http://www.omroep.nl/"

        ref = CoreFoundation.CFURLCreateWithBytes(
            None, url, len(url), CoreFoundation.kCFStringEncodingUTF8, None
        )
        self.assertIsInstance(ref, CoreFoundation.CFURLRef)

        strval = CoreFoundation.CFURLGetString(ref)
        self.assertEqual(strval, str(url, "utf-8"))

        ref2 = CoreFoundation.CFURLCreateWithBytes(
            None, url, len(url), CoreFoundation.kCFStringEncodingUTF8, ref
        )
        self.assertIsInstance(ref2, CoreFoundation.CFURLRef)

        a = array.array("b", b"http://www.nu.nl/")
        ref3 = CoreFoundation.CFURLCreateWithBytes(
            None, a, len(a), CoreFoundation.kCFStringEncodingUTF8, None
        )
        self.assertIsInstance(ref3, CoreFoundation.CFURLRef)

        # Explictely test for str's buffer madness.
        self.assertRaises(
            (ValueError, TypeError),
            CoreFoundation.CFURLCreateWithBytes,
            None,
            str(url),
            len(url),
            CoreFoundation.kCFStringEncodingUTF8,
            None,
        )

    def testCreateData(self):
        url = b"http://www.omroep.nl/ blank"

        ref = CoreFoundation.CFURLCreateWithBytes(
            None, url, len(url), CoreFoundation.kCFStringEncodingUTF8, None
        )
        self.assertIsInstance(ref, CoreFoundation.CFURLRef)

        data = CoreFoundation.CFURLCreateData(
            None, ref, CoreFoundation.kCFStringEncodingUTF8, False
        )
        self.assertIsInstance(data, CoreFoundation.CFDataRef)
        val = CoreFoundation.CFDataGetBytes(
            data, (0, CoreFoundation.CFDataGetLength(data)), None
        )
        self.assertEqual(val, url.replace(b" ", b"%20"))

        data = CoreFoundation.CFURLCreateData(
            None, ref, CoreFoundation.kCFStringEncodingUTF8, True
        )
        self.assertIsInstance(data, CoreFoundation.CFDataRef)
        val = CoreFoundation.CFDataGetBytes(
            data, (0, CoreFoundation.CFDataGetLength(data)), None
        )
        self.assertEqual(val, url.replace(b" ", b"%20"))

    def testCreateWithString(self):
        url = "http://www.omroep.nl/"

        ref = CoreFoundation.CFURLCreateWithString(None, url, None)
        self.assertIsInstance(ref, CoreFoundation.CFURLRef)

        strval = CoreFoundation.CFURLGetString(ref)
        self.assertEqual(strval, url)

        ref2 = CoreFoundation.CFURLCreateWithString(None, url, ref)
        self.assertIsInstance(ref2, CoreFoundation.CFURLRef)

    def testCreateAbsolute(self):
        url = "http://www.omroep.nl/sport/"
        baseref = CoreFoundation.CFURLCreateWithString(None, url, None)

        self.assertArgHasType(CoreFoundation.CFURLCreateAbsoluteURLWithBytes, 1, b"n^v")
        self.assertArgSizeInArg(CoreFoundation.CFURLCreateAbsoluteURLWithBytes, 1, 2)
        ref = CoreFoundation.CFURLCreateAbsoluteURLWithBytes(
            None,
            b"socker",
            len(b"socker"),
            CoreFoundation.kCFStringEncodingUTF8,
            baseref,
            True,
        )
        self.assertIsInstance(ref, CoreFoundation.CFURLRef)

        strval = CoreFoundation.CFURLGetString(ref)
        self.assertEqual(strval, "http://www.omroep.nl/sport/socker")

        relpath = b"../../../dummy"
        ref = CoreFoundation.CFURLCreateAbsoluteURLWithBytes(
            None,
            relpath,
            len(relpath),
            CoreFoundation.kCFStringEncodingUTF8,
            baseref,
            True,
        )
        self.assertIsInstance(ref, CoreFoundation.CFURLRef)
        strval = CoreFoundation.CFURLGetString(ref)
        self.assertEqual(strval, "http://www.omroep.nl/dummy")

        relpath = b"../../../dummy"
        ref = CoreFoundation.CFURLCreateAbsoluteURLWithBytes(
            None,
            relpath,
            len(relpath),
            CoreFoundation.kCFStringEncodingUTF8,
            baseref,
            False,
        )
        self.assertIsInstance(ref, CoreFoundation.CFURLRef)
        strval = CoreFoundation.CFURLGetString(ref)
        self.assertEqual(strval, "http://www.omroep.nl/../../dummy")

    def testCopyAbs(self):
        # CoreFoundation.CFURLCopyAbsoluteURL
        base = CoreFoundation.CFURLCreateWithString(None, "http://www.omroep.nl/", None)
        self.assertIsInstance(base, CoreFoundation.CFURLRef)

        ref = CoreFoundation.CFURLCreateWithString(None, "/sport", base)
        self.assertIsInstance(ref, CoreFoundation.CFURLRef)

        self.assertEqual(CoreFoundation.CFURLGetString(ref), "/sport")
        abs_url = CoreFoundation.CFURLCopyAbsoluteURL(ref)
        self.assertIsInstance(abs_url, CoreFoundation.CFURLRef)
        self.assertEqual(
            CoreFoundation.CFURLGetString(abs_url), "http://www.omroep.nl/sport"
        )

    def testPaths(self):
        url = CoreFoundation.CFURLCreateWithFileSystemPath(
            None, "/tmp/", CoreFoundation.kCFURLPOSIXPathStyle, True
        )
        self.assertIsInstance(url, CoreFoundation.CFURLRef)
        self.assertTrue(CoreFoundation.CFURLHasDirectoryPath(url))

        url = CoreFoundation.CFURLCreateWithFileSystemPath(
            None, "/etc/hosts", CoreFoundation.kCFURLPOSIXPathStyle, False
        )
        self.assertIsInstance(url, CoreFoundation.CFURLRef)
        self.assertFalse(CoreFoundation.CFURLHasDirectoryPath(url))

        p = os.path.expanduser("~")
        p = p.encode("utf-8")
        self.assertArgHasType(
            CoreFoundation.CFURLCreateFromFileSystemRepresentation, 1, b"n^t"
        )
        self.assertArgIsNullTerminated(
            CoreFoundation.CFURLCreateFromFileSystemRepresentation, 1
        )
        url = CoreFoundation.CFURLCreateFromFileSystemRepresentation(
            None, p, len(p), True
        )
        self.assertIsInstance(url, CoreFoundation.CFURLRef)
        self.assertRaises(
            (ValueError, TypeError),
            CoreFoundation.CFURLCreateFromFileSystemRepresentation,
            None,
            "/tmp/",
            4,
            True,
        )

        base = CoreFoundation.CFURLCreateWithFileSystemPath(
            None, "/tmp", CoreFoundation.kCFURLPOSIXPathStyle, True
        )
        self.assertIsInstance(base, CoreFoundation.CFURLRef)

        self.assertArgIsBOOL(
            CoreFoundation.CFURLCreateWithFileSystemPathRelativeToBase, 3
        )
        url = CoreFoundation.CFURLCreateWithFileSystemPathRelativeToBase(
            None, "filename", CoreFoundation.kCFURLPOSIXPathStyle, True, base
        )
        self.assertIsInstance(url, CoreFoundation.CFURLRef)

        strval = CoreFoundation.CFURLGetString(url)
        self.assertEqual(strval, "filename/")

        self.assertArgIsBOOL(
            CoreFoundation.CFURLCreateFromFileSystemRepresentationRelativeToBase, 3
        )
        url = CoreFoundation.CFURLCreateFromFileSystemRepresentationRelativeToBase(
            None, b"filename2", 9, False, base
        )
        self.assertIsInstance(url, CoreFoundation.CFURLRef)
        strval = CoreFoundation.CFURLGetString(url)
        self.assertEqual(strval, "filename2")

        ok, strval = CoreFoundation.CFURLGetFileSystemRepresentation(
            url, True, None, 100
        )
        self.assertTrue(ok)

        # Unfortunately metadata doesn't allow describing what we actually need
        if b"\0" in strval:
            strval = strval[: strval.index(b"\0")]
        self.assertEqual(strval, b"/tmp/filename2")

    def testParts(self):
        base = CoreFoundation.CFURLCreateWithString(None, "http://www.omroep.nl/", None)
        self.assertIsInstance(base, CoreFoundation.CFURLRef)

        ref = CoreFoundation.CFURLCreateWithString(None, "/sport", base)
        self.assertIsInstance(ref, CoreFoundation.CFURLRef)

        self.assertEqual(CoreFoundation.CFURLGetBaseURL(base), None)
        self.assertEqual(CoreFoundation.CFURLGetBaseURL(ref), base)
        self.assertTrue(CoreFoundation.CFURLCanBeDecomposed(ref) is True)

        self.assertEqual(CoreFoundation.CFURLCopyScheme(ref), "http")
        self.assertEqual(CoreFoundation.CFURLCopyNetLocation(ref), "www.omroep.nl")
        self.assertEqual(CoreFoundation.CFURLCopyPath(ref), "/sport")

        path, isDir = CoreFoundation.CFURLCopyStrictPath(ref, None)
        self.assertEqual(path, "sport")
        self.assertEqual(isDir, True)

        path = CoreFoundation.CFURLCopyFileSystemPath(
            ref, CoreFoundation.kCFURLPOSIXPathStyle
        )
        self.assertEqual(path, "/sport")

        path = CoreFoundation.CFURLCopyFileSystemPath(
            ref, CoreFoundation.kCFURLPOSIXPathStyle
        )
        self.assertEqual(path, "/sport")
        path = CoreFoundation.CFURLCopyFileSystemPath(
            ref, CoreFoundation.kCFURLWindowsPathStyle
        )
        self.assertEqual(path, "\\sport")

        self.assertFalse(CoreFoundation.CFURLHasDirectoryPath(ref))

        v = CoreFoundation.CFURLCopyResourceSpecifier(ref)
        self.assertEqual(v, None)

        v = CoreFoundation.CFURLCopyHostName(ref)
        self.assertEqual(v, "www.omroep.nl")

        v = CoreFoundation.CFURLGetPortNumber(ref)
        self.assertEqual(v, -1)

        ref = CoreFoundation.CFURLCreateWithString(
            None,
            b"https://ronald:test@www.nu.nl:42/sport/results.cgi?qs=1#anchor".decode(
                "ascii"
            ),
            None,
        )
        v = CoreFoundation.CFURLGetPortNumber(ref)
        self.assertEqual(v, 42)

        v = CoreFoundation.CFURLCopyResourceSpecifier(ref)
        self.assertEqual(v, "?qs=1#anchor")

        v = CoreFoundation.CFURLCopyUserName(ref)
        self.assertEqual(v, "ronald")

        v = CoreFoundation.CFURLCopyPassword(ref)
        self.assertEqual(v, "test")

        v = CoreFoundation.CFURLCopyParameterString(ref, None)
        self.assertEqual(v, None)

        v = CoreFoundation.CFURLCopyQueryString(ref, None)
        self.assertEqual(v, "qs=1")

        v = CoreFoundation.CFURLCopyLastPathComponent(ref)
        self.assertEqual(v, "results.cgi")

        v = CoreFoundation.CFURLCopyPathExtension(ref)
        self.assertEqual(v, "cgi")

        cnt, bytes_value = CoreFoundation.CFURLGetBytes(ref, None, 100)
        self.assertEqual(cnt, 62)
        self.assertEqual(
            bytes_value,
            b"https://ronald:test@www.nu.nl:42/sport/results.cgi?qs=1#anchor",
        )

        cnt, bytes_value = CoreFoundation.CFURLGetBytes(ref, objc.NULL, 0)
        self.assertEqual(cnt, 62)
        self.assertEqual(bytes_value, objc.NULL)

        rng1, rng2 = CoreFoundation.CFURLGetByteRangeForComponent(
            ref, CoreFoundation.kCFURLComponentHost, None
        )
        self.assertIsInstance(rng1, CoreFoundation.CFRange)
        self.assertIsInstance(rng2, CoreFoundation.CFRange)

    def testUpdating(self):
        base = CoreFoundation.CFURLCreateWithString(
            None, "http://www.omroep.nl/sport", None
        )
        self.assertIsInstance(base, CoreFoundation.CFURLRef)

        url = CoreFoundation.CFURLCreateCopyAppendingPathComponent(
            None, base, "soccer", True
        )
        self.assertIsInstance(url, CoreFoundation.CFURLRef)

        strval = CoreFoundation.CFURLGetString(url)
        self.assertEqual(strval, "http://www.omroep.nl/sport/soccer/")

        url = CoreFoundation.CFURLCreateCopyDeletingLastPathComponent(None, base)
        self.assertIsInstance(url, CoreFoundation.CFURLRef)
        strval = CoreFoundation.CFURLGetString(url)
        self.assertEqual(strval, "http://www.omroep.nl/")

        url = CoreFoundation.CFURLCreateCopyAppendingPathExtension(None, base, "cgi")
        self.assertIsInstance(url, CoreFoundation.CFURLRef)
        strval = CoreFoundation.CFURLGetString(url)
        self.assertEqual(strval, "http://www.omroep.nl/sport.cgi")

        url2 = CoreFoundation.CFURLCreateCopyDeletingPathExtension(None, base)
        self.assertIsInstance(url2, CoreFoundation.CFURLRef)
        strval = CoreFoundation.CFURLGetString(url2)
        self.assertEqual(strval, "http://www.omroep.nl/sport")

    def testStringEncoding(self):
        base = "http://www.omroep.nl/sport%20en%20%73%70el"

        strval = CoreFoundation.CFURLCreateStringByReplacingPercentEscapes(
            None, base, objc.NULL
        )
        self.assertEqual(strval, "http://www.omroep.nl/sport%20en%20%73%70el")

        strval = CoreFoundation.CFURLCreateStringByReplacingPercentEscapes(
            None, base, ""
        )
        self.assertEqual(strval, "http://www.omroep.nl/sport en spel")

        strval = CoreFoundation.CFURLCreateStringByReplacingPercentEscapes(
            None, base, " "
        )
        self.assertEqual(strval, "http://www.omroep.nl/sport%20en%20spel")

        strval = CoreFoundation.CFURLCreateStringByReplacingPercentEscapesUsingEncoding(
            None, base, "", CoreFoundation.kCFStringEncodingISOLatin1
        )
        self.assertEqual(strval, "http://www.omroep.nl/sport en spel")

        base = "http://www.omroep.nl/sport en spel"
        strval = CoreFoundation.CFURLCreateStringByAddingPercentEscapes(
            None, base, "", "", CoreFoundation.kCFStringEncodingISOLatin1
        )
        self.assertEqual(strval, "http://www.omroep.nl/sport%20en%20spel")
        strval = CoreFoundation.CFURLCreateStringByAddingPercentEscapes(
            None, base, " ", "s", CoreFoundation.kCFStringEncodingISOLatin1
        )
        self.assertEqual(strval, "http://www.omroep.nl/%73port en %73pel")

    def testFSRef(self):
        ref = CoreFoundation.CFURLCreateWithFileSystemPath(
            None, os.getcwd(), CoreFoundation.kCFURLPOSIXPathStyle, True
        )
        self.assertIsInstance(ref, CoreFoundation.CFURLRef)

        ok, fsref = CoreFoundation.CFURLGetFSRef(ref, None)
        self.assertTrue(ok)
        self.assertIsInstance(fsref, objc.FSRef)
        self.assertEqual(fsref.as_pathname(), os.getcwd())

        ref2 = CoreFoundation.CFURLCreateFromFSRef(None, fsref)
        self.assertEqual(ref, ref2)

    def testConstants(self):
        self.assertEqual(CoreFoundation.kCFURLPOSIXPathStyle, 0)
        self.assertEqual(CoreFoundation.kCFURLHFSPathStyle, 1)
        self.assertEqual(CoreFoundation.kCFURLWindowsPathStyle, 2)

        self.assertEqual(CoreFoundation.kCFURLComponentScheme, 1)
        self.assertEqual(CoreFoundation.kCFURLComponentNetLocation, 2)
        self.assertEqual(CoreFoundation.kCFURLComponentPath, 3)
        self.assertEqual(CoreFoundation.kCFURLComponentResourceSpecifier, 4)
        self.assertEqual(CoreFoundation.kCFURLComponentUser, 5)
        self.assertEqual(CoreFoundation.kCFURLComponentPassword, 6)
        self.assertEqual(CoreFoundation.kCFURLComponentUserInfo, 7)
        self.assertEqual(CoreFoundation.kCFURLComponentHost, 8)
        self.assertEqual(CoreFoundation.kCFURLComponentPort, 9)
        self.assertEqual(CoreFoundation.kCFURLComponentParameterString, 10)
        self.assertEqual(CoreFoundation.kCFURLComponentQuery, 11)
        self.assertEqual(CoreFoundation.kCFURLComponentFragment, 12)

    @min_os_level("10.6")
    def testFunctions10_6(self):
        fp = open("/tmp/pyobjc.test", "w")
        fp.close()
        try:
            baseURL = CoreFoundation.CFURLCreateWithFileSystemPath(
                None,
                os.path.realpath("/tmp/pyobjc.test"),
                CoreFoundation.kCFURLPOSIXPathStyle,
                False,
            )
            self.assertIsInstance(baseURL, CoreFoundation.CFURLRef)

            self.assertResultIsCFRetained(CoreFoundation.CFURLCreateFileReferenceURL)
            url, err = CoreFoundation.CFURLCreateFileReferenceURL(None, baseURL, None)
            self.assertIsInstance(url, CoreFoundation.CFURLRef)
            self.assertEqual(err, None)

            self.assertResultIsCFRetained(CoreFoundation.CFURLCreateFilePathURL)
            url, err = CoreFoundation.CFURLCreateFilePathURL(None, baseURL, None)
            self.assertIsInstance(url, CoreFoundation.CFURLRef)
            self.assertEqual(err, None)

            self.assertResultIsBOOL(CoreFoundation.CFURLCopyResourcePropertyForKey)
            self.assertArgIsCFRetained(
                CoreFoundation.CFURLCopyResourcePropertyForKey, 2
            )
            self.assertArgIsOut(CoreFoundation.CFURLCopyResourcePropertyForKey, 2)
            self.assertArgIsOut(CoreFoundation.CFURLCopyResourcePropertyForKey, 3)
            ok, value, error = CoreFoundation.CFURLCopyResourcePropertyForKey(
                url, CoreFoundation.kCFURLNameKey, None, None
            )
            self.assertTrue(ok)
            self.assertIsInstance(value, str)
            self.assertEqual(error, None)

            ok, value, error = CoreFoundation.CFURLCopyResourcePropertyForKey(
                url, CoreFoundation.kCFURLIsRegularFileKey, None, None
            )
            self.assertTrue(ok)
            self.assertIsInstance(value, bool)
            self.assertEqual(error, None)

            self.assertResultIsCFRetained(CoreFoundation.CFURLCreateFilePathURL)
            self.assertArgIsOut(CoreFoundation.CFURLCopyResourcePropertyForKey, 2)
            values, error = CoreFoundation.CFURLCopyResourcePropertiesForKeys(
                url,
                [CoreFoundation.kCFURLNameKey, CoreFoundation.kCFURLIsRegularFileKey],
                None,
            )
            self.assertIsInstance(values, CoreFoundation.CFDictionaryRef)
            self.assertEqual(error, None)

            CoreFoundation.CFURLClearResourcePropertyCacheForKey(
                url, CoreFoundation.kCFURLIsRegularFileKey
            )
            CoreFoundation.CFURLClearResourcePropertyCache(url)
            self.assertResultIsBOOL(CoreFoundation.CFURLResourceIsReachable)
            v, err = CoreFoundation.CFURLResourceIsReachable(url, None)
            self.assertIsInstance(v, bool)
            self.assertEqual(err, None)

            CoreFoundation.CFURLSetTemporaryResourcePropertyForKey(
                url, "pyobjc.test", "hello"
            )
            ok, v, err = CoreFoundation.CFURLCopyResourcePropertyForKey(
                url, "pyobjc.test", None, None
            )
            self.assertTrue(ok)
            self.assertEqual(v, "hello")

            ok, cur, err = CoreFoundation.CFURLCopyResourcePropertyForKey(
                url, CoreFoundation.kCFURLIsHiddenKey, None, None
            )
            self.assertTrue(ok)

            ok, err = CoreFoundation.CFURLSetResourcePropertyForKey(
                url, CoreFoundation.kCFURLIsHiddenKey, not cur, None
            )
            self.assertTrue(ok)

            ok, new, err = CoreFoundation.CFURLCopyResourcePropertyForKey(
                url, CoreFoundation.kCFURLIsHiddenKey, None, None
            )
            self.assertTrue(ok)
            self.assertEqual(new, not cur)
            self.assertEqual(err, None)

            ok, err = CoreFoundation.CFURLSetResourcePropertiesForKeys(
                url, {CoreFoundation.kCFURLIsHiddenKey: cur}, None
            )
            self.assertTrue(ok)
            self.assertEqual(err, None)

            ok, new, err = CoreFoundation.CFURLCopyResourcePropertyForKey(
                url, CoreFoundation.kCFURLIsHiddenKey, None, None
            )
            self.assertTrue(ok)
            self.assertEqual(new, cur)
            self.assertEqual(err, None)

            self.assertResultIsCFRetained(CoreFoundation.CFURLCreateBookmarkData)
            data, err = CoreFoundation.CFURLCreateBookmarkData(
                None,
                url,
                CoreFoundation.kCFURLBookmarkCreationSuitableForBookmarkFile,
                [CoreFoundation.kCFURLNameKey, CoreFoundation.kCFURLIsHiddenKey],
                None,
                None,
            )
            self.assertIs(err, None)
            self.assertIsInstance(data, CoreFoundation.CFDataRef)

            self.assertResultIsCFRetained(
                CoreFoundation.CFURLCreateByResolvingBookmarkData
            )
            u, stale, err = CoreFoundation.CFURLCreateByResolvingBookmarkData(
                None, data, 0, None, None, None, None
            )
            self.assertEqual(u, url)
            self.assertIsInstance(stale, bool)
            self.assertFalse(stale)
            self.assertIs(err, None)
            self.assertResultIsCFRetained(
                CoreFoundation.CFURLCreateResourcePropertiesForKeysFromBookmarkData
            )
            v = CoreFoundation.CFURLCreateResourcePropertiesForKeysFromBookmarkData(
                None, [CoreFoundation.kCFURLNameKey], data
            )
            self.assertIsInstance(v, CoreFoundation.CFDictionaryRef)

            self.assertResultIsCFRetained(
                CoreFoundation.CFURLCreateResourcePropertyForKeyFromBookmarkData
            )
            v = CoreFoundation.CFURLCreateResourcePropertyForKeyFromBookmarkData(
                None, CoreFoundation.kCFURLNameKey, data
            )
            self.assertIsInstance(v, str)

            refURL = CoreFoundation.CFURLCreateWithFileSystemPath(
                None, "/tmp/pyobjc.test.2", CoreFoundation.kCFURLPOSIXPathStyle, False
            )
            ok, err = CoreFoundation.CFURLWriteBookmarkDataToFile(data, refURL, 0, None)
            self.assertTrue(ok)
            self.assertIs(err, None)
            self.assertTrue(os.path.exists("/tmp/pyobjc.test.2"))

            self.assertResultIsCFRetained(
                CoreFoundation.CFURLCreateBookmarkDataFromFile
            )
            n, err = CoreFoundation.CFURLCreateBookmarkDataFromFile(None, refURL, None)
            self.assertIsInstance(n, CoreFoundation.CFDataRef)
            self.assertIs(err, None)
            self.assertResultIsCFRetained(
                CoreFoundation.CFURLCreateBookmarkDataFromAliasRecord
            )
            self.assertArgHasType(
                CoreFoundation.CFURLCreateBookmarkDataFromAliasRecord,
                0,
                b"^{__CFAllocator=}",
            )
            self.assertArgHasType(
                CoreFoundation.CFURLCreateBookmarkDataFromAliasRecord,
                1,
                b"^{__CFData=}",
            )

        finally:
            os.unlink("/tmp/pyobjc.test")
            if os.path.exists("/tmp/pyobjc.test.2"):
                os.unlink("/tmp/pyobjc.test.2")

    @min_os_level("10.8")
    def testFunctions10_8(self):
        self.assertResultIsBOOL(
            CoreFoundation.CFURLStartAccessingSecurityScopedResource
        )
        CoreFoundation.CFURLStopAccessingSecurityScopedResource

    @min_os_level("10.8")
    def testConstants10_8(self):
        self.assertIsInstance(CoreFoundation.kCFURLIsExcludedFromBackupKey, str)

        self.assertIsInstance(CoreFoundation.kCFURLPathKey, str)

        self.assertEqual(CoreFoundation.kCFBookmarkResolutionWithoutUIMask, 1 << 8)
        self.assertEqual(
            CoreFoundation.kCFBookmarkResolutionWithoutMountingMask, 1 << 9
        )
        self.assertEqual(
            CoreFoundation.kCFURLBookmarkResolutionWithSecurityScope, 1 << 10
        )
        self.assertEqual(
            CoreFoundation.kCFURLBookmarkResolutionWithoutImplicitStartAccessing,
            1 << 15,
        )

    @min_os_level("10.9")
    def testConstants10_9(self):
        self.assertIsInstance(CoreFoundation.kCFURLTagNamesKey, str)
        self.assertIsInstance(
            CoreFoundation.kCFURLUbiquitousItemDownloadingStatusKey, str
        )
        self.assertIsInstance(
            CoreFoundation.kCFURLUbiquitousItemDownloadingErrorKey, str
        )
        self.assertIsInstance(CoreFoundation.kCFURLUbiquitousItemUploadingErrorKey, str)
        self.assertIsInstance(
            CoreFoundation.kCFURLUbiquitousItemDownloadingStatusNotDownloaded, str
        )
        self.assertIsInstance(
            CoreFoundation.kCFURLUbiquitousItemDownloadingStatusDownloaded, str
        )
        self.assertIsInstance(
            CoreFoundation.kCFURLUbiquitousItemDownloadingStatusCurrent, str
        )

    @min_os_level("10.10")
    def testConstants10_10(self):
        self.assertIsInstance(CoreFoundation.kCFURLGenerationIdentifierKey, str)
        self.assertIsInstance(CoreFoundation.kCFURLDocumentIdentifierKey, str)
        self.assertIsInstance(CoreFoundation.kCFURLAddedToDirectoryDateKey, str)
        self.assertIsInstance(CoreFoundation.kCFURLQuarantinePropertiesKey, str)

    @min_os_level("10.11")
    def testConstants10_11(self):
        self.assertIsInstance(CoreFoundation.kCFURLIsApplicationKey, str)
        self.assertIsInstance(CoreFoundation.kCFURLApplicationIsScriptableKey, str)

    @min_os_level("10.6")
    def testConstants10_6(self):
        self.assertIsInstance(CoreFoundation.kCFURLNameKey, str)
        self.assertIsInstance(CoreFoundation.kCFURLLocalizedNameKey, str)
        self.assertIsInstance(CoreFoundation.kCFURLIsRegularFileKey, str)
        self.assertIsInstance(CoreFoundation.kCFURLIsDirectoryKey, str)
        self.assertIsInstance(CoreFoundation.kCFURLIsSymbolicLinkKey, str)
        self.assertIsInstance(CoreFoundation.kCFURLIsVolumeKey, str)
        self.assertIsInstance(CoreFoundation.kCFURLIsPackageKey, str)
        self.assertIsInstance(CoreFoundation.kCFURLIsSystemImmutableKey, str)
        self.assertIsInstance(CoreFoundation.kCFURLIsUserImmutableKey, str)
        self.assertIsInstance(CoreFoundation.kCFURLIsHiddenKey, str)
        self.assertIsInstance(CoreFoundation.kCFURLHasHiddenExtensionKey, str)
        self.assertIsInstance(CoreFoundation.kCFURLCreationDateKey, str)
        self.assertIsInstance(CoreFoundation.kCFURLContentAccessDateKey, str)
        self.assertIsInstance(CoreFoundation.kCFURLContentModificationDateKey, str)
        self.assertIsInstance(CoreFoundation.kCFURLAttributeModificationDateKey, str)
        self.assertIsInstance(CoreFoundation.kCFURLLinkCountKey, str)
        self.assertIsInstance(CoreFoundation.kCFURLParentDirectoryURLKey, str)
        self.assertIsInstance(CoreFoundation.kCFURLVolumeURLKey, str)
        self.assertIsInstance(CoreFoundation.kCFURLTypeIdentifierKey, str)
        self.assertIsInstance(CoreFoundation.kCFURLLocalizedTypeDescriptionKey, str)
        self.assertIsInstance(CoreFoundation.kCFURLLabelNumberKey, str)
        self.assertIsInstance(CoreFoundation.kCFURLLabelColorKey, str)
        self.assertIsInstance(CoreFoundation.kCFURLLocalizedLabelKey, str)
        self.assertIsInstance(CoreFoundation.kCFURLEffectiveIconKey, str)
        self.assertIsInstance(CoreFoundation.kCFURLCustomIconKey, str)
        self.assertIsInstance(CoreFoundation.kCFURLFileSizeKey, str)
        self.assertIsInstance(CoreFoundation.kCFURLFileAllocatedSizeKey, str)
        self.assertIsInstance(CoreFoundation.kCFURLIsAliasFileKey, str)
        self.assertIsInstance(
            CoreFoundation.kCFURLVolumeLocalizedFormatDescriptionKey, str
        )
        self.assertIsInstance(CoreFoundation.kCFURLVolumeTotalCapacityKey, str)
        self.assertIsInstance(CoreFoundation.kCFURLVolumeAvailableCapacityKey, str)
        self.assertIsInstance(CoreFoundation.kCFURLVolumeResourceCountKey, str)
        self.assertIsInstance(CoreFoundation.kCFURLVolumeSupportsPersistentIDsKey, str)
        self.assertIsInstance(CoreFoundation.kCFURLVolumeSupportsSymbolicLinksKey, str)
        self.assertIsInstance(CoreFoundation.kCFURLVolumeSupportsHardLinksKey, str)
        self.assertIsInstance(CoreFoundation.kCFURLVolumeSupportsJournalingKey, str)
        self.assertIsInstance(CoreFoundation.kCFURLVolumeIsJournalingKey, str)
        self.assertIsInstance(CoreFoundation.kCFURLVolumeSupportsSparseFilesKey, str)
        self.assertIsInstance(CoreFoundation.kCFURLVolumeSupportsZeroRunsKey, str)
        self.assertIsInstance(
            CoreFoundation.kCFURLVolumeSupportsCaseSensitiveNamesKey, str
        )
        self.assertIsInstance(
            CoreFoundation.kCFURLVolumeSupportsCasePreservedNamesKey, str
        )

        self.assertEqual(
            CoreFoundation.kCFURLBookmarkCreationPreferFileIDResolutionMask, 1 << 8
        )
        self.assertEqual(
            CoreFoundation.kCFURLBookmarkCreationMinimalBookmarkMask, 1 << 9
        )
        self.assertEqual(
            CoreFoundation.kCFURLBookmarkCreationSuitableForBookmarkFile, 1 << 10
        )
        self.assertEqual(CoreFoundation.kCFBookmarkResolutionWithoutUIMask, 1 << 8)
        self.assertEqual(
            CoreFoundation.kCFBookmarkResolutionWithoutMountingMask, 1 << 9
        )

        self.assertEqual(CoreFoundation.kCFURLBookmarkResolutionWithoutUIMask, 1 << 8)
        self.assertEqual(
            CoreFoundation.kCFURLBookmarkResolutionWithoutMountingMask, 1 << 9
        )

    @min_os_level("10.7")
    def testConstants10_7(self):
        self.assertEqual(
            CoreFoundation.kCFURLBookmarkCreationWithSecurityScope, 1 << 11
        )
        self.assertEqual(
            CoreFoundation.kCFURLBookmarkCreationSecurityScopeAllowOnlyReadAccess,
            1 << 12,
        )
        self.assertEqual(
            CoreFoundation.kCFURLBookmarkResolutionWithSecurityScope, 1 << 10
        )
        self.assertEqual(
            CoreFoundation.kCFURLBookmarkCreationWithoutImplicitSecurityScope, 1 << 29
        )

        self.assertIsInstance(CoreFoundation.kCFURLKeysOfUnsetValuesKey, str)
        self.assertIsInstance(CoreFoundation.kCFURLFileResourceIdentifierKey, str)
        self.assertIsInstance(CoreFoundation.kCFURLVolumeIdentifierKey, str)
        self.assertIsInstance(CoreFoundation.kCFURLPreferredIOBlockSizeKey, str)
        self.assertIsInstance(CoreFoundation.kCFURLIsReadableKey, str)
        self.assertIsInstance(CoreFoundation.kCFURLIsWritableKey, str)
        self.assertIsInstance(CoreFoundation.kCFURLIsExecutableKey, str)
        self.assertIsInstance(CoreFoundation.kCFURLFileSecurityKey, str)
        self.assertIsInstance(CoreFoundation.kCFURLFileResourceTypeKey, str)
        self.assertIsInstance(CoreFoundation.kCFURLFileResourceTypeNamedPipe, str)
        self.assertIsInstance(
            CoreFoundation.kCFURLFileResourceTypeCharacterSpecial, str
        )
        self.assertIsInstance(CoreFoundation.kCFURLFileResourceTypeDirectory, str)
        self.assertIsInstance(CoreFoundation.kCFURLFileResourceTypeBlockSpecial, str)
        self.assertIsInstance(CoreFoundation.kCFURLFileResourceTypeRegular, str)
        self.assertIsInstance(CoreFoundation.kCFURLFileResourceTypeSymbolicLink, str)
        self.assertIsInstance(CoreFoundation.kCFURLFileResourceTypeSocket, str)
        self.assertIsInstance(CoreFoundation.kCFURLFileResourceTypeUnknown, str)
        self.assertIsInstance(CoreFoundation.kCFURLTotalFileSizeKey, str)
        self.assertIsInstance(CoreFoundation.kCFURLTotalFileAllocatedSizeKey, str)
        self.assertIsInstance(CoreFoundation.kCFURLIsMountTriggerKey, str)
        self.assertIsInstance(
            CoreFoundation.kCFURLVolumeSupportsRootDirectoryDatesKey, str
        )
        self.assertIsInstance(CoreFoundation.kCFURLVolumeSupportsVolumeSizesKey, str)
        self.assertIsInstance(CoreFoundation.kCFURLVolumeSupportsRenamingKey, str)
        self.assertIsInstance(
            CoreFoundation.kCFURLVolumeSupportsAdvisoryFileLockingKey, str
        )
        self.assertIsInstance(
            CoreFoundation.kCFURLVolumeSupportsExtendedSecurityKey, str
        )
        self.assertIsInstance(CoreFoundation.kCFURLVolumeIsBrowsableKey, str)
        self.assertIsInstance(CoreFoundation.kCFURLVolumeMaximumFileSizeKey, str)
        self.assertIsInstance(CoreFoundation.kCFURLVolumeIsEjectableKey, str)
        self.assertIsInstance(CoreFoundation.kCFURLVolumeIsRemovableKey, str)
        self.assertIsInstance(CoreFoundation.kCFURLVolumeIsInternalKey, str)
        self.assertIsInstance(CoreFoundation.kCFURLVolumeIsAutomountedKey, str)
        self.assertIsInstance(CoreFoundation.kCFURLVolumeIsLocalKey, str)
        self.assertIsInstance(CoreFoundation.kCFURLVolumeIsReadOnlyKey, str)
        self.assertIsInstance(CoreFoundation.kCFURLVolumeCreationDateKey, str)
        self.assertIsInstance(CoreFoundation.kCFURLVolumeURLForRemountingKey, str)
        self.assertIsInstance(CoreFoundation.kCFURLVolumeUUIDStringKey, str)
        self.assertIsInstance(CoreFoundation.kCFURLVolumeNameKey, str)
        self.assertIsInstance(CoreFoundation.kCFURLVolumeLocalizedNameKey, str)
        self.assertIsInstance(CoreFoundation.kCFURLIsUbiquitousItemKey, str)
        self.assertIsInstance(
            CoreFoundation.kCFURLUbiquitousItemHasUnresolvedConflictsKey, str
        )
        self.assertIsInstance(CoreFoundation.kCFURLUbiquitousItemIsDownloadedKey, str)
        self.assertIsInstance(CoreFoundation.kCFURLUbiquitousItemIsDownloadingKey, str)
        self.assertIsInstance(CoreFoundation.kCFURLUbiquitousItemIsUploadedKey, str)
        self.assertIsInstance(CoreFoundation.kCFURLUbiquitousItemIsUploadingKey, str)
        self.assertIsInstance(
            CoreFoundation.kCFURLUbiquitousItemPercentDownloadedKey, str
        )
        self.assertIsInstance(
            CoreFoundation.kCFURLUbiquitousItemPercentUploadedKey, str
        )

    @min_os_level("10.12")
    def testConstants10_12(self):
        self.assertIsInstance(CoreFoundation.kCFURLVolumeLocalizedNameKey, str)
        self.assertIsInstance(CoreFoundation.kCFURLVolumeIsEncryptedKey, str)
        self.assertIsInstance(CoreFoundation.kCFURLVolumeIsRootFileSystemKey, str)
        self.assertIsInstance(CoreFoundation.kCFURLVolumeSupportsCompressionKey, str)
        self.assertIsInstance(CoreFoundation.kCFURLVolumeSupportsFileCloningKey, str)
        self.assertIsInstance(CoreFoundation.kCFURLVolumeSupportsSwapRenamingKey, str)
        self.assertIsInstance(
            CoreFoundation.kCFURLVolumeSupportsExclusiveRenamingKey, str
        )

    @min_os_level("10.13")
    def testConstants10_13(self):
        self.assertIsInstance(
            CoreFoundation.kCFURLVolumeAvailableCapacityForImportantUsageKey, str
        )
        self.assertIsInstance(
            CoreFoundation.kCFURLVolumeAvailableCapacityForOpportunisticUsageKey, str
        )
        self.assertIsInstance(CoreFoundation.kCFURLVolumeSupportsImmutableFilesKey, str)
        self.assertIsInstance(
            CoreFoundation.kCFURLVolumeSupportsAccessPermissionsKey, str
        )

    @min_os_level("11.0")
    def testConstants11_0(self):
        self.assertIsInstance(CoreFoundation.kCFURLFileContentIdentifierKey, str)
        self.assertIsInstance(CoreFoundation.kCFURLMayShareFileContentKey, str)
        self.assertIsInstance(CoreFoundation.kCFURLMayHaveExtendedAttributesKey, str)
        self.assertIsInstance(CoreFoundation.kCFURLIsPurgeableKey, str)
        self.assertIsInstance(CoreFoundation.kCFURLIsSparseKey, str)
        self.assertIsInstance(CoreFoundation.kCFURLLinkCountKey, str)
        self.assertIsInstance(CoreFoundation.kCFURLVolumeSupportsFileProtectionKey, str)

    @min_os_level("11.3")
    def testConstants11_3(self):
        self.assertIsInstance(
            CoreFoundation.kCFURLUbiquitousItemIsExcludedFromSyncKey, str
        )

    @min_os_level("10.9")
    def testFunctions10_9(self):
        self.assertResultIsBOOL(CoreFoundation.CFURLIsFileReferenceURL)
