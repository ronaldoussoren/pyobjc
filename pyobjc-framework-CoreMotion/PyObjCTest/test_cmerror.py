import CoreMotion
from PyObjCTools.TestSupport import TestCase


class TestCMError(TestCase):
    def test_constants(self):
        self.assertEqual(CoreMotion.CMErrorNULL, 100)
        self.assertEqual(CoreMotion.CMErrorDeviceRequiresMovement, 101)
        self.assertEqual(CoreMotion.CMErrorTrueNorthNotAvailable, 102)
        self.assertEqual(CoreMotion.CMErrorUnknown, 103)
        self.assertEqual(CoreMotion.CMErrorMotionActivityNotAvailable, 104)
        self.assertEqual(CoreMotion.CMErrorMotionActivityNotAuthorized, 105)
        self.assertEqual(CoreMotion.CMErrorMotionActivityNotEntitled, 106)
        self.assertEqual(CoreMotion.CMErrorInvalidParameter, 107)
        self.assertEqual(CoreMotion.CMErrorInvalidAction, 108)
        self.assertEqual(CoreMotion.CMErrorNotAvailable, 109)
        self.assertEqual(CoreMotion.CMErrorNotEntitled, 110)
        self.assertEqual(CoreMotion.CMErrorNotAuthorized, 111)
        self.assertEqual(CoreMotion.CMErrorNilData, 112)
        self.assertEqual(CoreMotion.CMErrorSize, 113)
