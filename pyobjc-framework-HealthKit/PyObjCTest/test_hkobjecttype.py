from PyObjCTools.TestSupport import TestCase
import HealthKit


class TestHKObjectType(TestCase):
    def test_methods(self):
        self.assertResultIsBOOL(HealthKit.HKObjectType.requiresPerObjectAuthorization)
        self.assertResultIsBOOL(HealthKit.HKSampleType.isMaximumDurationRestricted)
        self.assertResultIsBOOL(HealthKit.HKSampleType.isMinimumDurationRestricted)
        self.assertResultIsBOOL(HealthKit.HKSampleType.allowsRecalibrationForEstimates)
