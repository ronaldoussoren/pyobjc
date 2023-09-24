import Metal
from PyObjCTools.TestSupport import TestCase, min_os_level


class TestMTLAccelerationStructure(TestCase):
    def test_enum_types(self):
        self.assertIsEnumType(Metal.MTLAccelerationStructureInstanceDescriptorType)
        self.assertIsEnumType(Metal.MTLAccelerationStructureInstanceOptions)
        self.assertIsEnumType(Metal.MTLAccelerationStructureUsage)
        self.assertIsEnumType(Metal.MTLMotionBorderMode)

    def test_structs(self):
        v = Metal.MTLAccelerationStructureInstanceDescriptor()
        self.assertIsInstance(v.transformationMatrix, Metal.MTLPackedFloat4x3)
        self.assertIsInstance(v.options, int)
        self.assertIsInstance(v.intersectionFunctionTableOffset, int)
        self.assertIsInstance(v.accelerationStructureIndex, int)

        v = Metal.MTLAccelerationStructureUserIDInstanceDescriptor()
        self.assertIsInstance(v.transformationMatrix, Metal.MTLPackedFloat4x3)
        self.assertIsInstance(v.options, int)
        self.assertIsInstance(v.mask, int)
        self.assertIsInstance(v.intersectionFunctionTableOffset, int)
        self.assertIsInstance(v.accelerationStructureIndex, int)
        self.assertIsInstance(v.userID, int)

        v = Metal.MTLAccelerationStructureMotionInstanceDescriptor()
        self.assertIsInstance(v.options, int)
        self.assertIsInstance(v.mask, int)
        self.assertIsInstance(v.intersectionFunctionTableOffset, int)
        self.assertIsInstance(v.accelerationStructureIndex, int)
        self.assertIsInstance(v.userID, int)
        self.assertIsInstance(v.motionTransformsStartIndex, int)
        self.assertIsInstance(v.motionTransformsCount, int)
        self.assertIsInstance(v.motionStartBorderMode, int)
        self.assertIsInstance(v.motionEndBorderMode, int)
        self.assertIsInstance(v.motionStartTime, float)
        self.assertIsInstance(v.motionEndTime, float)
        self.assertPickleRoundTrips(v)

        v = Metal.MTLIndirectAccelerationStructureInstanceDescriptor()
        self.assertIsInstance(v.transformationMatrix, Metal.MTLPackedFloat4x3)
        self.assertIsInstance(v.options, int)
        self.assertIsInstance(v.mask, int)
        self.assertIsInstance(v.intersectionFunctionTableOffset, int)
        self.assertIsInstance(v.userID, int)
        self.assertIsInstance(v.accelerationStructureID, Metal.MTLResourceID)

        v = Metal.MTLIndirectAccelerationStructureMotionInstanceDescriptor()
        self.assertIsInstance(v.options, int)
        self.assertIsInstance(v.mask, int)
        self.assertIsInstance(v.intersectionFunctionTableOffset, int)
        self.assertIsInstance(v.userID, int)
        self.assertIsInstance(v.accelerationStructureID, Metal.MTLResourceID)
        self.assertIsInstance(v.motionTransformsStartIndex, int)
        self.assertIsInstance(v.motionTransformsCount, int)
        self.assertIsInstance(v.motionStartBorderMode, int)
        self.assertIsInstance(v.motionEndBorderMode, int)
        self.assertIsInstance(v.motionStartTime, float)
        self.assertIsInstance(v.motionEndTime, float)

    def test_constants(self):
        self.assertEqual(Metal.MTLAccelerationStructureUsageNone, 0)
        self.assertEqual(Metal.MTLAccelerationStructureUsageRefit, 1 << 0)
        self.assertEqual(Metal.MTLAccelerationStructureUsagePreferFastBuild, 1 << 1)
        self.assertEqual(Metal.MTLAccelerationStructureUsageExtendedLimits, 1 << 2)

        self.assertEqual(Metal.MTLAccelerationStructureInstanceOptionNone, 0)
        self.assertEqual(
            Metal.MTLAccelerationStructureInstanceOptionDisableTriangleCulling, 1 << 0
        )
        self.assertEqual(
            Metal.MTLAccelerationStructureInstanceOptionTriangleFrontFacingWindingCounterClockwise,
            1 << 1,
        )

        self.assertEqual(Metal.MTLAccelerationStructureInstanceOptionOpaque, 1 << 2)
        self.assertEqual(Metal.MTLAccelerationStructureInstanceOptionNonOpaque, 1 << 3)

        self.assertEqual(Metal.MTLMotionBorderModeClamp, 0)
        self.assertEqual(Metal.MTLMotionBorderModeVanish, 1)

        self.assertEqual(Metal.MTLAccelerationStructureInstanceDescriptorTypeDefault, 0)
        self.assertEqual(Metal.MTLAccelerationStructureInstanceDescriptorTypeUserID, 1)
        self.assertEqual(Metal.MTLAccelerationStructureInstanceDescriptorTypeMotion, 2)
        self.assertEqual(
            Metal.MTLAccelerationStructureInstanceDescriptorTypeIndirect, 3
        )
        self.assertEqual(
            Metal.MTLAccelerationStructureInstanceDescriptorTypeIndirectMotion, 4
        )

        self.assertIsEnumType(Metal.MTLCurveType)
        self.assertEqual(Metal.MTLCurveTypeRound, 0)
        self.assertEqual(Metal.MTLCurveTypeFlat, 1)

        self.assertIsEnumType(Metal.MTLCurveBasis)
        self.assertEqual(Metal.MTLCurveBasisBSpline, 0)
        self.assertEqual(Metal.MTLCurveBasisCatmullRom, 1)
        self.assertEqual(Metal.MTLCurveBasisLinear, 2)
        self.assertEqual(Metal.MTLCurveBasisBezier, 3)

        self.assertIsEnumType(Metal.MTLCurveEndCaps)
        self.assertEqual(Metal.MTLCurveEndCapsNone, 0)
        self.assertEqual(Metal.MTLCurveEndCapsDisk, 1)
        self.assertEqual(Metal.MTLCurveEndCapsSphere, 2)

    @min_os_level("11.0")
    def test_methods11_0(self):
        self.assertResultIsBOOL(Metal.MTLAccelerationStructureGeometryDescriptor.opaque)
        self.assertArgIsBOOL(
            Metal.MTLAccelerationStructureGeometryDescriptor.setOpaque_, 0
        )

        self.assertResultIsBOOL(
            Metal.MTLAccelerationStructureGeometryDescriptor.allowDuplicateIntersectionFunctionInvocation
        )
        self.assertArgIsBOOL(
            Metal.MTLAccelerationStructureGeometryDescriptor.setAllowDuplicateIntersectionFunctionInvocation_,
            0,
        )
