from PyObjCTools.TestSupport import TestCase, min_os_level
import HealthKit


class TestHKAudiogramSensitivityPointClampingRange(TestCase):
    @min_os_level("15.1")
    def test_methods(self):
        self.assertArgIsOut(
            HealthKit.HKAudiogramSensitivityPointClampingRange.clampingRangeWithLowerBound_upperBound_error_,
            2,
        )
