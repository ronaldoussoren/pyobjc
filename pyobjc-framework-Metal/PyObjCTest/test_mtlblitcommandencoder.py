from PyObjCTools.TestSupport import *

import Metal

class TestMTLBlitCommandEncoderHelper (Metal.NSObject):
    def synchronizeTexture_slice_level_(self, a, b, c): pass
    def copyFromTexture_sourceSlice_sourceLevel_sourceOrigin_sourceSize_toTexture_destinationSlice_destinationLevel_destinationOrigin_(self, a, b, c, d, e, f, g, h, i): pass
    def copyFromBuffer_sourceOffset_sourceBytesPerRow_sourceBytesPerImage_sourceSize_toTexture_destinationSlice_destinationLevel_destinationOrigin_(self, a, b, c, d, e, f, g, h, i): pass
    def copyFromBuffer_sourceOffset_sourceBytesPerRow_sourceBytesPerImage_sourceSize_toTexture_destinationSlice_destinationLevel_destinationOrigin_(self, a, b, c, d, e, f, g, h, i): pass

class TestMTLBlitCommandEncoder (TestCase):
    def test_constants(self):
        self.assertEqual(Metal.MTLBlitOptionNone, 0)
        self.assertEqual(Metal.MTLBlitOptionDepthFromDepthStencil, 1 << 0)
        self.assertEqual(Metal.MTLBlitOptionStencilFromDepthStencil, 1 << 1)
        self.assertEqual(Metal.MTLBlitOptionRowLinearPVRTC, 1 << 2)

    @min_sdk_level('10.11')
    def test_protocols10_11(self):
        objc.protocolNamed('MTLBlitCommandEncoder')

    def test_methods(self):
        self.assertArgHasType(TestMTLBlitCommandEncoderHelper.synchronizeTexture_slice_level_, 1, objc._C_NSUInteger)
        self.assertArgHasType(TestMTLBlitCommandEncoderHelper.synchronizeTexture_slice_level_, 2, objc._C_NSUInteger)

        self.assertArgHasType(TestMTLBlitCommandEncoderHelper.copyFromTexture_sourceSlice_sourceLevel_sourceOrigin_sourceSize_toTexture_destinationSlice_destinationLevel_destinationOrigin_, 1, objc._C_NSUInteger)
        self.assertArgHasType(TestMTLBlitCommandEncoderHelper.copyFromTexture_sourceSlice_sourceLevel_sourceOrigin_sourceSize_toTexture_destinationSlice_destinationLevel_destinationOrigin_, 2, objc._C_NSUInteger)
        self.assertArgHasType(TestMTLBlitCommandEncoderHelper.copyFromTexture_sourceSlice_sourceLevel_sourceOrigin_sourceSize_toTexture_destinationSlice_destinationLevel_destinationOrigin_, 3, Metal.MTLOrigin.__typestr__)
        self.assertArgHasType(TestMTLBlitCommandEncoderHelper.copyFromTexture_sourceSlice_sourceLevel_sourceOrigin_sourceSize_toTexture_destinationSlice_destinationLevel_destinationOrigin_, 4, Metal.MTLSize.__typestr__)
        self.assertArgHasType(TestMTLBlitCommandEncoderHelper.copyFromTexture_sourceSlice_sourceLevel_sourceOrigin_sourceSize_toTexture_destinationSlice_destinationLevel_destinationOrigin_, 6, objc._C_NSUInteger)
        self.assertArgHasType(TestMTLBlitCommandEncoderHelper.copyFromTexture_sourceSlice_sourceLevel_sourceOrigin_sourceSize_toTexture_destinationSlice_destinationLevel_destinationOrigin_, 7, objc._C_NSUInteger)
        self.assertArgHasType(TestMTLBlitCommandEncoderHelper.copyFromTexture_sourceSlice_sourceLevel_sourceOrigin_sourceSize_toTexture_destinationSlice_destinationLevel_destinationOrigin_, 8, objc._C_NSUInteger)
        self.assertArgHasType(TestMTLBlitCommandEncoderHelper.copyFromTexture_sourceSlice_sourceLevel_sourceOrigin_sourceSize_toTexture_destinationSlice_destinationLevel_destinationOrigin_, 9, Metal.MTLOrigin.__typestr__)

        self.assertArgHasType(TestMTLBlitCommandEncoderHelper.copyFromBuffer_sourceOffset_sourceBytesPerRow_sourceBytesPerImage_sourceSize_toTexture_destinationSlice_destinationLevel_destinationOrigin_, 1)
        self.assertArgHasType(TestMTLBlitCommandEncoderHelper.copyFromBuffer_sourceOffset_sourceBytesPerRow_sourceBytesPerImage_sourceSize_toTexture_destinationSlice_destinationLevel_destinationOrigin_, 2)
        self.assertArgHasType(TestMTLBlitCommandEncoderHelper.copyFromBuffer_sourceOffset_sourceBytesPerRow_sourceBytesPerImage_sourceSize_toTexture_destinationSlice_destinationLevel_destinationOrigin_, 3, Metal.MTLOrigin.__typestr__)
        self.assertArgHasType(TestMTLBlitCommandEncoderHelper.copyFromBuffer_sourceOffset_sourceBytesPerRow_sourceBytesPerImage_sourceSize_toTexture_destinationSlice_destinationLevel_destinationOrigin_, 4, Metal.MTLSize.__typestr__)
        self.assertArgHasType(TestMTLBlitCommandEncoderHelper.copyFromBuffer_sourceOffset_sourceBytesPerRow_sourceBytesPerImage_sourceSize_toTexture_destinationSlice_destinationLevel_destinationOrigin_, 6)
        self.assertArgHasType(TestMTLBlitCommandEncoderHelper.copyFromBuffer_sourceOffset_sourceBytesPerRow_sourceBytesPerImage_sourceSize_toTexture_destinationSlice_destinationLevel_destinationOrigin_, 7, Metal.MTLOrigin.__typestr__)

        self.assertArgHasType(TestMTLBlitCommandEncoderHelper.copyFromBuffer_sourceOffset_sourceBytesPerRow_sourceBytesPerImage_sourceSize_toTexture_destinationSlice_destinationLevel_destinationOrigin_, 1, objc._C_NSUInteger)
        self.assertArgHasType(TestMTLBlitCommandEncoderHelper.copyFromBuffer_sourceOffset_sourceBytesPerRow_sourceBytesPerImage_sourceSize_toTexture_destinationSlice_destinationLevel_destinationOrigin_, 2, objc._C_NSUInteger)
        self.assertArgHasType(TestMTLBlitCommandEncoderHelper.copyFromBuffer_sourceOffset_sourceBytesPerRow_sourceBytesPerImage_sourceSize_toTexture_destinationSlice_destinationLevel_destinationOrigin_, 3, objc._C_NSUInteger)
        self.assertArgHasType(TestMTLBlitCommandEncoderHelper.copyFromBuffer_sourceOffset_sourceBytesPerRow_sourceBytesPerImage_sourceSize_toTexture_destinationSlice_destinationLevel_destinationOrigin_, 4, Metal.MTLSize.__typestr__)
        self.assertArgHasType(TestMTLBlitCommandEncoderHelper.copyFromBuffer_sourceOffset_sourceBytesPerRow_sourceBytesPerImage_sourceSize_toTexture_destinationSlice_destinationLevel_destinationOrigin_, 6, objc._C_NSUInteger)
        self.assertArgHasType(TestMTLBlitCommandEncoderHelper.copyFromBuffer_sourceOffset_sourceBytesPerRow_sourceBytesPerImage_sourceSize_toTexture_destinationSlice_destinationLevel_destinationOrigin_, 7, objc._C_NSUInteger)
        self.assertArgHasType(TestMTLBlitCommandEncoderHelper.copyFromBuffer_sourceOffset_sourceBytesPerRow_sourceBytesPerImage_sourceSize_toTexture_destinationSlice_destinationLevel_destinationOrigin_, 8, Metal.MTLOrigin.__typestr__)

        self.fail("")
