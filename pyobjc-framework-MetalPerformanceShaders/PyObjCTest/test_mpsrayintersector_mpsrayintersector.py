from PyObjCTools.TestSupport import TestCase

import MetalPerformanceShaders


class TestMPSRayIntersector_MPSRayIntersector(TestCase):
    def test_enum_types(self):
        self.assertIsEnumType(
            MetalPerformanceShaders.MPSBoundingBoxIntersectionTestType
        )
        self.assertIsEnumType(MetalPerformanceShaders.MPSIntersectionDataType)
        self.assertIsEnumType(MetalPerformanceShaders.MPSIntersectionType)
        self.assertIsEnumType(MetalPerformanceShaders.MPSRayDataType)
        self.assertIsEnumType(MetalPerformanceShaders.MPSRayMaskOperator)
        self.assertIsEnumType(MetalPerformanceShaders.MPSRayMaskOptions)
        self.assertIsEnumType(MetalPerformanceShaders.MPSTriangleIntersectionTestType)

    def test_constants(self):
        self.assertEqual(MetalPerformanceShaders.MPSIntersectionTypeNearest, 0)
        self.assertEqual(MetalPerformanceShaders.MPSIntersectionTypeAny, 1)

        self.assertEqual(
            MetalPerformanceShaders.MPSTriangleIntersectionTestTypeDefault, 0
        )
        self.assertEqual(
            MetalPerformanceShaders.MPSTriangleIntersectionTestTypeWatertight, 1
        )

        self.assertEqual(
            MetalPerformanceShaders.MPSBoundingBoxIntersectionTestTypeDefault, 0
        )
        self.assertEqual(
            MetalPerformanceShaders.MPSBoundingBoxIntersectionTestTypeAxisAligned, 1
        )
        self.assertEqual(
            MetalPerformanceShaders.MPSBoundingBoxIntersectionTestTypeFast, 2
        )

        self.assertEqual(MetalPerformanceShaders.MPSRayMaskOptionNone, 0)
        self.assertEqual(MetalPerformanceShaders.MPSRayMaskOptionPrimitive, 1)
        self.assertEqual(MetalPerformanceShaders.MPSRayMaskOptionInstance, 2)

        self.assertEqual(MetalPerformanceShaders.MPSRayDataTypeOriginDirection, 0)
        self.assertEqual(
            MetalPerformanceShaders.MPSRayDataTypeOriginMinDistanceDirectionMaxDistance,
            1,
        )
        self.assertEqual(
            MetalPerformanceShaders.MPSRayDataTypeOriginMaskDirectionMaxDistance, 2
        )
        self.assertEqual(MetalPerformanceShaders.MPSRayDataTypePackedOriginDirection, 3)

        self.assertEqual(MetalPerformanceShaders.MPSIntersectionDataTypeDistance, 0)
        self.assertEqual(
            MetalPerformanceShaders.MPSIntersectionDataTypeDistancePrimitiveIndex, 1
        )
        self.assertEqual(
            MetalPerformanceShaders.MPSIntersectionDataTypeDistancePrimitiveIndexCoordinates,
            2,
        )
        self.assertEqual(
            MetalPerformanceShaders.MPSIntersectionDataTypeDistancePrimitiveIndexInstanceIndex,
            3,
        )
        self.assertEqual(
            MetalPerformanceShaders.MPSIntersectionDataTypeDistancePrimitiveIndexInstanceIndexCoordinates,
            4,
        )
        self.assertEqual(
            MetalPerformanceShaders.MPSIntersectionDataTypeDistancePrimitiveIndexBufferIndex,
            5,
        )
        self.assertEqual(
            MetalPerformanceShaders.MPSIntersectionDataTypeDistancePrimitiveIndexBufferIndexCoordinates,
            6,
        )
        self.assertEqual(
            MetalPerformanceShaders.MPSIntersectionDataTypeDistancePrimitiveIndexBufferIndexInstanceIndex,
            7,
        )
        self.assertEqual(
            MetalPerformanceShaders.MPSIntersectionDataTypeDistancePrimitiveIndexBufferIndexInstanceIndexCoordinates,
            8,
        )

        self.assertEqual(MetalPerformanceShaders.MPSRayMaskOperatorAnd, 0)
        self.assertEqual(MetalPerformanceShaders.MPSRayMaskOperatorNotAnd, 1)
        self.assertEqual(MetalPerformanceShaders.MPSRayMaskOperatorOr, 2)
        self.assertEqual(MetalPerformanceShaders.MPSRayMaskOperatorNotOr, 3)
        self.assertEqual(MetalPerformanceShaders.MPSRayMaskOperatorXor, 4)
        self.assertEqual(MetalPerformanceShaders.MPSRayMaskOperatorNotXor, 5)
        self.assertEqual(MetalPerformanceShaders.MPSRayMaskOperatorLessThan, 6)
        self.assertEqual(MetalPerformanceShaders.MPSRayMaskOperatorLessThanOrEqualTo, 7)
        self.assertEqual(MetalPerformanceShaders.MPSRayMaskOperatorGreaterThan, 8)
        self.assertEqual(
            MetalPerformanceShaders.MPSRayMaskOperatorGreaterThanOrEqualTo, 9
        )
        self.assertEqual(MetalPerformanceShaders.MPSRayMaskOperatorEqual, 10)
        self.assertEqual(MetalPerformanceShaders.MPSRayMaskOperatorNotEqual, 11)
