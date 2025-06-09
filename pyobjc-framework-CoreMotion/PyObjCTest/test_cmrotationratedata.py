import CoreMotion
from PyObjCTools.TestSupport import TestCase


class TestCMRotationRateData(TestCase):
    def test_methods(self):
        self.assertResultHasType(
            CoreMotion.CMRotationRateData.rotationRate,
            CoreMotion.CMRotationRate.__typestr__,
        )
