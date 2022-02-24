from PyObjCTools.TestSupport import TestCase, min_os_level, expectedFailure
import CoreML


class TestMLModelConfiguration(TestCase):
    def test_enum_types(self):
        self.assertIsEnumType(CoreML.MLComputeUnits)

    def test_constants(self):
        self.assertEqual(CoreML.MLComputeUnitsCPUOnly, 0)
        self.assertEqual(CoreML.MLComputeUnitsCPUAndGPU, 1)
        self.assertEqual(CoreML.MLComputeUnitsAll, 2)

    @min_os_level("10.15")
    def test_methods10_15(self):
        self.assertResultIsBOOL(
            CoreML.MLModelConfiguration.allowLowPrecisionAccumulationOnGPU
        )
        self.assertArgIsBOOL(
            CoreML.MLModelConfiguration.setAllowLowPrecisionAccumulationOnGPU_, 0
        )

    @expectedFailure
    def test_methods10_15_missing(self):
        self.assertResultIsBOOL(CoreML.MLModelDescription.isUpdatable)
