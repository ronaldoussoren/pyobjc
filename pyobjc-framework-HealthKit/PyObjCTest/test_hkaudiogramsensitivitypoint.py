from PyObjCTools.TestSupport import TestCase, min_os_level
import HealthKit


class TestHKAudiogramSensitivityPoint(TestCase):
    @min_os_level("15.0")
    def test_methods(self):
        self.assertArgIsOut(
            HealthKit.HKAudiogramSensitivityPoint.sensitivityPointWithFrequency_leftEarSensitivity_rightEarSensitivity_error_,
            3,
        )
