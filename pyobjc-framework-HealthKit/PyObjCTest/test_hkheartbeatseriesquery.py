from PyObjCTools.TestSupport import TestCase
import HealthKit


class TestHKHeartbeatSeriesQuery(TestCase):
    def test_methods(self):
        self.assertArgIsBlock(
            HealthKit.HKHeartbeatSeriesQuery.initWithHeartbeatSeries_dataHandler_,
            1,
            b"v@dZZ@",
        )
