from PyObjCTools.TestSupport import *

import Metal

MTLDeviceNotificationHandler = b'v@@'
MTLNewLibraryCompletionHandler = b'v@@'
MTLNewRenderPipelineStateCompletionHandler = b'v@@'
MTLNewRenderPipelineStateWithReflectionCompletionHandler = b'v@@@'
MTLNewComputePipelineStateCompletionHandler = b'v@@'
MTLNewComputePipelineStateWithReflectionCompletionHandler = b'v@@@'


class TestMTLDeviceHelper (Metal.NSObject):
    def registryID(self): return 1
    def maxThreadsPerThreadgroup(self): return 1
    def isLowPower(self): return 1
    def isHeadless(self): return 1
    def isRemovable(self): return 1
    def hasUnifiedMemory(self): return 1
    def recommendedMaxWorkingSetSize(self): return 1
    def location(self): return 1
    def locationNumber(self): return 1
    def maxTransferRate(self): return 1
    def isDepth24Stencil8PixelFormatSupported(self): return 1
    def readWriteTextureSupport(self): return 1
    def argumentBuffersSupport(self): return 1
    def areRasterOrderGroupsSupported(self): return 1
    def areBarycentricCoordsSupported(self): return 1
    def supportsShaderBarycentricCoordinates(self): return 1
    def currentAllocatedSize(self): return 1
    def newCommandQueueWithMaxCommandBufferCount_(self, a): return 1
    def heapBufferSizeAndAlignWithLength_options_(self, a, b): return 1
    def newBufferWithLength_options_(self, a, b): return 1

