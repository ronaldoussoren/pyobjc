import Metal
from PyObjCTools.TestSupport import TestCase, min_os_level
import objc

MTLIOCommandBufferHandler = b"v@"


class TestMTLIOCommandBufferHelper(Metal.NSObject):
    def addCompletedHandler_(self, a):
        pass

    def loadBytes_size_sourceHandle_sourceHandleOffset_(self, a, b, c, d):
        pass

    def loadBuffer_offset_size_sourceHandle_sourceHandleOffset_(self, a, b, c, d, e):
        pass

    def loadTexture_slice_level_size_sourceBytesPerRow_sourceBytesPerImage_destinationOrigin_sourceHandle_sourceHandleOffset_(
        self, a, b, c, d, e, f, g, h, i
    ):
        pass

    def copyStatusToBuffer_offset_(self, a, b):
        pass

    def waitForEvent_value_(self, a, b):
        pass

    def signalEvent_value_(self, a, b):
        pass

    def status(self):
        return 1


class TestMTLIOCommandBuffer(TestCase):
    def test_constants(self):
        self.assertIsEnumType(Metal.MTLIOStatus)
        self.assertEqual(Metal.MTLIOStatusPending, 0)
        self.assertEqual(Metal.MTLIOStatusCancelled, 1)
        self.assertEqual(Metal.MTLIOStatusError, 2)
        self.assertEqual(Metal.MTLIOStatusComplete, 3)

    @min_os_level("13.0")
    def test_protocols(self):
        self.assertProtocolExists("MTLIOCommandBuffer")

    def test_protocol_methods(self):
        self.assertArgIsBlock(
            TestMTLIOCommandBufferHelper.addCompletedHandler_,
            0,
            MTLIOCommandBufferHandler,
        )

        self.assertArgHasType(
            TestMTLIOCommandBufferHelper.loadBytes_size_sourceHandle_sourceHandleOffset_,
            0,
            b"n^v",
        )
        self.assertArgHasType(
            TestMTLIOCommandBufferHelper.loadBytes_size_sourceHandle_sourceHandleOffset_,
            1,
            objc._C_NSUInteger,
        )
        self.assertArgHasType(
            TestMTLIOCommandBufferHelper.loadBytes_size_sourceHandle_sourceHandleOffset_,
            3,
            objc._C_NSUInteger,
        )

        self.assertArgHasType(
            TestMTLIOCommandBufferHelper.loadBuffer_offset_size_sourceHandle_sourceHandleOffset_,
            1,
            objc._C_NSUInteger,
        )
        self.assertArgHasType(
            TestMTLIOCommandBufferHelper.loadBuffer_offset_size_sourceHandle_sourceHandleOffset_,
            2,
            objc._C_NSUInteger,
        )
        self.assertArgHasType(
            TestMTLIOCommandBufferHelper.loadBuffer_offset_size_sourceHandle_sourceHandleOffset_,
            4,
            objc._C_NSUInteger,
        )

        self.assertArgHasType(
            TestMTLIOCommandBufferHelper.loadTexture_slice_level_size_sourceBytesPerRow_sourceBytesPerImage_destinationOrigin_sourceHandle_sourceHandleOffset_,
            1,
            objc._C_NSUInteger,
        )
        self.assertArgHasType(
            TestMTLIOCommandBufferHelper.loadTexture_slice_level_size_sourceBytesPerRow_sourceBytesPerImage_destinationOrigin_sourceHandle_sourceHandleOffset_,
            2,
            objc._C_NSUInteger,
        )
        self.assertArgHasType(
            TestMTLIOCommandBufferHelper.loadTexture_slice_level_size_sourceBytesPerRow_sourceBytesPerImage_destinationOrigin_sourceHandle_sourceHandleOffset_,
            3,
            Metal.MTLSize.__typestr__,
        )
        self.assertArgHasType(
            TestMTLIOCommandBufferHelper.loadTexture_slice_level_size_sourceBytesPerRow_sourceBytesPerImage_destinationOrigin_sourceHandle_sourceHandleOffset_,
            4,
            objc._C_NSUInteger,
        )
        self.assertArgHasType(
            TestMTLIOCommandBufferHelper.loadTexture_slice_level_size_sourceBytesPerRow_sourceBytesPerImage_destinationOrigin_sourceHandle_sourceHandleOffset_,
            5,
            objc._C_NSUInteger,
        )
        self.assertArgHasType(
            TestMTLIOCommandBufferHelper.loadTexture_slice_level_size_sourceBytesPerRow_sourceBytesPerImage_destinationOrigin_sourceHandle_sourceHandleOffset_,
            6,
            Metal.MTLOrigin.__typestr__,
        )
        self.assertArgHasType(
            TestMTLIOCommandBufferHelper.loadTexture_slice_level_size_sourceBytesPerRow_sourceBytesPerImage_destinationOrigin_sourceHandle_sourceHandleOffset_,
            8,
            objc._C_NSUInteger,
        )

        self.assertArgHasType(
            TestMTLIOCommandBufferHelper.copyStatusToBuffer_offset_,
            1,
            objc._C_NSUInteger,
        )

        self.assertArgHasType(
            TestMTLIOCommandBufferHelper.waitForEvent_value_, 1, objc._C_ULNG_LNG
        )

        self.assertArgHasType(
            TestMTLIOCommandBufferHelper.signalEvent_value_, 1, objc._C_ULNG_LNG
        )

        self.assertResultHasType(
            TestMTLIOCommandBufferHelper.status, objc._C_NSUInteger
        )
