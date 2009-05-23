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
        self.failUnless( isinstance(val, (int, long)) )

    def testCreateWithBytes(self):
        url = "http://www.omroep.nl/"

        ref = CFURLCreateWithBytes(None, url, len(url), kCFStringEncodingUTF8, None)
        self.failUnless( isinstance(ref, CFURLRef) )

        strval =  CFURLGetString(ref)
        self.failUnlessEqual(strval, unicode(url, "utf-8"))

        ref2 = CFURLCreateWithBytes(None, url, len(url), kCFStringEncodingUTF8, ref)
        self.failUnless( isinstance(ref2, CFURLRef) )

        a = array.array('c', 'http://www.nu.nl/')
        ref3 = CFURLCreateWithBytes(None, a, len(a), kCFStringEncodingUTF8, None)
        self.failUnless( isinstance(ref3, CFURLRef) )

        # Explictely test for unicode's buffer madness.
        self.failUnlessRaises((ValueError, TypeError), CFURLCreateWithBytes, None, unicode(url), len(url), kCFStringEncodingUTF8, None)

    def testCreateData(self):
        url = "http://www.omroep.nl/ blank"

        ref = CFURLCreateWithBytes(None, url, len(url), kCFStringEncodingUTF8, None)
        self.failUnless( isinstance(ref, CFURLRef) )

        data = CFURLCreateData(None, ref, kCFStringEncodingUTF8, False)
        self.failUnless( isinstance(data, CFDataRef) )
        val = CFDataGetBytes(data, (0, CFDataGetLength(data)), None)
        self.assertEquals(val, url.replace(' ', '%20'))

        data = CFURLCreateData(None, ref, kCFStringEncodingUTF8, True)
        self.failUnless( isinstance(data, CFDataRef) )
        val = CFDataGetBytes(data, (0, CFDataGetLength(data)), None)
        self.assertEquals(val, url.replace(' ', '%20'))

    def testCreateWithString(self):
        url = u"http://www.omroep.nl/"

        ref = CFURLCreateWithString(None, url, None)
        self.failUnless( isinstance(ref, CFURLRef) )

        strval =  CFURLGetString(ref)
        self.failUnlessEqual(strval, url)

        ref2 = CFURLCreateWithString(None, url, ref)
        self.failUnless( isinstance(ref2, CFURLRef) )

    def testCreateAbsolute(self):
        url = u"http://www.omroep.nl/sport/"
        baseref = CFURLCreateWithString(None, url, None)

        self.failUnlessArgHasType(CFURLCreateAbsoluteURLWithBytes, 1, 'n^v')
        self.failUnlessArgSizeInArg(CFURLCreateAbsoluteURLWithBytes, 1, 2)
        ref = CFURLCreateAbsoluteURLWithBytes(None, "socker", len("socker"), kCFStringEncodingUTF8, baseref, True)
        self.failUnless( isinstance(ref, CFURLRef) )

        strval =  CFURLGetString(ref)
        self.failUnlessEqual(strval, u"http://www.omroep.nl/sport/socker")

        relpath = "../../../dummy"
        ref = CFURLCreateAbsoluteURLWithBytes(None, relpath, len(relpath), kCFStringEncodingUTF8, baseref, True)
        self.failUnless( isinstance(ref, CFURLRef) )
        strval =  CFURLGetString(ref)
        self.failUnlessEqual(strval, u"http://www.omroep.nl/dummy")

        relpath = "../../../dummy"
        ref = CFURLCreateAbsoluteURLWithBytes(None, relpath, len(relpath), kCFStringEncodingUTF8, baseref, False)
        self.failUnless( isinstance(ref, CFURLRef) )
        strval =  CFURLGetString(ref)
        self.failUnlessEqual(strval, u"http://www.omroep.nl/../../dummy")


    def testCopyAbs(self):
        # CFURLCopyAbsoluteURL
        base = CFURLCreateWithString(None, u"http://www.omroep.nl/", None)
        self.failUnless( isinstance(base, CFURLRef) )

        ref = CFURLCreateWithString(None, u"/sport", base)
        self.failUnless( isinstance(ref, CFURLRef) )

        self.failUnless( CFURLGetString(ref) == u"/sport" )

        abs = CFURLCopyAbsoluteURL(ref)
        self.failUnless( isinstance(abs, CFURLRef) )
        self.failUnless( CFURLGetString(abs) == u"http://www.omroep.nl/sport" )

    def testPaths(self):
        url = CFURLCreateWithFileSystemPath(None,
                u"/tmp/", kCFURLPOSIXPathStyle, True)
        self.failUnless( isinstance(url, CFURLRef) )
        self.failUnless(CFURLHasDirectoryPath(url))

        url = CFURLCreateWithFileSystemPath(None,
                u"/etc/hosts", kCFURLPOSIXPathStyle, False)
        self.failUnless( isinstance(url, CFURLRef) )
        self.failIf(CFURLHasDirectoryPath(url))

        p = os.path.expanduser('~')
        self.failUnlessArgHasType(CFURLCreateFromFileSystemRepresentation, 1, 'n^t')
        self.failUnlessArgIsNullTerminated(CFURLCreateFromFileSystemRepresentation, 1)
        url = CFURLCreateFromFileSystemRepresentation(None,
                p, len(p), True)
        self.failUnless( isinstance(url, CFURLRef))
        self.assertRaises((ValueError, TypeError),
            CFURLCreateFromFileSystemRepresentation, None,
                u"/tmp/", 4, True)

        base = CFURLCreateWithFileSystemPath(None,
                u"/tmp", kCFURLPOSIXPathStyle, True)
        self.failUnless( isinstance(base, CFURLRef) )

        self.failUnlessArgIsBOOL(CFURLCreateWithFileSystemPathRelativeToBase, 3)
        url = CFURLCreateWithFileSystemPathRelativeToBase(None,
                u"filename", kCFURLPOSIXPathStyle, True, base)
        self.failUnless( isinstance(url, CFURLRef) )

        strval =  CFURLGetString(url)
        self.assertEquals(strval, u"filename/")


        self.failUnlessArgIsBOOL(CFURLCreateFromFileSystemRepresentationRelativeToBase, 3)
        url = CFURLCreateFromFileSystemRepresentationRelativeToBase(None,
                "filename2", 9, False, base)
        self.failUnless( isinstance(url, CFURLRef) )
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
        self.failUnless( isinstance(base, CFURLRef) )

        ref = CFURLCreateWithString(None, u"/sport", base)
        self.failUnless( isinstance(ref, CFURLRef) )

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
        self.assert_(isinstance(rng1, CFRange))
        self.assert_(isinstance(rng2, CFRange))
        

    def testUpdating(self):
        base = CFURLCreateWithString(None, u"http://www.omroep.nl/sport", None)
        self.failUnless( isinstance(base, CFURLRef) )

        url = CFURLCreateCopyAppendingPathComponent(None, base, "soccer", True)
        self.failUnless( isinstance(url, CFURLRef) )

        strval =  CFURLGetString(url)
        self.assertEquals(strval, "http://www.omroep.nl/sport/soccer/")

        url = CFURLCreateCopyDeletingLastPathComponent(None, base)
        self.failUnless( isinstance(url, CFURLRef) )
        strval =  CFURLGetString(url)
        self.assertEquals(strval, "http://www.omroep.nl/")

        url = CFURLCreateCopyAppendingPathExtension(None, base, "cgi")
        self.failUnless( isinstance(url, CFURLRef) )
        strval =  CFURLGetString(url)
        self.assertEquals(strval, "http://www.omroep.nl/sport.cgi")

        url2 = CFURLCreateCopyDeletingPathExtension(None, base)
        self.failUnless( isinstance(url2, CFURLRef) )
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
        self.failUnless( isinstance(ref, CFURLRef) )

        ok, fsref = CFURLGetFSRef(ref, None)
        self.failUnless(ok)
        self.failUnless(isinstance(fsref, objc.FSRef))
        self.failUnless( fsref.as_pathname() ==  os.getcwd())

        ref2 = CFURLCreateFromFSRef(None, fsref)
        self.failUnlessEqual(ref, ref2) 

    def testConstants(self):
        self.failUnless( kCFURLPOSIXPathStyle == 0 )
        self.failUnless( kCFURLHFSPathStyle == 1 )
        self.failUnless( kCFURLWindowsPathStyle == 2 )

        self.failUnless( kCFURLComponentScheme == 1 )
        self.failUnless( kCFURLComponentNetLocation == 2 )
        self.failUnless( kCFURLComponentPath == 3 )
        self.failUnless( kCFURLComponentResourceSpecifier == 4 )
        self.failUnless( kCFURLComponentUser == 5 )
        self.failUnless( kCFURLComponentPassword == 6 )
        self.failUnless( kCFURLComponentUserInfo == 7 )
        self.failUnless( kCFURLComponentHost == 8 )
        self.failUnless( kCFURLComponentPort == 9 )
        self.failUnless( kCFURLComponentParameterString == 10 )
        self.failUnless( kCFURLComponentQuery == 11 )
        self.failUnless( kCFURLComponentFragment == 12 )


if __name__ == "__main__":
    main()