class TestMTLDevice (TestCase):
    def test_constants(self):
        self.assertEqual(Metal.MTLFeatureSet_iOS_GPUFamily1_v1, 0)
        self.assertEqual(Metal.MTLFeatureSet_iOS_GPUFamily2_v1, 1)
        self.assertEqual(Metal.MTLFeatureSet_iOS_GPUFamily1_v2, 2)
        self.assertEqual(Metal.MTLFeatureSet_iOS_GPUFamily2_v2, 3)
        self.assertEqual(Metal.MTLFeatureSet_iOS_GPUFamily3_v1, 4)
        self.assertEqual(Metal.MTLFeatureSet_iOS_GPUFamily1_v3, 5)
        self.assertEqual(Metal.MTLFeatureSet_iOS_GPUFamily2_v3, 6)
        self.assertEqual(Metal.MTLFeatureSet_iOS_GPUFamily3_v2, 7)
        self.assertEqual(Metal.MTLFeatureSet_iOS_GPUFamily1_v4, 8)
        self.assertEqual(Metal.MTLFeatureSet_iOS_GPUFamily2_v4, 9)
        self.assertEqual(Metal.MTLFeatureSet_iOS_GPUFamily3_v3, 10)
        self.assertEqual(Metal.MTLFeatureSet_iOS_GPUFamily4_v1, 11)
        self.assertEqual(Metal.MTLFeatureSet_iOS_GPUFamily1_v5, 12)
        self.assertEqual(Metal.MTLFeatureSet_iOS_GPUFamily2_v5, 13)
        self.assertEqual(Metal.MTLFeatureSet_iOS_GPUFamily3_v4, 14)
        self.assertEqual(Metal.MTLFeatureSet_iOS_GPUFamily4_v2, 15)
        self.assertEqual(Metal.MTLFeatureSet_macOS_GPUFamily1_v1, 10000)
        self.assertEqual(Metal.MTLFeatureSet_OSX_GPUFamily1_v1, Metal.MTLFeatureSet_macOS_GPUFamily1_v1)
        self.assertEqual(Metal.MTLFeatureSet_macOS_GPUFamily1_v2, 10001)
        self.assertEqual(Metal.MTLFeatureSet_OSX_GPUFamily1_v2, Metal.MTLFeatureSet_macOS_GPUFamily1_v2)
        self.assertEqual(Metal.MTLFeatureSet_macOS_ReadWriteTextureTier2, 10002)
        self.assertEqual(Metal.MTLFeatureSet_OSX_ReadWriteTextureTier2, Metal.MTLFeatureSet_macOS_ReadWriteTextureTier2)
        self.assertEqual(Metal.MTLFeatureSet_macOS_GPUFamily1_v3, 10003)
        self.assertEqual(Metal.MTLFeatureSet_macOS_GPUFamily1_v4, 10004)
        self.assertEqual(Metal.MTLFeatureSet_macOS_GPUFamily2_v1, 10005)
        self.assertEqual(Metal.MTLFeatureSet_tvOS_GPUFamily1_v1, 30000)
        self.assertEqual(Metal.MTLFeatureSet_TVOS_GPUFamily1_v1, Metal.MTLFeatureSet_tvOS_GPUFamily1_v1)
        self.assertEqual(Metal.MTLFeatureSet_tvOS_GPUFamily1_v2, 30001)
        self.assertEqual(Metal.MTLFeatureSet_tvOS_GPUFamily1_v3, 30002)
        self.assertEqual(Metal.MTLFeatureSet_tvOS_GPUFamily1_v4, 30004)

        self.assertEqual(Metal.MTLGPUFamilyApple1, 1001)
        self.assertEqual(Metal.MTLGPUFamilyApple2, 1002)
        self.assertEqual(Metal.MTLGPUFamilyApple3, 1003)
        self.assertEqual(Metal.MTLGPUFamilyApple4, 1004)
        self.assertEqual(Metal.MTLGPUFamilyApple5, 1005)

        self.assertEqual(Metal.MTLGPUFamilyMac1, 2001)
        self.assertEqual(Metal.MTLGPUFamilyMac2, 2002)

        self.assertEqual(Metal.MTLGPUFamilyCommon1, 3001)
        self.assertEqual(Metal.MTLGPUFamilyCommon2, 3002)
        self.assertEqual(Metal.MTLGPUFamilyCommon3, 3003)

        self.assertEqual(Metal.MTLGPUFamilyiOSMac1, 4001)
        self.assertEqual(Metal.MTLGPUFamilyiOSMac2, 4002)

        self.assertEqual(Metal.MTLDeviceLocationBuiltIn, 0)
        self.assertEqual(Metal.MTLDeviceLocationSlot, 1)
        self.assertEqual(Metal.MTLDeviceLocationExternal, 2)
        self.assertEqual(Metal.MTLDeviceLocationUnspecified, 0xFFFFFFFFFFFFFFFF)

        self.assertEqual(Metal.MTLPipelineOptionNone, 0)
        self.assertEqual(Metal.MTLPipelineOptionArgumentInfo, 1 << 0)
        self.assertEqual(Metal.MTLPipelineOptionBufferTypeInfo, 1 << 1)

        self.assertEqual(Metal.MTLReadWriteTextureTierNone, 0)
        self.assertEqual(Metal.MTLReadWriteTextureTier1, 1)
        self.assertEqual(Metal.MTLReadWriteTextureTier2, 2)

        self.assertEqual(Metal.MTLArgumentBuffersTier1, 0)
        self.assertEqual(Metal.MTLArgumentBuffersTier2, 1)

    @min_os_level('10.13')
    def test_constants10_13(self):
        self.assertIsInstance(Metal.MTLDeviceWasAddedNotification, unicode)
        self.assertIsInstance(Metal.MTLDeviceRemovalRequestedNotification, unicode)
        self.assertIsInstance(Metal.MTLDeviceWasRemovedNotification, unicode)

    def test_structs(self):
        v = Metal.MTLSizeAndAlign()
        self.assertEqual(v.size, 0)
        self.assertEqual(v.align, 0)

    @min_os_level('10.11')
    def test_funtions10_11(self):
        self.assertResultIsRetained(Metal.MTLCreateSystemDefaultDevice)
        self.assertResultIsRetained(Metal.MTLCopyAllDevices)

    @min_os_level('10.13')
    def test_funtions10_13(self):
        self.assertResultIsRetained(Metal.MTLCopyAllDevicesWithObserver)
        self.assertArgIsOut(Metal.MTLCopyAllDevicesWithObserver, 0)
        self.assertArgIsBlock(Metal.MTLCopyAllDevicesWithObserver, 1, MTLDeviceNotificationHandler)

        Metal.MTLRemoveDeviceObserver

    @min_sdk_level('10.11')
    def test_protocols(self):
        objc.protocolNamed('MTLDevice')

    def test_methods(self):
        self.assertResultHasType(TestMTLDeviceHelper.registryID, objc._C_ULNGLNG)
        self.assertResultHasType(TestMTLDeviceHelper.maxThreadsPerThreadgroup, Metal.MTLSize.__typestr__)
        self.assertResultIsBOOL(TestMTLDeviceHelper.isLowPower)
        self.assertResultIsBOOL(TestMTLDeviceHelper.isHeadless)
        self.assertResultIsBOOL(TestMTLDeviceHelper.isRemovable)
        self.assertResultIsBOOL(TestMTLDeviceHelper.hasUnifiedMemory)
        self.assertResultHasType(TestMTLDeviceHelper.recommendedMaxWorkingSetSize, objc._C_ULNGLNG)
        self.assertResultHasType(TestMTLDeviceHelper.location, objc._C_NSUInteger)
        self.assertResultHasType(TestMTLDeviceHelper.locationNumber, objc._C_NSUInteger)
        self.assertResultHasType(TestMTLDeviceHelper.maxTransferRate, objc._C_ULNGLNG)
        self.assertResultIsBOOL(TestMTLDeviceHelper.isDepth24Stencil8PixelFormatSupported)
        self.assertResultHasType(TestMTLDeviceHelper.readWriteTextureSupport, objc._C_NSUInteger)
        self.assertResultHasType(TestMTLDeviceHelper.argumentBuffersSupport, objc._C_NSUInteger)
        self.assertResultIsBOOL(TestMTLDeviceHelper.areRasterOrderGroupsSupported)
        self.assertResultIsBOOL(TestMTLDeviceHelper.areBarycentricCoordsSupported)
        self.assertResultIsBOOL(TestMTLDeviceHelper.supportsShaderBarycentricCoordinates)
        self.assertResultHasType(TestMTLDeviceHelper.currentAllocatedSize, objc._C_NSUInteger)
        self.assertArgHasType(TestMTLDeviceHelper.newCommandQueueWithMaxCommandBufferCount_, 0, objc._C_NSUInteger)
        self.assertResultHasType(TestMTLDeviceHelper.heapBufferSizeAndAlignWithLength_options_, Metal.MTLSizeAndAlign.__typestr__)
        self.assertArgHasType(TestMTLDeviceHelper.heapBufferSizeAndAlignWithLength_options_, 0, objc._C_NSUInteger)
        self.assertArgHasType(TestMTLDeviceHelper.heapBufferSizeAndAlignWithLength_options_, 1, objc._C_NSUInteger)
        self.assertArgHasType(TestMTLDeviceHelper.newBufferWithLength_options_, 0, objc._C_NSUInteger)
