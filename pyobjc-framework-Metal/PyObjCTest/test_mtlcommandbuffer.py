from PyObjCTools.TestSupport import *

import Metal

MTLCommandBufferHandler = b"v@"


class TestMTLCommandBufferHelper(Metal.NSObject):
    def addScheduledHandler_(self, a):
        pass

    def retainedReferences(self):
        return 1

    def kernelStartTime(self):
        pass

    def kernelEndTime(self):
        pass

    def GPUStartTime(self):
        pass

    def GPUEndTime(self):
        pass

    def presentDrawable_atTime_(self, a, b):
        pass

    def addCompletedHandler_(self, a):
        pass

    def status(self):
        return 1

    def computeCommandEncoderWithDispatchType_(self, a):
        pass

    def encodeWaitForEvent_value_(self, a, b):
        pass

    def encodeSignalEvent_value_(self, a, b):
        pass


class TestMTLCommandBuffer(TestCase):
    def test_constants(self):
        self.assertEqual(Metal.MTLCommandBufferStatusNotEnqueued, 0)
        self.assertEqual(Metal.MTLCommandBufferStatusEnqueued, 1)
        self.assertEqual(Metal.MTLCommandBufferStatusCommitted, 2)
        self.assertEqual(Metal.MTLCommandBufferStatusScheduled, 3)
        self.assertEqual(Metal.MTLCommandBufferStatusCompleted, 4)
        self.assertEqual(Metal.MTLCommandBufferStatusError, 5)

        self.assertEqual(Metal.MTLCommandBufferErrorNone, 0)
        self.assertEqual(Metal.MTLCommandBufferErrorInternal, 1)
        self.assertEqual(Metal.MTLCommandBufferErrorTimeout, 2)
        self.assertEqual(Metal.MTLCommandBufferErrorPageFault, 3)
        self.assertEqual(Metal.MTLCommandBufferErrorBlacklisted, 4)
        self.assertEqual(Metal.MTLCommandBufferErrorNotPermitted, 7)
        self.assertEqual(Metal.MTLCommandBufferErrorOutOfMemory, 8)
        self.assertEqual(Metal.MTLCommandBufferErrorInvalidResource, 9)
        self.assertEqual(Metal.MTLCommandBufferErrorMemoryless, 10)
        self.assertEqual(Metal.MTLCommandBufferErrorDeviceRemoved, 11)

        self.assertEqual(Metal.MTLDispatchTypeSerial, 0)
        self.assertEqual(Metal.MTLDispatchTypeConcurrent, 1)

    @min_sdk_level("10.11")
    def test_protocols(self):
        objc.protocolNamed("MTLCommandBuffer")

    @min_os_level("10.11")
    def test_constants10_11(self):
        self.assertIsInstance(Metal.MTLCommandBufferErrorDomain, unicode)

    def test_methods(self):
        self.assertResultIsBOOL(TestMTLCommandBufferHelper.retainedReferences)

        self.assertResultHasType(
            TestMTLCommandBufferHelper.kernelStartTime, objc._C_DBL
        )
        self.assertResultHasType(TestMTLCommandBufferHelper.kernelEndTime, objc._C_DBL)

        self.assertResultHasType(TestMTLCommandBufferHelper.GPUStartTime, objc._C_DBL)
        self.assertResultHasType(TestMTLCommandBufferHelper.GPUEndTime, objc._C_DBL)

        self.assertArgIsBlock(
            TestMTLCommandBufferHelper.addScheduledHandler_, 0, MTLCommandBufferHandler
        )

        self.assertArgHasType(
            TestMTLCommandBufferHelper.presentDrawable_atTime_, 1, objc._C_DBL
        )

        self.assertArgIsBlock(
            TestMTLCommandBufferHelper.addCompletedHandler_, 0, MTLCommandBufferHandler
        )

        self.assertResultHasType(TestMTLCommandBufferHelper.status, objc._C_NSUInteger)

        self.assertArgHasType(
            TestMTLCommandBufferHelper.computeCommandEncoderWithDispatchType_,
            0,
            objc._C_NSUInteger,
        )

        self.assertArgHasType(
            TestMTLCommandBufferHelper.encodeWaitForEvent_value_, 1, objc._C_ULNGLNG
        )
        self.assertArgHasType(
            TestMTLCommandBufferHelper.encodeSignalEvent_value_, 1, objc._C_ULNGLNG
        )
