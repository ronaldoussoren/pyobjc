from PyObjCTools.TestSupport import TestCase, min_sdk_level
import LocalAuthentication  # noqa: F401


class TestLAEnvironment(TestCase):
    @min_sdk_level("15.0")
    def test_protocols(self):
        self.assertProtocolExists("LAEnvironmentObserver")
