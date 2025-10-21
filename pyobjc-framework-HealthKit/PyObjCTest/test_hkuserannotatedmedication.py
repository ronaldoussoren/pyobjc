from PyObjCTools.TestSupport import TestCase, min_os_level
import HealthKit


class TestHKUserAnnotatedMedication(TestCase):
    @min_os_level("26.0")
    def test_methods(self):
        self.assertResultIsBOOL(HealthKit.HKUserAnnotatedMedication.isArchived)
        self.assertResultIsBOOL(HealthKit.HKUserAnnotatedMedication.hasSchedule)
