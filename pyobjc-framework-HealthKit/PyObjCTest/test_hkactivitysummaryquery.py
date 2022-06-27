from PyObjCTools.TestSupport import TestCase
import HealthKit


class TestHKActivitySummaryQuery(TestCase):
    def test_methods(self):
        self.assertResultIsBlock(
            HealthKit.HKActivitySummaryQuery.updateHandler, b"v@@@"
        )
        self.assertArgIsBlock(
            HealthKit.HKActivitySummaryQuery.setUpdateHandler_, 0, b"v@@@"
        )

        self.assertArgIsBlock(
            HealthKit.HKActivitySummaryQuery.initWithPredicate_resultsHandler_,
            1,
            b"v@@@",
        )
