from PyObjCTools.TestSupport import *
from CoreFoundation import *
import os

class TestCFURLEnumerator (TestCase):

    @min_os_level('10.6')
    def testTypes(self):
        self.assertIsCFType(CFURLEnumeratorRef)

    @min_os_level('10.6')
    def testFunctions(self):
        v = CFURLEnumeratorGetTypeID()
        self.assertIsInstance(v, (int, long))

        ref = CFURLEnumeratorCreateForDirectoryURL(None, 
                CFURLCreateWithFileSystemPath(None, os.path.expanduser('~'), kCFURLPOSIXPathStyle, True),
                kCFURLEnumeratorDefaultBehavior,
                [kCFURLNameKey])
        self.assertIsInstance(ref, CFURLEnumeratorRef)

        ref = CFURLEnumeratorCreateForMountedVolumes(
                None, kCFURLEnumeratorDefaultBehavior, [kCFURLNameKey])
        self.assertIsInstance(ref, CFURLEnumeratorRef)

        self.assertArgIsOut(CFURLEnumeratorGetNextURL, 1)
        self.assertArgIsOut(CFURLEnumeratorGetNextURL, 2)
        sts, url, err = CFURLEnumeratorGetNextURL(ref, None, None)
        self.assertEqual(sts, kCFURLEnumeratorSuccess)
        self.assertIsInstance(url, CFURLRef)
        self.assertEqual(err, None)

        lvl = CFURLEnumeratorGetDescendentLevel(ref)
        self.assertIsInstance(lvl, (int, long))

        CFURLEnumeratorSkipDescendents(ref)

        self.assertResultIsBool(CFURLEnumeratorGetSourceDidChange)
        v = CFURLEnumeratorGetSourceDidChange(ref)
        self.assertIsInstance(v, bool)


    @min_os_level('10.6')
    def testConstants(self):
        self.asertEqual(kCFURLEnumeratorDefaultBehavior, 0)
        self.asertEqual(kCFURLEnumeratorDescendRecursively, 1<<0)
        self.asertEqual(kCFURLEnumeratorSkipInvisibles, 1<<1)
        self.asertEqual(kCFURLEnumeratorGenerateFileReferenceURLs, 1<<2)
        self.asertEqual(kCFURLEnumeratorSkipPackageContents, 1<<3)
        self.asertEqual(kCFURLEnumeratorIncludeDirectoriesPreOrder, 1<<4)
        self.asertEqual(kCFURLEnumeratorIncludeDirectoriesPostOrder, 1<<5)
        self.asertEqual(kCFURLEnumeratorSuccess, 1)
        self.asertEqual(kCFURLEnumeratorEnd, 2)
        self.asertEqual(kCFURLEnumeratorError, 3)
        self.asertEqual(kCFURLEnumeratorDirectoryPostOrderSuccess, 4)



