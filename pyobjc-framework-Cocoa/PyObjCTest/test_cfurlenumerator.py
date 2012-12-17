from PyObjCTools.TestSupport import *
from CoreFoundation import *
import os

try:
    long
except NameError:
    long = int


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

        self.assertResultIsBOOL(CFURLEnumeratorGetSourceDidChange)
        v = CFURLEnumeratorGetSourceDidChange(ref)
        self.assertIsInstance(v, bool)


    @min_os_level('10.6')
    def testConstants(self):
        self.assertEqual(kCFURLEnumeratorDefaultBehavior, 0)
        self.assertEqual(kCFURLEnumeratorDescendRecursively, 1<<0)
        self.assertEqual(kCFURLEnumeratorSkipInvisibles, 1<<1)
        self.assertEqual(kCFURLEnumeratorGenerateFileReferenceURLs, 1<<2)
        self.assertEqual(kCFURLEnumeratorSkipPackageContents, 1<<3)
        self.assertEqual(kCFURLEnumeratorIncludeDirectoriesPreOrder, 1<<4)
        self.assertEqual(kCFURLEnumeratorIncludeDirectoriesPostOrder, 1<<5)
        self.assertEqual(kCFURLEnumeratorSuccess, 1)
        self.assertEqual(kCFURLEnumeratorEnd, 2)
        self.assertEqual(kCFURLEnumeratorError, 3)
        self.assertEqual(kCFURLEnumeratorDirectoryPostOrderSuccess, 4)


if __name__ == "__main__":
    main()
