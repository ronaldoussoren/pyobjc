import unittest
import array
from CoreFoundation import *
import os


class TestURL (unittest.TestCase):
    def testDummy(self):
        self.fail("CFURL tests not implemented yet")


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
        val = str(data)
        self.assertEquals(val, url)

        data = CFURLCreateData(None, ref, kCFStringEncodingUTF8, True)
        self.failUnless( isinstance(data, CFDataRef) )
        val = str(data)
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
        # CFURLCreateWithFileSystemPath
        # CFURLCreateFromFileSystemRepresentation
        # CFURLCreateWithFileSystemPathRelativeToBase
        # CFURLCreateFromFileSystemRepresentationRelativeToBase
        # CFURLGetFileSystemRepresentation
        pass

    def testParts(self):
        # CFURLGetBaseURL
        # CFURLCanBeDecomposed
        # CFURLCopyScheme
        # CFURLCopyNetLocation
        # CFURLCopyPath
        # CFURLCopyStrictPath
        # CFURLCopyFileSystemPath
        # CFURLHasDirectoryPath
        # CFURLCopyResourceSpecifier
        # CFURLCopyHostName
        # CFURLGetPortNumber
        # CFURLCopyUserName
        # CFURLCopyPassword
        # CFURLCopyParameterString
        # CFURLCopyQueryString
        # CFURLCopyFragment
        # CFURLCopyLastPathComponent
        # CFURLCopyPathExtension
        # CFURLGetBytes
        # CFURLGetByteRangeForComponent

        pass
        

    def testUpdating(self):
        # CFURLCreateCopyAppendingPathComponent
        # CFURLCreateCopyDeletingLastPathComponent
        # CFURLCreateCopyAppendingPathExtension
        # CFURLCreateCopyDeletingPathExtension
        pass

    def testStringEncoding(self):
        # CFURLGetString
        # CFURLCreateStringByReplacingPercentEscapes
        # CFURLCreateStringByReplacingPercentEscapesUsingEncoding
        # CFURLCreateStringByAddingPercentEscapes
        pass

    def testFSRef(self):
        try:
            from  Carbon.File import FSRef
        except ImportError:
            # Ignore this test when Carbon.File is not present
            return

        ref = CFURLCreateWithFileSystemPath(None, os.getcwd(), kCFURLPOSIXPathStyle, True)
        self.failUnless( isinstance(ref, CFURLRef) )

        ok, fsref = CFURLGetFSRef(ref, None)
        self.failUnless(ok)
        self.failUnless(isinstance(fsref, FSRef))
        self.failUnless( fsref.FSRefMakePath() ==  os.getcwd())

        ref2 = CFURLCreateFromFSRef(None, fsref)
        self.failUnless(ref is ref2) 

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
    unittest.main()
