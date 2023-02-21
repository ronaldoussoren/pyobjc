import CoreMotion
from PyObjCTools.TestSupport import TestCase


class TestCMWaterSubmersionData(TestCase):
    def test_constants(self):
        self.assertIsEnumType(CoreMotion.CMWaterSubmersionState)
        self.assertEqual(CoreMotion.CMWaterSubmersionStateUnknown, 0)
        self.assertEqual(CoreMotion.CMWaterSubmersionStateNotSubmerged, 1)
        self.assertEqual(CoreMotion.CMWaterSubmersionStateSubmerged, 2)

        self.assertIsEnumType(CoreMotion.CMWaterSubmersionDepthState)
        self.assertEqual(CoreMotion.CMWaterSubmersionDepthStateUnknown, 0)
        self.assertEqual(CoreMotion.CMWaterSubmersionDepthStateNotSubmerged, 100)
        self.assertEqual(CoreMotion.CMWaterSubmersionDepthStateSubmergedShallow, 200)
        self.assertEqual(CoreMotion.CMWaterSubmersionDepthStateSubmergedDeep, 300)
        self.assertEqual(CoreMotion.CMWaterSubmersionDepthStateApproachingMaxDepth, 400)
        self.assertEqual(CoreMotion.CMWaterSubmersionDepthStatePastMaxDepth, 500)
        self.assertEqual(CoreMotion.CMWaterSubmersionDepthStateSensorDepthError, 600)
