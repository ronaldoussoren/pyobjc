from PyObjCTools.TestSupport import TestCase, min_os_level
import LocalAuthentication


class TestLAEnvironmentMechanismBiometry(TestCase):
    @min_os_level("15.0")
    def test_methods(self):
        self.assertResultIsBOOL(
            LocalAuthentication.LAEnvironmentMechanismBiometry.isEnrolled
        )
        self.assertResultIsBOOL(
            LocalAuthentication.LAEnvironmentMechanismBiometry.isLockedOut
        )
        self.assertResultIsBOOL(
            LocalAuthentication.LAEnvironmentMechanismBiometry.builtInSensorInaccessible
        )
