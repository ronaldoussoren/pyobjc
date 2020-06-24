from PyObjCTools.TestSupport import TestCase, min_os_level, expectedFailure
import ModelIO


class TestMDLVoxelArray(TestCase):
    @expectedFailure
    def testStructs(self):
        self.fail("MDLVoxelIndexExtent contains SIMD types")

    def testMethods(self):
        self.assertResultIsBOOL(
            ModelIO.MDLVoxelArray.voxelExistsAtIndex_allowAnyX_allowAnyY_allowAnyZ_allowAnyShell_
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

    @min_os_level("10.12")
    def testMethods10_12(self):
        self.assertResultIsBOOL(ModelIO.MDLVoxelArray.isValidSignedShellField)
