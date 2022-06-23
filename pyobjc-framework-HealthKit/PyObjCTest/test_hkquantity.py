from PyObjCTools.TestSupport import TestCase
import HealthKit


class TestHKQuantity(TestCase):
    def test_methods(self):
        self.assertResultIsBOOL(HealthKit.HKQuantity.isCompatibleWithUnit_)
