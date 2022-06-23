from PyObjCTools.TestSupport import TestCase
import HealthKit


class TestHKWorkoutRouteQuery(TestCase):
    def test_methods(self):
        self.assertArgIsBlock(
            HealthKit.HKWorkoutRouteQuery.initWithRoute_dataHandler_, 1, b"v@@Z@"
        )
        self.assertArgIsBlock(
            HealthKit.HKWorkoutRouteQuery.initWithRoute_dateInterval_dataHandler_,
            2,
            b"v@@Z@",
        )
