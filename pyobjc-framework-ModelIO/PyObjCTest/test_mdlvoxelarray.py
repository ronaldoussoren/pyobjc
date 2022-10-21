from PyObjCTools.TestSupport import TestCase, min_os_level, expectedFailure
import ModelIO
from objc import simd


class TestMDLVoxelArray(TestCase):
    @expectedFailure
    def testStructs(self):
        self.assertEqual(
            ModelIO.MDLVoxelIndexExtent.__typestr__, b"{_MDLVoxelIndexExtent=<4i><4i>"
        )
        v = ModelIO.MDLVoxelIndexExtent()
        self.assertIs(v.minimumExtent, None)
        self.assertIs(v.maximumExtent, None)

    def testMethods(self):
        self.assertResultIsBOOL(
            ModelIO.MDLVoxelArray.voxelExistsAtIndex_allowAnyX_allowAnyY_allowAnyZ_allowAnyShell_
        )
        self.assertArgHasType(
            ModelIO.MDLVoxelArray.voxelExistsAtIndex_allowAnyX_allowAnyY_allowAnyZ_allowAnyShell_,
            0,
            simd.vector_int4.__typestr__,
        )
        self.assertArgIsBOOL(
            ModelIO.MDLVoxelArray.voxelExistsAtIndex_allowAnyX_allowAnyY_allowAnyZ_allowAnyShell_,
            1,
        )
        self.assertArgIsBOOL(
            ModelIO.MDLVoxelArray.voxelExistsAtIndex_allowAnyX_allowAnyY_allowAnyZ_allowAnyShell_,
            2,
        )
        self.assertArgIsBOOL(
            ModelIO.MDLVoxelArray.voxelExistsAtIndex_allowAnyX_allowAnyY_allowAnyZ_allowAnyShell_,
            3,
        )
        self.assertArgIsBOOL(
            ModelIO.MDLVoxelArray.voxelExistsAtIndex_allowAnyX_allowAnyY_allowAnyZ_allowAnyShell_,
            3,
        )

        self.assertArgHasType(
            ModelIO.MDLVoxelArray.setVoxelAtIndex_, 0, simd.vector_int4.__typestr__
        )

        self.assertArgHasType(
            ModelIO.MDLVoxelArray.initWithData_boundingBox_voxelExtent_,
            1,
            ModelIO.MDLAxisAlignedBoundingBox.__typestr__,
        )
        self.assertResultHasType(
            ModelIO.MDLVoxelArray.boundingBox,
            ModelIO.MDLAxisAlignedBoundingBox.__typestr__,
        )
        self.assertResultHasType(
            ModelIO.MDLVoxelArray.voxelBoundingBoxAtIndex_,
            ModelIO.MDLAxisAlignedBoundingBox.__typestr__,
        )
        self.assertArgHasType(
            ModelIO.MDLVoxelArray.voxelBoundingBoxAtIndex_,
            0,
            simd.vector_int4.__typestr__,
        )

        self.assertResultHasType(
            ModelIO.MDLVoxelArray.indexOfSpatialLocation_, simd.vector_int4.__typestr__
        )
        self.assertArgHasType(
            ModelIO.MDLVoxelArray.indexOfSpatialLocation_,
            0,
            simd.vector_float3.__typestr__,
        )

        self.assertResultHasType(
            ModelIO.MDLVoxelArray.spatialLocationOfIndex_,
            simd.vector_float3.__typestr__,
        )
        self.assertArgHasType(
            ModelIO.MDLVoxelArray.spatialLocationOfIndex_,
            0,
            simd.vector_int4.__typestr__,
        )

        self.assertResultHasType(
            ModelIO.MDLVoxelArray.voxelIndexExtent,
            ModelIO.MDLVoxelIndexExtent.__typestr__,
        )
        self.assertArgHasType(
            ModelIO.MDLVoxelArray.voxelsWithinExtent_,
            0,
            ModelIO.MDLVoxelIndexExtent.__typestr__,
        )

    @min_os_level("10.12")
    def testMethods10_12(self):
        self.assertResultIsBOOL(ModelIO.MDLVoxelArray.isValidSignedShellField)
