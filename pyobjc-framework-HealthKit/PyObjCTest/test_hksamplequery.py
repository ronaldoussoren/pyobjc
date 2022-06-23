from PyObjCTools.TestSupport import TestCase
import HealthKit


class TestHKSampleQuery(TestCase):
    def test_constants(self):
        self.assertEqual(HealthKit.HKObjectQueryNoLimit, 0)

    def test_methods(self):
        self.assertArgIsBlock(
            HealthKit.HKSampleQuery.initWithSampleType_predicate_limit_sortDescriptors_resultsHandler_,
            4,
            b"v@@@",
        )
        self.assertArgIsBlock(
            HealthKit.HKSampleQuery.initWithQueryDescriptors_limit_resultsHandler_,
            2,
            b"v@@@",
        )
        self.assertArgIsBlock(
            HealthKit.HKSampleQuery.initWithQueryDescriptors_limit_sortDescriptors_resultsHandler_,
            3,
            b"v@@@",
        )
