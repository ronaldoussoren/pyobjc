from PyObjCTools.TestSupport import TestCase
import HealthKit


class TestHKFHIRVersion(TestCase):
    def test_methods(self):
        self.assertArgIsOut(HealthKit.HKFHIRVersion.versionFromVersionString_error_, 1)
