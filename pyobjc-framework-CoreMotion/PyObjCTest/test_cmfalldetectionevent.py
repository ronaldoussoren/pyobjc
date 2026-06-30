import CoreMotion
from PyObjCTools.TestSupport import TestCase


class TestCMFallDetectionEvent(TestCase):
    def test_enums(self):
        self.assertIsEnumType(CoreMotion.CMFallDetectionEventUserResolution)
        self.assertEqual(CoreMotion.CMFallDetectionEventUserResolutionConfirmed, 0)
        self.assertEqual(CoreMotion.CMFallDetectionEventUserResolutionDismissed, 1)
        self.assertEqual(CoreMotion.CMFallDetectionEventUserResolutionRejected, 2)
        self.assertEqual(CoreMotion.CMFallDetectionEventUserResolutionUnresponsive, 3)
