from PyObjCTools.TestSupport import TestCase, min_os_level, min_sdk_level
import objc
import ModelIO
from objc import simd


class TestMDLAssetHelper(ModelIO.NSObject):
    def sphericalHarmonicsLevel(self):
        return 1

    def setSphericalHarmonicsLevel_(self, v):
        pass

    def boundingBox(self):
        return 1

    def setBoundingBox_(self, v):
        pass

    def sphericalHarmonicsCoefficientsAtPosition_(self, v):
        return 1


class TestMDLAsset(TestCase):
    def testMethods(self):
        self.assertArgIsBOOL(
            ModelIO.MDLAsset.initWithURL_vertexDescriptor_bufferAllocator_preserveTopology_error_,
            3,
        )
        self.assertArgIsOut(
            ModelIO.MDLAsset.initWithURL_vertexDescriptor_bufferAllocator_preserveTopology_error_,
            4,
        )

        self.assertResultIsBOOL(ModelIO.MDLAsset.exportAssetToURL_)

        self.assertResultIsBOOL(ModelIO.MDLAsset.exportAssetToURL_error_)
        self.assertArgIsOut(ModelIO.MDLAsset.exportAssetToURL_error_, 1)

        self.assertResultIsBOOL(ModelIO.MDLAsset.canImportFileExtension_)

        self.assertResultIsBOOL(ModelIO.MDLAsset.canExportFileExtension_)

        self.assertResultHasType(
            TestMDLAssetHelper.boundingBox,
            ModelIO.MDLAxisAlignedBoundingBox.__typestr__,
        )
        self.assertArgHasType(
            TestMDLAssetHelper.setBoundingBox_,
            0,
            ModelIO.MDLAxisAlignedBoundingBox.__typestr__,
        )
        self.assertArgHasType(
            TestMDLAssetHelper.sphericalHarmonicsCoefficientsAtPosition_,
            0,
            simd.vector_float3.__typestr__,
        )

        self.assertResultHasType(
            TestMDLAssetHelper.sphericalHarmonicsLevel, objc._C_NSUInteger
        )
        self.assertArgHasType(
            TestMDLAssetHelper.setSphericalHarmonicsLevel_, 0, objc._C_NSUInteger
        )

    @min_os_level("10.13")
    def testMethods10_13(self):
        self.assertArgIsBOOL(
            ModelIO.MDLAsset.initWithURL_bufferAllocator_preserveIndexing_error_, 2
        )
        self.assertArgIsOut(
            ModelIO.MDLAsset.initWithURL_bufferAllocator_preserveIndexing_error_, 3
        )

        self.assertResultHasType(
            ModelIO.MDLAsset.upAxis, simd.vector_float3.__typestr__
        )
        self.assertArgHasType(
            ModelIO.MDLAsset.setUpAxis_, 0, simd.vector_float3.__typestr__
        )

    @min_sdk_level("10.12")
    def testProtocolObjects(self):
        self.assertProtocolExists("MDLLightProbeIrradianceDataSource")
