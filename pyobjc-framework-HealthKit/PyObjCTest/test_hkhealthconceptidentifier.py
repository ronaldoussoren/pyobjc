from PyObjCTools.TestSupport import TestCase, min_os_level
import HealthKit


class TestHKHealthConceptIdentifier(TestCase):
    def test_constants(self):
        self.assertIsTypedEnum(HealthKit.HKHealthConceptDomain, str)

    @min_os_level("26.0")
    def test_constants26_0(self):
        self.assertIsInstance(HealthKit.HKHealthConceptDomainMedication, str)

    @min_os_level("15.0")
    def test_methods(self):
        self.assertResultIsBOOL(HealthKit.HKActivitySummary.isPaused)
        self.assertArgIsBOOL(HealthKit.HKActivitySummary.setPaused_, 0)
