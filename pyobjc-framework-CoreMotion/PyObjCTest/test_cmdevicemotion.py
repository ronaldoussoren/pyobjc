import CoreMotion
from PyObjCTools.TestSupport import TestCase


class TestCMDeviceMotion(TestCase):
    def test_enums(self):
        self.assertIsEnumType(CoreMotion.CMDeviceMotionSensorLocation)
        self.assertEqual(CoreMotion.CMDeviceMotionSensorLocationDefault, 0)
        self.assertEqual(CoreMotion.CMDeviceMotionSensorLocationHeadphoneLeft, 1)
        self.assertEqual(CoreMotion.CMDeviceMotionSensorLocationHeadphoneRight, 2)

        self.assertIsEnumType(CoreMotion.CMMagneticFieldCalibrationAccuracy)
        self.assertEqual(CoreMotion.CMMagneticFieldCalibrationAccuracyUncalibrated, -1)
        self.assertEqual(CoreMotion.CMMagneticFieldCalibrationAccuracyLow, 0)
        self.assertEqual(CoreMotion.CMMagneticFieldCalibrationAccuracyMedium, 1)
        self.assertEqual(CoreMotion.CMMagneticFieldCalibrationAccuracyHigh, 2)

    def test_structs(self):
        v = CoreMotion.CMCalibratedMagneticField()
        self.assertEqual(v.field, CoreMotion.CMMagneticField())
        self.assertEqual(v.accuracy, 0)
        self.assertPickleRoundTrips(v)

    def test_methods(self):
        self.assertResultHasType(
            CoreMotion.CMDeviceMotion.gravity, CoreMotion.CMAcceleration.__typestr__
        )
        self.assertResultHasType(
            CoreMotion.CMDeviceMotion.magneticField,
            CoreMotion.CMCalibratedMagneticField.__typestr__,
        )
        self.assertResultHasType(
            CoreMotion.CMDeviceMotion.rotationRate,
            CoreMotion.CMRotationRate.__typestr__,
        )
        self.assertResultHasType(
            CoreMotion.CMDeviceMotion.userAcceleration,
            CoreMotion.CMAcceleration.__typestr__,
        )
