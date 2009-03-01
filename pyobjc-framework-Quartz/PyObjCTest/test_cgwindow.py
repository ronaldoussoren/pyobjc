
from PyObjCTools.TestSupport import *
from Quartz.CoreGraphics import *

class TestCGWindow (TestCase):
    def testConstants(self):
        self.failUnlessEqual(kCGWindowIDCFNumberType, kCFNumberSInt32Type)
        self.failUnlessEqual(kCGNullWindowID, 0)
        self.failUnlessEqual(kCGWindowSharingNone, 0)
        self.failUnlessEqual(kCGWindowSharingReadOnly, 1)
        self.failUnlessEqual(kCGWindowSharingReadWrite, 2)
        self.failUnlessEqual(kCGBackingStoreRetained, 0)
        self.failUnlessEqual(kCGBackingStoreNonretained, 1)
        self.failUnlessEqual(kCGBackingStoreBuffered, 2)

        self.failUnlessIsInstance(kCGWindowNumber, unicode)
        self.failUnlessIsInstance(kCGWindowStoreType, unicode)
        self.failUnlessIsInstance(kCGWindowLayer, unicode)
        self.failUnlessIsInstance(kCGWindowBounds, unicode)
        self.failUnlessIsInstance(kCGWindowSharingState, unicode)
        self.failUnlessIsInstance(kCGWindowAlpha, unicode)
        self.failUnlessIsInstance(kCGWindowOwnerPID, unicode)
        self.failUnlessIsInstance(kCGWindowMemoryUsage, unicode)
        self.failUnlessIsInstance(kCGWindowWorkspace, unicode)
        self.failUnlessIsInstance(kCGWindowOwnerName, unicode)
        self.failUnlessIsInstance(kCGWindowName, unicode)
        self.failUnlessIsInstance(kCGWindowIsOnscreen, unicode)
        self.failUnlessIsInstance(kCGWindowBackingLocationVideoMemory, unicode)

        self.failUnlessEqual(kCGWindowListOptionAll, 0)
        self.failUnlessEqual(kCGWindowListOptionOnScreenOnly, (1 << 0))
        self.failUnlessEqual(kCGWindowListOptionOnScreenAboveWindow, (1 << 1))
        self.failUnlessEqual(kCGWindowListOptionOnScreenBelowWindow, (1 << 2))
        self.failUnlessEqual(kCGWindowListOptionIncludingWindow, (1 << 3))
        self.failUnlessEqual(kCGWindowListExcludeDesktopElements, (1 << 4))

        self.failUnlessEqual(kCGWindowImageDefault, 0)
        self.failUnlessEqual(kCGWindowImageBoundsIgnoreFraming, (1 << 0))
        self.failUnlessEqual(kCGWindowImageShouldBeOpaque, (1 << 1))
        self.failUnlessEqual(kCGWindowImageOnlyShadows, (1 << 2))


    def testFunctions(self):

        self.failUnlessResultIsCFRetained(CGWindowListCopyWindowInfo)
        v = CGWindowListCopyWindowInfo(0, 0)
        self.failUnlessIsInstance(v, CFArrayRef)
        self.failUnless(len(v) > 0)
        self.failUnlessIsInstance(v[0], CFDictionaryRef)

        v = CGWindowListCreate(0, 0)
        self.failUnlessIsInstance(v, tuple)
        self.failUnless(len(v) > 0)
        self.failUnlessIsInstance(v[0], (int, long))

        aWindowID = v[0]
        windowArray = v

        v = CGWindowListCreateDescriptionFromArray(v)
        self.failUnlessIsInstance(v, CFArrayRef)
        self.failUnless(len(v) > 0)
        self.failUnlessIsInstance(v[0], CFDictionaryRef)

        self.failUnlessResultIsCFRetained(CGWindowListCreateImage)
        v = CGWindowListCreateImage(((0, 0), (100, 100)), aWindowID, 0, 0)
        self.failUnlessIsInstance(v, CGImageRef)

        v = CGWindowListCreateImageFromArray(((0, 0), (100, 100)), windowArray, 0)
        self.failUnlessIsInstance(v, CGImageRef)

if __name__ == "__main__":
    main()