"""
        - (void)copyFromBuffer:(id<MTLBuffer>)sourceBuffer sourceOffset:(NSUInteger)sourceOffset sourceBytesPerRow:(NSUInteger)sourceBytesPerRow sourceBytesPerImage:(NSUInteger)sourceBytesPerImage sourceSize:(MTLSize)sourceSize toTexture:(id<MTLTexture>)destinationTexture destinationSlice:(NSUInteger)destinationSlice destinationLevel:(NSUInteger)destinationLevel destinationOrigin:(MTLOrigin)destinationOrigin options:(MTLBlitOption)options API_AVAILABLE(macos(10.11), ios(9.0));

/*!
 @method copyFromTexture:sourceSlice:sourceLevel:sourceOrigin:sourceSize:toBuffer:destinationOffset:destinationBytesPerRow:destinationBytesPerImage:
 @abstract Copy an image from a texture into a buffer.
 */
- (void)copyFromTexture:(id<MTLTexture>)sourceTexture sourceSlice:(NSUInteger)sourceSlice sourceLevel:(NSUInteger)sourceLevel sourceOrigin:(MTLOrigin)sourceOrigin sourceSize:(MTLSize)sourceSize toBuffer:(id<MTLBuffer>)destinationBuffer destinationOffset:(NSUInteger)destinationOffset destinationBytesPerRow:(NSUInteger)destinationBytesPerRow destinationBytesPerImage:(NSUInteger)destinationBytesPerImage;

- (void)copyFromTexture:(id<MTLTexture>)sourceTexture sourceSlice:(NSUInteger)sourceSlice sourceLevel:(NSUInteger)sourceLevel sourceOrigin:(MTLOrigin)sourceOrigin sourceSize:(MTLSize)sourceSize toBuffer:(id<MTLBuffer>)destinationBuffer destinationOffset:(NSUInteger)destinationOffset destinationBytesPerRow:(NSUInteger)destinationBytesPerRow destinationBytesPerImage:(NSUInteger)destinationBytesPerImage options:(MTLBlitOption)options API_AVAILABLE(macos(10.11), ios(9.0));

- (void)fillBuffer:(id<MTLBuffer>)buffer range:(NSRange)range value:(uint8_t)value;

- (void)copyFromTexture:(id<MTLTexture>)sourceTexture sourceSlice:(NSUInteger)sourceSlice sourceLevel:(NSUInteger)sourceLevel
              toTexture:(id<MTLTexture>)destinationTexture destinationSlice:(NSUInteger)destinationSlice destinationLevel:(NSUInteger)destinationLevel
             sliceCount:(NSUInteger)sliceCount levelCount:(NSUInteger)levelCount API_AVAILABLE(macos(10.15), ios(13.0));

- (void)copyFromBuffer:(id <MTLBuffer>)sourceBuffer sourceOffset:(NSUInteger)sourceOffset toBuffer:(id <MTLBuffer>)destinationBuffer destinationOffset:(NSUInteger)destinationOffset size:(NSUInteger)size;

- (void)optimizeContentsForGPUAccess:(id<MTLTexture>)texture slice:(NSUInteger)slice level:(NSUInteger)level API_AVAILABLE(macos(10.14), ios(12.0));

- (void)optimizeContentsForCPUAccess:(id<MTLTexture>)texture slice:(NSUInteger)slice level:(NSUInteger)level API_AVAILABLE(macos(10.14), ios(12.0));

- (void) resetCommandsInBuffer: (id<MTLIndirectCommandBuffer>)buffer withRange:(NSRange)range API_AVAILABLE(macos(10.14), ios(12.0));

- (void)optimizeIndirectCommandBuffer:(id <MTLIndirectCommandBuffer>)indirectCommandBuffer withRange:(NSRange)range API_AVAILABLE(macos(10.14), ios(12.0));

-(void)sampleCountersInBuffer:(id<MTLCounterSampleBuffer>)sampleBuffer
                atSampleIndex:(NSUInteger)sampleIndex
                  withBarrier:(BOOL)barrier API_AVAILABLE(macos(10.15)) API_UNAVAILABLE(ios);

-(void)resolveCounters:(id<MTLCounterSampleBuffer>)sampleBuffer
               inRange:(NSRange)range
     destinationBuffer:(id<MTLBuffer>)destinationBuffer
     destinationOffset:(NSUInteger)destinationOffset API_AVAILABLE(macos(10.15)) API_UNAVAILABLE(ios);
     """
