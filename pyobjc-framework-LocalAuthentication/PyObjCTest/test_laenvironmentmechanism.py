from PyObjCTools.TestSupport import TestCase, min_os_level
import LocalAuthentication


class TestLAEnvironmentMechanism(TestCase):
    @min_os_level("15.0")
    def test_methods(self):
        self.assertResultIsBOOL(LocalAuthentication.LAEnvironmentMechanism.isUsable)
