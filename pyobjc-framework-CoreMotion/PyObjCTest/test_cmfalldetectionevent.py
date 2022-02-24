import CoreMotion
from PyObjCTools.TestSupport import TestCase


class TestCMFallDetectionEvent(TestCase):
    def test_enum_types(self):
        self.assertIsEnumType(CoreMotion.CMFallDetectionEventUserResolution)

    def test_constants(self):
        self.assertEqual(CoreMotion.CMFallDetectionEventUserResolutionConfirmed, 0)
        self.assertEqual(CoreMotion.CMFallDetectionEventUserResolutionDismissed, 1)
        self.assertEqual(CoreMotion.CMFallDetectionEventUserResolutionRejected, 2)
        self.assertEqual(CoreMotion.CMFallDetectionEventUserResolutionUnresponsive, 3)
