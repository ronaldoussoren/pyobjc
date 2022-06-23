from PyObjCTools.TestSupport import TestCase
import HealthKit


class TestHKQuantitySeriesSampleBuilder(TestCase):
    def test_methods(self):
        self.assertResultIsBOOL(
            HealthKit.HKQuantitySeriesSampleBuilder.insertQuantity_dateInterval_error_
        )
        self.assertArgIsOut(
            HealthKit.HKQuantitySeriesSampleBuilder.insertQuantity_dateInterval_error_,
            2,
        )

        self.assertResultIsBOOL(
            HealthKit.HKQuantitySeriesSampleBuilder.insertQuantity_date_error_
        )
        self.assertArgIsOut(
            HealthKit.HKQuantitySeriesSampleBuilder.insertQuantity_date_error_, 2
        )

        self.assertArgIsBlock(
            HealthKit.HKQuantitySeriesSampleBuilder.finishSeriesWithMetadata_endDate_completion_,
            2,
            b"v@@",
        )
        self.assertArgIsBlock(
            HealthKit.HKQuantitySeriesSampleBuilder.finishSeriesWithMetadata_completion_,
            1,
            b"v@@",
        )
