import CoreMotion
from PyObjCTools.TestSupport import TestCase, min_os_level

CMPedometerHandler = b"v@"
CMPedometerEventHandler = b"v@@"


class TestCMPedometer(TestCase):
    def test_constants(self):
        self.assertEqual(CoreMotion.CMPedometerEventTypePause, 0)
        self.assertEqual(CoreMotion.CMPedometerEventTypeResume, 1)

    @min_os_level("10.15")
    def test_methods10_15(self):
        self.assertResultIsBOOL(CoreMotion.CMPedometer.isStepCountingAvailable)
        self.assertResultIsBOOL(CoreMotion.CMPedometer.isDistanceAvailable)
        self.assertResultIsBOOL(CoreMotion.CMPedometer.isFloorCountingAvailable)
        self.assertResultIsBOOL(CoreMotion.CMPedometer.isPaceAvailable)

        self.assertArgIsBlock(
            CoreMotion.CMPedometer.queryPedometerDataFromDate_toDate_withHandler_,
            2,
            CMPedometerHandler,
        )
        self.assertArgIsBlock(
            CoreMotion.CMPedometer.startPedometerUpdatesFromDate_withHandler_,
            1,
            CMPedometerHandler,
        )
        self.assertArgIsBlock(
            CoreMotion.CMPedometer.startPedometerEventUpdatesWithHandler_,
            0,
            CMPedometerEventHandler,
        )
