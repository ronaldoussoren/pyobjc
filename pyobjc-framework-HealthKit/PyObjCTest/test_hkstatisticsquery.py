from PyObjCTools.TestSupport import TestCase
import HealthKit


class TestHKStatisticsQuery(TestCase):
    def test_methods(self):
        self.assertArgIsBlock(
            HealthKit.HKStatisticsQuery.initWithQuantityType_quantitySamplePredicate_options_completionHandler_,
            3,
            b"v@@@",
        )
