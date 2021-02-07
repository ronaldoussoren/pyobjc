import Quartz
from PyObjCTools.TestSupport import TestCase, min_os_level

CGDisplayStreamFrameAvailableHandler = b"vIQ@@"


class TestCGDisplayStream(TestCase):
    @min_os_level("10.8")
    def testTypes10_8(self):
        self.assertIsCFType(Quartz.CGDisplayStreamRef)
        self.assertIsCFType(Quartz.CGDisplayStreamUpdateRef)

    @min_os_level("10.8")
    def testConstants10_8(self):
        self.assertEqual(Quartz.kCGDisplayStreamUpdateRefreshedRects, 0)
        self.assertEqual(Quartz.kCGDisplayStreamUpdateMovedRects, 1)
        self.assertEqual(Quartz.kCGDisplayStreamUpdateDirtyRects, 2)
        self.assertEqual(Quartz.kCGDisplayStreamUpdateReducedDirtyRects, 3)

        self.assertEqual(Quartz.kCGDisplayStreamFrameStatusFrameComplete, 0)
        self.assertEqual(Quartz.kCGDisplayStreamFrameStatusFrameIdle, 1)
        self.assertEqual(Quartz.kCGDisplayStreamFrameStatusFrameBlank, 2)
        self.assertEqual(Quartz.kCGDisplayStreamFrameStatusStopped, 3)

        self.assertIsInstance(Quartz.kCGDisplayStreamSourceRect, str)
        self.assertIsInstance(Quartz.kCGDisplayStreamDestinationRect, str)
        self.assertIsInstance(Quartz.kCGDisplayStreamPreserveAspectRatio, str)
        self.assertIsInstance(Quartz.kCGDisplayStreamColorSpace, str)
        self.assertIsInstance(Quartz.kCGDisplayStreamMinimumFrameTime, str)
        self.assertIsInstance(Quartz.kCGDisplayStreamShowCursor, str)
        self.assertIsInstance(Quartz.kCGDisplayStreamQueueDepth, str)
        self.assertIsInstance(Quartz.kCGDisplayStreamYCbCrMatrix, str)
        self.assertIsInstance(Quartz.kCGDisplayStreamYCbCrMatrix_ITU_R_709_2, str)
        self.assertIsInstance(Quartz.kCGDisplayStreamYCbCrMatrix_ITU_R_601_4, str)
        self.assertIsInstance(Quartz.kCGDisplayStreamYCbCrMatrix_SMPTE_240M_1995, str)

    @min_os_level("10.8")
    def testFunctions10_8(self):
        self.assertIsInstance(Quartz.CGDisplayStreamUpdateGetTypeID(), int)
        self.assertIsInstance(Quartz.CGDisplayStreamGetTypeID(), int)

        self.assertResultSizeInArg(Quartz.CGDisplayStreamUpdateGetRects, 2)
        self.assertArgIsOut(Quartz.CGDisplayStreamUpdateGetRects, 2)

        Quartz.CGDisplayStreamUpdateCreateMergedUpdate  # XXX: test using actual call

        self.assertArgIsOut(Quartz.CGDisplayStreamUpdateGetMovedRectsDelta, 1)
        self.assertArgIsOut(Quartz.CGDisplayStreamUpdateGetMovedRectsDelta, 2)

        Quartz.CGDisplayStreamUpdateGetDropCount  # XXX

        self.assertResultIsCFRetained(Quartz.CGDisplayStreamCreate)
        self.assertArgIsBlock(
            Quartz.CGDisplayStreamCreate, 5, CGDisplayStreamFrameAvailableHandler
        )

        self.assertResultIsCFRetained(Quartz.CGDisplayStreamCreateWithDispatchQueue)
        self.assertArgIsBlock(
            Quartz.CGDisplayStreamCreateWithDispatchQueue,
            6,
            CGDisplayStreamFrameAvailableHandler,
        )

        Quartz.CGDisplayStreamStart  # XXX
        Quartz.CGDisplayStreamStop  # XXX

        Quartz.CGDisplayStreamGetRunLoopSource  # XXX
