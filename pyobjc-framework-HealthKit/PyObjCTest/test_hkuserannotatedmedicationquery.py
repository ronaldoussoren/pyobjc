from PyObjCTools.TestSupport import TestCase, min_os_level
import HealthKit


class TestHKUserAnnotatedMedicationQuery(TestCase):
    @min_os_level("26.0")
    def test_methods(self):
        self.assertArgIsBlock(
            HealthKit.HKUserAnnotatedMedicationQuery.initWithPredicate_limit_resultsHandler_,
            2,
            b"v@@Z@",
        )