"""
- (nullable id <MTLBuffer>)newBufferWithBytes:(const void *)pointer length:(NSUInteger)length options:(MTLResourceOptions)options;
- (nullable id <MTLBuffer>)newBufferWithBytesNoCopy:(void *)pointer length:(NSUInteger)length options:(MTLResourceOptions)options deallocator:(void (^ __nullable)(void *pointer, NSUInteger length))deallocator;
- (nullable id <MTLDepthStencilState>)newDepthStencilStateWithDescriptor:(MTLDepthStencilDescriptor *)descriptor;
- (nullable id <MTLTexture>)newTextureWithDescriptor:(MTLTextureDescriptor *)descriptor iosurface:(IOSurfaceRef)iosurface plane:(NSUInteger)plane API_AVAILABLE(macos(10.11), ios(11.0));
- (nullable id <MTLLibrary>)newDefaultLibraryWithBundle:(NSBundle *)bundle error:(__autoreleasing NSError **)error API_AVAILABLE(macos(10.12), ios(10.0));
- (nullable id <MTLLibrary>)newLibraryWithFile:(NSString *)filepath error:(__autoreleasing NSError **)error;
- (nullable id <MTLLibrary>)newLibraryWithURL:(NSURL *)url error:(__autoreleasing NSError **)error API_AVAILABLE(macos(10.13), ios(11.0));
- (nullable id <MTLLibrary>)newLibraryWithData:(dispatch_data_t)data error:(__autoreleasing NSError **)error;
- (nullable id <MTLLibrary>)newLibraryWithSource:(NSString *)source options:(nullable MTLCompileOptions *)options error:(__autoreleasing NSError **)error;
- (void)newLibraryWithSource:(NSString *)source options:(nullable MTLCompileOptions *)options completionHandler:(MTLNewLibraryCompletionHandler)completionHandler;
- (nullable id <MTLRenderPipelineState>)newRenderPipelineStateWithDescriptor:(MTLRenderPipelineDescriptor *)descriptor error:(__autoreleasing NSError **)error;
- (nullable id <MTLRenderPipelineState>)newRenderPipelineStateWithDescriptor:(MTLRenderPipelineDescriptor *)descriptor options:(MTLPipelineOption)options reflection:(MTLAutoreleasedRenderPipelineReflection * __nullable)reflection error:(__autoreleasing NSError **)error;
- (void)newRenderPipelineStateWithDescriptor:(MTLRenderPipelineDescriptor *)descriptor completionHandler:(MTLNewRenderPipelineStateCompletionHandler)completionHandler;
- (void)newRenderPipelineStateWithDescriptor:(MTLRenderPipelineDescriptor *)descriptor options:(MTLPipelineOption)options completionHandler:(MTLNewRenderPipelineStateWithReflectionCompletionHandler)completionHandler;
- (nullable id <MTLComputePipelineState>)newComputePipelineStateWithFunction:(id <MTLFunction>)computeFunction error:(__autoreleasing NSError **)error;
- (nullable id <MTLComputePipelineState>)newComputePipelineStateWithFunction:(id <MTLFunction>)computeFunction options:(MTLPipelineOption)options reflection:(MTLAutoreleasedComputePipelineReflection * __nullable)reflection error:(__autoreleasing NSError **)error;
- (void)newComputePipelineStateWithFunction:(id <MTLFunction>)computeFunction completionHandler:(MTLNewComputePipelineStateCompletionHandler)completionHandler;
- (void)newComputePipelineStateWithFunction:(id <MTLFunction>)computeFunction options:(MTLPipelineOption)options completionHandler:(MTLNewComputePipelineStateWithReflectionCompletionHandler)completionHandler;
- (nullable id <MTLComputePipelineState>)newComputePipelineStateWithDescriptor:(MTLComputePipelineDescriptor *)descriptor options:(MTLPipelineOption)options reflection:(MTLAutoreleasedComputePipelineReflection * __nullable)reflection error:(__autoreleasing NSError **)error API_AVAILABLE(macos(10.11), ios(9.0));
- (void)newComputePipelineStateWithDescriptor:(MTLComputePipelineDescriptor *)descriptor options:(MTLPipelineOption)options completionHandler:(MTLNewComputePipelineStateWithReflectionCompletionHandler)completionHandler API_AVAILABLE(macos(10.11), ios(9.0));
- (nullable id <MTLFence>)newFence API_AVAILABLE(macos(10.13), ios(10.0));
- (BOOL)supportsFeatureSet:(MTLFeatureSet)featureSet;
- (BOOL)supportsFamily:(MTLGPUFamily)gpuFamily API_AVAILABLE(macos(10.15), ios(13.0));
- (BOOL)supportsTextureSampleCount:(NSUInteger)sampleCount API_AVAILABLE(macos(10.11), ios(9.0));
- (NSUInteger)minimumLinearTextureAlignmentForPixelFormat:(MTLPixelFormat)format API_AVAILABLE(macos(10.13), ios(11.0));
- (NSUInteger)minimumTextureBufferAlignmentForPixelFormat:(MTLPixelFormat)format API_AVAILABLE(macos(10.14), ios(12.0));
@property (readonly) NSUInteger maxThreadgroupMemoryLength API_AVAILABLE(macos(10.13), ios(11.0));
@property (readonly) NSUInteger maxArgumentBufferSamplerCount API_AVAILABLE(macos(10.14), ios(12.0));
@property (readonly, getter=areProgrammableSamplePositionsSupported) BOOL programmableSamplePositionsSupported API_AVAILABLE(macos(10.13), ios(11.0));
- (void)getDefaultSamplePositions:(MTLSamplePosition *)positions count:(NSUInteger)count API_AVAILABLE(macos(10.13), ios(11.0));
- (nullable id <MTLArgumentEncoder>)newArgumentEncoderWithArguments:(NSArray <MTLArgumentDescriptor *> *)arguments API_AVAILABLE(macos(10.13), ios(11.0));
- (nullable id <MTLIndirectCommandBuffer>)newIndirectCommandBufferWithDescriptor:(MTLIndirectCommandBufferDescriptor*)descriptor maxCommandCount:(NSUInteger)maxCount options:(MTLResourceOptions)options API_AVAILABLE(macos(10.14), ios(12.0));
- (nullable id <MTLEvent>)newEvent API_AVAILABLE(macos(10.14), ios(12.0));
- (nullable id <MTLSharedEvent>)newSharedEvent API_AVAILABLE(macos(10.14), ios(12.0));
- (nullable id <MTLSharedEvent>)newSharedEventWithHandle:(MTLSharedEventHandle *)sharedEventHandle API_AVAILABLE(macos(10.14), ios(12.0));
@property (readonly) uint64_t peerGroupID API_AVAILABLE(macos(10.14.6)) API_UNAVAILABLE(ios);
@property (readonly) uint32_t peerIndex API_AVAILABLE(macos(10.14.6)) API_UNAVAILABLE(ios);
@property (readonly) uint32_t peerCount API_AVAILABLE(macos(10.14.6)) API_UNAVAILABLE(ios);
@property (readonly) NSUInteger maxBufferLength API_AVAILABLE(macos(10.14), ios(12.0));
- (nullable id<MTLCounterSampleBuffer>) newCounterSampleBufferWithDescriptor:(MTLCounterSampleBufferDescriptor*)descriptor
                                                              error:(NSError**)error
    API_AVAILABLE(macos(10.15)) API_UNAVAILABLE(ios);
-(void)sampleTimestamps:(NSUInteger *)cpuTimestamp
       gpuTimestamp:(NSUInteger *)gpuTimestamp
API_AVAILABLE(macos(10.15)) API_UNAVAILABLE(ios);
"""
