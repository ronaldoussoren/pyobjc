from PyObjCTools.TestSupport import *

import Metal

class TestMTLComputeCommandEncoderHelp (Metal.NSObject):
    def dispatchType(self): return 1
    def setBytes_length_atIndex_(self, a, b, c): pass
    def setBuffer_offset_atIndex_(self, a, b, c): pass
    def setBufferOffset_atIndex_(self, a, b): pass
    def setBuffers_offsets_withRange_(self, a, b, c): pass
    def setTexture_atIndex_(self, a, b): pass
    def setTextures_withRange_(self, a, b): pass
    def setSamplerState_atIndex_(self, a, b): pass
    def setSamplerStates_withRange_(self, a, b): pass


class TestMTLComputeCommandEncoder (TestCase):
    def test_structs(self):
        v = Metal.MTLDispatchThreadgroupsIndirectArguments()
        self.assertEqual(v.threadgroupsPerGrid, None)

        v = Metal.MTLStageInRegionIndirectArguments()
        self.assertEqual(v.stageInOrigin, None)
        self.assertEqual(v.stageInSize, None)

    @min_sdk_level('10.11')
    def test_protocols(self):
        objc.protocolNamed('MTLComputeCommandEncoder')

    def test_methods(self):
        self.assertResultHasType(TestMTLComputeCommandEncoderHelper.dispatchType, objc._C_NSUinteger)

        self.assertArgHasType(TestMTLComputeCommandEncoderHelper.setBytes_length_atIndex_, 0, objc._C_IN + objc._C_PTR + objc._C_VOID)
        self.assertArgSizeInArg(TestMTLComputeCommandEncoderHelper.setBytes_length_atIndex_, 0, 1)
        self.assertArgHasType(TestMTLComputeCommandEncoderHelper.setBytes_length_atIndex_, 1, objc._C_NSUInteger)
        self.assertArgHasType(TestMTLComputeCommandEncoderHelper.setBytes_length_atIndex_, 2, objc._C_NSUInteger)

        self.assertArgHasType(TestMTLComputeCommandEncoderHelper.setBuffer_offset_atIndex_, 1, objc._C_NSUInteger)
        self.assertArgHasType(TestMTLComputeCommandEncoderHelper.setBuffer_offset_atIndex_, 2, objc._C_NSUInteger)

        self.assertArgHasType(TestMTLComputeCommandEncoderHelper.setBufferOffset_atIndex_, 1, objc._C_NSUInteger)
        self.assertArgHasType(TestMTLComputeCommandEncoderHelper.setBufferOffset_atIndex_, 2, objc._C_NSUInteger)

        self.assertArgHasType(TestMTLComputeCommandEncoderHelper.setBuffers_offsets_withRange_, 0, b'n^@')
        self.assertArgSizeInArg(TestMTLComputeCommandEncoderHelper.setBuffers_offsets_withRange_, 0, 2)
        self.assertArgHasType(TestMTLComputeCommandEncoderHelper.setBuffers_offsets_withRange_, 1, b'n^' + objc._C_NSUInteger)
        self.assertArgSizeInArg(TestMTLComputeCommandEncoderHelper.setBuffers_offsets_withRange_, 1, 2)
        self.assertArgHasType(TestMTLComputeCommandEncoderHelper.setBuffers_offsets_withRange_, 2, Metal.NSRange.__typestr__)

        self.assertArgHasType(TestMTLComputeCommandEncoderHelper.setTexture_atIndex_, 1, objc._C_NSUInteger)

        self.assertArgHasType(TestMTLComputeCommandEncoderHelper.setTextures_withRange_, 0, b'n^@')
        self.assertArgSizeInArg(TestMTLComputeCommandEncoderHelper.setTextures_withRange_, 0, 1)
        self.assertArgHasType(TestMTLComputeCommandEncoderHelper.setTextures_withRange_, 1, Metal.NSRange.__typestr__)

        self.assertArgHasType(TestMTLComputeCommandEncoderHelper.setSamplerState_atIndex_, 1, objc._C_NSUInteger)

        self.assertArgHasType(TestMTLComputeCommandEncoderHelper.setSamplerStates_withRange_, 0, b'n^@')
        self.assertArgSizeInArg(TestMTLComputeCommandEncoderHelper.setSamplerStates_withRange_, 0, 1)
        self.assertArgHasType(TestMTLComputeCommandEncoderHelper.setSamplerStates_withRange_, 1, Metal.NSRange.__typestr__)

"""
- (void)setSamplerStates:(const id <MTLSamplerState> __nullable [__nonnull])samplers lodMinClamps:(const float [__nonnull])lodMinClamps lodMaxClamps:(const float [__nonnull])lodMaxClamps withRange:(NSRange)range;

- (void)setThreadgroupMemoryLength:(NSUInteger)length atIndex:(NSUInteger)index;

- (void)setStageInRegion:(MTLRegion)region API_AVAILABLE(macos(10.12), ios(10.0));

- (void)setStageInRegionWithIndirectBuffer:(id <MTLBuffer>)indirectBuffer indirectBufferOffset:(NSUInteger)indirectBufferOffset API_AVAILABLE(macos(10.14), ios(12.0));

- (void)dispatchThreadgroups:(MTLSize)threadgroupsPerGrid threadsPerThreadgroup:(MTLSize)threadsPerThreadgroup;


- (void)dispatchThreadgroupsWithIndirectBuffer:(id <MTLBuffer>)indirectBuffer indirectBufferOffset:(NSUInteger)indirectBufferOffset threadsPerThreadgroup:(MTLSize)threadsPerThreadgroup API_AVAILABLE(macos(10.11), ios(9.0));


- (void)dispatchThreads:(MTLSize)threadsPerGrid threadsPerThreadgroup:(MTLSize)threadsPerThreadgroup API_AVAILABLE(macos(10.13), ios(11.0)) API_UNAVAILABLE(tvos);

- (void)useResource:(id <MTLResource>)resource usage:(MTLResourceUsage)usage API_AVAILABLE(macos(10.13), ios(11.0));

- (void)useResources:(const id <MTLResource> __nonnull[__nonnull])resources count:(NSUInteger)count usage:(MTLResourceUsage)usage API_AVAILABLE(macos(10.13), ios(11.0));

- (void)useHeaps:(const id <MTLHeap> __nonnull[__nonnull])heaps count:(NSUInteger)count API_AVAILABLE(macos(10.13), ios(11.0));

-(void)memoryBarrierWithScope:(MTLBarrierScope)scope API_AVAILABLE(macos(10.14), ios(12.0));

- (void)memoryBarrierWithResources:(const id<MTLResource> __nonnull [__nonnull])resources count:(NSUInteger)count API_AVAILABLE(macos(10.14), ios(12.0));

-(void)sampleCountersInBuffer:(id<MTLCounterSampleBuffer>)sampleBuffer
                atSampleIndex:(NSUInteger)sampleIndex
                  withBarrier:(BOOL)barrier API_AVAILABLE(macos(10.15)) API_UNAVAILABLE(ios);

"""
