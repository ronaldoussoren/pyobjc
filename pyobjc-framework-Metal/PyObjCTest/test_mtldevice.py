import Metal
from PyObjCTools.TestSupport import TestCase, min_os_level, min_sdk_level
import objc

MTLDeviceNotificationHandler = b"v@@"
MTLNewLibraryCompletionHandler = b"v@@"
MTLNewRenderPipelineStateCompletionHandler = b"v@@"
MTLNewRenderPipelineStateWithReflectionCompletionHandler = b"v@@@"
MTLNewComputePipelineStateCompletionHandler = b"v@@"
MTLNewComputePipelineStateWithReflectionCompletionHandler = b"v@@@"


class TestMTLDeviceHelper(Metal.NSObject):
    def supportsFeatureSet_(self, a):
        return 1

    def supportsFamily_(self, a):
        return 1

    def minimumTextureBufferAlignmentForPixelFormat_(self, a):
        return 1

    def supportsTextureSampleCount_(self, a):
        return 1

    def getDefaultSamplePositions_count_(self, a, b):
        return 1

    def minimumLinearTextureAlignmentForPixelFormat_(self, a):
        return 1

    def registryID(self):
        return 1

    def maxThreadsPerThreadgroup(self):
        return 1

    def isLowPower(self):
        return 1

    def isHeadless(self):
        return 1

    def isRemovable(self):
        return 1

    def hasUnifiedMemory(self):
        return 1

    def recommendedMaxWorkingSetSize(self):
        return 1

    def location(self):
        return 1

    def locationNumber(self):
        return 1

    def maxTransferRate(self):
        return 1

    def isDepth24Stencil8PixelFormatSupported(self):
        return 1

    def readWriteTextureSupport(self):
        return 1

    def argumentBuffersSupport(self):
        return 1

    def areRasterOrderGroupsSupported(self):
        return 1

    def areBarycentricCoordsSupported(self):
        return 1

    def supportsShaderBarycentricCoordinates(self):
        return 1

    def currentAllocatedSize(self):
        return 1

    def newCommandQueueWithMaxCommandBufferCount_(self, a):
        return 1

    def heapBufferSizeAndAlignWithLength_options_(self, a, b):
        return 1

    def newBufferWithLength_options_(self, a, b):
        return 1

    def newBufferWithBytes_length_options_(self, a, b, c):
        return 1

    def newBufferWithBytesNoCopy_length_options_deallocator_(self, a, b, c, d):
        return 1

    def newDefaultLibraryWithBundle_error_(self, a, b):
        return 1

    def newLibraryWithFile_error_(self, a, b):
        return 1

    def newLibraryWithURL_error_(self, a, b):
        return 1

    def newLibraryWithData_error_(self, a, b):
        return 1

    def newLibraryWithSource_options_error_(self, a, b, c):
        return 1

    def maxThreadgroupMemoryLength(self):
        return 1

    def maxArgumentBufferSamplerCount(self):
        return 1

    def areProgrammableSamplePositionsSupported(self):
        return 1

    def peerGroupID(self):
        return 1

    def peerIndex(self):
        return 1

    def peerCount(self):
        return 1

    def maxBufferLength(self):
        return 1

    def newCounterSampleBufferWithDescriptor_error_(self, a, b):
        pass

    def sampleTimestamps_gpuTimestamp_(self, a, b):
        pass

    def newTextureWithDescriptor_iosurface_plane_(self, a, b, c):
        return 1

    def newLibraryWithSource_options_completionHandler_(self, a, b, c):
        return 1

    def newRenderPipelineStateWithDescriptor_error_(self, a, b):
        return 1

    def newRenderPipelineStateWithDescriptor_options_reflection_error_(
        self, a, b, c, d
    ):
        return 1

    def newRenderPipelineStateWithDescriptor_completionHandler_(self, a, b):
        return 1

    def newRenderPipelineStateWithDescriptor_options_completionHandler_(self, a, b, c):
        return 1

    def newComputePipelineStateWithFunction_error_(self, a, b):
        return 1

    def newComputePipelineStateWithFunction_options_reflection_error_(self, a, b, c, d):
        return 1

    def newComputePipelineStateWithFunction_completionHandler_(self, a, b):
        return 1

    def newComputePipelineStateWithFunction_options_completionHandler_(self, a, b, c):
        return 1

    def newComputePipelineStateWithDescriptor_options_reflection_error_(
        self, a, b, c, d
    ):
        return 1

    def newComputePipelineStateWithDescriptor_options_completionHandler_(self, a, b, c):
        return 1

    def newIndirectCommandBufferWithDescriptor_maxCommandCount_options_(self, a, b, c):
        return 1

    def supportsRasterizationRateMapWithLayerCount_(self, a):
        return 1

    def supportsVertexAmplificationCount_(self, a):
        return 1

    def supportsPullModelInterpolation(self):
        return 1

    def supportsCounterSampling_(self, a):
        return 1

    def supportsDynamicLibraries(self):
        return 1

    def supportsRenderDynamicLibraries(self):
        return 1

    def newDynamicLibrary_errror_(self, a, b):
        return 1

    def newDynamicLibraryWithURL_errror_(self, a, b):
        return 1

    def newBinaryArchiveWithDescriptor_errror_(self, a, b):
        return 1

    def supportsRaytracing(self):
        return 1

    def accelerationStructureSizesWithDescriptor_(self, a):
        return 1

    def supportsFunctionPointers(self):
        return 1

    def supportsFunctionPointersFromRender(self):
        return 1

    def supportsRaytracingFromRender(self):
        return 1

    def supportsPrimitiveMotionBlur(self):
        return 1

    def shouldMaximizeConcurrentCompilation(self):
        return 1

    def setShouldMaximizeConcurrentCompilation_(self, a):
        pass

    def maximumConcurrentCompilationTaskCount(self):
        return 1

    def supportsBinaryFunctionPointers(self):
        return 1

    def newDynamicLibrary_error_(self, a, b):
        return 1

    def newDynamicLibraryWithURL_error_(self, a, b):
        return 1

    def newBinaryArchiveWithDescriptor_error_(self, a, b):
        return 1

    def supports32BitFloatFiltering(self):
        return 1

    def supports32BitMSAA(self):
        return 1

    def supportsQueryTextureLOD(self):
        return 1

    def supportsBCTextureCompression(self):
        return 1

    def newRenderPipelineStateWithTileDescriptor_options_reflection_error_(
        self, a, b, c, d
    ):
        return 1

    def newRenderPipelineStateWithTileDescriptor_options_completionHandler_(
        self, a, b, c
    ):
        pass

    def sparseTileSizeWithTextureType_pixelFormat_sampleCount_(self, a, b, c):
        return 1

    def sparseTileSizeInBytes(self):
        return 1

    def convertSparsePixelRegions_toTileRegions_withTileSize_alignmentMode_numRegions_(
        self, a, b, c, d, e
    ):
        pass

    def convertSparseTileRegions_toPixelRegions_withTileSize_numRegions_(
        self, a, b, c, d
    ):
        pass

    def newRenderPipelineStateWithMeshDescriptor_options_reflection_error_(
        self, a, b, c, d
    ):
        return 1

    def newRenderPipelineStateWithMeshDescriptor_options_completionHandler_(
        self, a, b, c
    ):
        return 1

    def newIOHandleWithURL_error_(self, a, b):
        return 1

    def newIOCommandQueueWithDescriptor_error_(self, a, b):
        return 1

    def newIOHandleWithURL_compressionMethod_error_(self, a, b, c):
        return 1

    def sparseTileSizeInBytesForSparsePageSize_(self, a):
        return 1

    def sparseTileSizeWithTextureType_pixelFormat_sampleCount_sparsePageSize_(
        self, a, b, c, d
    ):
        return 1

    def heapAccelerationStructureSizeAndAlignWithSize_(self, a):
        return 1

    def heapAccelerationStructureSizeAndAlignWithDescriptor_(self, a):
        return 1

    def newIOFileHandleWithURL_error_(self, a, b):
        return 1

    def newIOFileHandleWithURL_compressionMethod_error_(self, a, b, c):
        return 1


