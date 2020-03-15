import os

import CoreFoundation
from PyObjCTools.TestSupport import TestCase, min_os_level


class TestCFURLEnumerator(TestCase):
    @min_os_level("10.6")
    def testTypes(self):
        self.assertIsCFType(CoreFoundation.CFURLEnumeratorRef)

    @min_os_level("10.6")
    def testFunctions(self):
        v = CoreFoundation.CFURLEnumeratorGetTypeID()
        self.assertIsInstance(v, int)

        ref = CoreFoundation.CFURLEnumeratorCreateForDirectoryURL(
            None,
            CoreFoundation.CFURLCreateWithFileSystemPath(
                None, os.path.expanduser("~"), CoreFoundation.kCFURLPOSIXPathStyle, True
            ),
            CoreFoundation.kCFURLEnumeratorDefaultBehavior,
            [CoreFoundation.kCFURLNameKey],
        )
        self.assertIsInstance(ref, CoreFoundation.CFURLEnumeratorRef)

        ref = CoreFoundation.CFURLEnumeratorCreateForMountedVolumes(
            None, CoreFoundation.kCFURLEnumeratorDefaultBehavior, None
        )  # [kCFURLNameKey])
        self.assertIsInstance(ref, CoreFoundation.CFURLEnumeratorRef)

        self.assertArgIsOut(CoreFoundation.CFURLEnumeratorGetNextURL, 1)
        self.assertArgIsOut(CoreFoundation.CFURLEnumeratorGetNextURL, 2)
        sts, url, err = CoreFoundation.CFURLEnumeratorGetNextURL(ref, None, None)
        self.assertEqual(sts, CoreFoundation.kCFURLEnumeratorSuccess)
        self.assertIsInstance(url, CoreFoundation.CFURLRef)
        self.assertEqual(err, None)

        lvl = CoreFoundation.CFURLEnumeratorGetDescendentLevel(ref)
        self.assertIsInstance(lvl, int)

        CoreFoundation.CFURLEnumeratorSkipDescendents(ref)

        self.assertResultIsBOOL(CoreFoundation.CFURLEnumeratorGetSourceDidChange)
        v = CoreFoundation.CFURLEnumeratorGetSourceDidChange(ref)
        self.assertIsInstance(v, bool)

    @min_os_level("10.6")
    def testConstants(self):
        self.assertEqual(CoreFoundation.kCFURLEnumeratorDefaultBehavior, 0)
        self.assertEqual(CoreFoundation.kCFURLEnumeratorDescendRecursively, 1 << 0)
        self.assertEqual(CoreFoundation.kCFURLEnumeratorSkipInvisibles, 1 << 1)
        self.assertEqual(
            CoreFoundation.kCFURLEnumeratorGenerateFileReferenceURLs, 1 << 2
        )
        self.assertEqual(CoreFoundation.kCFURLEnumeratorSkipPackageContents, 1 << 3)
        self.assertEqual(
            CoreFoundation.kCFURLEnumeratorIncludeDirectoriesPreOrder, 1 << 4
        )
        self.assertEqual(
            CoreFoundation.kCFURLEnumeratorIncludeDirectoriesPostOrder, 1 << 5
        )
        self.assertEqual(
            CoreFoundation.kCFURLEnumeratorGenerateRelativePathURLs, 1 << 6
        )
        self.assertEqual(CoreFoundation.kCFURLEnumeratorSuccess, 1)
        self.assertEqual(CoreFoundation.kCFURLEnumeratorEnd, 2)
        self.assertEqual(CoreFoundation.kCFURLEnumeratorError, 3)
        self.assertEqual(CoreFoundation.kCFURLEnumeratorDirectoryPostOrderSuccess, 4)
