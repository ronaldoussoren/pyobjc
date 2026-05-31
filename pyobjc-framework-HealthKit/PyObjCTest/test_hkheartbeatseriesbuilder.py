from PyObjCTools.TestSupport import TestCase
import HealthKit


class TestHKHeartbeatSeriesBuilder(TestCase):
    def test_methods(self):
        self.assertArgIsBlock(
            HealthKit.HKHeartbeatSeriesBuilder.addHeartbeatWithTimeIntervalSinceSeriesStartDate_precededByGap_completion_,
            2,
            b"vZ@",
        )
        self.assertArgIsBlock(
            HealthKit.HKHeartbeatSeriesBuilder.addMetadata_completion_, 1, b"vZ@"
        )
        self.assertArgIsBlock(
            HealthKit.HKHeartbeatSeriesBuilder.finishSeriesWithCompletion_, 0, b"v@@"
        )
