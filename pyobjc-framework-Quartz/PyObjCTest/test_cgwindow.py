
from PyObjCTools.TestSupport import *
from Quartz.CoreGraphics import *

class TestCGWindow (TestCase):
    def testConstants(self):
        self.assertEqual(kCGWindowIDCFNumberType, kCFNumberSInt32Type)
        self.assertEqual(kCGNullWindowID, 0)
        self.assertEqual(kCGWindowSharingNone, 0)
        self.assertEqual(kCGWindowSharingReadOnly, 1)
        self.assertEqual(kCGWindowSharingReadWrite, 2)
        self.assertEqual(kCGBackingStoreRetained, 0)
        self.assertEqual(kCGBackingStoreNonretained, 1)
        self.assertEqual(kCGBackingStoreBuffered, 2)

        self.assertIsInstance(kCGWindowNumber, unicode)
        self.assertIsInstance(kCGWindowStoreType, unicode)
        self.assertIsInstance(kCGWindowLayer, unicode)
        self.assertIsInstance(kCGWindowBounds, unicode)
        self.assertIsInstance(kCGWindowSharingState, unicode)
        self.assertIsInstance(kCGWindowAlpha, unicode)
        self.assertIsInstance(kCGWindowOwnerPID, unicode)
        self.assertIsInstance(kCGWindowMemoryUsage, unicode)
        self.assertIsInstance(kCGWindowWorkspace, unicode)
        self.assertIsInstance(kCGWindowOwnerName, unicode)
        self.assertIsInstance(kCGWindowName, unicode)
        self.assertIsInstance(kCGWindowIsOnscreen, unicode)
        self.assertIsInstance(kCGWindowBackingLocationVideoMemory, unicode)

        self.assertEqual(kCGWindowListOptionAll, 0)
        self.assertEqual(kCGWindowListOptionOnScreenOnly, (1 << 0))
        self.assertEqual(kCGWindowListOptionOnScreenAboveWindow, (1 << 1))
        self.assertEqual(kCGWindowListOptionOnScreenBelowWindow, (1 << 2))
        self.assertEqual(kCGWindowListOptionIncludingWindow, (1 << 3))
        self.assertEqual(kCGWindowListExcludeDesktopElements, (1 << 4))

        self.assertEqual(kCGWindowImageDefault, 0)
        self.assertEqual(kCGWindowImageBoundsIgnoreFraming, (1 << 0))
        self.assertEqual(kCGWindowImageShouldBeOpaque, (1 << 1))
        self.assertEqual(kCGWindowImageOnlyShadows, (1 << 2))


    def testFunctions(self):

        self.assertResultIsCFRetained(CGWindowListCopyWindowInfo)
        v = CGWindowListCopyWindowInfo(0, 0)
        self.assertIsInstance(v, CFArrayRef)
        self.assertTrue(len(v) > 0)
        self.assertIsInstance(v[0], CFDictionaryRef)

        v = CGWindowListCreate(0, 0)
        self.assertIsInstance(v, tuple)
        self.assertTrue(len(v) > 0)
        self.assertIsInstance(v[0], (int, long))

        aWindowID = v[0]
        windowArray = v

        v = CGWindowListCreateDescriptionFromArray(v)
        self.assertIsInstance(v, CFArrayRef)
        self.assertTrue(len(v) > 0)
        self.assertIsInstance(v[0], CFDictionaryRef)

        self.assertResultIsCFRetained(CGWindowListCreateImage)
        v = CGWindowListCreateImage(((0, 0), (100, 100)), aWindowID, 0, 0)
        self.assertIsInstance(v, CGImageRef)

        v = CGWindowListCreateImageFromArray(((0, 0), (100, 100)), windowArray, 0)
        self.assertIsInstance(v, CGImageRef)

if __name__ == "__main__":
    main()
