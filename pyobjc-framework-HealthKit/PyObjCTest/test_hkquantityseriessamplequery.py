from PyObjCTools.TestSupport import TestCase
import HealthKit


class TestHKQuantitySeriesSampleQuery(TestCase):
    def test_methods(self):
        self.assertResultIsBOOL(HealthKit.HKQuantitySeriesSampleQuery.includeSample)
        self.assertArgIsBOOL(HealthKit.HKQuantitySeriesSampleQuery.setIncludeSample_, 0)

        self.assertResultIsBOOL(
            HealthKit.HKQuantitySeriesSampleQuery.orderByQuantitySampleStartDate
        )
        self.assertArgIsBOOL(
            HealthKit.HKQuantitySeriesSampleQuery.setOrderByQuantitySampleStartDate_, 0
        )

        self.assertArgIsBlock(
            HealthKit.HKQuantitySeriesSampleQuery.initWithQuantityType_predicate_quantityHandler_,
            2,
            b"v@@@@Z@",
        )
        self.assertArgIsBlock(
            HealthKit.HKQuantitySeriesSampleQuery.initWithSample_quantityHandler_,
            1,
            b"v@@@Z@",
        )
