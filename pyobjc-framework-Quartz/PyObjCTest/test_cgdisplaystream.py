from PyObjCTools.TestSupport import *

import Quartz

CGDisplayStreamFrameAvailableHandler = b'vIQ@@'

try:
    long
except NameError:
    long = int

try:
    unicode
except NameError:
    unicode = str

class TestCGDisplayStream (TestCase):
    @min_os_level('10.8')
    def testTypes10_8(self):
        self.assertIsCFType(Quartz.CGDisplayStreamRef)
        self.assertIsCFType(Quartz.CGDisplayStreamUpdateRef)

    @min_os_level('10.8')
    def testConstants10_8(self):
        self.assertEqual(Quartz.kCGDisplayStreamUpdateRefreshedRects, 0)
        self.assertEqual(Quartz.kCGDisplayStreamUpdateMovedRects, 1)
        self.assertEqual(Quartz.kCGDisplayStreamUpdateDirtyRects, 2)
        self.assertEqual(Quartz.kCGDisplayStreamUpdateReducedDirtyRects, 3)

        self.assertEqual(Quartz.kCGDisplayStreamFrameStatusFrameComplete, 0)
        self.assertEqual(Quartz.kCGDisplayStreamFrameStatusFrameIdle, 1)
        self.assertEqual(Quartz.kCGDisplayStreamFrameStatusFrameBlank, 2)
        self.assertEqual(Quartz.kCGDisplayStreamFrameStatusStopped, 3)

        self.assertIsInstance(Quartz.kCGDisplayStreamSourceRect, unicode)
        self.assertIsInstance(Quartz.kCGDisplayStreamPreserveAspectRatio, unicode)
        self.assertIsInstance(Quartz.kCGDisplayStreamColorSpace, unicode)
        self.assertIsInstance(Quartz.kCGDisplayStreamMinimumFrameTime, unicode)
        self.assertIsInstance(Quartz.kCGDisplayStreamShowCursor, unicode)
        self.assertIsInstance(Quartz.kCGDisplayStreamQueueDepth, unicode)
        self.assertIsInstance(Quartz.kCGDisplayStreamYCbCrMatrix, unicode)
        self.assertIsInstance(Quartz.kCGDisplayStreamYCbCrMatrix_ITU_R_709_2, unicode)
        self.assertIsInstance(Quartz.kCGDisplayStreamYCbCrMatrix_ITU_R_601_4, unicode)
        self.assertIsInstance(Quartz.kCGDisplayStreamYCbCrMatrix_SMPTE_240M_1995, unicode)

    @min_os_level('10.8')
    def testFunctions10_8(self):
        self.assertIsInstance(Quartz.CGDisplayStreamUpdateGetTypeID(), (int, long))
        self.assertIsInstance(Quartz.CGDisplayStreamGetTypeID(), (int, long))

        self.assertResultSizeInArg(Quartz.CGDisplayStreamUpdateGetRects, 2)
        self.assertArgIsOut(Quartz.CGDisplayStreamUpdateGetRects, 2)

        Quartz.CGDisplayStreamUpdateCreateMergedUpdate # XXX: test using actual call

        self.assertArgIsOut(Quartz.CGDisplayStreamUpdateGetMovedRectsDelta, 1)
        self.assertArgIsOut(Quartz.CGDisplayStreamUpdateGetMovedRectsDelta, 2)

        Quartz.CGDisplayStreamUpdateGetDropCount # XXX

        self.assertResultIsCFRetained(Quartz.CGDisplayStreamCreate)
        self.assertArgIsBlock(Quartz.CGDisplayStreamCreate, 5, CGDisplayStreamFrameAvailableHandler)

        self.assertResultIsCFRetained(Quartz.CGDisplayStreamCreateWithDispatchQueue)
        self.assertArgIsBlock(Quartz.CGDisplayStreamCreateWithDispatchQueue, 6, CGDisplayStreamFrameAvailableHandler)

        Quartz.CGDisplayStreamStart # XXX
        Quartz.CGDisplayStreamStop # XXX

        Quartz.CGDisplayStreamGetRunLoopSource # XXX

if __name__ == "__main__":
    main()
