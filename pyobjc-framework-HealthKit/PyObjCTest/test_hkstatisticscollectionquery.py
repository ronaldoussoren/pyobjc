from PyObjCTools.TestSupport import TestCase
import HealthKit


class TestHKStatisticsCollectionQuery(TestCase):
    def test_methods(self):
        self.assertArgIsBlock(
            HealthKit.HKStatisticsCollection.enumerateStatisticsFromDate_toDate_withBlock_,
            2,
            b"v@o^Z",
        )

        self.assertResultIsBlock(
            HealthKit.HKStatisticsCollectionQuery.initialResultsHandler, b"v@@@"
        )
        self.assertArgIsBlock(
            HealthKit.HKStatisticsCollectionQuery.setInitialResultsHandler_, 0, b"v@@@"
        )
        self.assertResultIsBlock(
            HealthKit.HKStatisticsCollectionQuery.statisticsUpdateHandler, b"v@@@@"
        )
        self.assertArgIsBlock(
            HealthKit.HKStatisticsCollectionQuery.setStatisticsUpdateHandler_,
            0,
            b"v@@@@",
        )
