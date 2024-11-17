from PyObjCTools.TestSupport import TestCase, min_os_level
import HealthKit


class TestHKAudiogramSensitivityTest(TestCase):
    def test_constants(self):
        self.assertIsEnumType(HealthKit.HKAudiogramConductionType)
        self.assertEqual(HealthKit.HKAudiogramConductionTypeAir, 0)

        self.assertIsEnumType(HealthKit.HKAudiogramSensitivityTestSide)
        self.assertEqual(HealthKit.HKAudiogramSensitivityTestSideLeft, 0)
        self.assertEqual(HealthKit.HKAudiogramSensitivityTestSideRight, 1)

    @min_os_level("15.1")
    def test_methods(self):
        self.assertResultIsBOOL(HealthKit.HKAudiogramSensitivityTest.masked)

        self.assertArgIsBOOL(
            HealthKit.HKAudiogramSensitivityTest.initWithSensitivity_type_masked_side_clampingRange_error_,
            2,
        )
        self.assertArgIsOut(
            HealthKit.HKAudiogramSensitivityTest.initWithSensitivity_type_masked_side_clampingRange_error_,
            5,
        )
