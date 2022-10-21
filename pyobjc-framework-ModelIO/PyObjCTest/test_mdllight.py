from PyObjCTools.TestSupport import TestCase, min_os_level
import ModelIO
from objc import simd


class TestMDLCamera(TestCase):
    def test_enum_types(self):
        self.assertIsEnumType(ModelIO.MDLLightType)

    def testConstants(self):
        self.assertEqual(ModelIO.MDLLightTypeUnknown, 0)
        self.assertEqual(ModelIO.MDLLightTypeAmbient, 1)
        self.assertEqual(ModelIO.MDLLightTypeDirectional, 2)
        self.assertEqual(ModelIO.MDLLightTypeSpot, 3)
        self.assertEqual(ModelIO.MDLLightTypePoint, 4)
        self.assertEqual(ModelIO.MDLLightTypeLinear, 5)
        self.assertEqual(ModelIO.MDLLightTypeDiscArea, 6)
        self.assertEqual(ModelIO.MDLLightTypeRectangularArea, 7)
        self.assertEqual(ModelIO.MDLLightTypeSuperElliptical, 8)
        self.assertEqual(ModelIO.MDLLightTypePhotometric, 9)
        self.assertEqual(ModelIO.MDLLightTypeProbe, 10)
        self.assertEqual(ModelIO.MDLLightTypeEnvironment, 11)

    @min_os_level("10.11")
    def test_methods(self):
        self.assertArgHasType(
            ModelIO.MDLLight.irradianceAtPoint_, 0, simd.vector_float3.__typestr__
        )
        self.assertArgHasType(
            ModelIO.MDLLight.irradianceAtPoint_colorSpace_,
            0,
            simd.vector_float3.__typestr__,
        )

        self.assertResultHasType(
            ModelIO.MDLAreaLight.superEllipticPower, simd.vector_float2.__typestr__
        )
        self.assertArgHasType(
            ModelIO.MDLAreaLight.setSuperEllipticPower_,
            0,
            simd.vector_float2.__typestr__,
        )
