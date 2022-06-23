from PyObjCTools.TestSupport import TestCase
import HealthKit


class TestHKAudiogramSample(TestCase):
    def test_methods(self):
        self.assertArgIsOut(
            HealthKit.HKAudiogramSensitivityPoint.sensitivityPointWithFrequency_leftEarSensitivity_rightEarSensitivity_error_,
            3,
        )
