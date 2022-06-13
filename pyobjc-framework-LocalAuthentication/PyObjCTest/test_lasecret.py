from PyObjCTools.TestSupport import TestCase, min_os_level
import LocalAuthentication


class TestLASecret(TestCase):
    @min_os_level("13.0")
    def test_methods13_0(self):
        self.assertArgIsBlock(
            LocalAuthentication.LASecret.loadDataWithCompletion_, 0, b"v@@"
        )
