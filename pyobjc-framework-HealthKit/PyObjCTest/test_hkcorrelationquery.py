from PyObjCTools.TestSupport import TestCase
import HealthKit


class TestHKCorrelationQuery(TestCase):
    def test_methods(self):
        self.assertArgIsBlock(
            HealthKit.HKCorrelationQuery.initWithType_predicate_samplePredicates_completion_,
            3,
            b"v@@@",
        )