class TestMTLDevice(TestCase):
    def test_typed_enum(self):
        self.assertIsTypedEnum(Metal.MTLDeviceNotificationName, str)

    def test_enum_types(self):
        self.assertIsEnumType(Metal.MTLArgumentBuffersTier)
        self.assertIsEnumType(Metal.MTLCounterSamplingPoint)
        self.assertIsEnumType(Metal.MTLDeviceLocation)
        self.assertIsEnumType(Metal.MTLFeatureSet)
        self.assertIsEnumType(Metal.MTLGPUFamily)
        self.assertIsEnumType(Metal.MTLPipelineOption)
        self.assertIsEnumType(Metal.MTLReadWriteTextureTier)
        self.assertIsEnumType(Metal.MTLSparseTextureRegionAlignmentMode)
        self.assertIsEnumType(Metal.MTLIOCompressionMethod)
        self.assertIsEnumType(Metal.MTLSparsePageSize)

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
        self.assertEqual(
            Metal.MTLFeatureSet_OSX_GPUFamily1_v1,
            Metal.MTLFeatureSet_macOS_GPUFamily1_v1,
        )
        self.assertEqual(Metal.MTLFeatureSet_macOS_GPUFamily1_v2, 10001)
        self.assertEqual(
            Metal.MTLFeatureSet_OSX_GPUFamily1_v2,
            Metal.MTLFeatureSet_macOS_GPUFamily1_v2,
        )
        self.assertEqual(Metal.MTLFeatureSet_macOS_ReadWriteTextureTier2, 10002)
        self.assertEqual(
            Metal.MTLFeatureSet_OSX_ReadWriteTextureTier2,
            Metal.MTLFeatureSet_macOS_ReadWriteTextureTier2,
        )
        self.assertEqual(Metal.MTLFeatureSet_macOS_GPUFamily1_v3, 10003)
        self.assertEqual(Metal.MTLFeatureSet_macOS_GPUFamily1_v4, 10004)
        self.assertEqual(Metal.MTLFeatureSet_macOS_GPUFamily2_v1, 10005)
        self.assertEqual(Metal.MTLFeatureSet_tvOS_GPUFamily1_v1, 30000)
        self.assertEqual(
            Metal.MTLFeatureSet_TVOS_GPUFamily1_v1,
            Metal.MTLFeatureSet_tvOS_GPUFamily1_v1,
        )
        self.assertEqual(Metal.MTLFeatureSet_tvOS_GPUFamily1_v2, 30001)
        self.assertEqual(Metal.MTLFeatureSet_tvOS_GPUFamily1_v3, 30002)
        self.assertEqual(Metal.MTLFeatureSet_tvOS_GPUFamily1_v4, 30004)

        self.assertEqual(Metal.MTLGPUFamilyApple1, 1001)
        self.assertEqual(Metal.MTLGPUFamilyApple2, 1002)
        self.assertEqual(Metal.MTLGPUFamilyApple3, 1003)
        self.assertEqual(Metal.MTLGPUFamilyApple4, 1004)
        self.assertEqual(Metal.MTLGPUFamilyApple5, 1005)
        self.assertEqual(Metal.MTLGPUFamilyApple6, 1006)
        self.assertEqual(Metal.MTLGPUFamilyApple7, 1007)
        self.assertEqual(Metal.MTLGPUFamilyApple8, 1008)
        self.assertEqual(Metal.MTLGPUFamilyApple9, 1009)

        self.assertEqual(Metal.MTLGPUFamilyMac1, 2001)
        self.assertEqual(Metal.MTLGPUFamilyMac2, 2002)

        self.assertEqual(Metal.MTLGPUFamilyCommon1, 3001)
        self.assertEqual(Metal.MTLGPUFamilyCommon2, 3002)
        self.assertEqual(Metal.MTLGPUFamilyCommon3, 3003)

        self.assertEqual(Metal.MTLGPUFamilyMacCatalyst1, 4001)
        self.assertEqual(Metal.MTLGPUFamilyMacCatalyst2, 4002)

        self.assertEqual(Metal.MTLGPUFamilyMetal3, 5001)

        self.assertEqual(Metal.MTLDeviceLocationBuiltIn, 0)
        self.assertEqual(Metal.MTLDeviceLocationSlot, 1)
        self.assertEqual(Metal.MTLDeviceLocationExternal, 2)
        self.assertEqual(Metal.MTLDeviceLocationUnspecified, 0xFFFFFFFFFFFFFFFF)

        self.assertEqual(Metal.MTLPipelineOptionNone, 0)
        self.assertEqual(Metal.MTLPipelineOptionArgumentInfo, 1 << 0)
        self.assertEqual(Metal.MTLPipelineOptionBufferTypeInfo, 1 << 1)
        self.assertEqual(Metal.MTLPipelineOptionFailOnBinaryArchiveMiss, 1 << 2)

        self.assertEqual(Metal.MTLReadWriteTextureTierNone, 0)
        self.assertEqual(Metal.MTLReadWriteTextureTier1, 1)
        self.assertEqual(Metal.MTLReadWriteTextureTier2, 2)

        self.assertEqual(Metal.MTLArgumentBuffersTier1, 0)
        self.assertEqual(Metal.MTLArgumentBuffersTier2, 1)

        self.assertEqual(Metal.MTLCounterSamplingPointAtStageBoundary, 0)
        self.assertEqual(Metal.MTLCounterSamplingPointAtDrawBoundary, 1)
        self.assertEqual(Metal.MTLCounterSamplingPointAtDispatchBoundary, 2)
        self.assertEqual(Metal.MTLCounterSamplingPointAtTileDispatchBoundary, 3)
        self.assertEqual(Metal.MTLCounterSamplingPointAtBlitBoundary, 4)

        self.assertEqual(Metal.MTLSparseTextureRegionAlignmentModeOutward, 0)
        self.assertEqual(Metal.MTLSparseTextureRegionAlignmentModeInward, 1)

        self.assertEqual(Metal.MTLIOCompressionMethodZlib, 0)
        self.assertEqual(Metal.MTLIOCompressionMethodLZFSE, 1)
        self.assertEqual(Metal.MTLIOCompressionMethodLZ4, 2)
        self.assertEqual(Metal.MTLIOCompressionMethodLZMA, 3)
        self.assertEqual(Metal.MTLIOCompressionMethodLZBitmap, 4)

        self.assertEqual(Metal.MTLSparsePageSize16, 101)
        self.assertEqual(Metal.MTLSparsePageSize64, 102)
        self.assertEqual(Metal.MTLSparsePageSize256, 103)

    @min_os_level("10.13")
    def test_constants10_13(self):
        self.assertIsInstance(Metal.MTLDeviceWasAddedNotification, str)
        self.assertIsInstance(Metal.MTLDeviceRemovalRequestedNotification, str)
        self.assertIsInstance(Metal.MTLDeviceWasRemovedNotification, str)

    def test_structs(self):
        v = Metal.MTLSizeAndAlign()
        self.assertEqual(v.size, 0)
        self.assertEqual(v.align, 0)
        self.assertPickleRoundTrips(v)

        v = Metal.MTLAccelerationStructureSizes()
        self.assertEqual(v.accelerationStructureSize, 0)
        self.assertEqual(v.buildScratchBufferSize, 0)
        self.assertEqual(v.refitScratchBufferSize, 0)
        self.assertPickleRoundTrips(v)

    @min_os_level("10.11")
    def test_funtions10_11(self):
        self.assertResultIsCFRetained(Metal.MTLCreateSystemDefaultDevice)
        self.assertResultIsCFRetained(Metal.MTLCopyAllDevices)

    @min_os_level("10.13")
    def test_funtions10_13(self):
        self.assertResultIsCFRetained(Metal.MTLCopyAllDevicesWithObserver)
        self.assertArgIsOut(Metal.MTLCopyAllDevicesWithObserver, 0)
        self.assertArgIsBlock(
            Metal.MTLCopyAllDevicesWithObserver, 1, MTLDeviceNotificationHandler
        )

        Metal.MTLRemoveDeviceObserver

    @min_sdk_level("10.11")
    def test_protocols(self):
        self.assertProtocolExists("MTLDevice")

    def test_methods(self):
        self.assertResultHasType(TestMTLDeviceHelper.registryID, objc._C_ULNGLNG)
        self.assertResultHasType(
            TestMTLDeviceHelper.maxThreadsPerThreadgroup, Metal.MTLSize.__typestr__
        )
        self.assertResultIsBOOL(TestMTLDeviceHelper.isLowPower)
        self.assertResultIsBOOL(TestMTLDeviceHelper.isHeadless)
        self.assertResultIsBOOL(TestMTLDeviceHelper.isRemovable)
        self.assertResultIsBOOL(TestMTLDeviceHelper.hasUnifiedMemory)
        self.assertResultHasType(
            TestMTLDeviceHelper.recommendedMaxWorkingSetSize, objc._C_ULNGLNG
        )
        self.assertResultHasType(TestMTLDeviceHelper.location, objc._C_NSUInteger)
        self.assertResultHasType(TestMTLDeviceHelper.locationNumber, objc._C_NSUInteger)
        self.assertResultHasType(TestMTLDeviceHelper.maxTransferRate, objc._C_ULNGLNG)
        self.assertResultIsBOOL(
            TestMTLDeviceHelper.isDepth24Stencil8PixelFormatSupported
        )
        self.assertResultHasType(
            TestMTLDeviceHelper.readWriteTextureSupport, objc._C_NSUInteger
        )
        self.assertResultHasType(
            TestMTLDeviceHelper.argumentBuffersSupport, objc._C_NSUInteger
        )
        self.assertResultIsBOOL(TestMTLDeviceHelper.areRasterOrderGroupsSupported)
        self.assertResultIsBOOL(TestMTLDeviceHelper.supports32BitFloatFiltering)
        self.assertResultIsBOOL(TestMTLDeviceHelper.supports32BitMSAA)
        self.assertResultIsBOOL(TestMTLDeviceHelper.supportsQueryTextureLOD)
        self.assertResultIsBOOL(TestMTLDeviceHelper.supportsBCTextureCompression)
        self.assertResultIsBOOL(TestMTLDeviceHelper.areBarycentricCoordsSupported)
        self.assertResultIsBOOL(
            TestMTLDeviceHelper.supportsShaderBarycentricCoordinates
        )
        self.assertResultHasType(
            TestMTLDeviceHelper.currentAllocatedSize, objc._C_NSUInteger
        )
        self.assertArgHasType(
            TestMTLDeviceHelper.newCommandQueueWithMaxCommandBufferCount_,
            0,
            objc._C_NSUInteger,
        )
        self.assertResultHasType(
            TestMTLDeviceHelper.heapBufferSizeAndAlignWithLength_options_,
            Metal.MTLSizeAndAlign.__typestr__,
        )
        self.assertArgHasType(
            TestMTLDeviceHelper.heapBufferSizeAndAlignWithLength_options_,
            0,
            objc._C_NSUInteger,
        )
        self.assertArgHasType(
            TestMTLDeviceHelper.heapBufferSizeAndAlignWithLength_options_,
            1,
            objc._C_NSUInteger,
        )
        self.assertArgHasType(
            TestMTLDeviceHelper.newBufferWithLength_options_, 0, objc._C_NSUInteger
        )

        self.assertArgHasType(
            TestMTLDeviceHelper.newBufferWithBytes_length_options_, 0, b"n^v"
        )
        self.assertArgSizeInArg(
            TestMTLDeviceHelper.newBufferWithBytes_length_options_, 0, 1
        )
        self.assertArgHasType(
            TestMTLDeviceHelper.newBufferWithBytes_length_options_,
            1,
            objc._C_NSUInteger,
        )
        self.assertArgHasType(
            TestMTLDeviceHelper.newBufferWithBytes_length_options_,
            2,
            objc._C_NSUInteger,
        )

        self.assertArgHasType(
            TestMTLDeviceHelper.newBufferWithBytesNoCopy_length_options_deallocator_,
            0,
            b"n^v",
        )
        self.assertArgSizeInArg(
            TestMTLDeviceHelper.newBufferWithBytesNoCopy_length_options_deallocator_,
            0,
            1,
        )
        self.assertArgHasType(
            TestMTLDeviceHelper.newBufferWithBytesNoCopy_length_options_deallocator_,
            1,
            objc._C_NSUInteger,
        )
        self.assertArgHasType(
            TestMTLDeviceHelper.newBufferWithBytesNoCopy_length_options_deallocator_,
            2,
            objc._C_NSUInteger,
        )
        self.assertArgIsBlock(
            TestMTLDeviceHelper.newBufferWithBytesNoCopy_length_options_deallocator_,
            3,
            b"vn^v" + objc._C_NSUInteger,
        )

        self.assertArgHasType(
            TestMTLDeviceHelper.newDefaultLibraryWithBundle_error_, 1, b"o^@"
        )
        self.assertArgHasType(TestMTLDeviceHelper.newLibraryWithFile_error_, 1, b"o^@")
        self.assertArgHasType(TestMTLDeviceHelper.newLibraryWithURL_error_, 1, b"o^@")
        self.assertArgHasType(TestMTLDeviceHelper.newLibraryWithData_error_, 1, b"o^@")
        self.assertArgHasType(
            TestMTLDeviceHelper.newLibraryWithSource_options_error_, 2, b"o^@"
        )

        self.assertArgHasType(
            TestMTLDeviceHelper.newTextureWithDescriptor_iosurface_plane_,
            1,
            b"^{__IOSurface=}",
        )
        self.assertArgHasType(
            TestMTLDeviceHelper.newTextureWithDescriptor_iosurface_plane_,
            2,
            objc._C_NSUInteger,
        )

        self.assertArgIsBlock(
            TestMTLDeviceHelper.newLibraryWithSource_options_completionHandler_,
            2,
            b"v@@",
        )

        self.assertArgHasType(
            TestMTLDeviceHelper.newRenderPipelineStateWithDescriptor_error_, 1, b"o^@"
        )

        self.assertArgHasType(
            TestMTLDeviceHelper.newRenderPipelineStateWithDescriptor_options_reflection_error_,
            1,
            objc._C_NSUInteger,
        )
        self.assertArgHasType(
            TestMTLDeviceHelper.newRenderPipelineStateWithDescriptor_options_reflection_error_,
            3,
            b"o^@",
        )

        self.assertArgIsBlock(
            TestMTLDeviceHelper.newRenderPipelineStateWithDescriptor_completionHandler_,
            1,
            b"v@@",
        )

        self.assertArgHasType(
            TestMTLDeviceHelper.newRenderPipelineStateWithDescriptor_options_completionHandler_,  # noqa: B950
            1,
            objc._C_NSUInteger,
        )
        self.assertArgIsBlock(
            TestMTLDeviceHelper.newRenderPipelineStateWithDescriptor_options_completionHandler_,  # noqa: B950
            2,
            b"v@@",
        )

        self.assertArgHasType(
            TestMTLDeviceHelper.newComputePipelineStateWithFunction_error_, 1, b"o^@"
        )
        self.assertArgHasType(
            TestMTLDeviceHelper.newComputePipelineStateWithFunction_options_reflection_error_,
            1,
            objc._C_NSUInteger,
        )
        self.assertArgHasType(
            TestMTLDeviceHelper.newComputePipelineStateWithFunction_options_reflection_error_,
            3,
            b"o^@",
        )

        self.assertArgIsBlock(
            TestMTLDeviceHelper.newComputePipelineStateWithFunction_completionHandler_,
            1,
            b"v@@",
        )

        self.assertArgHasType(
            TestMTLDeviceHelper.newComputePipelineStateWithFunction_options_completionHandler_,  # noqa: B950
            1,
            objc._C_NSUInteger,
        )
        self.assertArgIsBlock(
            TestMTLDeviceHelper.newComputePipelineStateWithFunction_options_completionHandler_,  # noqa: B950
            2,
            b"v@@",
        )

        self.assertArgHasType(
            TestMTLDeviceHelper.newComputePipelineStateWithDescriptor_options_reflection_error_,  # noqa: B950
            1,
            objc._C_NSUInteger,
        )
        self.assertArgHasType(
            TestMTLDeviceHelper.newComputePipelineStateWithDescriptor_options_reflection_error_,  # noqa: B950
            3,
            b"o^@",
        )

        self.assertArgHasType(
            TestMTLDeviceHelper.newComputePipelineStateWithDescriptor_options_completionHandler_,  # noqa: B950
            1,
            objc._C_NSUInteger,
        )
        self.assertArgIsBlock(
            TestMTLDeviceHelper.newComputePipelineStateWithDescriptor_options_completionHandler_,  # noqa: B950
            2,
            b"v@@",
        )

        self.assertResultIsBOOL(TestMTLDeviceHelper.supportsFeatureSet_)
        self.assertArgHasType(
            TestMTLDeviceHelper.supportsFeatureSet_, 0, objc._C_NSUInteger
        )

        self.assertResultIsBOOL(TestMTLDeviceHelper.supportsFamily_)
        self.assertArgHasType(TestMTLDeviceHelper.supportsFamily_, 0, objc._C_NSInteger)

        self.assertResultIsBOOL(TestMTLDeviceHelper.supportsTextureSampleCount_)
        self.assertArgHasType(
            TestMTLDeviceHelper.supportsTextureSampleCount_, 0, objc._C_NSUInteger
        )

        self.assertResultHasType(
            TestMTLDeviceHelper.minimumLinearTextureAlignmentForPixelFormat_,
            objc._C_NSUInteger,
        )
        self.assertArgHasType(
            TestMTLDeviceHelper.minimumLinearTextureAlignmentForPixelFormat_,
            0,
            objc._C_NSUInteger,
        )

        self.assertResultHasType(
            TestMTLDeviceHelper.minimumTextureBufferAlignmentForPixelFormat_,
            objc._C_NSUInteger,
        )
        self.assertArgHasType(
            TestMTLDeviceHelper.minimumTextureBufferAlignmentForPixelFormat_,
            0,
            objc._C_NSUInteger,
        )

        self.assertResultHasType(
            TestMTLDeviceHelper.maxThreadgroupMemoryLength, objc._C_NSUInteger
        )
        self.assertResultHasType(
            TestMTLDeviceHelper.maxArgumentBufferSamplerCount, objc._C_NSUInteger
        )
        self.assertResultHasType(
            TestMTLDeviceHelper.areProgrammableSamplePositionsSupported, objc._C_NSBOOL
        )

        self.assertArgHasType(
            TestMTLDeviceHelper.getDefaultSamplePositions_count_,
            0,
            b"o^{MTLSamplePosition=ff}",
        )
        self.assertArgSizeInArg(
            TestMTLDeviceHelper.getDefaultSamplePositions_count_, 0, 1
        )
        self.assertArgHasType(
            TestMTLDeviceHelper.getDefaultSamplePositions_count_, 1, objc._C_NSUInteger
        )

        self.assertArgHasType(
            TestMTLDeviceHelper.newIndirectCommandBufferWithDescriptor_maxCommandCount_options_,
            1,
            objc._C_NSUInteger,
        )
        self.assertArgHasType(
            TestMTLDeviceHelper.newIndirectCommandBufferWithDescriptor_maxCommandCount_options_,
            2,
            objc._C_NSUInteger,
        )

        self.assertResultIsBOOL(
            TestMTLDeviceHelper.supportsRasterizationRateMapWithLayerCount_
        )
        self.assertArgHasType(
            TestMTLDeviceHelper.supportsRasterizationRateMapWithLayerCount_,
            0,
            objc._C_NSUInteger,
        )

        self.assertResultIsBOOL(TestMTLDeviceHelper.supportsVertexAmplificationCount_)
        self.assertArgHasType(
            TestMTLDeviceHelper.supportsVertexAmplificationCount_, 0, objc._C_NSUInteger
        )

        self.assertResultHasType(TestMTLDeviceHelper.peerGroupID, objc._C_ULNGLNG)
        self.assertResultHasType(TestMTLDeviceHelper.peerIndex, objc._C_UINT)
        self.assertResultHasType(TestMTLDeviceHelper.peerCount, objc._C_UINT)
        self.assertResultHasType(
            TestMTLDeviceHelper.maxBufferLength, objc._C_NSUInteger
        )
        self.assertArgHasType(
            TestMTLDeviceHelper.newCounterSampleBufferWithDescriptor_error_, 1, b"o^@"
        )
        self.assertArgHasType(
            TestMTLDeviceHelper.sampleTimestamps_gpuTimestamp_,
            0,
            b"o^" + objc._C_NSUInteger,
        )
        self.assertArgHasType(
            TestMTLDeviceHelper.sampleTimestamps_gpuTimestamp_,
            1,
            b"o^" + objc._C_NSUInteger,
        )
        self.assertResultIsBOOL(TestMTLDeviceHelper.supportsPullModelInterpolation)
        self.assertResultIsBOOL(
            TestMTLDeviceHelper.supportsShaderBarycentricCoordinates
        )
        self.assertResultIsBOOL(TestMTLDeviceHelper.supportsCounterSampling_)
        self.assertArgHasType(
            TestMTLDeviceHelper.supportsCounterSampling_, 0, objc._C_NSUInteger
        )
        self.assertResultIsBOOL(TestMTLDeviceHelper.supportsDynamicLibraries)
        self.assertResultIsBOOL(TestMTLDeviceHelper.supportsRenderDynamicLibraries)
        self.assertArgHasType(TestMTLDeviceHelper.newDynamicLibrary_error_, 1, b"o^@")
        self.assertArgHasType(
            TestMTLDeviceHelper.newDynamicLibraryWithURL_error_, 1, b"o^@"
        )
        self.assertArgHasType(
            TestMTLDeviceHelper.newBinaryArchiveWithDescriptor_error_, 1, b"o^@"
        )
        self.assertResultIsBOOL(TestMTLDeviceHelper.supportsRaytracing)
        self.assertResultHasType(
            TestMTLDeviceHelper.accelerationStructureSizesWithDescriptor_,
            Metal.MTLAccelerationStructureSizes.__typestr__,
        )
        self.assertResultIsBOOL(TestMTLDeviceHelper.supportsFunctionPointers)
        self.assertResultIsBOOL(TestMTLDeviceHelper.supportsFunctionPointersFromRender)
        self.assertResultIsBOOL(TestMTLDeviceHelper.supportsRaytracingFromRender)

        self.assertArgHasType(
            TestMTLDeviceHelper.newRenderPipelineStateWithTileDescriptor_options_reflection_error_,
            1,
            objc._C_NSUInteger,
        )
        self.assertArgIsOut(
            TestMTLDeviceHelper.newRenderPipelineStateWithTileDescriptor_options_reflection_error_,
            3,
        )

        self.assertArgHasType(
            TestMTLDeviceHelper.newRenderPipelineStateWithTileDescriptor_options_completionHandler_,
            1,
            objc._C_NSUInteger,
        )
        self.assertArgIsBlock(
            TestMTLDeviceHelper.newRenderPipelineStateWithTileDescriptor_options_completionHandler_,
            2,
            MTLNewRenderPipelineStateWithReflectionCompletionHandler,
        )

        self.assertArgHasType(
            TestMTLDeviceHelper.sparseTileSizeWithTextureType_pixelFormat_sampleCount_,
            0,
            objc._C_NSUInteger,
        )
        self.assertArgHasType(
            TestMTLDeviceHelper.sparseTileSizeWithTextureType_pixelFormat_sampleCount_,
            1,
            objc._C_NSUInteger,
        )
        self.assertArgHasType(
            TestMTLDeviceHelper.sparseTileSizeWithTextureType_pixelFormat_sampleCount_,
            2,
            objc._C_NSUInteger,
        )

        self.assertResultHasType(
            TestMTLDeviceHelper.sparseTileSizeInBytes, objc._C_NSUInteger
        )

        self.assertArgHasType(
            TestMTLDeviceHelper.convertSparsePixelRegions_toTileRegions_withTileSize_alignmentMode_numRegions_,
            0,
            b"n^" + Metal.MTLRegion.__typestr__,
        )
        self.assertArgSizeInArg(
            TestMTLDeviceHelper.convertSparsePixelRegions_toTileRegions_withTileSize_alignmentMode_numRegions_,
            0,
            4,
        )
        self.assertArgHasType(
            TestMTLDeviceHelper.convertSparsePixelRegions_toTileRegions_withTileSize_alignmentMode_numRegions_,
            1,
            b"n^" + Metal.MTLRegion.__typestr__,
        )
        self.assertArgSizeInArg(
            TestMTLDeviceHelper.convertSparsePixelRegions_toTileRegions_withTileSize_alignmentMode_numRegions_,
            1,
            4,
        )
        self.assertArgHasType(
            TestMTLDeviceHelper.convertSparsePixelRegions_toTileRegions_withTileSize_alignmentMode_numRegions_,
            2,
            Metal.MTLSize.__typestr__,
        )
        self.assertArgHasType(
            TestMTLDeviceHelper.convertSparsePixelRegions_toTileRegions_withTileSize_alignmentMode_numRegions_,
            3,
            objc._C_NSUInteger,
        )
        self.assertArgHasType(
            TestMTLDeviceHelper.convertSparsePixelRegions_toTileRegions_withTileSize_alignmentMode_numRegions_,
            4,
            objc._C_NSUInteger,
        )

        self.assertArgHasType(
            TestMTLDeviceHelper.convertSparseTileRegions_toPixelRegions_withTileSize_numRegions_,
            0,
            b"n^" + Metal.MTLRegion.__typestr__,
        )
        self.assertArgSizeInArg(
            TestMTLDeviceHelper.convertSparseTileRegions_toPixelRegions_withTileSize_numRegions_,
            0,
            3,
        )
        self.assertArgHasType(
            TestMTLDeviceHelper.convertSparseTileRegions_toPixelRegions_withTileSize_numRegions_,
            1,
            b"n^" + Metal.MTLRegion.__typestr__,
        )
        self.assertArgSizeInArg(
            TestMTLDeviceHelper.convertSparseTileRegions_toPixelRegions_withTileSize_numRegions_,
            1,
            3,
        )
        self.assertArgHasType(
            TestMTLDeviceHelper.convertSparseTileRegions_toPixelRegions_withTileSize_numRegions_,
            2,
            Metal.MTLSize.__typestr__,
        )
        self.assertArgHasType(
            TestMTLDeviceHelper.convertSparseTileRegions_toPixelRegions_withTileSize_numRegions_,
            3,
            objc._C_NSUInteger,
        )

        self.assertResultIsBOOL(TestMTLDeviceHelper.supportsPrimitiveMotionBlur)

        self.assertResultIsBOOL(TestMTLDeviceHelper.shouldMaximizeConcurrentCompilation)
        self.assertArgIsBOOL(
            TestMTLDeviceHelper.setShouldMaximizeConcurrentCompilation_, 0
        )

        self.assertResultHasType(
            TestMTLDeviceHelper.maximumConcurrentCompilationTaskCount,
            objc._C_NSUInteger,
        )

        self.assertArgHasType(
            TestMTLDeviceHelper.newRenderPipelineStateWithMeshDescriptor_options_reflection_error_,
            3,
            b"o^@",
        )

        self.assertArgIsBlock(
            TestMTLDeviceHelper.newRenderPipelineStateWithMeshDescriptor_options_completionHandler_,
            2,
            MTLNewRenderPipelineStateWithReflectionCompletionHandler,
        )

        self.assertArgHasType(TestMTLDeviceHelper.newIOHandleWithURL_error_, 1, b"o^@")

        self.assertArgHasType(
            TestMTLDeviceHelper.newIOCommandQueueWithDescriptor_error_, 1, b"o^@"
        )

        self.assertArgHasType(
            TestMTLDeviceHelper.newIOHandleWithURL_compressionMethod_error_, 2, b"o^@"
        )

        self.assertResultHasType(
            TestMTLDeviceHelper.sparseTileSizeInBytesForSparsePageSize_,
            objc._C_NSUInteger,
        )

        self.assertArgHasType(
            TestMTLDeviceHelper.sparseTileSizeInBytesForSparsePageSize_,
            0,
            objc._C_NSInteger,
        )

        self.assertResultHasType(
            TestMTLDeviceHelper.sparseTileSizeWithTextureType_pixelFormat_sampleCount_sparsePageSize_,
            Metal.MTLSize.__typestr__,
        )
        self.assertArgHasType(
            TestMTLDeviceHelper.sparseTileSizeWithTextureType_pixelFormat_sampleCount_sparsePageSize_,
            0,
            objc._C_NSUInteger,
        )
        self.assertArgHasType(
            TestMTLDeviceHelper.sparseTileSizeWithTextureType_pixelFormat_sampleCount_sparsePageSize_,
            1,
            objc._C_NSUInteger,
        )
        self.assertArgHasType(
            TestMTLDeviceHelper.sparseTileSizeWithTextureType_pixelFormat_sampleCount_sparsePageSize_,
            2,
            objc._C_NSUInteger,
        )
        self.assertArgHasType(
            TestMTLDeviceHelper.sparseTileSizeWithTextureType_pixelFormat_sampleCount_sparsePageSize_,
            3,
            objc._C_NSInteger,
        )

        self.assertResultHasType(
            TestMTLDeviceHelper.heapAccelerationStructureSizeAndAlignWithSize_,
            Metal.MTLSizeAndAlign.__typestr__,
        )
        self.assertArgHasType(
            TestMTLDeviceHelper.heapAccelerationStructureSizeAndAlignWithSize_,
            0,
            objc._C_NSUInteger,
        )

        self.assertResultHasType(
            TestMTLDeviceHelper.heapAccelerationStructureSizeAndAlignWithDescriptor_,
            Metal.MTLSizeAndAlign.__typestr__,
        )

        self.assertArgHasType(
            TestMTLDeviceHelper.newIOFileHandleWithURL_error_, 1, b"o^@"
        )
        self.assertArgHasType(
            TestMTLDeviceHelper.newIOFileHandleWithURL_compressionMethod_error_,
            1,
            objc._C_NSInteger,
        )
        self.assertArgHasType(
            TestMTLDeviceHelper.newIOFileHandleWithURL_compressionMethod_error_,
            2,
            b"o^@",
        )
